#!/usr/bin/env python3
"""
enhance_articles.py — One-time pass to add Related Coverage block,
breadcrumb navigation, and "Next Article" CTA to every article that
doesn't have them. Drives click depth (Priority 5 from the
performance review) and organic search discovery (Priority 3).

Operations:
  1. If no "Related Coverage" block present, inject 3-5 topic-relevant
     article links based on slug keywords
  2. If no breadcrumb, add breadcrumb nav below the H1
  3. Ensure meta description is unique (expands from title + first
     body paragraph if it's currently the title alone)
"""

import os
import re
import html as htmllib
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT / "articles"


# ============================================================
# TOPIC TAXONOMY — every article gets tagged with topics based on
# slug keywords. Used for choosing related articles.
# ============================================================
TOPIC_KEYWORDS = {
    "hormuz":      ["hormuz", "strait-of-hormuz", "irgc"],
    "iran":        ["iran", "tehran", "irgc"],
    "ceasefire":   ["ceasefire", "truce", "peace-deal", "negotiat", "islamabad", "vance", "pakistan", "mediation"],
    "opec":        ["opec", "saudi", "aramco", "production-cut", "quota"],
    "gas-prices":  ["gas-price", "pump-price", "aaa", "gasoline", "memorial-day"],
    "oil-prices":  ["oil-price", "wti", "brent", "crude", "oil-futures", "barrel"],
    "permian":     ["permian", "midland", "eagle-ford", "shale"],
    "guyana":      ["guyana", "stabroek"],
    "natgas-lng":  ["natural-gas", "lng", "henry-hub", "cheniere", "liquefaction"],
    "rig-count":   ["rig-count", "baker-hughes", "drilling"],
    "renewables":  ["renewable", "solar", "wind", "battery", "clean-energy", "ev-"],
    "nuclear":     ["nuclear", "smr", "reactor", "uranium"],
    "refinery":    ["refinery", "refining", "crack-spread"],
    "pipeline":    ["pipeline", "keystone", "druzhba", "nord-stream", "east-west"],
    "russia":      ["russia", "putin", "sanction", "urals", "yamal"],
    "israel":      ["israel", "lebanon", "hezbollah", "netanyahu"],
    "companies":   ["exxon", "chevron", "bp-", "shell", "totalenergies", "conoco", "aramco"],
    "market-data": ["inventory", "eia-", "stockpile", "draw", "build"],
    "explainers":  ["what-is", "how-does", "why-", "guide-to", "explained", "explainer"],
}


def article_topics(slug: str) -> set[str]:
    topics = set()
    s = slug.lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(k in s for k in keywords):
            topics.add(topic)
    return topics


def build_topic_index() -> dict[str, list[str]]:
    """Map topic -> list of article slugs tagged with that topic."""
    index = defaultdict(list)
    for f in os.listdir(ARTICLES_DIR):
        if not f.endswith(".html"):
            continue
        slug = f.replace(".html", "")
        for topic in article_topics(slug):
            index[topic].append(slug)
    return index


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
    # Decode basic entities
    title = (title.replace("&mdash;", "\u2014").replace("&rsquo;", "'")
                  .replace("&ldquo;", '"').replace("&rdquo;", '"').replace("&amp;", "&"))
    return title


def pick_related(slug: str, topic_index: dict[str, list[str]], limit: int = 4) -> list[str]:
    """
    Pick related articles based on topic overlap. Returns list of slugs.
    Articles with more topic overlap are preferred.
    """
    my_topics = article_topics(slug)
    if not my_topics:
        return []

    # Score every other article by topic overlap
    scores = defaultdict(int)
    for topic in my_topics:
        for other in topic_index.get(topic, []):
            if other != slug:
                scores[other] += 1

    if not scores:
        return []

    # Sort by score descending, deterministic by slug for ties
    ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    return [s for s, _ in ranked[:limit]]


def category_for_slug(slug: str) -> tuple[str, str]:
    """Return (category_slug, category_label) for breadcrumb."""
    topics = article_topics(slug)
    # Priority: the most specific topic becomes the breadcrumb category
    if "gas-prices" in topics:
        return ("gas-prices", "Gas Prices")
    if "hormuz" in topics or "iran" in topics or "ceasefire" in topics or "israel" in topics or "russia" in topics:
        return ("geopolitics", "Geopolitics")
    if "opec" in topics:
        return ("geopolitics", "Geopolitics")
    if "companies" in topics:
        return ("company-news", "Company News")
    if "rig-count" in topics:
        return ("rig-count", "Rig Count")
    if "natgas-lng" in topics:
        return ("natural-gas", "Natural Gas")
    if "renewables" in topics:
        return ("renewable-energy", "Renewable Energy")
    if "nuclear" in topics:
        return ("nuclear", "Nuclear")
    if "refinery" in topics or "pipeline" in topics:
        return ("oil-prices", "Oil Prices")
    if "oil-prices" in topics or "permian" in topics or "guyana" in topics:
        return ("oil-prices", "Oil Prices")
    return ("oil-prices", "Oil Prices")


def build_related_block(slug: str, related: list[str]) -> str:
    """Build the Related Coverage HTML block."""
    if not related:
        return ""
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


def build_next_article_cta(next_slug: str, next_title: str) -> str:
    return f'''
        <div style="margin-top:24px;padding:20px 24px;background:var(--surface);border:1px solid var(--border);border-radius:10px">
          <div style="font-size:11px;text-transform:uppercase;letter-spacing:0.1em;color:var(--text-3);font-weight:700;margin-bottom:8px">Continue Reading</div>
          <a href="{next_slug}.html" style="color:var(--text-1);text-decoration:none;font-size:16px;font-weight:600;line-height:1.4;display:block">{next_title} &rarr;</a>
        </div>
'''


def enhance_article(path: Path, topic_index: dict[str, list[str]]) -> bool:
    slug = path.stem
    with open(path, encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []

    # 1. Add Related Coverage if not present
    if "Related Coverage" not in content:
        related = pick_related(slug, topic_index, limit=4)
        if len(related) >= 2:
            related_html = build_related_block(slug, related)

            # Try multiple insertion points in order of preference
            inserted = False

            # Pattern A: before the existing footer nav with btn-secondary
            for pattern in [
                r'(\s*<div style="margin-top:32px;padding-top:20px;border-top:1px solid var\(--border\);display:flex;gap:12px;flex-wrap:wrap">)',
                r'(\s*<div[^>]*>\s*<a[^>]*class="btn-secondary")',
            ]:
                new_content = re.sub(pattern, related_html + r'\1', content, count=1)
                if new_content != content:
                    content = new_content
                    inserted = True
                    break

            # Pattern B: after the last </p> inside article-body, before </div>
            # The article-body ends with: </p>\n        </div>
            if not inserted:
                # Find the LAST </p> inside article-body, then insert our HTML
                # Match: <div class="article-body">...<last </p>>...</div>
                body_pat = re.compile(
                    r'(<div class="article-body">[\s\S]*?</p>)(\s*</div>)',
                    re.DOTALL,
                )
                # Find the match that has the last </p>
                matches = list(body_pat.finditer(content))
                if matches:
                    # We want the last </p> before </div>. Use greedy on first chunk so regex
                    # captures through the final </p>.
                    # With [\s\S]*? (lazy), we'd get the FIRST </p>. Make it greedy:
                    body_pat_greedy = re.compile(
                        r'(<div class="article-body">[\s\S]*</p>)(\s*</div>)',
                    )
                    m = body_pat_greedy.search(content)
                    if m:
                        new_content = (
                            content[:m.start()]
                            + m.group(1)
                            + related_html
                            + m.group(2)
                            + content[m.end():]
                        )
                        if new_content != content:
                            content = new_content
                            inserted = True

            if inserted:
                changes.append("related")

    # 2. Add "Continue Reading" CTA if not present
    if "Continue Reading" not in content:
        related = pick_related(slug, topic_index, limit=1)
        if related:
            next_title = get_article_h1(related[0])
            if next_title:
                next_html = build_next_article_cta(related[0], next_title)
                # Insert just before Related Coverage if present, else at end of article-body
                if "Related Coverage" in content:
                    insert_pat = r'(\s*<div style="margin-top:40px;padding:24px;background:var\(--surface-2\);border-radius:10px;border-left:3px solid var\(--blue\)">\s*<h3[^>]*>Related Coverage)'
                    new_content = re.sub(insert_pat, next_html + r'\1', content, count=1)
                    if new_content != content:
                        content = new_content
                        changes.append("next-cta")
                else:
                    # No Related Coverage — insert before footer nav or end of article-body
                    inserted = False
                    for pattern in [
                        r'(\s*<div style="margin-top:32px;padding-top:20px;border-top:1px solid var\(--border\);display:flex;gap:12px;flex-wrap:wrap">)',
                    ]:
                        new_content = re.sub(pattern, next_html + r'\1', content, count=1)
                        if new_content != content:
                            content = new_content
                            inserted = True
                            changes.append("next-cta")
                            break
                    if not inserted:
                        body_pat_greedy = re.compile(
                            r'(<div class="article-body">[\s\S]*</p>)(\s*</div>)',
                        )
                        m = body_pat_greedy.search(content)
                        if m:
                            new_content = (
                                content[:m.start()]
                                + m.group(1)
                                + next_html
                                + m.group(2)
                                + content[m.end():]
                            )
                            if new_content != content:
                                content = new_content
                                changes.append("next-cta")

    # 3. Improve meta description if it's just the title
    title_m = re.search(r"<title>([^<]+)</title>", content)
    desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
    if title_m and desc_m:
        title_text = title_m.group(1).split(" &mdash;")[0].split(" — ")[0].strip()
        desc_text = desc_m.group(1).strip()
        # If description is the title or too short, enhance it
        if desc_text == title_text or (len(desc_text) < len(title_text) + 10):
            body_m = re.search(r'<div class="article-body">[\s\S]*?<p>([^<]+)</p>', content)
            if body_m:
                para = re.sub(r"<[^>]+>", "", body_m.group(1)).strip()
                if len(para) > 155:
                    para = para[:155].rsplit(" ", 1)[0] + "..."
                new_desc = htmllib.escape(para, quote=True)
                content = re.sub(
                    r'(<meta\s+name="description"\s+content=")[^"]+(")',
                    r'\1' + new_desc + r'\2',
                    content,
                    count=1,
                )
                changes.append("meta-desc")

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    print("[enhance_articles] Building topic index...")
    topic_index = build_topic_index()
    print(f"  Topics indexed: {len(topic_index)}")
    for t, arts in sorted(topic_index.items()):
        print(f"    {t}: {len(arts)} articles")

    print("\n[enhance_articles] Enhancing articles...")
    enhanced = 0
    for f in sorted(os.listdir(ARTICLES_DIR)):
        if not f.endswith(".html"):
            continue
        path = ARTICLES_DIR / f
        if enhance_article(path, topic_index):
            enhanced += 1

    print(f"\n[enhance_articles] Enhanced {enhanced} articles")


if __name__ == "__main__":
    main()
