#!/usr/bin/env python3
"""
cluster_stories.py — Phase 2.2 story clustering and ranking.

Reads the normalized headlines cache produced by fetch_headlines.py
(Phase 2.1) and builds story clusters: groups of headlines from
different sources reporting the same underlying event.

Outputs:
  data/clusters/clusters-{topic}.json — per-topic ranked clusters
  data/clusters/top-stories.json      — cross-topic top-story index

The output of this script is the single source for:
  - Phase 2.3 event-state resolver
  - Phase 2.4 synchronized site render
  - future article prioritization

This script is stateless except for "did I see this cluster last run?"
which we infer from the previous output files. The materiality signal
(is this genuinely new, decaying, etc) uses that comparison.

Does not touch any user-facing HTML in this phase. Additive and reversible.

Exit codes:
  0 — built new clusters (meaningful change vs prior run)
  1 — built clusters but no meaningful change
  2 — error (missing inputs, cannot write output)
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "data" / "sources"
CLUSTERS_DIR = ROOT / "data" / "clusters"
CLUSTERS_DIR.mkdir(parents=True, exist_ok=True)

# ─── Clustering thresholds ─────────────────────────────────────────
# News headlines from different wire services about the same event
# frequently share only 1-2 words beyond the core entities. So we rely
# on entity overlap as the PRIMARY signal, with title similarity as a
# corroborating signal.
#
# Tuned against real-world wire-service variation where same-event
# headlines routinely score 0.10-0.20 Jaccard.
JACCARD_CORROBORATE = 0.10     # with 2+ shared entities, this level is enough
JACCARD_HIGH = 0.40            # with 1 shared entity, need stronger title match
JACCARD_SOLO = 0.60            # with 0 entities, need very strong title match
TIME_WINDOW_HOURS = 48         # only cluster within 48h of latest_seen
LOW_PRIORITY_SCORE = 15.0      # below this → flagged but kept
TOP_TIER_COUNT = 3             # top N per topic get top_tier flag

# Small stopword set shared with the observer's fingerprinting.
# Duplicated here (rather than imported) so this script stays decoupled
# from the observer's internals.
STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "at", "to", "for", "and", "or",
    "but", "with", "by", "from", "as", "is", "are", "was", "were",
    "has", "have", "been", "being", "be", "that", "this", "these",
    "those", "it", "its", "their", "they", "them", "which", "who",
    "what", "when", "where", "why", "how", "will", "would", "could",
    "should", "may", "might", "can", "say", "says", "said", "new",
    "us", "u.s.", "eu", "uk",
}


# ─── Utilities ─────────────────────────────────────────────────────
def iso_to_dt(iso_str: str) -> datetime | None:
    if not iso_str:
        return None
    try:
        # Handle both Z-suffix and +00:00 form
        s = iso_str.replace("Z", "+00:00")
        dt = datetime.fromisoformat(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError):
        return None


def significant_words(title: str) -> set[str]:
    """Lowercase, strip punctuation, drop stopwords. Returns a set."""
    import re
    t = title.lower()
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    words = t.split()
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = a & b
    union = a | b
    return len(inter) / len(union) if union else 0.0


def hours_between(a: datetime | None, b: datetime | None) -> float:
    if a is None or b is None:
        return float("inf")
    return abs((a - b).total_seconds()) / 3600.0


# ─── Cluster data model ────────────────────────────────────────────
class Cluster:
    """Mutable cluster accumulator. Serialized to dict at the end."""

    def __init__(self, seed: dict, topic: str):
        self.topic = topic
        self.evidence: list[dict] = [seed]
        # Union of all significant words across all members — grows as cluster grows.
        # Gives more recall (captures variant phrasings) than comparing only to the lead.
        self.cluster_words: set[str] = significant_words(seed.get("title", ""))
        self.canonical_entities: set[str] = set(seed.get("entities", []))

    def try_add(self, story: dict) -> bool:
        """Check if story belongs in this cluster; if so add it and return True."""
        s_words = significant_words(story.get("title", ""))
        s_entities = set(story.get("entities", []))

        # Compute similarity against the accumulated cluster vocabulary.
        # Also compute against just the seed's words as a second signal —
        # if story is close to the ORIGINAL seed, that's strong evidence.
        similarity = jaccard(self.cluster_words, s_words)
        shared_entities = self.canonical_entities & s_entities
        num_shared_entities = len(shared_entities)

        # Time proximity — story must be within window of cluster's latest evidence
        latest = max(
            (iso_to_dt(e.get("published_at", "")) for e in self.evidence),
            default=None,
        )
        story_dt = iso_to_dt(story.get("published_at", ""))
        if story_dt and latest:
            if hours_between(story_dt, latest) > TIME_WINDOW_HOURS:
                return False
        # If either timestamp is missing, don't let time block the match;
        # let title+entity signal decide.

        # Entity-first matching rule — news headlines about the same event
        # may share few words lexically but WILL share named entities.
        if num_shared_entities >= 2 and similarity >= JACCARD_CORROBORATE:
            matched = True
        elif num_shared_entities >= 1 and similarity >= JACCARD_HIGH:
            matched = True
        elif num_shared_entities == 0 and similarity >= JACCARD_SOLO:
            # No entity overlap at all — need near-identical titles
            matched = True
        else:
            matched = False

        if matched:
            self.evidence.append(story)
            # Expand cluster vocabulary and entities (union with new member)
            self.cluster_words.update(s_words)
            self.canonical_entities.update(s_entities)
            return True
        return False

    def to_dict(self) -> dict:
        """Serialize cluster with scoring."""
        ev = self.evidence

        # Lead story — highest confidence, tiebreak by most recent
        lead = max(
            ev,
            key=lambda s: (s.get("confidence", 0), s.get("published_at", "")),
        )

        # Time bounds
        timestamps = [iso_to_dt(s.get("published_at", "")) for s in ev]
        timestamps = [t for t in timestamps if t is not None]
        earliest = min(timestamps) if timestamps else None
        latest = max(timestamps) if timestamps else None
        now = datetime.now(timezone.utc)
        age_hours = hours_between(now, latest) if latest else 999.0

        # Distinct publishers vs raw source count
        publishers = {s.get("source", "").strip() for s in ev if s.get("source")}
        source_types = sorted({s.get("source_type", "") for s in ev if s.get("source_type")})

        # Generate stable cluster_id from the seed's fingerprint + canonical entities
        seed_id = ev[0].get("id", "")
        entity_key = ",".join(sorted(self.canonical_entities))
        raw = f"{seed_id}|{entity_key}|{self.topic}"
        cluster_id = "c_" + hashlib.sha1(raw.encode("utf-8")).hexdigest()[:14]

        # ─── SCORING ───
        # A. Source count points (0-20)
        source_count_points = min(len(publishers) * 5, 20)

        # B. Recency points (0-25) — smooth linear decay, zero at 42h
        if age_hours >= 42:
            recency_points = 0.0
        else:
            recency_points = max(0.0, 25.0 - (age_hours * 0.6))

        # C. Source quality points (0-30)
        confidences = [float(s.get("confidence", 0.6)) for s in ev]
        mean_conf = sum(confidences) / len(confidences) if confidences else 0.6
        source_quality_points = mean_conf * 30.0

        # D. Entity relevance points (0-20)
        unique_entities = len(self.canonical_entities)
        entity_relevance_points = min(unique_entities * 4, 20)

        # E. Materiality — filled in later by caller (needs previous-run comparison)
        # Default is 5.0 (ongoing but not decaying); overridden by main()
        materiality_points = 5.0

        total = round(
            source_count_points
            + recency_points
            + source_quality_points
            + entity_relevance_points
            + materiality_points,
            2,
        )
        total = min(total, 100.0)

        return {
            "cluster_id": cluster_id,
            "topic": self.topic,
            "lead_title": lead.get("title", ""),
            "lead_url": lead.get("url", ""),
            "lead_source": lead.get("source", ""),
            "canonical_entities": sorted(self.canonical_entities),
            "source_count": len(ev),
            "distinct_publishers": len(publishers),
            "source_types": source_types,
            "earliest_seen": earliest.isoformat() if earliest else "",
            "latest_seen": latest.isoformat() if latest else "",
            "age_hours": round(age_hours, 2),
            "score": total,
            "score_components": {
                "source_count_points": round(source_count_points, 2),
                "recency_points": round(recency_points, 2),
                "source_quality_points": round(source_quality_points, 2),
                "entity_relevance_points": round(entity_relevance_points, 2),
                "materiality_points": round(materiality_points, 2),
            },
            "novelty": "pending",     # filled in by main() using prev_clusters
            "first_seen_cluster": False,  # filled in by main()
            "evidence": [
                {
                    "headline_id": s.get("id", ""),
                    "title": s.get("title", ""),
                    "url": s.get("url", ""),
                    "source": s.get("source", ""),
                    "source_type": s.get("source_type", ""),
                    "published_at": s.get("published_at", ""),
                    "confidence": s.get("confidence", 0.0),
                }
                for s in ev
            ],
        }


def build_clusters_for_topic(topic: str, headlines: list[dict]) -> list[Cluster]:
    """Greedy single-pass clustering. Returns list of Cluster objects."""
    clusters: list[Cluster] = []
    # Sort by confidence desc so highest-quality headline seeds each cluster
    sorted_headlines = sorted(
        headlines,
        key=lambda s: float(s.get("confidence", 0.0)),
        reverse=True,
    )
    for story in sorted_headlines:
        if not story.get("title"):
            continue
        placed = False
        for c in clusters:
            if c.try_add(story):
                placed = True
                break
        if not placed:
            clusters.append(Cluster(story, topic))
    return clusters


def apply_materiality(
    new_clusters: list[dict],
    prev_clusters_by_id: dict[str, dict],
) -> None:
    """Mutate cluster dicts in-place to set novelty + materiality_points."""
    now = datetime.now(timezone.utc)
    for c in new_clusters:
        prev = prev_clusters_by_id.get(c["cluster_id"])

        if prev is None:
            # Brand new cluster
            c["novelty"] = "new"
            c["first_seen_cluster"] = True
            materiality = 10.0
        else:
            prev_src = prev.get("source_count", 0)
            curr_src = c.get("source_count", 0)
            latest = iso_to_dt(c.get("latest_seen", ""))
            hours_since_new_evidence = hours_between(now, latest) if latest else 999.0

            if curr_src > prev_src:
                c["novelty"] = "growing"
                materiality = 5.0
            elif hours_since_new_evidence > 12:
                c["novelty"] = "decaying"
                materiality = -5.0
            else:
                c["novelty"] = "ongoing"
                materiality = 0.0

        # Rewrite the materiality_points component + total
        old_mat = c["score_components"]["materiality_points"]
        c["score_components"]["materiality_points"] = round(materiality, 2)
        c["score"] = round(c["score"] - old_mat + materiality, 2)
        # Clamp 0-100
        c["score"] = max(0.0, min(100.0, c["score"]))


# ─── Main ──────────────────────────────────────────────────────────
def main() -> int:
    index_path = SOURCES_DIR / "headlines-index.json"
    if not index_path.exists():
        print(f"[cluster_stories] No headlines index at {index_path}")
        print("[cluster_stories] Run fetch_headlines.py first (Phase 2.1)")
        return 2

    try:
        index = json.loads(index_path.read_text())
    except json.JSONDecodeError as e:
        print(f"[cluster_stories] headlines-index.json malformed: {e}")
        return 2

    topics: list[str] = index.get("topics", [])
    if not topics:
        print("[cluster_stories] no topics listed in headlines-index.json")
        return 2

    print(f"[cluster_stories] clustering {len(topics)} topics")

    all_topic_clusters: dict[str, list[dict]] = {}
    any_meaningful_change = False

    for topic in topics:
        cache_path = SOURCES_DIR / f"headlines-{topic}.json"
        if not cache_path.exists():
            print(f"  {topic:14s} SKIP (cache missing)")
            continue

        try:
            cache = json.loads(cache_path.read_text())
        except json.JSONDecodeError:
            print(f"  {topic:14s} SKIP (malformed cache)")
            continue

        headlines = cache.get("stories", [])
        if not headlines:
            print(f"  {topic:14s} SKIP (0 headlines)")
            continue

        # Load previous clusters for materiality comparison
        prev_path = CLUSTERS_DIR / f"clusters-{topic}.json"
        prev_by_id: dict[str, dict] = {}
        if prev_path.exists():
            try:
                prev = json.loads(prev_path.read_text())
                for c in prev.get("clusters", []):
                    prev_by_id[c["cluster_id"]] = c
            except json.JSONDecodeError:
                pass

        clusters = build_clusters_for_topic(topic, headlines)
        cluster_dicts = [c.to_dict() for c in clusters]
        apply_materiality(cluster_dicts, prev_by_id)

        # Sort by score desc
        cluster_dicts.sort(key=lambda c: c["score"], reverse=True)

        # Annotate top_tier + low_priority
        for i, c in enumerate(cluster_dicts):
            c["top_tier"] = i < TOP_TIER_COUNT
            c["low_priority"] = c["score"] < LOW_PRIORITY_SCORE

        payload = {
            "topic": topic,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "sources_scanned": cache.get("sources_used", []),
            "total_headlines": len(headlines),
            "clusters_found": len(cluster_dicts),
            "clusters": cluster_dicts,
        }

        # Atomic write + change detection (ignore generated_at)
        changed = True
        if prev_path.exists():
            try:
                prev = json.loads(prev_path.read_text())
                prev_ids = sorted(c["cluster_id"] for c in prev.get("clusters", []))
                new_ids = sorted(c["cluster_id"] for c in cluster_dicts)
                prev_scores = {c["cluster_id"]: c.get("score", 0) for c in prev.get("clusters", [])}
                new_scores = {c["cluster_id"]: c.get("score", 0) for c in cluster_dicts}
                if prev_ids == new_ids and all(
                    abs(new_scores.get(cid, 0) - prev_scores.get(cid, 0)) < 2.0
                    for cid in new_ids
                ):
                    # IDs identical AND all scores within 2 points — treat as unchanged
                    changed = False
            except (json.JSONDecodeError, KeyError):
                pass

        tmp = prev_path.with_suffix(".new.json")
        tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        tmp.replace(prev_path)

        all_topic_clusters[topic] = cluster_dicts
        status = "CHANGED" if changed else "same"
        top_score = cluster_dicts[0]["score"] if cluster_dicts else 0
        print(f"  {topic:14s} {len(cluster_dicts):3d} clusters  top_score={top_score:5.1f}  {status}")
        if changed:
            any_meaningful_change = True

    # Build cross-topic top-stories index
    top_overall = []
    top_by_topic = {}
    for topic, clusters in all_topic_clusters.items():
        if clusters:
            top_by_topic[topic] = clusters[0]["cluster_id"]
            for c in clusters[:3]:
                top_overall.append({
                    "cluster_id": c["cluster_id"],
                    "topic": topic,
                    "score": c["score"],
                    "lead_title": c["lead_title"],
                    "lead_url": c["lead_url"],
                    "lead_source": c["lead_source"],
                    "source_count": c["source_count"],
                    "novelty": c["novelty"],
                })
    top_overall.sort(key=lambda x: x["score"], reverse=True)
    top_overall = top_overall[:15]

    top_payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "top_overall": top_overall,
        "top_by_topic": top_by_topic,
    }
    (CLUSTERS_DIR / "top-stories.json").write_text(
        json.dumps(top_payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    if any_meaningful_change:
        print(f"[cluster_stories] ✓ clusters rebuilt across {len(all_topic_clusters)} topics")
        return 0
    print("[cluster_stories] no meaningful cluster changes")
    return 1


if __name__ == "__main__":
    sys.exit(main())
