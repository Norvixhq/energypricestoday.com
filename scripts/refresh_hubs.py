#!/usr/bin/env python3
"""
Hub refresh — update country/topic hubs with current verified context.

For each hub, replaces the "Current Context" box content with current
(May 22, 2026) framing, and adds a "Last reviewed" indicator.

All content is grounded in real, verified May 21-22 reporting.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

# ─── Per-hub current context (verified May 17, 2026) ──────────────────
HUBS = {
    "iran.html": {
        "context": "Current state (May 28, 2026): The conflict\u2019s two tracks diverged sharply today. On the ground, U.S. forces struck an Iranian military site near Bandar Abbas and intercepted several drones near the Strait of Hormuz; Iran\u2019s Revolutionary Guard Corps said it retaliated against the U.S. airbase that launched the strikes, warning that \"any act of aggression will not go unanswered.\" On paper, U.S. officials confirmed President Trump has been briefed on a draft MOU that would reopen the strait over 60 days in synchronized steps. Washington sanctioned an Iranian agency seeking to control Hormuz shipping on Wednesday. Iranians are back online after a monthslong internet shutdown. Rubio: talks made \"some progress\"; Trump will give diplomacy \"every chance to succeed.\"",
        "lead_articles": [
            ("U.S. Strikes Iranian Military Site at Bandar Abbas; IRGC Claims Retaliatory Airbase Attack", "us-strikes-bandar-abbas-irgc-claims-retaliatory-airbase-attack.html", "May 28, 2026",
             "U.S. forces struck an Iranian military site near Bandar Abbas Thursday and intercepted drones near the strait. Iran\u2019s IRGC said it retaliated against the U.S. airbase that launched the strikes; Kuwait\u2019s air defenses responded to threats."),
            ("Trump Briefed on Draft MOU That Would Reopen Hormuz Over 60 Days in Synchronized Steps", "trump-briefed-draft-mou-hormuz-60-day-synchronized-reopening.html", "May 28, 2026",
             "U.S. officials confirmed Trump has been briefed on a draft MOU that would reopen the strait over 60 days in synchronized steps \u2014 Iran loosening its grip as the U.S. pulls back its blockade until pre-war status quo."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (May 28, 2026): Saudi Arabia remains among the regional partners pressing Washington to accept a U.S.-Iran framework even as hostilities flared anew. U.S. forces struck an Iranian site near Bandar Abbas Thursday; Iran\u2019s IRGC claimed a retaliatory airbase attack, and Kuwait\u2019s air defenses responded to threats \u2014 underscoring continued Gulf spillover risk. In parallel, Trump has been briefed on a draft MOU to reopen Hormuz over 60 days in synchronized steps. Saudi Aramco CEO Amin Nasser has warned market normalization is pushed to 2027 if reopening is delayed past mid-June. Saudi production remains at the lowest level since 1990. Brent rebounded toward $96\u2013$97 Thursday; oil is down >10% since May 18.",
        "lead_articles": [
            ("Trump Briefed on Draft MOU That Would Reopen Hormuz Over 60 Days in Synchronized Steps", "trump-briefed-draft-mou-hormuz-60-day-synchronized-reopening.html", "May 28, 2026",
             "Saudi Arabia is among the regional partners pressing Washington to accept a framework. The draft MOU would reopen the strait over 60 days in synchronized steps."),
            ("U.S. Strikes Iranian Military Site at Bandar Abbas; IRGC Claims Retaliatory Airbase Attack", "us-strikes-bandar-abbas-irgc-claims-retaliatory-airbase-attack.html", "May 28, 2026",
             "Renewed hostilities underscored continued Gulf spillover risk: Kuwait\u2019s air defenses responded to hostile missile and drone threats Thursday morning."),
        ],
    },
    "uae.html": {
        "context": "Current state (May 28, 2026): The UAE remains among the Gulf states pressing Washington to accept a U.S.-Iran framework. The UAE formally departed OPEC effective May 1, 2026. Renewed hostilities Thursday \u2014 a U.S. strike near Bandar Abbas, an IRGC claim of a retaliatory airbase attack, and Kuwait air defenses responding to threats \u2014 underscored that Gulf spillover risk remains live. In parallel, Trump has been briefed on a draft MOU to reopen Hormuz over 60 days in synchronized steps; Washington sanctioned an Iranian shipping agency Wednesday. ADCOP pipeline continues to carry available bypass volumes that don\u2019t transit Hormuz. The UAE remains a primary U.S. security partner in the Gulf.",
        "lead_articles": [
            ("Trump Briefed on Draft MOU That Would Reopen Hormuz Over 60 Days in Synchronized Steps", "trump-briefed-draft-mou-hormuz-60-day-synchronized-reopening.html", "May 28, 2026",
             "The UAE, alongside Saudi Arabia and Qatar, has pressed Washington to accept a framework. The draft MOU envisions a phased, reciprocal reopening of the strait."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (May 28, 2026): Renewed U.S.-Iran hostilities Thursday \u2014 a U.S. strike near Bandar Abbas and an IRGC claim of a retaliatory airbase attack \u2014 reminded markets the conflict is not resolved even as a draft MOU to reopen Hormuz over 60 days was briefed to Trump. Saudi Arabia, Qatar, and the UAE (former member, departed May 1) are among the regional partners pressing acceptance. The proposed framework would let Iran freely sell oil during the synchronized reopening. EIA assessed 10.5M bpd of Persian Gulf production shut in during April; energy executives via MUFG still warn full normalization may not occur until 2027. Brent rebounded toward $96\u2013$97 Thursday; oil is down >10% since May 18.",
        "lead_articles": [
            ("Trump Briefed on Draft MOU That Would Reopen Hormuz Over 60 Days in Synchronized Steps", "trump-briefed-draft-mou-hormuz-60-day-synchronized-reopening.html", "May 28, 2026",
             "Saudi Arabia, Qatar, and the UAE are among the regional partners pressing acceptance. A phased reopening would let Iran freely sell oil during the window."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (May 28, 2026): Qatar remains one of the principal mediators of the U.S.-Iran framework alongside Pakistan. Renewed hostilities Thursday \u2014 a U.S. strike near Bandar Abbas, an IRGC retaliatory-airbase claim, and Kuwait air defenses responding to threats \u2014 underscored regional spillover risk even as a draft MOU to reopen Hormuz over 60 days was briefed to Trump. The framework would allow Qatari LNG exports to resume as the strait reopens in synchronized steps. JKM and TTF benchmarks remain elevated. Qatar\u2019s diplomats continue shuttle contacts with Iranian counterparts and U.S. envoy Steve Witkoff.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (May 28, 2026): Russia remains one of few major producers outside the Persian Gulf disruption zone. The proposed U.S.-Iran 60-day MOU sets nuclear-program negotiations as a parallel track rather than a precondition, and Iran\u2019s foreign ministry has said nuclear issues are not part of current talks \u2014 deprioritizing the earlier uranium-transfer-to-Russia element of Iran\u2019s proposals. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers. With Brent pulling back toward $96\u2013$97 and oil down >10% since May 18, Urals discount dynamics are again in focus.",
        "lead_articles": [
            ("Trump Briefed on Draft MOU That Would Reopen Hormuz Over 60 Days in Synchronized Steps", "trump-briefed-draft-mou-hormuz-60-day-synchronized-reopening.html", "May 28, 2026",
             "The 60-day MOU keeps nuclear negotiations on a parallel track. Iran\u2019s foreign ministry has said nuclear issues are not part of current talks."),
        ],
    },
    "brazil.html": {
        "context": "Current state (May 28, 2026): Brazilian pre-salt production continues to grow as a non-OPEC supply source even as a U.S.-Iran 60-day MOU to reopen Hormuz advances. Renewed hostilities Thursday \u2014 a U.S. strike near Bandar Abbas and an IRGC retaliatory-airbase claim \u2014 reminded markets the Persian Gulf disruption is not yet resolved. Brent pulled back toward $96\u2013$97 (oil down >10% since May 18), which affects pre-salt project economics at the margin. Petrobras Q1 results and pre-salt output milestones remain key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (May 28, 2026): Nigerian crude remains important to the non-OPEC supply mix even as a U.S.-Iran 60-day MOU to reopen Hormuz advances. Light, sweet Nigerian grades have served as alternatives for refiners losing access to Middle East crude through the conflict. Renewed hostilities Thursday \u2014 a U.S. strike near Bandar Abbas and an IRGC retaliatory-airbase claim \u2014 underscored that the disruption persists; Brent rebounded toward $96\u2013$97 with oil down >10% since May 18. The G7 leaders summit June 15-17 in Evian is expected to address supply-chain diversification.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (May 28, 2026): Venezuelan production capacity remains a structurally relevant question as a U.S.-Iran 60-day MOU to reopen Hormuz advances. Renewed hostilities Thursday \u2014 a U.S. strike near Bandar Abbas and an IRGC retaliatory-airbase claim \u2014 reminded markets the Persian Gulf disruption persists. EIA\u2019s May STEO cut OPEC 2027 spare capacity to 2.5M bpd from 3.8M prior, keeping non-OPEC supply quality in focus. U.S. sanctions policy on Venezuelan crude remains a relevant input to Atlantic Basin balances. Brent rebounded toward $96\u2013$97; oil is down >10% since May 18.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: May 28, 2026</div>'''


def render_article_row(title, slug, date, excerpt):
    return (f'<article class="hub-article-row"><a href="{slug}" class="hub-article-title">{title}</a>'
            f'<div class="hub-article-meta"><span>{date}</span></div>'
            f'<p class="hub-article-excerpt">{excerpt}…</p></article>')


def main():
    touched = 0
    for slug, data in HUBS.items():
        path = ARTICLES / slug
        if not path.exists():
            print(f"  ✗ missing: {slug}")
            continue
        txt = path.read_text(encoding="utf-8")
        orig = txt

        # 1) Replace the Current Context paragraph
        ctx_pattern = re.compile(
            r'(<h3 style="margin:0 0 8px;font-size:13px;text-transform:uppercase;letter-spacing:0\.06em;color:var\(--blue\)">Current Context</h3>\s*)'
            r'<p style="margin:0;font-size:14\.5px;line-height:1\.6;color:var\(--text-2\)">[^<]*</p>',
            re.DOTALL
        )
        replacement_ctx = (r'\1<p style="margin:0;font-size:14.5px;line-height:1.6;color:var(--text-2)">'
                           + data["context"] + '</p>')
        new_txt, ctx_n = ctx_pattern.subn(replacement_ctx, txt, count=1)
        if ctx_n == 0:
            print(f"  · {slug}: context not matched, skipping context update")
        txt = new_txt

        # 2) Add Last reviewed badge after the lead intro paragraph
        if "Last reviewed: May 28, 2026" not in txt:
            # Find the close of the lead p tag inside .article-body
            lead_pattern = re.compile(
                r'(<p style="font-size:16\.5px;line-height:1\.7;color:var\(--text-2\)">[^<]*?</p>)',
                re.DOTALL
            )
            new_txt, n = lead_pattern.subn(r'\1\n          ' + LAST_REVIEWED_BLOCK, txt, count=1)
            if n > 0:
                txt = new_txt

        # 3) Prepend lead_articles to the article list, if any
        if data["lead_articles"]:
            # Find the start of <article class="hub-article-row"> and inject before
            new_articles_html = "\n            ".join(
                render_article_row(t, s, d, e) for t, s, d, e in data["lead_articles"]
            )
            # Avoid duplicate prepends — check if first lead article slug already appears as first row
            first_slug = data["lead_articles"][0][1]
            # The pattern: <div>\n<article ... href="<first_slug>"... only count one match
            already = f'<article class="hub-article-row"><a href="{first_slug}"' in txt
            # Check if it's the FIRST article in the list (not just present)
            list_open_match = re.search(r'<p[^>]*>30 articles[^<]*</p>\s*<div>\s*(.+?)(?:<article|</div>)', txt, re.DOTALL)
            already_first = False
            if list_open_match:
                already_first = f'href="{first_slug}"' in list_open_match.group(1)[:200]

            if not already_first:
                # Insert right after the opening <div> of the list, before the first <article>
                list_open_pattern = re.compile(
                    r'(<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">[^<]*</p>\s*<div>\s*)',
                    re.DOTALL
                )
                injection = r'\1' + new_articles_html + '\n            '
                new_txt, n = list_open_pattern.subn(injection, txt, count=1)
                if n > 0:
                    txt = new_txt

        # 4) Update the article count if we added articles
        added = len(data["lead_articles"]) if data["lead_articles"] else 0
        if added > 0:
            count_pattern = re.compile(r'<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">(\d+) articles, most recent first\.')
            m = count_pattern.search(txt)
            if m:
                new_count = int(m.group(1)) + added
                txt = count_pattern.sub(
                    f'<p style="color:var(--text-3);font-size:13px;margin:0 0 20px">{new_count} articles, most recent first.',
                    txt, count=1
                )

        if txt != orig:
            path.write_text(txt, encoding="utf-8")
            touched += 1
            print(f"  ✓ {slug}")

    print(f"\n{touched} hubs refreshed.")


if __name__ == "__main__":
    main()
