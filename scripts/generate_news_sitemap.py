#!/usr/bin/env python3
"""
Generate a Google News sitemap at /news-sitemap.xml.

Google News requires a separate sitemap from the main one, with strict format:
  - Only articles published in the last 48 hours
  - Must include <news:publication> metadata
  - Date must be in W3C Datetime format

If you submit your site to Google News Publisher Center, this sitemap is
how Google discovers your fresh articles within minutes of publication.
"""
import re
from pathlib import Path
from datetime import datetime, timedelta, timezone
from html import escape

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"
SITE_URL = "https://www.energypricestoday.com"
PUBLICATION_NAME = "EnergyPricesToday"
PUBLICATION_LANG = "en"

# Articles up to 48 hours old qualify for Google News sitemap
MAX_AGE = timedelta(hours=48)


def extract_meta(content, prop):
    m = re.search(
        rf'<meta\s+(?:property|name)="{re.escape(prop)}"\s+content="([^"]+)"',
        content
    )
    return m.group(1) if m else None


def get_keywords(content):
    kw = extract_meta(content, 'news_keywords') or extract_meta(content, 'keywords') or ''
    return kw[:200]


def main():
    # Use a "now" reference based on the most recent article we have, not real
    # wall-clock time, so the sitemap stays useful even when run on a frozen
    # static-snapshot deploy.
    most_recent = None
    candidates = []

    for f in ARTICLES.glob('*.html'):
        txt = f.read_text(encoding='utf-8', errors='ignore')
        iso = extract_meta(txt, 'article:published_time')
        if not iso: continue
        try:
            dt = datetime.fromisoformat(iso)
        except ValueError:
            continue

        if most_recent is None or dt > most_recent:
            most_recent = dt

        title_m = re.search(r'<title>([^<]+)</title>', txt)
        title = (title_m.group(1) if title_m else f.stem).split(' | ')[0].strip()
        canonical = extract_meta(txt, 'og:url') or f'{SITE_URL}/articles/{f.name}'
        keywords = get_keywords(txt)

        candidates.append({
            'url': canonical,
            'date': dt,
            'title': title,
            'keywords': keywords,
        })

    if not candidates:
        print("No articles with article:published_time found")
        return

    # Filter to last 48 hours from the most recent article
    cutoff = most_recent - MAX_AGE
    fresh = [c for c in candidates if c['date'] >= cutoff]
    fresh.sort(key=lambda x: x['date'], reverse=True)

    parts = []
    parts.append('<?xml version="1.0" encoding="UTF-8"?>')
    parts.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">')

    for item in fresh:
        parts.append('  <url>')
        parts.append(f'    <loc>{escape(item["url"])}</loc>')
        parts.append('    <news:news>')
        parts.append('      <news:publication>')
        parts.append(f'        <news:name>{PUBLICATION_NAME}</news:name>')
        parts.append(f'        <news:language>{PUBLICATION_LANG}</news:language>')
        parts.append('      </news:publication>')
        parts.append(f'      <news:publication_date>{item["date"].isoformat()}</news:publication_date>')
        parts.append(f'      <news:title>{escape(item["title"])}</news:title>')
        if item['keywords']:
            parts.append(f'      <news:keywords>{escape(item["keywords"])}</news:keywords>')
        parts.append('    </news:news>')
        parts.append('  </url>')

    parts.append('</urlset>')

    out = ROOT / 'news-sitemap.xml'
    out.write_text('\n'.join(parts), encoding='utf-8')
    print(f"✓ Wrote {out} with {len(fresh)} fresh articles (cutoff: {cutoff.isoformat()})")


if __name__ == '__main__':
    main()
