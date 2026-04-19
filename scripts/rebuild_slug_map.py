#!/usr/bin/env python3
"""
rebuild_slug_map.py — Regenerate js/article-slugs.js from the actual
article files in articles/. Called by every content-update script after
articles are added or removed.

Exit codes:
  0 — Rebuilt successfully
  2 — Error
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ARTICLES_DIR = Path(__file__).resolve().parent.parent / "articles"
SLUGS_JS_PATH = Path(__file__).resolve().parent.parent / "js" / "article-slugs.js"

ENTITIES = {
    "&mdash;": "\u2014",
    "&ndash;": "\u2013",
    "&amp;": "&",
    "&rsquo;": "\u2019",
    "&lsquo;": "\u2018",
    "&ldquo;": "\u201C",
    "&rdquo;": "\u201D",
    "&quot;": '"',
    "&#39;": "'",
    "&apos;": "'",
    "&nbsp;": " ",
}


def decode_entities(s: str) -> str:
    for e, c in ENTITIES.items():
        s = s.replace(e, c)
    return s


def build_slug_map() -> dict[str, str]:
    slug_map = {}
    for fname in sorted(os.listdir(ARTICLES_DIR)):
        if not fname.endswith(".html"):
            continue
        path = ARTICLES_DIR / fname
        with open(path, encoding="utf-8") as f:
            content = f.read()
        m = re.search(r"<h1[^>]*>([^<]+)</h1>", content)
        if not m:
            continue
        title = decode_entities(m.group(1).strip())
        slug = fname.replace(".html", "")
        if len(title) >= 15 and " " in title:
            slug_map[title] = slug
    return slug_map


def render_js(slug_map: dict[str, str]) -> str:
    entries = ",\n".join(
        f"  {json.dumps(t)}: {json.dumps(s)}"
        for t, s in sorted(slug_map.items())
    )
    return f"""// Auto-generated article slug map — do not edit manually.
// Rebuild with: python3 scripts/rebuild_slug_map.py
const ARTICLE_SLUGS = {{
{entries}
}};

function slugifyTitle(title) {{
  return title.toLowerCase()
    .replace(/[^a-z0-9\\s-]/g, '')
    .replace(/\\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '')
    .substring(0, 80);
}}

function articleUrl(title) {{
  if (typeof ARTICLE_SLUGS !== 'undefined' && ARTICLE_SLUGS[title]) {{
    return 'articles/' + ARTICLE_SLUGS[title] + '.html';
  }}
  return 'articles/' + slugifyTitle(title) + '.html';
}}

function categoryArticleUrl(title) {{
  return '../' + articleUrl(title);
}}
"""


def main() -> int:
    slug_map = build_slug_map()
    js = render_js(slug_map)

    tmp = str(SLUGS_JS_PATH) + ".new.js"  # must keep .js so node -c accepts it
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(js)

    # Validate before replacing
    result = subprocess.run(["node", "-c", tmp], capture_output=True, text=True)
    if result.returncode != 0:
        os.remove(tmp)
        print(f"[rebuild_slug_map] JS syntax check FAILED:\n{result.stderr}")
        return 2

    os.replace(tmp, str(SLUGS_JS_PATH))
    print(f"[rebuild_slug_map] ✓ {len(slug_map)} articles mapped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
