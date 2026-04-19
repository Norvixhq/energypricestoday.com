#!/usr/bin/env python3
"""
update_news.py — Fetch Google News RSS feeds for key energy topics,
deduplicate headlines, and refresh the BREAKING_NEWS block in data.js.

For every new headline that doesn't already have a matching article
file, create a stub article so the link resolves (no 404s).

Exit codes:
  0 — Updated successfully
  1 — No new headlines (nothing to do)
  2 — Error
"""

import html
import re
import sys
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).parent))
from lib import data_js  # noqa: E402
from lib import article_template  # noqa: E402

# Topics to query. Each feed returns top ~20 headlines.
# Combined + deduplicated, we'll pick 8 for BREAKING_NEWS.
TOPICS = [
    ("oil prices OR crude oil today", "Oil Markets", "oil-prices"),
    ("gas prices AAA today", "Gas Prices", "gas-prices"),
    ("Strait of Hormuz OR Iran ceasefire OR OPEC", "Geopolitics", "geopolitics"),
    ("natural gas LNG Henry Hub", "Natural Gas", "natural-gas"),
    ("refinery outage OR pipeline shutdown", "Energy", "oil-prices"),
]

RSS_URL = "https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"

HEADLINE_MIN_LEN = 30
HEADLINE_MAX_LEN = 130
MAX_HEADLINES = 8


def fetch_rss(query: str, timeout: int = 15) -> list[tuple[str, str]]:
    """Return list of (title, description) tuples from a Google News RSS feed."""
    url = RSS_URL.format(q=urllib.parse.quote_plus(query))
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/131.0.0.0 Safari/537.36",
            "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            xml_data = resp.read()
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"[update_news] RSS fetch failed for '{query}': {e}")
        return []

    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        print(f"[update_news] RSS parse failed for '{query}': {e}")
        return []

    items = []
    for item in root.iter("item"):
        t = item.findtext("title") or ""
        d = item.findtext("description") or ""
        t = html.unescape(t).strip()
        d = html.unescape(re.sub(r"<[^>]+>", "", d)).strip()
        # Google News appends " - Publisher" to titles — strip
        t = re.sub(r"\s+-\s+[^-]+$", "", t)
        if HEADLINE_MIN_LEN <= len(t) <= HEADLINE_MAX_LEN:
            items.append((t, d))
    return items


def clean_headline(title: str) -> str:
    """Normalize a headline to site voice."""
    # Remove ALL CAPS runs (Google News sometimes yells)
    if sum(1 for c in title if c.isupper()) / max(len(title), 1) > 0.4:
        # Too many caps — title-case it
        title = title.title()
        # Fix common words
        for word in ["Of", "The", "And", "To", "In", "On", "At", "By", "For", "With", "As"]:
            title = re.sub(rf"\b{word}\b", word.lower(), title)
        # Keep first word capitalized
        title = title[0].upper() + title[1:] if title else title
    # Collapse whitespace
    title = re.sub(r"\s+", " ", title)
    return title


def deduplicate(headlines: list[tuple[str, str, str, str]]) -> list[tuple[str, str, str, str]]:
    """
    Deduplicate by fuzzy title overlap.
    Keep first occurrence of each distinct story.
    """
    seen_stems = []
    out = []
    for title, desc, cat, slug in headlines:
        # Get significant word stem — first 5 content words
        words = [w for w in re.findall(r"\w+", title.lower()) if len(w) > 3]
        stem = " ".join(words[:5])
        # Check overlap with existing stems
        is_dup = False
        for existing in seen_stems:
            if stem == existing:
                is_dup = True
                break
            # Jaccard-style overlap
            a = set(words[:6])
            b = set(re.findall(r"\w+", existing))
            if a and b and len(a & b) / len(a | b) > 0.6:
                is_dup = True
                break
        if not is_dup:
            seen_stems.append(stem)
            out.append((title, desc, cat, slug))
    return out


def build_breaking_news_js(items: list[tuple[str, str, str, str]]) -> str:
    """Serialize the BREAKING_NEWS array."""
    lines = []
    for i, (title, desc, cat, slug) in enumerate(items):
        safe_title = title.replace('"', '\\"')
        time_label = f"{i+1}h"  # Relative hours ago — 1h, 2h, 3h...
        lines.append(
            f'  {{ title: "{safe_title}", cat: "{cat}", '
            f'slug: "{slug}", time: "{time_label}" }}'
        )
    entries = ",\n".join(lines)
    return f"const BREAKING_NEWS = [\n{entries},\n];"


def ensure_article_exists(title: str, summary: str) -> bool:
    """Create stub article if missing. Returns True if newly created."""
    slug = data_js.slugify(title)
    path = article_template.ARTICLES_DIR / f"{slug}.html"
    if path.exists():
        return False
    try:
        article_template.write_stub_article(title, summary)
        print(f"  [+] Created stub: {slug}")
        return True
    except Exception as e:
        print(f"  [!] Failed to create stub for '{title}': {e}")
        return False


def main() -> int:
    print("[update_news] Fetching RSS feeds...")
    all_items = []
    for query, cat, slug in TOPICS:
        results = fetch_rss(query)
        print(f"  {query[:50]}: {len(results)} headlines")
        for title, desc in results:
            cleaned = clean_headline(title)
            all_items.append((cleaned, desc, cat, slug))

    if not all_items:
        print("[update_news] No RSS results — network issue or all feeds empty")
        return 2

    # Dedupe and take top N
    unique_items = deduplicate(all_items)
    top_items = unique_items[:MAX_HEADLINES]
    print(f"[update_news] After dedup: {len(unique_items)} unique, taking top {len(top_items)}")

    # Compare to existing BREAKING_NEWS
    existing_titles = set(data_js.extract_titles_from_block("BREAKING_NEWS"))
    new_titles = set(t for t, _, _, _ in top_items)

    if existing_titles == new_titles:
        print("[update_news] Same top headlines — no change.")
        return 1

    # Write new BREAKING_NEWS block
    new_js = build_breaking_news_js(top_items)
    if not data_js.replace_block("BREAKING_NEWS", new_js):
        print("[update_news] Failed to replace BREAKING_NEWS block")
        return 2

    print(f"[update_news] ✓ Updated BREAKING_NEWS with {len(top_items)} headlines")

    # Ensure articles exist for every headline
    created = 0
    for title, desc, cat, slug in top_items:
        if ensure_article_exists(title, desc):
            created += 1
    print(f"[update_news] Created {created} new stub articles")

    return 0


if __name__ == "__main__":
    sys.exit(main())
