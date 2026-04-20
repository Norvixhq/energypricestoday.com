#!/usr/bin/env python3
"""
send_health_digest.py — Phase 5.4: Daily digest + weekly heartbeat via GitHub Issues.

Runs once nightly (from nightly-audit.yml). Reads data/health.json and
emits a monitoring signal by managing GitHub Issues in the current repo.

Why Issues (not email/Slack/SMS):
  - Zero new secrets — uses GITHUB_TOKEN already available to workflows
  - Audit trail for free — every alert is a timestamped record
  - You already get emails from GitHub on new issues in your own repo
  - Labels let you filter/mute (e.g. mute the heartbeat label)
  - De-dup is natural: open one issue, close it on recovery

Behavior:
  1. Read data/health.json
  2. If status in (degraded, failing):
       - If an open monitoring issue exists: update its body with fresh snapshot
       - Else: open a new issue tagged [monitoring:<status>]
  3. If status == healthy AND an open monitoring issue exists:
       - Close that issue with a "system recovered" comment
  4. Weekly heartbeat (configurable day):
       - Post/update a heartbeat issue tagged [monitoring:heartbeat]
       - Closed immediately — it's a heartbeat, not something to fix
       - Its absence from the issue history tells you the digest itself died

Environment required:
  GITHUB_TOKEN       — standard workflow token (provided by nightly-audit.yml)
  GITHUB_REPOSITORY  — "owner/repo" (provided automatically by Actions)

Exit codes:
  0 — Ran to completion (may have posted 0, 1, or 2 issue operations)
  1 — Could not read health.json or send API request
  2 — Missing required env vars (GITHUB_TOKEN or GITHUB_REPOSITORY)

Safety:
  - Never blocks the nightly-audit workflow (failures logged, exit 0-1)
  - Uses issue LABELS for state, not title parsing — robust to edits
  - Only touches issues with the monitoring:* label prefix
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEALTH_PATH = ROOT / "data" / "health.json"

# Label conventions — all have "monitoring:" prefix for filterability
LABEL_DEGRADED  = "monitoring:degraded"
LABEL_FAILING   = "monitoring:failing"
LABEL_HEARTBEAT = "monitoring:heartbeat"
ALL_MONITORING_LABELS = [LABEL_DEGRADED, LABEL_FAILING, LABEL_HEARTBEAT]

# Heartbeat cadence: post on ISO weekday N (Monday=1 ... Sunday=7).
# Monday = start of the work week, most-likely-noticed.
HEARTBEAT_WEEKDAY = 1

GITHUB_API = "https://api.github.com"


# ─── Helpers ──────────────────────────────────────────────────────
def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def gh_request(method: str, url: str, token: str, body: dict | None = None) -> dict | list | None:
    """Minimal GitHub REST API client. Returns parsed JSON or None on error."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "energypricestoday-monitoring",
    }
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")

    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        body_text = ""
        try:
            body_text = e.read().decode("utf-8", errors="replace")[:400]
        except Exception:
            pass
        print(f"[digest] GitHub API {method} {url} -> HTTP {e.code}: {body_text}")
        return None
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"[digest] GitHub API {method} {url} -> {e}")
        return None


def list_open_monitoring_issues(repo: str, token: str) -> list[dict]:
    """Return all OPEN issues in the repo that have any monitoring:* label."""
    out: list[dict] = []
    for label in ALL_MONITORING_LABELS:
        url = f"{GITHUB_API}/repos/{repo}/issues?state=open&labels={label}&per_page=20"
        result = gh_request("GET", url, token)
        if isinstance(result, list):
            # De-dupe by issue number
            existing_numbers = {i["number"] for i in out}
            for issue in result:
                if issue["number"] not in existing_numbers:
                    out.append(issue)
    return out


def post_issue(repo: str, token: str, title: str, body: str, labels: list[str]) -> dict | None:
    url = f"{GITHUB_API}/repos/{repo}/issues"
    return gh_request("POST", url, token, {
        "title": title,
        "body":  body,
        "labels": labels,
    })


def update_issue(repo: str, token: str, number: int, body: str, labels: list[str] | None = None) -> dict | None:
    url = f"{GITHUB_API}/repos/{repo}/issues/{number}"
    payload: dict = {"body": body}
    if labels is not None:
        payload["labels"] = labels
    return gh_request("PATCH", url, token, payload)


def comment_on_issue(repo: str, token: str, number: int, body: str) -> dict | None:
    url = f"{GITHUB_API}/repos/{repo}/issues/{number}/comments"
    return gh_request("POST", url, token, {"body": body})


def close_issue(repo: str, token: str, number: int) -> dict | None:
    url = f"{GITHUB_API}/repos/{repo}/issues/{number}"
    return gh_request("PATCH", url, token, {"state": "closed"})


# ─── Body formatters ──────────────────────────────────────────────
def format_digest_body(health: dict) -> str:
    """Markdown body for a degraded/failing issue."""
    status = health.get("status", "unknown")
    generated_at = health.get("generated_at", "unknown")
    codes = health.get("reason_codes", [])
    recent = health.get("recent_activity", {})
    checks = health.get("checks", {})
    quotas = health.get("quotas", {}).get("apis", {})

    lines = [
        f"## System status: `{status.upper()}`",
        "",
        f"**Snapshot generated:** {generated_at}",
        f"**Source:** `data/health.json`",
        "",
        "### Reason codes",
    ]
    if codes:
        for code in codes:
            lines.append(f"- `{code}`")
    else:
        lines.append("_(none)_")
    lines.append("")

    lines.append("### Check details")
    lines.append("| Check | Status | Age | Last success |")
    lines.append("|---|---|---|---|")
    for name, c in checks.items():
        age = c.get("age_minutes") or c.get("minutes_since")
        age_str = f"{age} min" if age is not None else "—"
        last = c.get("last_success") or "—"
        if last and last != "—":
            # Shorten the ISO timestamp for readability
            last = last[:16].replace("T", " ") + " UTC"
        lines.append(f"| `{name}` | {c.get('status','—')} | {age_str} | {last} |")
    lines.append("")

    if quotas:
        lines.append("### API quotas (today)")
        lines.append("| API | Calls | Succeeded | Failed | % of limit |")
        lines.append("|---|---|---|---|---|")
        for api, q in quotas.items():
            lines.append(
                f"| `{api}` | {q.get('calls_today', 0)} | "
                f"{q.get('succeeded', 0)} | {q.get('failed', 0)} | "
                f"{q.get('pct_of_limit', 0)}% |"
            )
        lines.append("")

    lines.append("### Recent activity")
    lines.append(f"- Last successful autopilot: `{recent.get('last_successful_autopilot') or '—'}`")
    lines.append(f"- Last successful news update: `{recent.get('last_successful_news_update') or '—'}`")
    lines.append(f"- Last successful nightly audit: `{recent.get('last_successful_nightly_audit') or '—'}`")
    lines.append(f"- Meaningful changes last 24h: **{recent.get('meaningful_changes_last_24h', 0)}**")
    lines.append(f"- Articles created last 24h: **{recent.get('articles_created_last_24h', 0)}**")
    lines.append("")

    lines.append("---")
    lines.append(
        "_Auto-generated by `scripts/send_health_digest.py`. "
        "This issue will be updated on subsequent runs and auto-closed "
        "when `status` returns to `healthy`._"
    )
    return "\n".join(lines)


def format_heartbeat_body(health: dict) -> str:
    """Markdown body for a weekly heartbeat (post-then-close)."""
    recent = health.get("recent_activity", {})
    generated_at = health.get("generated_at", "unknown")
    lines = [
        "## Weekly system heartbeat",
        "",
        f"Snapshot at {generated_at}.",
        "",
        f"- System status: **{health.get('status', 'unknown')}**",
        f"- Autopilot runs last week: see recent commits for `auto-update` entries",
        f"- Meaningful changes last 24h: **{recent.get('meaningful_changes_last_24h', 0)}**",
        f"- Articles created last 24h: **{recent.get('articles_created_last_24h', 0)}**",
        f"- Last successful autopilot: `{recent.get('last_successful_autopilot') or '—'}`",
        f"- Last successful nightly audit: `{recent.get('last_successful_nightly_audit') or '—'}`",
        "",
        "This issue is **auto-closed** immediately. Its purpose is to prove "
        "the monitoring digest itself is alive. If you don't see a heartbeat "
        "issue for several weeks, the monitoring layer has died and needs "
        "investigation.",
        "",
        "---",
        "_Auto-generated by `scripts/send_health_digest.py`._",
    ]
    return "\n".join(lines)


# ─── Main logic ───────────────────────────────────────────────────
def main() -> int:
    token = os.environ.get("GITHUB_TOKEN")
    repo  = os.environ.get("GITHUB_REPOSITORY")  # "owner/repo" from Actions
    if not token or not repo:
        print("[digest] GITHUB_TOKEN or GITHUB_REPOSITORY missing — cannot send digest")
        return 2

    if not HEALTH_PATH.exists():
        print(f"[digest] {HEALTH_PATH} not found — autopilot may not have run yet")
        return 1
    try:
        health = json.loads(HEALTH_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"[digest] could not read health.json: {e}")
        return 1

    status = health.get("status", "unknown")
    print(f"[digest] health.json status={status}")

    # Fetch open monitoring issues (to decide open/update/close)
    open_issues = list_open_monitoring_issues(repo, token)
    # Partition by label
    issues_by_label: dict[str, list[dict]] = {lbl: [] for lbl in ALL_MONITORING_LABELS}
    for issue in open_issues:
        labels = {lbl["name"] for lbl in issue.get("labels", [])}
        for lbl in ALL_MONITORING_LABELS:
            if lbl in labels:
                issues_by_label[lbl].append(issue)

    # ─── Handle degraded/failing ──────────────────────────────
    if status in ("degraded", "failing"):
        desired_label = LABEL_FAILING if status == "failing" else LABEL_DEGRADED
        # An existing OPEN issue on EITHER monitoring label is reused — we
        # just update its labels and body. This way, if a degraded issue
        # exists and we now escalate to failing, we don't spawn a new one.
        existing = issues_by_label[LABEL_DEGRADED] + issues_by_label[LABEL_FAILING]
        body = format_digest_body(health)
        title = f"[{status}] system health — {health.get('generated_at','')[:10]}"

        if existing:
            issue = existing[0]  # just use the first if multiple somehow open
            print(f"[digest] updating existing monitoring issue #{issue['number']}")
            # Keep only the new status label, drop the other
            result = update_issue(repo, token, issue["number"], body, labels=[desired_label])
            if result:
                print(f"[digest] ✓ issue #{issue['number']} updated")
            else:
                print(f"[digest] ✗ failed to update issue #{issue['number']}")
                return 1
        else:
            print(f"[digest] opening new monitoring issue with label={desired_label}")
            result = post_issue(repo, token, title, body, [desired_label])
            if result:
                print(f"[digest] ✓ issue #{result.get('number')} created")
            else:
                print("[digest] ✗ failed to create issue")
                return 1

    # ─── Handle healthy — close any open monitoring issues ─────
    elif status == "healthy":
        to_close = issues_by_label[LABEL_DEGRADED] + issues_by_label[LABEL_FAILING]
        for issue in to_close:
            num = issue["number"]
            print(f"[digest] system recovered — closing issue #{num}")
            comment_on_issue(repo, token, num, (
                f"✅ System recovered to `healthy` at {now_iso()}.\n\n"
                "Auto-closing."
            ))
            close_issue(repo, token, num)

    # ─── Weekly heartbeat (post-then-close) ────────────────────
    # Only on the configured weekday, and only if we haven't already posted
    # a heartbeat today (prevents duplicates on manual re-runs).
    weekday = datetime.now(timezone.utc).isoweekday()  # 1 = Monday
    if weekday == HEARTBEAT_WEEKDAY:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        # Check recent heartbeat issues (including closed) to dedupe
        recent_url = f"{GITHUB_API}/repos/{repo}/issues?state=all&labels={LABEL_HEARTBEAT}&per_page=5"
        recent = gh_request("GET", recent_url, token) or []
        already_posted_today = any(
            today in issue.get("title", "")
            for issue in (recent if isinstance(recent, list) else [])
        )
        if already_posted_today:
            print(f"[digest] heartbeat already posted today — skipping")
        else:
            print(f"[digest] posting weekly heartbeat (weekday={weekday})")
            heartbeat_body = format_heartbeat_body(health)
            title = f"[heartbeat] weekly system check — {today}"
            result = post_issue(repo, token, title, heartbeat_body, [LABEL_HEARTBEAT])
            if result:
                num = result.get("number")
                print(f"[digest] ✓ heartbeat issue #{num} posted")
                # Close immediately — the heartbeat's purpose is proof-of-life
                close_issue(repo, token, num)
            else:
                print("[digest] ✗ failed to post heartbeat")
                # Non-fatal

    print("[digest] done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
