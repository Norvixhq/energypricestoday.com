#!/usr/bin/env python3
"""
complete_articles.py — Final standardization pass.

Closes the remaining gaps:
  1. Related Coverage on the remaining articles using fuzzy matching
     (significant-word overlap, not just keyword match)
  2. Continue Reading CTA on the remaining articles
  3. Unique meta descriptions on articles currently sharing template text

This is idempotent — running it twice is safe because each operation
checks for existing content before adding.
"""

import os
import re
import html as htmllib
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"

# Stopwords — ignored for fuzzy matching (too generic)
STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "into", "over",
    "under", "after", "before", "new", "now", "day", "days", "year", "years",
    "has", "have", "will", "would", "could", "should", "than", "more",
    "most", "less", "least", "some", "any", "all", "one", "two", "three",
    "first", "second", "third", "not", "but", "yet", "still", "also",
    "very", "about", "above", "below", "between", "across", "through",
    "during", "while", "amid", "upon", "without", "within", "says", "said",
    "was", "were", "been", "being", "are", "its", "their", "them", "they",
    "per", "since", "hours", "hour", "percent", "pct",
    # Time-related filler
    "today", "yesterday", "tomorrow", "morning", "evening", "night",
    # Common filler words
    "report", "reports", "reported", "reporting", "report", "update", "updates",
    "news", "latest", "breaking",
}


def tokens(slug: str) -> set[str]:
    """Significant words from a slug."""
    words = re.split(r"[\-_]+", slug.lower())
    return {w for w in words if len(w) >= 3 and w not in STOPWORDS and not w.isdigit()}


def token_overlap(a: set[str], b: set[str]) -> int:
    """Return count of shared significant tokens."""
    return len(a & b)


def get_article_h1(slug: str) -> str | None:
    path = ARTICLES_DIR / f"{slug}.html"
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        c = f.read()
    m = re.search(r"<h1[^>]*>([^<]+)</h1>", c)
    if not m:
        return None
    title = m.group(1).strip()
    title = (title.replace("&mdash;", "\u2014").replace("&rsquo;", "'")
                  .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&amp;", "&"))
    return title


def find_related_fuzzy(slug: str, all_slugs: list[str], limit: int = 4) -> list[str]:
    """
    Find related articles by significant-word token overlap.
    Used as a fallback when keyword-topic matching fails.
    """
    my_tokens = tokens(slug)
    if len(my_tokens) < 2:
        return []  # Not enough to work with

    # Score every other article
    scored = []
    for other in all_slugs:
        if other == slug:
            continue
        other_tokens = tokens(other)
        overlap = token_overlap(my_tokens, other_tokens)
        if overlap >= 2:  # Require at least 2 shared significant words
            scored.append((other, overlap))

    # Sort by overlap descending, then slug alphabetical for determinism
    scored.sort(key=lambda x: (-x[1], x[0]))
    return [s for s, _ in scored[:limit]]


def build_related_block(related: list[str]) -> str:
    items = []
    for r in related:
        title = get_article_h1(r) or r.replace("-", " ").title()
        items.append(
            f'              <li style="padding:6px 0"><a href="{r}.html" style="color:var(--blue);text-decoration:none;font-weight:500">{title}</a></li>'
        )
    return f'''
        <div style="margin-top:40px;padding:24px;background:var(--surface-2);border-radius:10px;border-left:3px solid var(--blue)">
          <h3 style="margin:0 0 14px 0;font-size:13px;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-2);font-weight:700">Related Coverage</h3>
          <ul style="margin:0;padding:0;list-style:none;line-height:1.7">
{chr(10).join(items)}
          </ul>
        </div>
'''


def build_continue_block(next_slug: str, next_title: str) -> str:
    return f'''
        <div style="margin-top:24px;padding:20px 24px;background:var(--surface);border:1px solid var(--border);border-radius:10px">
          <div style="font-size:11px;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-3);font-weight:700;margin-bottom:8px">Continue Reading</div>
          <a href="{next_slug}.html" style="color:var(--text-1);text-decoration:none;font-size:16px;font-weight:600;line-height:1.4;display:block">{next_title} &rarr;</a>
        </div>
'''


def insert_block_before_footer(content: str, block_html: str) -> tuple[str, bool]:
    """
    Insert block_html at the appropriate place near the end of article-body.
    Returns (new_content, inserted).
    """
    # Pattern A: before existing footer-nav div
    for pattern in [
        r'(\s*<div style="margin-top:32px;padding-top:20px;border-top:1px solid var\(--border\);display:flex;gap:12px;flex-wrap:wrap">)',
        r'(\s*<div[^>]*>\s*<a[^>]*class="btn-secondary")',
    ]:
        new_content = re.sub(pattern, block_html + r"\1", content, count=1)
        if new_content != content:
            return new_content, True

    # Pattern B: at the end of article-body (greedy to last </p>)
    body_pat = re.compile(r'(<div class="article-body">[\s\S]*</p>)(\s*</div>)')
    m = body_pat.search(content)
    if m:
        new_content = (
            content[:m.start()]
            + m.group(1)
            + block_html
            + m.group(2)
            + content[m.end():]
        )
        if new_content != content:
            return new_content, True

    return content, False


def insert_continue_before_related(content: str, continue_html: str) -> tuple[str, bool]:
    """Insert continue block right before Related Coverage."""
    related_pat = r'(\s*<div style="margin-top:40px;padding:24px;background:var\(--surface-2\);border-radius:10px;border-left:3px solid var\(--blue\)">\s*<h3[^>]*>Related Coverage)'
    new_content = re.sub(related_pat, continue_html + r"\1", content, count=1)
    return new_content, (new_content != content)


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s).strip()


def generate_unique_meta_desc(slug: str, title: str, body_paras: list[str], first_template_para: str | None) -> str:
    """
    Build a unique, concrete meta description from the article's title + body.
    Uses article-specific phrasing derived from the TITLE rather than generic
    template intro paragraphs.
    """
    # Strategy: open with a rewording of the title + include a specific detail
    # from the body that's likely unique to this article.
    # Then prune to 150-160 chars.
    title_clean = title.strip().rstrip(".")

    # Prefer the 2ND body paragraph if available (the 1st is often the shared template intro)
    detail_para = None
    if len(body_paras) >= 2:
        detail_para = strip_html(body_paras[1])
    elif body_paras:
        detail_para = strip_html(body_paras[0])

    # Extract first sentence of the detail paragraph
    first_sentence = ""
    if detail_para:
        sentences = re.split(r"(?<=[.!?])\s+", detail_para.strip())
        if sentences:
            first_sentence = sentences[0]

    # If the first paragraph we chose is the known repeated template text, try 3rd
    if first_template_para and detail_para and first_template_para.strip()[:80] == detail_para.strip()[:80]:
        if len(body_paras) >= 3:
            detail_para = strip_html(body_paras[2])
            sentences = re.split(r"(?<=[.!?])\s+", detail_para.strip())
            if sentences:
                first_sentence = sentences[0]

    # Combine title + first sentence of detail
    # Pattern: "{title}. {first_sentence}"
    combined = f"{title_clean}. {first_sentence}".strip()

    # Prune to 158 chars at word boundary
    if len(combined) > 158:
        combined = combined[:158].rsplit(" ", 1)[0] + "..."

    # Fallback: just use the title + a generic suffix if everything failed
    if len(combined) < 60:
        combined = f"{title_clean}. EnergyPricesToday.com covers live oil prices, U.S. gas prices, and energy geopolitics."
        if len(combined) > 158:
            combined = combined[:158].rsplit(" ", 1)[0] + "..."

    return combined


def process_article(
    path: Path,
    all_slugs: list[str],
    duplicate_descriptions: set[str],
) -> dict:
    """Process a single article. Returns dict of changes made."""
    slug = path.stem
    with open(path, encoding="utf-8") as f:
        content = f.read()
    original = content
    changes = {"related": False, "continue": False, "meta": False}

    # 1. Related Coverage — fuzzy match if still missing
    if "Related Coverage" not in content:
        related = find_related_fuzzy(slug, all_slugs, limit=4)
        if len(related) >= 2:
            block = build_related_block(related)
            content, inserted = insert_block_before_footer(content, block)
            if inserted:
                changes["related"] = True

    # 2. Continue Reading — fuzzy match if still missing
    if "Continue Reading" not in content:
        related = find_related_fuzzy(slug, all_slugs, limit=1)
        if related:
            next_title = get_article_h1(related[0])
            if next_title:
                block = build_continue_block(related[0], next_title)
                # Prefer inserting before Related Coverage if present
                if "Related Coverage" in content:
                    content, inserted = insert_continue_before_related(content, block)
                    if not inserted:
                        content, inserted = insert_block_before_footer(content, block)
                else:
                    content, inserted = insert_block_before_footer(content, block)
                if inserted:
                    changes["continue"] = True

    # 3. Unique meta description — rewrite if currently a duplicate
    title_m = re.search(r"<title>([^<]+)</title>", content)
    desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
    if title_m and desc_m:
        current_desc = desc_m.group(1).strip()
        if current_desc in duplicate_descriptions:
            # Extract title (strip site suffix)
            title_text = title_m.group(1)
            title_text = re.split(r"\s+[\u2014—]\s+EnergyPricesToday", title_text)[0]
            title_text = re.split(r"\s+\&mdash;\s+EnergyPricesToday", title_text)[0]
            title_text = htmllib.unescape(title_text).strip()

            # Grab body paragraphs
            body_m = re.search(r'<div class="article-body">([\s\S]*?)</div>', content)
            body_paras = []
            if body_m:
                body_paras = re.findall(r"<p>([\s\S]*?)</p>", body_m.group(1))

            # Build unique description
            new_desc = generate_unique_meta_desc(
                slug, title_text, body_paras, current_desc
            )
            new_desc_html = htmllib.escape(new_desc, quote=True)
            content = re.sub(
                r'(<meta\s+name="description"\s+content=")[^"]+(")',
                r"\1" + new_desc_html + r"\2",
                content,
                count=1,
            )
            changes["meta"] = True

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    return changes


def main():
    print("[complete_articles] Building catalog...")
    all_files = sorted(f for f in os.listdir(ARTICLES_DIR) if f.endswith(".html"))
    all_slugs = [f.replace(".html", "") for f in all_files]

    # Build set of duplicated meta descriptions (appear 2+ times)
    print("[complete_articles] Finding duplicate descriptions...")
    desc_counts = Counter()
    for f in all_files:
        with open(ARTICLES_DIR / f, encoding="utf-8") as fp:
            c = fp.read()
        m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', c)
        if m:
            desc_counts[m.group(1).strip()] += 1
    duplicate_descs = {d for d, n in desc_counts.items() if n >= 2}
    print(f"  Found {len(duplicate_descs)} duplicate descriptions across articles")

    # Process each article
    print("[complete_articles] Processing articles...")
    totals = Counter()
    for f in all_files:
        path = ARTICLES_DIR / f
        changes = process_article(path, all_slugs, duplicate_descs)
        for k, v in changes.items():
            if v:
                totals[k] += 1

    print(f"\n[complete_articles] Changes applied:")
    print(f"  Related Coverage added:    {totals['related']}")
    print(f"  Continue Reading added:    {totals['continue']}")
    print(f"  Meta descriptions rewritten: {totals['meta']}")


if __name__ == "__main__":
    main()
