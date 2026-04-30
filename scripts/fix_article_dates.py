#!/usr/bin/env python3
"""
Fix article publish dates that defaulted to "now" because my SEO upgrade
script didn't recognize the article-author-date markup variant.

Reads the actual published date from EITHER:
  <div class="article-meta">...<span>April 27, 2026</span>...</div>
  <div class="article-author-date">April 18, 2026</div>

Updates the article:published_time, article:modified_time, and the
datePublished/dateModified fields in the NewsArticle JSON-LD schema.
"""
import re
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

MONTH_TO_NUM = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

def date_to_iso(date_str):
    m = re.match(r'(\w+)\s+(\d+),\s+(\d+)', (date_str or '').strip())
    if not m: return None
    mon, day, year = m.group(1), int(m.group(2)), int(m.group(3))
    if mon not in MONTH_TO_NUM: return None
    return f"{year:04d}-{MONTH_TO_NUM[mon]:02d}-{day:02d}T08:00:00-04:00"


def find_real_date(txt):
    # Format 1: <div class="article-meta">...<span>Author</span><span>Date</span>...
    m = re.search(r'<div class="article-meta"[^>]*>.*?<span>[^<]*</span>\s*<span>([^<]+)</span>', txt, re.DOTALL)
    if m:
        d = date_to_iso(m.group(1))
        if d: return d
    # Format 2: <div class="article-author-date">Date</div>
    m = re.search(r'<div class="article-author-date"[^>]*>([^<]+)</div>', txt)
    if m:
        d = date_to_iso(m.group(1))
        if d: return d
    # Format 3: Pre-existing NewsArticle schema with datePublished
    # Skip the one I added (always at end of head with publisher field) — match the FIRST schema
    m = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', txt)
    if m:
        return f"{m.group(1)}T08:00:00-04:00"
    # Format 4: Some articles have date in <p class="article-date"> or <time>
    m = re.search(r'<time[^>]*datetime="(\d{4}-\d{2}-\d{2})"', txt)
    if m:
        return f"{m.group(1)}T08:00:00-04:00"
    m = re.search(r'<p class="article-date">([^<]+)</p>', txt)
    if m:
        d = date_to_iso(m.group(1))
        if d: return d
    return None


def fix_article(path):
    txt = path.read_text(encoding='utf-8', errors='ignore')
    real_date = find_real_date(txt)
    if not real_date:
        return False, 'no date found'

    # Find the existing published_time
    m = re.search(r'article:published_time"\s+content="([^"]+)"', txt)
    if not m:
        return False, 'no article:published_time tag'
    current = m.group(1)

    if current == real_date:
        return False, 'already correct'

    # Replace article:published_time
    new_txt = txt.replace(
        f'<meta property="article:published_time" content="{current}">',
        f'<meta property="article:published_time" content="{real_date}">',
        1
    )
    # Replace article:modified_time (also defaults to current; keep it = published time
    # since these are static articles that don't get edited after publish)
    m_mod = re.search(r'<meta property="article:modified_time" content="([^"]+)">', new_txt)
    if m_mod:
        new_txt = new_txt.replace(
            f'<meta property="article:modified_time" content="{m_mod.group(1)}">',
            f'<meta property="article:modified_time" content="{real_date}">',
            1
        )

    # Replace datePublished and dateModified inside NewsArticle JSON-LD
    new_txt = re.sub(
        r'"datePublished":"[^"]+"',
        f'"datePublished":"{real_date}"',
        new_txt,
        count=1
    )
    new_txt = re.sub(
        r'"dateModified":"[^"]+"',
        f'"dateModified":"{real_date}"',
        new_txt,
        count=1
    )

    path.write_text(new_txt, encoding='utf-8')
    return True, real_date


def main():
    fixed = 0
    skipped = 0
    failed = 0
    for f in sorted(ARTICLES.glob('*.html')):
        try:
            ok, info = fix_article(f)
            if ok:
                fixed += 1
            else:
                skipped += 1
        except Exception as e:
            failed += 1
            print(f"  ✗ {f.name}: {e}")
    print(f"Fixed dates: {fixed}")
    print(f"Skipped: {skipped}")
    print(f"Failed: {failed}")


if __name__ == '__main__':
    main()
