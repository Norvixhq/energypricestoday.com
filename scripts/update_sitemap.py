#!/usr/bin/env python3
"""
update_sitemap.py — Refresh <lastmod> dates in sitemap.xml to today.

Also adds <url> entries for any new article files not yet in the sitemap.

Exit codes:
  0 — Updated
  1 — No change
  2 — Error
"""

import os
import re
import sys
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
SITEMAP = ROOT / "sitemap.xml"
ARTICLES_DIR = ROOT / "articles"
BASE_URL = "https://www.energypricestoday.com"


def main() -> int:
    if not SITEMAP.exists():
        print("[update_sitemap] sitemap.xml not found")
        return 2

    today = date.today().isoformat()
    with open(SITEMAP, encoding="utf-8") as f:
        content = f.read()

    original = content

    # Bump all lastmod to today
    content = re.sub(
        r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>",
        f"<lastmod>{today}</lastmod>",
        content,
    )

    # Find article URLs already in sitemap
    existing_article_slugs = set(
        re.findall(r"/articles/([a-z0-9\-]+)\.html", content)
    )

    # Find article files on disk
    disk_slugs = {
        f.replace(".html", "")
        for f in os.listdir(ARTICLES_DIR)
        if f.endswith(".html")
    }

    missing_in_sitemap = disk_slugs - existing_article_slugs
    obsolete_in_sitemap = existing_article_slugs - disk_slugs

    # Remove entries for articles that no longer exist
    removed = 0
    for slug in obsolete_in_sitemap:
        pattern = re.compile(
            rf"<url>\s*<loc>[^<]*?/articles/{re.escape(slug)}\.html</loc>"
            rf"\s*<lastmod>[^<]*</lastmod>\s*</url>\s*",
            re.DOTALL,
        )
        new_content, n = pattern.subn("", content)
        if n:
            content = new_content
            removed += n

    # Add new article entries before </urlset>
    added = 0
    if missing_in_sitemap:
        new_entries = []
        for slug in sorted(missing_in_sitemap):
            new_entries.append(
                f"  <url>\n"
                f"    <loc>{BASE_URL}/articles/{slug}.html</loc>\n"
                f"    <lastmod>{today}</lastmod>\n"
                f"  </url>"
            )
        block = "\n".join(new_entries) + "\n"
        content = content.replace("</urlset>", f"{block}</urlset>")
        added = len(new_entries)

    if content == original:
        print("[update_sitemap] No changes needed")
        return 1

    # Validate XML before writing
    try:
        ET.fromstring(content)
    except ET.ParseError as e:
        print(f"[update_sitemap] Would produce invalid XML: {e}")
        return 2

    tmp = str(SITEMAP) + ".new.xml"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, str(SITEMAP))

    total_urls = content.count("<url>")
    print(f"[update_sitemap] ✓ Updated: {total_urls} URLs, "
          f"{added} added, {removed} removed, all dated {today}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
