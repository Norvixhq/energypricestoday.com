#!/usr/bin/env python3
"""
Generate an RSS 2.0 feed at /feed.xml from the most recent 30 articles.

Reads article publish dates from the article:published_time meta tag (added by
upgrade_article_seo.py). Falls back to inferring from the article-meta div
if that tag isn't present.
"""
import re
from pathlib import Path
from datetime import datetime
from email.utils import format_datetime, parsedate_to_datetime
from html import escape

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"
SITE_URL = "https://www.energypricestoday.com"
FEED_TITLE = "EnergyPricesToday — Live Oil Prices, Gas Prices, Energy Geopolitics"
FEED_DESC = "Daily updates on oil prices, U.S. gas prices, electricity rates, and energy geopolitics."

MAX_ITEMS = 30


def extract_meta(content, prop):
    """Find <meta property|name="prop" content="..."> value."""
    m = re.search(
        rf'<meta\s+(?:property|name)="{re.escape(prop)}"\s+content="([^"]+)"',
        content
    )
    return m.group(1) if m else None


def parse_iso_to_datetime(iso_str):
    """Convert '2026-04-27T08:00:00-04:00' to datetime."""
    if not iso_str: return None
    try:
        # Python 3.7+ handles colon in offset since 3.11; strip if present
        s = iso_str
        return datetime.fromisoformat(s)
    except ValueError:
        return None


def article_data(path):
    txt = path.read_text(encoding='utf-8', errors='ignore')

    title_m = re.search(r'<title>([^<]+)</title>', txt)
    title = (title_m.group(1) if title_m else path.stem).split(' | ')[0].strip()

    description = extract_meta(txt, 'description') or extract_meta(txt, 'og:description') or ''
    description = description[:500]

    iso_pub = extract_meta(txt, 'article:published_time')
    pub_dt = parse_iso_to_datetime(iso_pub)

    if pub_dt is None:
        # Fallback: try to read date from article-meta div
        m = re.search(r'<div class="article-meta"[^>]*>.*?<span>[^<]*</span>\s*<span>([^<]+)</span>', txt, re.DOTALL)
        if m:
            try:
                naive = datetime.strptime(m.group(1).strip(), '%B %d, %Y')
                # Default to 8 AM ET → use local naive then attach UTC offset for ET (-04:00 in April)
                from datetime import timezone, timedelta
                pub_dt = naive.replace(hour=8, tzinfo=timezone(timedelta(hours=-4)))
            except ValueError:
                pass

    # Ensure timezone-aware
    if pub_dt is not None and pub_dt.tzinfo is None:
        from datetime import timezone, timedelta
        pub_dt = pub_dt.replace(tzinfo=timezone(timedelta(hours=-4)))

    section = extract_meta(txt, 'article:section') or 'Energy'
    canonical = extract_meta(txt, 'og:url') or f'{SITE_URL}/articles/{path.name}'

    return {
        'title': title,
        'link': canonical,
        'description': description,
        'pub_date': pub_dt,
        'category': section,
        'guid': canonical,
    }


def main():
    items = []
    for f in ARTICLES.glob('*.html'):
        try:
            d = article_data(f)
            if d['pub_date']:
                items.append(d)
        except Exception as e:
            print(f"  Skipped {f.name}: {e}")

    # Sort by publish date desc
    items.sort(key=lambda x: x['pub_date'], reverse=True)
    items = items[:MAX_ITEMS]

    now = datetime.now().astimezone()
    last_build = format_datetime(now)
    pub_date_feed = format_datetime(items[0]['pub_date']) if items else last_build

    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/">')
    parts.append('  <channel>')
    parts.append(f'    <title>{escape(FEED_TITLE)}</title>')
    parts.append(f'    <link>{SITE_URL}/</link>')
    parts.append(f'    <description>{escape(FEED_DESC)}</description>')
    parts.append('    <language>en-us</language>')
    parts.append(f'    <lastBuildDate>{last_build}</lastBuildDate>')
    parts.append(f'    <pubDate>{pub_date_feed}</pubDate>')
    parts.append(f'    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>')
    parts.append(f'    <generator>EnergyPricesToday Static Generator</generator>')
    parts.append(f'    <image><url>{SITE_URL}/images/logo.png</url><title>EnergyPricesToday</title><link>{SITE_URL}/</link></image>')

    for item in items:
        parts.append('    <item>')
        parts.append(f'      <title>{escape(item["title"])}</title>')
        parts.append(f'      <link>{escape(item["link"])}</link>')
        parts.append(f'      <guid isPermaLink="true">{escape(item["guid"])}</guid>')
        parts.append(f'      <pubDate>{format_datetime(item["pub_date"])}</pubDate>')
        parts.append(f'      <category>{escape(item["category"])}</category>')
        parts.append(f'      <description><![CDATA[{item["description"]}]]></description>')
        parts.append(f'      <dc:creator>EnergyPricesToday Staff</dc:creator>')
        parts.append('    </item>')

    parts.append('  </channel>')
    parts.append('</rss>')

    out_path = ROOT / 'feed.xml'
    out_path.write_text('\n'.join(parts), encoding='utf-8')
    print(f"✓ Wrote {out_path} with {len(items)} items")


if __name__ == '__main__':
    main()
