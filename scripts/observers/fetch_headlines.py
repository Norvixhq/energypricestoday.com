#!/usr/bin/env python3
"""
fetch_headlines.py — Phase 2.1 multi-source headline observer.

Ingests headlines from multiple lawful/free sources, normalizes them into a
common schema, and caches per-topic JSON for downstream consumption by:
  - the homepage breaking banner (fallback when rss2json fails)
  - the Live Headlines blocks on every pillar page
  - the story clustering layer (Phase 2.2)
  - the event-state resolver (Phase 2.3)

Sources (all free, no authentication needed):
  1. Google News RSS  — broad, already known-good
  2. GDELT 2.0 DOC    — entity/event codes, global coverage
  3. (future) EIA STEO RSS, Reuters public RSS

Output:
  data/sources/headlines-{topic}.json   — one cache file per topic

Normalized schema for every story:
  {
    "id":          "<fingerprint-sha1>",      # dedupe key
    "title":       "<clean title>",
    "url":         "<https://...>",
    "source":      "<publisher name>",
    "source_type": "rss" | "gdelt",
    "published_at": "<iso 8601>",
    "fetched_at":  "<iso 8601>",
    "topic":       "<energy|geopolitics|gasoline|natgas|...>",
    "entities":    ["Iran", "Hormuz", "OPEC", ...],
    "confidence":  <0..1>,                    # source-quality weight
  }

Exit codes:
  0 — updated successfully (wrote fresh cache)
  1 — no changes / all sources failed gracefully
  2 — unrecoverable error
"""

from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent.parent
CACHE_DIR = ROOT / "data" / "sources"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

# ─── Topic definitions ─────────────────────────────────────────────
# Each topic → (google_news_query, gdelt_query, entity_hints)
# entity_hints are used to boost confidence when matched in titles.
TOPICS = {
    "energy":      ("oil prices OR energy markets",
                    "oil price OR crude OR energy market",
                    ["oil", "crude", "energy", "WTI", "Brent"]),
    "geopolitics": ("Iran OR Hormuz OR OPEC OR Middle East oil",
                    "Iran oil OR Hormuz OR OPEC",
                    ["Iran", "Hormuz", "OPEC", "Israel", "Saudi", "Yemen", "Gaza", "Russia", "Ukraine"]),
    "oil":         ("crude oil OR Brent OR WTI",
                    "crude oil OR Brent OR WTI",
                    ["WTI", "Brent", "crude", "oil", "barrel"]),
    "gasoline":    ("gas prices OR gasoline OR pump prices",
                    "gas prices OR gasoline",
                    ["gasoline", "pump", "AAA", "retail"]),
    "natgas":      ("natural gas OR LNG OR Henry Hub",
                    "natural gas OR LNG",
                    ["natural gas", "LNG", "Henry Hub", "TTF", "JKM"]),
    "heating":     ("heating oil OR distillate OR diesel",
                    "heating oil OR diesel",
                    ["heating oil", "diesel", "distillate", "ULSD"]),
    "rigcount":    ("oil rig count OR Baker Hughes OR drilling",
                    "oil rig count OR drilling",
                    ["Baker Hughes", "rig count", "drilling", "Permian"]),
    "renewables":  ("renewable energy OR solar OR wind energy",
                    "renewable energy OR solar power OR wind power",
                    ["solar", "wind", "renewable", "battery", "hydrogen"]),
    "companies":   ("ExxonMobil OR Chevron OR Shell OR Aramco OR BP",
                    "ExxonMobil OR Chevron OR Shell OR Saudi Aramco",
                    ["Exxon", "Chevron", "Shell", "Aramco", "BP", "TotalEnergies"]),
    "breaking":    ("oil energy breaking news OR Middle East attack",
                    "oil attack OR refinery OR pipeline OR tanker",
                    ["attack", "outage", "disruption", "ceasefire", "sanctions"]),
}

# ─── Source quality weights (drives confidence) ────────────────────
SOURCE_WEIGHTS = {
    # Tier-1 wire / financial / official
    "reuters.com":   0.95,
    "bloomberg.com": 0.95,
    "ft.com":        0.92,
    "wsj.com":       0.92,
    "ap.org":        0.92,
    "apnews.com":    0.92,
    "cnbc.com":      0.88,
    "energy.gov":    0.95,
    "eia.gov":       0.95,
    # Tier-2 industry
    "oilprice.com":     0.82,
    "spglobal.com":     0.88,
    "platts.com":       0.88,
    "argusmedia.com":   0.85,
    "rigzone.com":      0.82,
    "bakerhughes.com":  0.95,
    # Tier-2 quality general
    "bbc.com":       0.85,
    "bbc.co.uk":     0.85,
    "theguardian.com": 0.80,
    "economist.com": 0.88,
    # Default unknown
    "_default":      0.60,
}

# ─── HTTP helpers ──────────────────────────────────────────────────
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)

def http_get(url: str, timeout: int = 15, accept: str = "*/*") -> bytes | None:
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": accept,
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
        print(f"[fetch_headlines] HTTP fail {url[:80]}...: {e}")
        return None


# ─── Source: Google News RSS ───────────────────────────────────────
def fetch_google_news(query: str) -> list[dict]:
    """Return list of normalized story dicts from Google News RSS."""
    url = "https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en".format(
        q=urllib.parse.quote_plus(query)
    )
    xml = http_get(url, accept="application/rss+xml, application/xml")
    if not xml:
        return []

    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        print(f"[fetch_headlines] google_news parse fail: {e}")
        return []

    stories = []
    for item in root.findall(".//item"):
        title_el = item.find("title")
        link_el  = item.find("link")
        pub_el   = item.find("pubDate")
        src_el   = item.find("source")
        if title_el is None or title_el.text is None:
            continue
        if link_el is None or link_el.text is None:
            continue

        title_raw = html.unescape(title_el.text).strip()
        link = link_el.text.strip()
        source = src_el.text.strip() if (src_el is not None and src_el.text) else ""

        # Google News titles often end with " - Source" — split cleanly
        if not source:
            dash_idx = title_raw.rfind(" - ")
            if dash_idx > 20:
                source = title_raw[dash_idx + 3:].strip()
                title = title_raw[:dash_idx].strip()
            else:
                title = title_raw
        else:
            # Strip the trailing " - Source" if present
            suffix = f" - {source}"
            if title_raw.endswith(suffix):
                title = title_raw[:-len(suffix)].strip()
            else:
                title = title_raw

        # Parse RFC-822 pubDate
        pub_iso = ""
        if pub_el is not None and pub_el.text:
            pub_iso = parse_rfc822(pub_el.text.strip())

        stories.append({
            "title": title,
            "url": link,
            "source": source or "Google News",
            "source_type": "rss",
            "published_at": pub_iso,
        })
    return stories


# ─── Source: GDELT 2.0 DOC API ─────────────────────────────────────
def fetch_gdelt(query: str) -> list[dict]:
    """Return list of normalized story dicts from GDELT 2.0 DOC API."""
    # GDELT DOC API: Article search, JSON response, past 24h
    params = {
        "query": f"{query} sourcelang:english",
        "mode": "ArtList",
        "maxrecords": 25,
        "format": "json",
        "timespan": "24h",
        "sort": "DateDesc",
    }
    url = "https://api.gdeltproject.org/api/v2/doc/doc?" + urllib.parse.urlencode(params)
    raw = http_get(url, accept="application/json")
    if not raw:
        return []

    try:
        data = json.loads(raw.decode("utf-8", errors="replace"))
    except json.JSONDecodeError as e:
        print(f"[fetch_headlines] gdelt parse fail: {e}")
        return []

    articles = data.get("articles") or []
    stories = []
    for a in articles:
        title = (a.get("title") or "").strip()
        url_  = (a.get("url") or "").strip()
        if not title or not url_:
            continue
        source = (a.get("domain") or "").strip()
        seen   = (a.get("seendate") or "").strip()
        # GDELT seendate is YYYYMMDDTHHMMSSZ
        pub_iso = ""
        if len(seen) >= 15:
            try:
                dt = datetime.strptime(seen[:15], "%Y%m%dT%H%M%S").replace(tzinfo=timezone.utc)
                pub_iso = dt.isoformat()
            except ValueError:
                pub_iso = ""
        stories.append({
            "title": title,
            "url": url_,
            "source": source,
            "source_type": "gdelt",
            "published_at": pub_iso,
        })
    return stories


# ─── Normalization & fingerprinting ────────────────────────────────
def parse_rfc822(s: str) -> str:
    """Parse RFC-822 pubDate string → ISO 8601. Returns "" on failure."""
    from email.utils import parsedate_to_datetime
    try:
        dt = parsedate_to_datetime(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except (TypeError, ValueError):
        return ""


def normalize_title_for_fingerprint(title: str) -> str:
    """Lowercase, strip punctuation, keep first 8 significant words."""
    t = title.lower()
    t = re.sub(r"[^\w\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    words = t.split()
    stopwords = {"the","a","an","of","in","on","at","to","for","and","or","but","with","by","from","as","is","are","was","were","has","have"}
    sig_words = [w for w in words if w not in stopwords][:8]
    return " ".join(sig_words)


def extract_entities(title: str, entity_hints: list[str]) -> list[str]:
    """Return entities from the hint list that appear in the title."""
    t_lower = title.lower()
    found = []
    for e in entity_hints:
        if e.lower() in t_lower:
            found.append(e)
    return found


def compute_confidence(story: dict, entity_hints: list[str]) -> float:
    """Combine source quality + entity relevance into a 0..1 confidence score."""
    # Source quality
    domain = ""
    if story.get("source"):
        # Try extract domain-like token
        s = story["source"].lower()
        if "." in s and " " not in s:
            domain = s
        else:
            # Map known source names → domain for weighting
            # Map common Google-News-displayed names back to domains
            name_to_domain = {
                "reuters": "reuters.com", "bloomberg": "bloomberg.com",
                "the wall street journal": "wsj.com", "wsj": "wsj.com",
                "the associated press": "ap.org", "ap": "ap.org", "associated press": "ap.org",
                "cnbc": "cnbc.com", "financial times": "ft.com",
                "oilprice.com": "oilprice.com", "s&p global": "spglobal.com",
                "bbc": "bbc.com", "the guardian": "theguardian.com",
                "the economist": "economist.com", "rigzone": "rigzone.com",
            }
            domain = name_to_domain.get(s, "")

    quality = SOURCE_WEIGHTS.get(domain, SOURCE_WEIGHTS["_default"])

    # Entity relevance — more matched entities = higher relevance
    entities = extract_entities(story.get("title", ""), entity_hints)
    entity_boost = min(len(entities) * 0.05, 0.20)  # cap at +0.20

    return round(min(quality + entity_boost, 1.0), 3)


def fingerprint_story(story: dict) -> str:
    """Create a dedupe-friendly fingerprint for a story."""
    title_norm = normalize_title_for_fingerprint(story.get("title", ""))
    # 6-hour bucket so we don't fragment same story across timezones
    pub = story.get("published_at", "")
    bucket = ""
    if pub:
        try:
            dt = datetime.fromisoformat(pub.replace("Z", "+00:00"))
            bucket = dt.strftime("%Y%m%d%H")[:9]  # YYYYMMDDH (6-hr buckets: H/4)
            bucket = bucket[:-1] + str(int(bucket[-1]) // 6 * 6)
        except ValueError:
            bucket = ""
    raw = f"{title_norm}|{bucket}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def normalize_story(raw: dict, topic: str, entity_hints: list[str]) -> dict:
    """Take raw source output, produce normalized story dict."""
    title = raw.get("title", "").strip()
    entities = extract_entities(title, entity_hints)
    confidence = compute_confidence(raw, entity_hints)
    return {
        "id": fingerprint_story(raw),
        "title": title,
        "url": raw.get("url", ""),
        "source": raw.get("source", ""),
        "source_type": raw.get("source_type", "rss"),
        "published_at": raw.get("published_at", ""),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "topic": topic,
        "entities": entities,
        "confidence": confidence,
    }


# ─── Topic fetch + merge ───────────────────────────────────────────
def fetch_topic(topic: str) -> dict:
    """Fetch a single topic from all sources, merge + dedupe + cache."""
    g_query, gdelt_query, entity_hints = TOPICS[topic]

    all_raw = []
    all_raw.extend(fetch_google_news(g_query))
    all_raw.extend(fetch_gdelt(gdelt_query))

    # Normalize + dedupe by fingerprint, keep highest-confidence version
    by_id = {}
    for raw in all_raw:
        if not raw.get("title") or not raw.get("url"):
            continue
        story = normalize_story(raw, topic, entity_hints)
        existing = by_id.get(story["id"])
        if existing is None or story["confidence"] > existing["confidence"]:
            by_id[story["id"]] = story

    # Sort by (confidence desc, published_at desc)
    stories = sorted(
        by_id.values(),
        key=lambda s: (s["confidence"], s["published_at"]),
        reverse=True,
    )
    # Keep top 30 per topic — plenty of headroom for consumers
    stories = stories[:30]

    return {
        "topic": topic,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(stories),
        "sources_used": list({s["source_type"] for s in stories}),
        "stories": stories,
    }


def write_cache(topic: str, payload: dict) -> bool:
    """Atomically write topic cache. Return True if content actually changed."""
    target = CACHE_DIR / f"headlines-{topic}.json"
    new_text = json.dumps(payload, indent=2, ensure_ascii=False)

    # Compare to existing (ignore generated_at timestamp)
    changed = True
    if target.exists():
        try:
            existing = json.loads(target.read_text())
            existing_ids = sorted(s["id"] for s in existing.get("stories", []))
            new_ids = sorted(s["id"] for s in payload.get("stories", []))
            if existing_ids == new_ids:
                changed = False
        except (json.JSONDecodeError, KeyError):
            pass

    if changed:
        tmp = target.with_suffix(".new.json")
        tmp.write_text(new_text, encoding="utf-8")
        tmp.replace(target)
    return changed


# ─── Entry point ───────────────────────────────────────────────────
def main() -> int:
    print(f"[fetch_headlines] Starting multi-source headline observer — {len(TOPICS)} topics")
    any_changed = False
    total_stories = 0
    failed_topics = []

    for topic in TOPICS:
        try:
            payload = fetch_topic(topic)
            changed = write_cache(topic, payload)
            status = "CHANGED" if changed else "same"
            print(f"  {topic:14s} {payload['count']:3d} stories ({','.join(payload['sources_used']) or 'no sources'})  {status}")
            total_stories += payload["count"]
            if changed:
                any_changed = True
            if payload["count"] == 0:
                failed_topics.append(topic)
        except Exception as e:
            print(f"  {topic:14s} ERROR: {e}")
            failed_topics.append(topic)

    # Aggregate index file so consumers can discover topics without filesystem listing
    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topics": list(TOPICS.keys()),
        "total_stories": total_stories,
        "failed_topics": failed_topics,
    }
    (CACHE_DIR / "headlines-index.json").write_text(
        json.dumps(index, indent=2), encoding="utf-8"
    )

    if failed_topics and len(failed_topics) == len(TOPICS):
        print("[fetch_headlines] ALL topics failed — probably a network issue")
        return 2
    if any_changed:
        print(f"[fetch_headlines] ✓ cache updated ({total_stories} total stories, {len(failed_topics)} failed topics)")
        return 0
    print(f"[fetch_headlines] no changes ({total_stories} stories cached)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
