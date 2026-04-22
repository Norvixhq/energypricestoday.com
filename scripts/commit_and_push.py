#!/usr/bin/env python3
"""
commit_and_push.py — Git commit + push helper for automated runs.

Behavior:
  - Only commits if there are actual content changes (diff is non-trivial)
  - Generates a descriptive commit message from what changed
  - Configured for GitHub Actions (uses GITHUB_ACTOR / GITHUB_TOKEN via env)

Exit codes:
  0 — Committed + pushed (or nothing to commit, clean exit)
  1 — Error (push rejected, etc.)
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(
        cmd, cwd=ROOT, capture_output=True, text=True
    )
    if check and result.returncode != 0:
        print(f"[commit] Command failed: {' '.join(cmd)}")
        print(f"  stdout: {result.stdout}")
        print(f"  stderr: {result.stderr}")
    return result


def has_changes() -> bool:
    """Return True if there are any uncommitted changes."""
    result = run(["git", "status", "--porcelain"], check=False)
    return bool(result.stdout.strip())


def status_summary() -> tuple[str, list[str]]:
    """Return (summary line, list of changed paths) covering tracked + untracked."""
    result = run(["git", "status", "--porcelain"], check=False)
    lines = [ln for ln in result.stdout.strip().split("\n") if ln.strip()]
    paths = []
    added = 0
    modified = 0
    deleted = 0
    untracked = 0
    for ln in lines:
        # Format: "XY path" where X/Y are status codes
        code = ln[:2]
        path = ln[3:].strip() if len(ln) > 3 else ""
        paths.append(path)
        if code.strip() == "??":
            untracked += 1
        elif "A" in code:
            added += 1
        elif "M" in code:
            modified += 1
        elif "D" in code:
            deleted += 1
    parts = []
    if untracked: parts.append(f"{untracked} new")
    if modified: parts.append(f"{modified} modified")
    if added: parts.append(f"{added} added")
    if deleted: parts.append(f"{deleted} deleted")
    summary = ", ".join(parts) if parts else f"{len(lines)} changes"
    return summary, paths


def diff_summary() -> str:
    """Short summary of what files changed (including untracked)."""
    summary, _paths = status_summary()
    return summary


def changed_files() -> list[str]:
    """All files affected in working tree — includes tracked modifications and untracked new files."""
    _, paths = status_summary()
    return paths


def build_commit_message(reason: str) -> str:
    """Build a descriptive commit message from what changed."""
    files = changed_files()

    tags = []
    if any("data.js" in f for f in files):
        tags.append("data")
    if any(f.startswith("articles/") for f in files):
        tags.append("articles")
    if any(f.endswith(".html") and "articles/" not in f for f in files):
        tags.append("pages")
    if any("sitemap" in f for f in files):
        tags.append("sitemap")
    if any("article-slugs.js" in f for f in files):
        tags.append("slugmap")

    scope = ",".join(tags) or "misc"
    return f"auto-update ({scope}): {reason} [skip ci]"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: commit_and_push.py <reason>")
        return 1
    reason = sys.argv[1]

    if not has_changes():
        print("[commit] No changes to commit")
        return 0

    print(f"[commit] Changes detected: {diff_summary()}")

    # Configure git identity for CI
    actor = os.environ.get("GITHUB_ACTOR", "energypricestoday-bot")
    run(["git", "config", "user.name", actor], check=False)
    run(["git", "config", "user.email", f"{actor}@users.noreply.github.com"], check=False)

    # Log the RAW git status before we touch anything — tells us what git sees
    pre_status = run(["git", "status", "--porcelain"], check=False)
    pre_lines = pre_status.stdout.strip().split("\n") if pre_status.stdout.strip() else []
    print(f"[commit] git status shows {len(pre_lines)} entries before add:")
    untracked = [ln for ln in pre_lines if ln.startswith("??")]
    modified = [ln for ln in pre_lines if ln.startswith(" M") or ln.startswith("M ")]
    print(f"  untracked: {len(untracked)}, modified: {len(modified)}, other: {len(pre_lines) - len(untracked) - len(modified)}")
    # Explicitly show any data/ paths git sees as untracked
    data_entries = [ln for ln in pre_lines if "data/" in ln]
    if data_entries:
        print(f"  data/ entries git sees:")
        for entry in data_entries[:30]:
            print(f"    {entry}")

    # Explicitly add data directories first — belt-and-suspenders in case
    # something about git's default add-A behavior is excluding them.
    run(["git", "add", "data/"], check=False)
    run(["git", "add", "-A"])

    # Diagnostic: log exactly what's now staged so runner output shows ground truth
    staged = run(["git", "diff", "--cached", "--name-only"], check=False)
    staged_files = [f for f in staged.stdout.strip().split("\n") if f]
    print(f"[commit] Staged {len(staged_files)} file(s):")
    # Group by top-level directory for readable output
    by_dir: dict[str, int] = {}
    for f in staged_files:
        top = f.split("/", 1)[0] if "/" in f else "(root)"
        by_dir[top] = by_dir.get(top, 0) + 1
    for top, count in sorted(by_dir.items()):
        print(f"  {top}/ — {count} file(s)")
    # Also explicitly list any data/ files so autopilot logs show them
    data_files = [f for f in staged_files if f.startswith("data/")]
    if data_files:
        print(f"[commit] data/ files in this commit:")
        for f in sorted(data_files):
            print(f"    • {f}")

    msg = build_commit_message(reason)
    print(f"[commit] Message: {msg}")

    result = run(["git", "commit", "-m", msg], check=False)
    if result.returncode != 0:
        # Nothing to commit (race), treat as success
        if "nothing to commit" in result.stdout + result.stderr:
            print("[commit] Nothing to commit after add (race)")
            return 0
        return 1

    print("[commit] Pushing...")
    result = run(["git", "push", "origin", "HEAD"], check=False)
    if result.returncode != 0:
        print("[commit] Push failed — may need rebase")
        # Try rebase + retry once
        pull = run(["git", "pull", "--rebase", "origin", "HEAD"], check=False)
        if pull.returncode != 0:
            print("[commit] Rebase failed, giving up")
            return 1
        result = run(["git", "push", "origin", "HEAD"], check=False)
        if result.returncode != 0:
            return 1

    print("[commit] ✓ Pushed successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
