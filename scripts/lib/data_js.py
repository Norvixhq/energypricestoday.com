"""
data_js.py — Safe read/write helpers for js/data.js content blocks.

The site stores all structured content in a single JavaScript file
(js/data.js) as named const arrays/objects. This module provides
helpers to read and rewrite those blocks without touching the rest
of the file.

All functions take/return Python types; they handle the JS syntax
serialization transparently.
"""

import re
import os
import subprocess
from pathlib import Path

DATA_JS_PATH = Path(__file__).resolve().parent.parent.parent / "js" / "data.js"


def read_raw() -> str:
    """Read the full data.js file."""
    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        return f.read()


def write_raw(content: str) -> None:
    """Write the full data.js file, atomic via temp-then-rename."""
    # Must keep .js extension so `node -c` on the temp file works
    tmp = str(DATA_JS_PATH) + ".new.js"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, str(DATA_JS_PATH))


def validate_syntax() -> bool:
    """Run `node -c` against data.js. Returns True if syntax is valid."""
    result = subprocess.run(
        ["node", "-c", str(DATA_JS_PATH)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[data_js] SYNTAX ERROR in data.js:\n{result.stderr}")
        return False
    return True


def replace_block(block_name: str, new_block_js: str) -> bool:
    """
    Replace a `const BLOCK_NAME = {...};` or `const BLOCK_NAME = [...];`
    block with `new_block_js`. `new_block_js` must be the complete
    replacement including `const NAME = ` prefix and `;` suffix.

    Returns True if replaced, False if block not found.
    Validates JS syntax before committing; reverts on failure.
    """
    original = read_raw()

    # Try array first, then object
    patterns = [
        re.compile(rf"const\s+{re.escape(block_name)}\s*=\s*\[.*?\];", re.DOTALL),
        re.compile(rf"const\s+{re.escape(block_name)}\s*=\s*\{{.*?\}};", re.DOTALL),
    ]

    replaced = None
    for pat in patterns:
        if pat.search(original):
            replaced = pat.sub(lambda m: new_block_js, original)
            break

    if replaced is None:
        print(f"[data_js] Block '{block_name}' not found in data.js")
        return False

    # Write candidate, validate, revert on failure
    write_raw(replaced)
    if not validate_syntax():
        print(f"[data_js] Syntax broke after replacing '{block_name}'; reverting")
        write_raw(original)
        return False

    return True


def extract_titles_from_block(block_name: str) -> list[str]:
    """Extract all `title: "..."` strings inside a named block."""
    content = read_raw()
    pat = re.compile(
        rf"const\s+{re.escape(block_name)}\s*=\s*[\[\{{].*?[\]\}}];",
        re.DOTALL,
    )
    m = pat.search(content)
    if not m:
        return []
    titles = []
    for tm in re.finditer(r'title:\s*"([^"]{10,})"', m.group(0)):
        t = tm.group(1)
        if "\\u" in t:
            t = t.encode().decode("unicode_escape")
        titles.append(t)
    return titles


def extract_all_visible_titles() -> set[str]:
    """All titles across all content blocks — what needs article files."""
    titles = set()
    for block in [
        "BREAKING_NEWS",
        "FEATURED_ARTICLES",
        "GEO_ITEMS",
        "COMPANY_NEWS",
        "CATEGORY_CONTENT",
    ]:
        titles.update(extract_titles_from_block(block))
    return titles


def slugify(text: str) -> str:
    """Match the slug logic used in the site's JS."""
    s = text.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s.strip())
    s = re.sub(r"-+", "-", s)
    return s[:80]


def format_news_item(title: str, cat: str, slug: str, time: str) -> str:
    """Serialize a breaking news entry."""
    safe_title = title.replace('"', '\\"')
    return (
        f'  {{ title: "{safe_title}", cat: "{cat}", '
        f'slug: "{slug}", time: "{time}" }}'
    )


def format_geo_item(id_: int, region: str, title: str, desc: str) -> str:
    """Serialize a geopolitics item."""
    safe_title = title.replace('"', '\\"')
    safe_desc = desc.replace('"', '\\"')
    return (
        f'  {{ id: {id_}, region: "{region}", title: "{safe_title}", '
        f'desc: "{safe_desc}" }}'
    )
