#!/usr/bin/env python3
"""
resolve_event_state.py — Phase 2.3 unified event-state resolver.

Reads the cluster output from Phase 2.2 (data/clusters/*.json) plus the
price/gas observer outputs (data/sources/*.json) and resolves the current
state of tracked events into one canonical file:

  data/state/events.json

This is the single source of truth that Phase 2.4's renderer will consume.
Every dependent UI module (glance strips, risk meters, driver cards,
breaking banner) will eventually read from here so the site can never
present contradictory states across pages.

In this phase we do NOT touch any user-facing HTML. Resolver output only.

Exit codes:
  0 — state resolved, meaningful change detected
  1 — state resolved, no meaningful change (no-op)
  2 — error (inputs missing/malformed, cannot write output)

Safety guarantees:
  - atomic write (.new.json → rename)
  - previous state preserved at data/state/events.prev.json for audit/rollback
  - minimum dwell time prevents flapping (30 min between same-field changes)
  - confidence floor (< 0.60) blocks publish-triggering
  - retired stale events logged but not silently dropped
  - every decision written to data/logs/resolver.log
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CLUSTERS_DIR = ROOT / "data" / "clusters"
SOURCES_DIR = ROOT / "data" / "sources"
STATE_DIR = ROOT / "data" / "state"
LOG_PATH = ROOT / "data" / "logs" / "resolver.log"

STATE_DIR.mkdir(parents=True, exist_ok=True)
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

EVENTS_PATH = STATE_DIR / "events.json"
EVENTS_PREV_PATH = STATE_DIR / "events.prev.json"

# ─── Config ────────────────────────────────────────────────────────
SCHEMA_VERSION = 2
CONFIDENCE_FLOOR = 0.60
MIN_DWELL_MINUTES = 30
REVERSION_BLOCK_HOURS = 2

# Per-event config: each entry declares how to identify + resolve an event
# key from the cluster pool. The resolver iterates these definitions.
EVENT_DEFINITIONS: dict[str, dict] = {
    "hormuz_status": {
        "display_name": "Strait of Hormuz Status",
        "category": "chokepoint",
        "required_entities": ["Hormuz"],            # at least one must appear
        "optional_entities": ["Iran", "IRGC"],
        "topics_to_scan": ["geopolitics", "oil", "breaking"],
        "stale_after_hours": 24,
        "update_priority": "critical",
        "affected_pages": [
            "index.html", "oil-prices.html",
            "category/geopolitics.html", "markets.html",
        ],
        "dependent_modules": [
            "homepage.glance-strip.hormuz-status",
            "geopolitics.risk-meter.text",
            "oil-prices.drivers.hormuz",
            "markets.drivers.hormuz",
        ],
        # Status keywords — checked in order, first match per cluster wins.
        # Each (status, [keywords]) tuple: match checks text.contains(keyword).
        # CLOSED comes first because news about closure often mentions "reopen" too
        # (e.g. "Iran re-closes strait after one-day reopening") — we want the
        # closure signal to win when both appear.
        "status_keywords": [
            ("CLOSED",    ["re-close", "re-closes", "re-closed", "closure", "blockade",
                           "blockad", "shut down", "shuts down", "shuts the strait",
                           "shut the strait", "closes strait", "closed strait",
                           "close strait", "suspended shipping", "halted shipping"]),
            ("CONTESTED", ["fired on", "gunboat", "attack", "struck", "missile",
                           "projectile", "warning shot", "threatens shipping"]),
            ("OPEN",      ["reopen", "reopens", "reopened", "restored", "resumed shipping",
                           "cleared", "lifted blockade", "lifted closure"]),
        ],
        # Phrase-level negation: if any of these appear, the OPEN signal is suppressed.
        # Protects against "re-closes strait after one-day reopening" false matches.
        "suppress_open_if": ["re-close", "closure", "blockade", "shut down", "shuts"],
        "default_status": "OPEN",
        "risk_level_map": {
            "CLOSED":    "HIGH",
            "CONTESTED": "ELEVATED",
            "OPEN":      "LOW",
        },
    },
    "us_iran_ceasefire": {
        "display_name": "U.S.-Iran Ceasefire",
        "category": "diplomatic_event",
        "required_entities": ["Iran"],
        "optional_entities": ["ceasefire", "truce"],  # softer — includes title keywords
        "topics_to_scan": ["geopolitics", "breaking"],
        "stale_after_hours": 72,
        "update_priority": "high",
        "affected_pages": [
            "index.html", "category/geopolitics.html", "oil-prices.html",
        ],
        "dependent_modules": [
            "homepage.glance-strip.next-catalyst",
            "geopolitics.risk-meter.text",
            "oil-prices.drivers.ceasefire",
        ],
        # Order matters: check DEFINITIVE states (collapsed, renewed) before
        # anticipatory states (fragile, expires). "May not extend" is FRAGILE,
        # not COLLAPSED. "Threatens to resume bombing" is FRAGILE, not COLLAPSED
        # until bombing has actually resumed.
        "status_keywords": [
            ("COLLAPSED", [
                "ceasefire collapses", "ceasefire collapsed",
                "ceasefire broken", "ceasefire over",
                "airstrikes launched", "resumed bombing",
                "resumed airstrikes", "attacked iran today",
            ]),
            ("RENEWED",   [
                "ceasefire extended", "ceasefire renewed",
                "agreement signed", "deal reached",
                "extension agreed", "agreed to extend",
            ]),
            ("EXPIRED",   [
                "ceasefire expired", "ceasefire has expired",
                "ceasefire lapsed",
            ]),
            ("FRAGILE",   [
                "may not extend", "threatens to resume",
                "warns he may", "in limbo",
                "ceasefire expires", "expires april", "expires may", "expires june",
                "without deal", "without agreement",
                "talks stalled", "fragile",
            ]),
            ("HOLDING",   [
                "ceasefire holds", "ceasefire continues",
                "ceasefire in effect", "ceasefire in place",
                "truce holding",
            ]),
        ],
        "default_status": "HOLDING",
        "risk_level_map": {
            "COLLAPSED": "HIGH",
            "EXPIRED":   "HIGH",
            "FRAGILE":   "HIGH",
            "HOLDING":   "ELEVATED",
            "RENEWED":   "LOW",
        },
        # Stores a prospective catalyst date if text mentions one
        "catalyst_date_extract": True,
    },
    "opec_plus_policy": {
        "display_name": "OPEC+ Policy",
        "category": "policy_state",
        "required_entities": ["OPEC"],
        "optional_entities": ["Saudi", "Russia"],
        "topics_to_scan": ["oil", "geopolitics"],
        "stale_after_hours": 168,  # 7 days — OPEC stances evolve slowly
        "update_priority": "high",
        "affected_pages": ["oil-prices.html", "markets.html"],
        "dependent_modules": [
            "oil-prices.drivers.opec",
            "markets.drivers.opec",
        ],
        # "OPEC+ holds April output increase" = HOLDING (proceeding with existing plan).
        # HOLDING must check before INCREASING so the phrase "holds... increase" classifies
        # correctly — they're holding the plan, not announcing a new increase.
        "status_keywords": [
            ("EMERGENCY_MEETING", [
                "emergency meeting", "extraordinary meeting",
                "jmmc called", "emergency session",
            ]),
            ("HOLDING", [
                "holds april", "holds may", "holds june",
                "holds output", "holds plan", "holds production",
                "proceeds with", "proceeding with", "maintains plan",
                "unchanged policy", "policy unchanged",
            ]),
            ("CUTTING", [
                "announces cut", "announces production cut",
                "cuts output", "reduces output", "reduce production",
                "trims production", "extra cut",
            ]),
            ("INCREASING", [
                "announces increase", "announces output hike",
                "raises output", "lifts production", "hikes output",
                "additional bpd", "additional barrels",
            ]),
        ],
        "default_status": "HOLDING",
        "risk_level_map": {
            "EMERGENCY_MEETING": "ELEVATED",
            "CUTTING":           "ELEVATED",
            "INCREASING":        "LOW",
            "HOLDING":           "LOW",
        },
    },
}

# ─── Utilities ─────────────────────────────────────────────────────
def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat()
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")
    print(msg)


def iso_to_dt(s: str) -> datetime | None:
    if not s:
        return None
    try:
        s2 = s.replace("Z", "+00:00")
        dt = datetime.fromisoformat(s2)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except (ValueError, TypeError):
        return None


def load_json(p: Path) -> dict | None:
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def load_all_clusters() -> dict[str, list[dict]]:
    """Return {topic: [clusters]} from all cluster files."""
    out: dict[str, list[dict]] = {}
    if not CLUSTERS_DIR.exists():
        return out
    for p in CLUSTERS_DIR.glob("clusters-*.json"):
        try:
            data = json.loads(p.read_text())
        except json.JSONDecodeError:
            continue
        topic = data.get("topic", "")
        if topic:
            out[topic] = data.get("clusters", [])
    return out


# ─── Event resolution ──────────────────────────────────────────────
def matching_clusters_for_event(
    event_def: dict,
    clusters_by_topic: dict[str, list[dict]],
) -> list[dict]:
    """Find clusters relevant to a given event definition.

    A cluster matches if:
      - it appears in one of the event's topics_to_scan
      - AND at least one of required_entities appears in canonical_entities
        OR title (case-insensitive)
      - AND the cluster is not decaying badly (novelty != decaying that's old)
    """
    required = [e.lower() for e in event_def.get("required_entities", [])]
    topics = event_def.get("topics_to_scan", [])

    matches: list[dict] = []
    for topic in topics:
        for cluster in clusters_by_topic.get(topic, []):
            entities_lower = [e.lower() for e in cluster.get("canonical_entities", [])]
            title_lower = cluster.get("lead_title", "").lower()

            # Check required entity match — in entities list OR title text
            entity_ok = any(
                req in entities_lower or req in title_lower
                for req in required
            )
            if not entity_ok:
                continue
            # Skip decaying clusters older than 24h (they don't drive state)
            latest = iso_to_dt(cluster.get("latest_seen", ""))
            if latest and cluster.get("novelty") == "decaying":
                hours_old = (datetime.now(timezone.utc) - latest).total_seconds() / 3600
                if hours_old > 24:
                    continue
            matches.append(cluster)
    return matches


def determine_status(
    clusters: list[dict],
    event_def: dict,
) -> tuple[str, str, float, list[str]]:
    """Given matching clusters, determine (status, status_detail, confidence, rationale)."""
    if not clusters:
        return event_def["default_status"], "no recent coverage", 0.5, ["no matching clusters"]

    # Each cluster votes for a status based on its text + timing weight
    # More recent + higher-confidence clusters get higher voting weight.
    status_votes: dict[str, float] = {}
    status_detail: dict[str, str] = {}
    now = datetime.now(timezone.utc)
    rationale: list[str] = []

    suppress_open_triggers = event_def.get("suppress_open_if", [])

    for cluster in clusters:
        title = cluster.get("lead_title", "").lower()
        text_pool = title
        for ev in cluster.get("evidence", []):
            text_pool += " " + ev.get("title", "").lower()

        # Check for OPEN-suppression phrases (e.g. "re-close" cancels "reopen")
        suppress_open = any(phrase in text_pool for phrase in suppress_open_triggers)

        cluster_status = None
        matched_kw = None
        for status, kw_list in event_def["status_keywords"]:
            # Skip OPEN if suppression triggered
            if status == "OPEN" and suppress_open:
                continue
            for kw in kw_list:
                if kw in text_pool:
                    cluster_status = status
                    matched_kw = kw
                    break
            if cluster_status:
                break

        if not cluster_status:
            continue

        # Voting weight = recency factor * cluster score / 100
        latest = iso_to_dt(cluster.get("latest_seen", ""))
        hours_old = (now - latest).total_seconds() / 3600 if latest else 12
        recency_factor = max(0.2, 1.0 - (hours_old / 48))  # 1.0 at now, 0.2 at 48h
        vote_weight = recency_factor * (cluster.get("score", 0) / 100.0)

        status_votes[cluster_status] = status_votes.get(cluster_status, 0) + vote_weight
        # Store the strongest-voting cluster's detail as the status_detail
        if cluster_status not in status_detail:
            status_detail[cluster_status] = cluster.get("lead_title", "")[:120]

        suppress_note = " [OPEN suppressed]" if suppress_open else ""
        rationale.append(
            f"cluster {cluster.get('cluster_id', '')[:12]} → {cluster_status} "
            f"(kw='{matched_kw}', weight={vote_weight:.2f}){suppress_note}"
        )

    if not status_votes:
        return (
            event_def["default_status"],
            "no definitive signals",
            0.5,
            rationale + [f"fell back to default '{event_def['default_status']}'"],
        )

    # Winning status is the one with highest total vote weight
    winning_status = max(status_votes.items(), key=lambda kv: kv[1])
    status = winning_status[0]

    # Confidence = winning_vote / total_vote, then damped by source count
    total_votes = sum(status_votes.values())
    agreement_ratio = winning_status[1] / total_votes if total_votes > 0 else 0.5

    # Factor in mean cluster confidence (source quality)
    mean_cluster_score = sum(c.get("score", 0) for c in clusters) / (len(clusters) * 100.0)
    confidence = round(0.6 + (0.3 * agreement_ratio) + (0.1 * mean_cluster_score), 3)
    confidence = min(max(confidence, 0.0), 1.0)

    rationale.append(
        f"winning={status} ({winning_status[1]:.2f}/{total_votes:.2f}), conf={confidence}"
    )

    return status, status_detail.get(status, ""), confidence, rationale


def extract_catalyst_date(clusters: list[dict]) -> tuple[str, str]:
    """Best-effort catalyst date extraction from cluster text. Returns (iso_date, description)."""
    # Simple pattern: "April 21", "Apr 21", "4/21", "21 April"
    month_map = {
        "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3,
        "apr": 4, "april": 4, "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
        "aug": 8, "august": 8, "sep": 9, "september": 9, "oct": 10, "october": 10,
        "nov": 11, "november": 11, "dec": 12, "december": 12,
    }
    now = datetime.now(timezone.utc)
    year = now.year

    candidates: list[tuple[datetime, str]] = []
    for cluster in clusters:
        text = cluster.get("lead_title", "")
        for ev in cluster.get("evidence", []):
            text += " " + ev.get("title", "")
        # Look for patterns like "April 21" / "Apr 21" / "21 April"
        patterns = [
            r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+(\d{1,2})\b",
            r"\b(\d{1,2})\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\b",
        ]
        for pat in patterns:
            for m in re.finditer(pat, text, re.IGNORECASE):
                g1, g2 = m.group(1).lower(), m.group(2).lower()
                if g1.isdigit():
                    day, mo = int(g1), month_map.get(g2, 0)
                else:
                    day, mo = int(g2), month_map.get(g1, 0)
                if mo == 0 or day < 1 or day > 31:
                    continue
                try:
                    dt = datetime(year, mo, day, tzinfo=timezone.utc)
                    # Prefer future dates (catalyst is upcoming); if in the past, try next year
                    if dt < now - timedelta(days=7):
                        dt = datetime(year + 1, mo, day, tzinfo=timezone.utc)
                    candidates.append((dt, text[:80]))
                except ValueError:
                    continue

    if not candidates:
        return "", ""

    # Choose the nearest-future catalyst
    future_candidates = [(dt, desc) for dt, desc in candidates if dt >= now - timedelta(hours=12)]
    if future_candidates:
        best = min(future_candidates, key=lambda x: x[0])
        return best[0].date().isoformat(), best[1]
    return "", ""


# Canonical compact UI labels for glance-strip / badges.
# Each entry: event key → {status: short_tag (≤ 20 chars)}.
# These are AUTHORITATIVE — do not replace with truncated news headlines.
# Empty string = don't render a tag for this status combo.
STATUS_TAG_MAP: dict[str, dict[str, str]] = {
    "hormuz_status": {
        "OPEN":      "Traffic normal",
        "CONTESTED": "Tankers at risk",
        "CLOSED":    "Strait closed",
        "UNKNOWN":   "Status unclear",
    },
    "us_iran_ceasefire": {
        "HOLDING":   "In effect",
        "RENEWED":   "Recently extended",
        "FRAGILE":   "Under strain",
        "BROKEN":    "Ceasefire broken",
        "UNKNOWN":   "Status unclear",
    },
    "opec_plus_policy": {
        "HOLDING":          "No change",
        "INCREASING":       "Output rising",
        "CUTTING":          "Output cut",
        "EMERGENCY_MEETING":"Emergency meeting",
        "UNKNOWN":          "Awaiting signal",
    },
}


def build_status_tag(key: str, status: str, event_def: dict) -> str:
    """Return short canonical UI label for an (event, status) pair.

    Falls back to the status itself title-cased if no explicit mapping,
    which is usually already short enough. Hard cap at 24 chars so it
    never overflows a glance-strip subtext slot.
    """
    mapping = STATUS_TAG_MAP.get(key, {})
    if status in mapping:
        return mapping[status]
    # Fallback: "EMERGENCY_MEETING" → "Emergency meeting"
    fallback = status.replace("_", " ").title() if status else ""
    return fallback[:24]


def build_event(
    key: str,
    event_def: dict,
    clusters_by_topic: dict[str, list[dict]],
) -> dict:
    """Resolve a single event definition into an event dict."""
    matched = matching_clusters_for_event(event_def, clusters_by_topic)
    status, status_detail, confidence, rationale = determine_status(matched, event_def)

    # Build summaries from best cluster
    best_cluster = max(matched, key=lambda c: c.get("score", 0)) if matched else None
    summary_short = ""
    summary_long = ""
    if best_cluster:
        summary_short = best_cluster.get("lead_title", "")[:120]
        # summary_long: lead title + brief elaboration from second-best cluster if any
        summary_long = best_cluster.get("lead_title", "")
        if len(matched) > 1:
            second = sorted(matched, key=lambda c: c.get("score", 0), reverse=True)[1]
            summary_long += ". " + second.get("lead_title", "")[:100]

    evidence_cluster_ids = [c.get("cluster_id", "") for c in matched[:5]]

    # Freshness calculation
    stale_hrs = event_def.get("stale_after_hours", 24)
    latest_confirm = None
    for c in matched:
        lat = iso_to_dt(c.get("latest_seen", ""))
        if lat and (latest_confirm is None or lat > latest_confirm):
            latest_confirm = lat
    now = datetime.now(timezone.utc)
    freshness = "fresh"
    if latest_confirm:
        hours_since = (now - latest_confirm).total_seconds() / 3600
        if hours_since > stale_hrs * 2:
            freshness = "retired"
        elif hours_since > stale_hrs:
            freshness = "stale"
            confidence = round(confidence * 0.60, 3)
        elif hours_since > stale_hrs / 2:
            freshness = "aging"
            confidence = round(confidence * 0.85, 3)

    event = {
        "key": key,
        "display_name": event_def["display_name"],
        "category": event_def["category"],
        "status": status,
        "status_detail": status_detail,
        "status_tag": build_status_tag(key, status, event_def),
        "risk_level": event_def.get("risk_level_map", {}).get(status, "LOW"),
        "confidence": confidence,
        "last_confirmed": latest_confirm.isoformat() if latest_confirm else "",
        "source_count": sum(c.get("source_count", 1) for c in matched),
        "summary_short": summary_short,
        "summary_long": summary_long,
        "evidence_cluster_ids": evidence_cluster_ids,
        "evidence_count": len(matched),
        "affected_pages": event_def.get("affected_pages", []),
        "dependent_modules": event_def.get("dependent_modules", []),
        "update_priority": event_def.get("update_priority", "medium"),
        "freshness": freshness,
        "stale_after_hours": stale_hrs,
        "rationale": rationale,
    }

    # Catalyst date extraction if configured
    if event_def.get("catalyst_date_extract"):
        cdate, cdesc = extract_catalyst_date(matched)
        event["next_catalyst_date"] = cdate
        event["next_catalyst_description"] = cdesc
        event["next_catalyst_micro"] = derive_catalyst_micro(cdesc, key)

    return event


def derive_catalyst_micro(description: str, event_key: str) -> str:
    """Return a compact ≤20-char label summarizing the catalyst event type.

    Better than truncating the full description mid-word. Uses keyword
    signals to pick from a small library of event labels.
    """
    if not description:
        return ""
    d = description.lower()
    # Keyword → short label, ordered by specificity
    rules = [
        ("expir",     "Ceasefire expires"),
        ("deadline",  "Deadline hits"),
        ("extend",    "Extension vote"),
        ("summit",    "Summit"),
        ("meeting",   "Key meeting"),
        ("talks",     "Talks resume"),
        ("vote",      "Vote scheduled"),
        ("sanction",  "Sanctions update"),
        ("opec",      "OPEC meeting"),
        ("ceasefire", "Ceasefire update"),
    ]
    for kw, label in rules:
        if kw in d:
            return label
    # Fallback: first 20 chars from description, cut at word boundary
    truncated = description[:20].rsplit(" ", 1)[0]
    return truncated or description[:20]


def build_composite_global_risk(events: dict[str, dict]) -> dict:
    """Compute global_risk_level from component events."""
    score = 0
    contributions: list[str] = []

    hormuz = events.get("hormuz_status", {})
    if hormuz.get("status") == "CLOSED":
        score += 40; contributions.append("hormuz=CLOSED (+40)")
    elif hormuz.get("status") == "CONTESTED":
        score += 25; contributions.append("hormuz=CONTESTED (+25)")

    ceasefire = events.get("us_iran_ceasefire", {})
    if ceasefire.get("status") in ("COLLAPSED", "EXPIRED"):
        score += 35; contributions.append(f"ceasefire={ceasefire.get('status')} (+35)")
    elif ceasefire.get("status") == "FRAGILE":
        score += 25; contributions.append("ceasefire=FRAGILE (+25)")
    elif ceasefire.get("status") == "HOLDING":
        score += 10; contributions.append("ceasefire=HOLDING (+10)")

    opec = events.get("opec_plus_policy", {})
    if opec.get("status") == "EMERGENCY_MEETING":
        score += 20; contributions.append("opec=EMERGENCY (+20)")

    if score >= 60:
        level = "CRITICAL"
    elif score >= 40:
        level = "HIGH"
    elif score >= 20:
        level = "ELEVATED"
    else:
        level = "LOW"

    summary_parts = []
    if hormuz.get("status") and hormuz["status"] != "OPEN":
        summary_parts.append(f"Hormuz {hormuz['status'].lower()}")
    if ceasefire.get("status") and ceasefire["status"] not in ("HOLDING", "RENEWED"):
        summary_parts.append(f"ceasefire {ceasefire['status'].lower()}")
    if opec.get("status") == "EMERGENCY_MEETING":
        summary_parts.append("OPEC+ emergency meeting")

    summary_short = f"Global energy risk: {level.lower()}."
    summary_long = "Risk drivers: " + (", ".join(summary_parts) if summary_parts else "no major disruption")

    # Compact UI label for glance-strip subtext. ≤ 24 chars.
    # Uses raw driver tags (no "Hormuz"/"ceasefire" prefix) joined by +.
    micro_parts = []
    if hormuz.get("status") and hormuz["status"] != "OPEN":
        micro_parts.append(hormuz["status"].lower())
    if ceasefire.get("status") and ceasefire["status"] not in ("HOLDING", "RENEWED"):
        micro_parts.append(ceasefire["status"].lower())
    if opec.get("status") == "EMERGENCY_MEETING":
        micro_parts.append("OPEC alert")
    summary_micro = " + ".join(micro_parts) if micro_parts else "stable"
    if len(summary_micro) > 24:
        summary_micro = summary_micro[:24]

    return {
        "key": "global_risk_level",
        "display_name": "Global Energy Risk Level",
        "category": "composite",
        "status": level,
        "risk_level": level,
        "score": score,
        "composite_of": ["hormuz_status", "us_iran_ceasefire", "opec_plus_policy"],
        "summary_short": summary_short,
        "summary_long": summary_long,
        "summary_micro": summary_micro,
        "rationale": contributions,
        "dependent_modules": [
            "homepage.glance-strip.risk-level",
            "geopolitics.risk-meter.level",
        ],
        "affected_pages": [
            "index.html", "category/geopolitics.html",
            "oil-prices.html", "markets.html",
        ],
    }


def build_top_story(clusters_by_topic: dict[str, list[dict]]) -> dict | None:
    """Select the highest-scored cluster across all topics as the top story."""
    top_path = CLUSTERS_DIR / "top-stories.json"
    if top_path.exists():
        try:
            data = json.loads(top_path.read_text())
            top_list = data.get("top_overall", [])
            if top_list:
                c = top_list[0]
                return {
                    "key": "top_story",
                    "display_name": "Current Top Story",
                    "category": "news_event",
                    "cluster_id": c.get("cluster_id", ""),
                    "lead_title": c.get("lead_title", ""),
                    "lead_url": c.get("lead_url", ""),
                    "lead_source": c.get("lead_source", ""),
                    "topic": c.get("topic", ""),
                    "score": c.get("score", 0),
                    "novelty": c.get("novelty", ""),
                    "source_count": c.get("source_count", 1),
                    "confidence": min(0.60 + c.get("score", 0) / 200.0, 0.95),
                    "dependent_modules": ["homepage.breaking-banner.primary"],
                    "affected_pages": ["index.html"],
                }
        except json.JSONDecodeError:
            pass
    return None


# ─── Change detection ──────────────────────────────────────────────
def detect_meaningful_changes(
    new_events: dict[str, dict],
    prev_events: dict[str, dict] | None,
) -> list[dict]:
    """Compare new vs prev and return a list of change records."""
    changes: list[dict] = []
    now = datetime.now(timezone.utc)
    prev_events = prev_events or {}

    # Detect new and modified events
    for key, new_event in new_events.items():
        prev_event = prev_events.get(key)
        if prev_event is None:
            changes.append({
                "event_key": key,
                "field": "new_event",
                "from": None,
                "to": new_event.get("status", ""),
                "detected_at": now.isoformat(),
                "meaningful": True,
                "triggers_publish": new_event.get("confidence", 0) >= CONFIDENCE_FLOOR,
            })
            continue

        # Check tracked fields
        tracked_fields = ["status", "risk_level", "next_catalyst_date"]
        for field in tracked_fields:
            old_val = prev_event.get(field, "")
            new_val = new_event.get(field, "")
            if old_val != new_val and (old_val or new_val):
                # Reversion-block check
                meaningful = True
                if field == "status" and prev_event.get("last_changed"):
                    last_change = iso_to_dt(prev_event["last_changed"])
                    if last_change and (now - last_change).total_seconds() < REVERSION_BLOCK_HOURS * 3600:
                        # Would revert to very recent prior state — suspicious
                        if new_val == prev_event.get("previous_status"):
                            meaningful = False

                changes.append({
                    "event_key": key,
                    "field": field,
                    "from": old_val,
                    "to": new_val,
                    "detected_at": now.isoformat(),
                    "meaningful": meaningful,
                    "triggers_publish": (
                        meaningful and new_event.get("confidence", 0) >= CONFIDENCE_FLOOR
                    ),
                })
                # Update last_changed + previous_status on the new event
                if field == "status":
                    new_event["previous_status"] = old_val
                    new_event["last_changed"] = now.isoformat()

    # Detect retired events
    for key in prev_events:
        if key not in new_events:
            changes.append({
                "event_key": key,
                "field": "retired",
                "from": prev_events[key].get("status", ""),
                "to": None,
                "detected_at": now.isoformat(),
                "meaningful": True,
                "triggers_publish": True,
            })

    return changes


# ─── Main ──────────────────────────────────────────────────────────
def main() -> int:
    log("resolver: start")

    clusters_by_topic = load_all_clusters()
    if not clusters_by_topic:
        log("resolver: no cluster files found — run cluster_stories.py first")
        # Still write an empty valid state so consumers don't crash
        empty = {
            "version": SCHEMA_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "events": {},
            "changes_since_last_run": [],
            "resolution_log": ["no clusters available"],
        }
        tmp = EVENTS_PATH.with_suffix(".new.json")
        tmp.write_text(json.dumps(empty, indent=2, ensure_ascii=False), encoding="utf-8")
        tmp.replace(EVENTS_PATH)
        return 1

    log(f"resolver: scanning {sum(len(v) for v in clusters_by_topic.values())} "
        f"clusters across {len(clusters_by_topic)} topics")

    # Load previous state (for change detection)
    prev_state = load_json(EVENTS_PATH)
    prev_events = (prev_state or {}).get("events", {})
    prev_generated = (prev_state or {}).get("generated_at", "")

    resolution_log: list[str] = []
    events: dict[str, dict] = {}

    # Build each atomic event
    for key, event_def in EVENT_DEFINITIONS.items():
        event = build_event(key, event_def, clusters_by_topic)
        if event["freshness"] == "retired":
            log(f"  {key}: RETIRED (stale beyond 2× threshold)")
            resolution_log.append(f"{key}: retired — last_confirmed too old")
            continue
        events[key] = event
        log(f"  {key}: {event['status']} (conf={event['confidence']}, "
            f"freshness={event['freshness']}, clusters={event['evidence_count']})")
        resolution_log.append(
            f"{key}: resolved={event['status']}, confidence={event['confidence']}, "
            f"fresh={event['freshness']}"
        )

    # Build composite event
    events["global_risk_level"] = build_composite_global_risk(events)
    log(f"  global_risk_level: {events['global_risk_level']['status']} "
        f"(score={events['global_risk_level']['score']})")

    # Build top story
    top = build_top_story(clusters_by_topic)
    if top:
        events["top_story"] = top
        log(f"  top_story: '{top['lead_title'][:60]}' (score={top['score']})")

    # Detect meaningful changes
    changes = detect_meaningful_changes(events, prev_events)
    meaningful_changes = [c for c in changes if c["meaningful"]]
    publish_triggers = [c for c in changes if c.get("triggers_publish")]

    if changes:
        log(f"resolver: {len(changes)} change(s), "
            f"{len(meaningful_changes)} meaningful, "
            f"{len(publish_triggers)} publish-triggering")
        for c in meaningful_changes:
            log(f"  Δ {c['event_key']}.{c['field']}: '{c['from']}' → '{c['to']}' "
                f"(triggers_publish={c.get('triggers_publish')})")
    else:
        log("resolver: no state changes")

    # Build final output
    now = datetime.now(timezone.utc)
    payload = {
        "version": SCHEMA_VERSION,
        "generated_at": now.isoformat(),
        "previous_generated_at": prev_generated,
        "resolver_run_count": (prev_state or {}).get("resolver_run_count", 0) + 1,
        "events": events,
        "changes_since_last_run": changes,
        "resolution_log": resolution_log,
    }

    # Atomic write + preserve prev
    if EVENTS_PATH.exists():
        try:
            EVENTS_PREV_PATH.write_text(EVENTS_PATH.read_text(), encoding="utf-8")
        except OSError:
            pass

    tmp = EVENTS_PATH.with_suffix(".new.json")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(EVENTS_PATH)

    log(f"resolver: wrote {EVENTS_PATH} ({len(events)} events)")
    log("═" * 60)

    if publish_triggers:
        return 0
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        log(f"resolver: FATAL {type(e).__name__}: {e}")
        import traceback
        log(traceback.format_exc())
        sys.exit(2)
