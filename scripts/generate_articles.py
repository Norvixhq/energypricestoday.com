#!/usr/bin/env python3
"""
generate_articles.py — Upgrade stub articles to full 4-paragraph articles
using the Anthropic API (Claude Haiku for cost efficiency).

Runs as part of the news update cycle. Finds articles marked as stubs
(via a marker comment in the HTML) and regenerates them with real body
content based on their title and any available context.

If ANTHROPIC_API_KEY is not set, this script no-ops cleanly —
the stub articles created by update_news.py remain as-is. This lets
Phase 1 work standalone without AI.

Exit codes:
  0 — Ran to completion (may have upgraded 0 or more articles)
  2 — Error
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib import article_template  # noqa: E402
from lib import quota  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-haiku-4-5-20251001"  # Cost-efficient; change to opus/sonnet if preferred
MAX_UPGRADES_PER_RUN = 8  # cap to control cost


STUB_MARKER = "This is a developing story. For the latest"  # inserted by write_stub_article


SYSTEM_PROMPT = """You are a writer for EnergyPricesToday.com, a modern energy intelligence website covering oil, gas, geopolitics, and energy markets.

Your voice:
- Clear, factual, professional — no hype, no clickbait
- Short paragraphs (2-4 sentences each)
- Informed about energy markets, OPEC+, WTI/Brent, the Strait of Hormuz, refining, LNG, rig counts
- Uses precise numbers when reasonable, honest uncertainty when not
- Never speculates beyond what the title supports

You output JSON only, no prose outside the JSON."""


def get_stub_articles() -> list[Path]:
    """Find article files that are currently stubs (short body, marker present)."""
    stubs = []
    for f in ARTICLES_DIR.glob("*.html"):
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue
        if STUB_MARKER in content:
            stubs.append(f)
    return stubs


def extract_title(html: str) -> str | None:
    m = re.search(r"<h1[^>]*>([^<]+)</h1>", html)
    return m.group(1).strip() if m else None


def call_claude(title: str) -> list[str] | None:
    """Ask Claude for 4 body paragraphs about the topic."""
    user_prompt = f"""Write a 4-paragraph article body for this headline:

"{title}"

Requirements:
- Exactly 4 paragraphs
- 2-4 sentences each
- Professional news voice for an energy markets site
- Do not repeat the headline verbatim in the first paragraph
- Use simple HTML entities only (&mdash; &rsquo; &ldquo; &rdquo;). No raw apostrophes or quotes that would break HTML.
- Do not speculate on specific prices or figures not implied by the headline
- Do not invent sources, names, or numbers

Return JSON only:
{{"paragraphs": ["para 1", "para 2", "para 3", "para 4"]}}
"""

    req_body = json.dumps({
        "model": MODEL,
        "max_tokens": 800,
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_prompt}],
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=req_body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            quota.record("anthropic", endpoint="messages", succeeded=True)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        quota.record("anthropic", endpoint="messages", succeeded=False)
        print(f"  [!] API error for '{title[:40]}...': {e}")
        return None
    except json.JSONDecodeError:
        quota.record("anthropic", endpoint="messages", succeeded=False)
        print(f"  [!] API returned invalid JSON for '{title[:40]}...'")
        return None

    # Extract text from response
    try:
        text = data["content"][0]["text"]
    except (KeyError, IndexError):
        print(f"  [!] Unexpected API response shape for '{title[:40]}...'")
        return None

    # Parse JSON out of response
    # Strip any markdown fences
    text = re.sub(r"```json\s*|\s*```", "", text).strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        # Sometimes Claude wraps in extra prose; try to find the JSON block
        m = re.search(r"\{[^{}]*\"paragraphs\"[^{}]*\[.*?\][^{}]*\}", text, re.DOTALL)
        if not m:
            return None
        try:
            parsed = json.loads(m.group(0))
        except json.JSONDecodeError:
            return None

    paragraphs = parsed.get("paragraphs", [])
    if not isinstance(paragraphs, list) or len(paragraphs) < 3:
        return None
    # Sanity: reject if any paragraph is suspiciously short or contains obvious placeholders
    for p in paragraphs:
        if len(p) < 30 or "lorem ipsum" in p.lower() or "[TODO]" in p:
            return None
    return paragraphs[:4]


def upgrade_stub(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    title = extract_title(html)
    if not title:
        return False

    print(f"  upgrading: {path.name}")
    paragraphs = call_claude(title)
    if not paragraphs:
        print(f"  [!] Skipping {path.name} — API call failed")
        return False

    # Rewrite the article with full body, preserving date if present
    date_m = re.search(r"<span>([A-Z][a-z]{2} \d{1,2}, \d{4})</span>", html)
    date_str = date_m.group(1) if date_m else None

    # Extract slug from filename
    slug = path.stem
    category = article_template.infer_category(title)

    article_template.write_article(
        title,
        paragraphs,
        slug=slug,
        category=category,
        date_str=date_str,
        overwrite=True,
    )
    return True


def main() -> int:
    if not API_KEY:
        print("[generate_articles] ANTHROPIC_API_KEY not set — skipping (Phase 1 mode)")
        return 0

    stubs = get_stub_articles()
    if not stubs:
        print("[generate_articles] No stubs to upgrade")
        return 0

    to_upgrade = stubs[:MAX_UPGRADES_PER_RUN]
    print(f"[generate_articles] Found {len(stubs)} stubs, upgrading {len(to_upgrade)}")

    upgraded = 0
    for path in to_upgrade:
        if upgrade_stub(path):
            upgraded += 1

    print(f"[generate_articles] ✓ Upgraded {upgraded}/{len(to_upgrade)} articles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
