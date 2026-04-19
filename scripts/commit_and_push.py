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


def diff_summary() -> str:
    """Short summary of what files changed."""
    result = run(["git", "diff", "--stat", "HEAD"], check=False)
    # Keep last line (e.g., "5 files changed, 120 insertions(+), 30 deletions(-)")
    lines = result.stdout.strip().split("\n")
    return lines[-1] if lines else "changes"


def changed_files() -> list[str]:
    result = run(["git", "diff", "--name-only", "HEAD"], check=False)
    return [f for f in result.stdout.strip().split("\n") if f]


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

    run(["git", "add", "-A"])

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
