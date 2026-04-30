#!/usr/bin/env python3
"""
One-shot SEO upgrade for every article page.

Adds:
  - article:published_time and article:modified_time meta
  - article:author and article:section meta
  - news_keywords + googlebot-news robots directive
  - twitter:card upgrade to summary_large_image
  - og:image (default site OG card)
  - NewsArticle JSON-LD schema with publisher reference

Idempotent: skipped if the page already has article:published_time meta.
"""
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

PUBLISHER_LD = (
    '"publisher":{"@type":"NewsMediaOrganization","name":"EnergyPricesToday.com",'
    '"url":"https://www.energypricestoday.com",'
    '"logo":{"@type":"ImageObject","url":"https://www.energypricestoday.com/images/logo.png","width":674,"height":130}}'
)

DEFAULT_OG_IMAGE = "https://www.energypricestoday.com/images/og-image.png"

# Map article URL slug suffix → category for article:section meta
def infer_section(slug, breadcrumb_text):
    s = slug.lower()
    bt = (breadcrumb_text or '').lower()
    if 'gas-prices' in s or 'aaa' in s or 'pump' in s or 'gas average' in s: return 'Gas Prices'
    if 'electric' in s or 'kwh' in s: return 'Electricity'
    if 'rig-count' in s or 'baker hughes' in bt: return 'Rig Count'
    if 'opec' in s: return 'OPEC'
    if 'lng' in s or 'natural-gas' in s: return 'Natural Gas'
    if 'iran' in s or 'hormuz' in s or 'lebanon' in s or 'pakistan' in s or 'trump' in s or 'geopolitics' in bt: return 'Geopolitics'
    if 'wti' in s or 'brent' in s or 'crude' in s or 'oil' in s or 'oil markets' in bt: return 'Oil Markets'
    if 'company' in bt or 'earnings' in s or 'cheniere' in s or 'exxonmobil' in s: return 'Company News'
    return 'Energy'

MONTH_TO_NUM = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

def date_to_iso(date_str):
    """Convert 'April 27, 2026' → '2026-04-27T08:00:00-04:00' (publish time, ET)."""
    m = re.match(r'(\w+)\s+(\d+),\s+(\d+)', (date_str or '').strip())
    if not m: return None
    mon, day, year = m.group(1), int(m.group(2)), int(m.group(3))
    if mon not in MONTH_TO_NUM: return None
    # Default publish time: 8 AM ET
    return f"{year:04d}-{MONTH_TO_NUM[mon]:02d}-{day:02d}T08:00:00-04:00"

def iso_now():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S-04:00")

def upgrade_article(path):
    txt = path.read_text(encoding='utf-8', errors='ignore')

    # Skip if already upgraded
    if 'article:published_time' in txt:
        return False, 'already upgraded'

    # Extract article-level info from existing markup
    title_m = re.search(r'<title>([^<]+)</title>', txt)
    title = title_m.group(1) if title_m else 'Article'
    title_clean = title.split(' | ')[0].strip()

    desc_m = re.search(r'<meta name="description" content="([^"]+)"', txt)
    description = desc_m.group(1) if desc_m else ''

    canonical_m = re.search(r'<link rel="canonical" href="([^"]+)"', txt)
    canonical = canonical_m.group(1) if canonical_m else f'https://www.energypricestoday.com/articles/{path.name}'

    meta_m = re.search(r'<div class="article-meta"[^>]*>.*?<span>([^<]*)</span>\s*<span>([^<]*)</span>\s*<span>([^<]*)</span>', txt, re.DOTALL)
    author = (meta_m.group(1) if meta_m else 'Staff').strip() or 'Staff'
    date_str = (meta_m.group(2) if meta_m else '').strip()
    read_time = (meta_m.group(3) if meta_m else '').strip()

    breadcrumb_m = re.search(r'<a href="\.\./category/[^"]+"[^>]*>([^<]+)</a>', txt)
    breadcrumb_text = breadcrumb_m.group(1) if breadcrumb_m else ''

    section = infer_section(path.stem, breadcrumb_text)
    iso_pub = date_to_iso(date_str)
    iso_mod = iso_pub  # treat publish time as last-modified by default

    # Word count (rough — for schema.wordCount)
    body_m = re.search(r'<div class="article-body">(.*?)</div>\s*\n', txt, re.DOTALL)
    word_count = 0
    if body_m:
        plain = re.sub(r'<[^>]+>', ' ', body_m.group(1))
        word_count = len(plain.split())

    # Build keyword list from title + section
    kw_seed = title_clean.lower()
    keywords = [section.lower(), 'energy', 'oil prices', 'energy markets']
    if 'iran' in kw_seed or 'hormuz' in kw_seed: keywords += ['Iran', 'Strait of Hormuz', 'Middle East']
    if 'wti' in kw_seed or 'brent' in kw_seed or 'crude' in kw_seed: keywords += ['WTI', 'Brent crude', 'oil prices']
    if 'gas' in kw_seed and 'natural' not in kw_seed: keywords += ['gas prices', 'AAA', 'gasoline']
    if 'opec' in kw_seed: keywords += ['OPEC', 'oil supply']
    if 'lng' in kw_seed: keywords += ['LNG', 'natural gas']
    if 'rig' in kw_seed or 'baker' in kw_seed: keywords += ['Baker Hughes', 'rig count']
    keywords_str = ', '.join(dict.fromkeys(keywords))

    # ── Build the upgrade block ────────────────────────────────────
    upgrade = f'''
  <meta name="news_keywords" content="{keywords_str}">
  <meta name="keywords" content="{keywords_str}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
  <meta name="googlebot-news" content="index, follow">
  <meta property="article:published_time" content="{iso_pub or iso_now()}">
  <meta property="article:modified_time" content="{iso_mod or iso_now()}">
  <meta property="article:author" content="{author}">
  <meta property="article:section" content="{section}">
  <meta property="article:tag" content="{section}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="EnergyPricesToday.com">
  <meta property="og:image" content="{DEFAULT_OG_IMAGE}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@energypricestoday">
  <meta name="twitter:title" content="{title_clean[:70]}">
  <meta name="twitter:description" content="{description[:200].replace('"', '&quot;')}">
  <meta name="twitter:image" content="{DEFAULT_OG_IMAGE}">'''

    # NewsArticle schema
    headline = title_clean.replace('"', '\\"')[:110]
    desc_safe = description.replace('"', '\\"')[:500]
    news_schema = (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@type":"NewsArticle",'
        f'"headline":"{headline}",'
        f'"description":"{desc_safe}",'
        f'"datePublished":"{iso_pub or iso_now()}",'
        f'"dateModified":"{iso_mod or iso_now()}",'
        f'"author":[{{"@type":"Organization","name":"EnergyPricesToday Staff","url":"https://www.energypricestoday.com/about.html"}}],'
        f'"image":["{DEFAULT_OG_IMAGE}"],'
        f'"articleSection":"{section}",'
        f'"wordCount":{word_count},'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{canonical}"}},'
        f'"isAccessibleForFree":true,'
        f'{PUBLISHER_LD}'
        '}</script>'
    )

    # Insert upgrade right after og:description (so all OG-related tags sit together)
    og_desc_pat = re.compile(r'(<meta property="og:description"[^>]*>)', re.DOTALL)
    if og_desc_pat.search(txt):
        new_txt = og_desc_pat.sub(r'\1' + upgrade, txt, count=1)
    else:
        # Fallback: inject before </head>
        new_txt = txt.replace('</head>', upgrade + '\n</head>', 1)

    # Insert NewsArticle schema right before </head>
    new_txt = new_txt.replace('</head>', '  ' + news_schema + '\n</head>', 1)

    path.write_text(new_txt, encoding='utf-8')
    return True, f'{section} | {date_str}'


def main():
    upgraded = 0
    skipped = 0
    failed = 0
    for f in sorted(ARTICLES.glob('*.html')):
        try:
            ok, info = upgrade_article(f)
            if ok:
                upgraded += 1
            else:
                skipped += 1
        except Exception as e:
            failed += 1
            print(f"  ✗ {f.name}: {e}")
    print(f"Upgraded: {upgraded}")
    print(f"Skipped (already upgraded): {skipped}")
    print(f"Failed: {failed}")


if __name__ == '__main__':
    main()
