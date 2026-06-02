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
        "context": "Current state (June 1, 2026): Iran announced Monday it is halting all communication with the United States unless Israel stops its expanding offensive in southern Lebanon, freezing a negotiating track that days earlier looked close to a 60-day MOU. Foreign Minister Araghchi: a U.S.-Iran ceasefire \"constitutes, without any ambiguity, a comprehensive ceasefire across all fronts, including Lebanon.\" Tehran threatened to completely close the Strait of Hormuz and open the Bab el-Mandeb front. Iran crude loadings fell below 0.3M bpd in May (from 1.5M in April per UBS). President Trump told CNBC he \"couldn\u2019t care less\" if talks end, then said calls with Netanyahu and Hezbollah secured a halt to the Lebanon shooting; the Iran-U.S. channel stayed frozen.",
        "lead_articles": [
            ("Iran Halts Communication With U.S. Over Israel\u2019s Lebanon Offensive; Threatens to Close Hormuz", "iran-halts-us-communication-lebanon-offensive-hormuz-threat.html", "June 1, 2026",
             "Iran announced Monday it is halting all communication with the U.S. unless Israel stops its Lebanon offensive. FM Araghchi said any ceasefire must cover \"all fronts, including Lebanon.\" Tehran threatened to close Hormuz and open the Bab el-Mandeb front."),
            ("Trump Brokers Israel-Hezbollah Shooting Halt as Iran Freezes U.S. Talks Over Lebanon", "trump-brokers-israel-hezbollah-shooting-halt-iran-freezes-talks.html", "June 1, 2026",
             "Trump said calls with Netanyahu and, via intermediaries, Hezbollah secured pledges that \"all shooting will stop\" in Lebanon, even as Iran suspended its diplomatic channel with Washington over the same escalation."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 1, 2026): Saudi Arabia is watching the U.S.-Iran channel freeze after Iran suspended communication over Israel\u2019s Lebanon offensive and threatened to close the Strait of Hormuz. Saudi Aramco CEO Amin Nasser has warned market normalization is pushed to 2027 if reopening is delayed past mid-June \u2014 a deadline now in jeopardy with talks stalled. Saudi production remains at the lowest level since 1990. Oil rallied Monday (Brent +4% to $94.98, WTI +5% to $92.16) after Brent\u2019s ~19% slide in May, its worst month since the pandemic.",
        "lead_articles": [
            ("Oil Jumps as Trump Says He \u2018Couldn\u2019t Care Less\u2019 Whether Iran Talks End", "oil-jumps-trump-couldnt-care-less-iran-talks-end.html", "June 1, 2026",
             "Oil rallied Monday after the U.S.-Iran channel froze. WTI rose more than 5% to $92.16, Brent more than 4% to $94.98, erasing hopes for a near-term Hormuz reopening."),
            ("Iran Halts Communication With U.S. Over Israel\u2019s Lebanon Offensive; Threatens to Close Hormuz", "iran-halts-us-communication-lebanon-offensive-hormuz-threat.html", "June 1, 2026",
             "Tehran threatened to completely close the Strait of Hormuz and open the Bab el-Mandeb front, reviving the supply-disruption fears that keep Saudi shut-in barrels off the market."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 1, 2026): The UAE, which formally departed OPEC effective May 1, is watching the U.S.-Iran channel freeze after Iran suspended communication over Israel\u2019s Lebanon offensive and threatened to close the Strait of Hormuz and open the Bab el-Mandeb front. The renewed Lebanon escalation and Hormuz-closure threat keep Gulf spillover risk live. ADCOP pipeline continues to carry available bypass volumes that don\u2019t transit Hormuz. Oil rallied Monday (Brent +4% to $94.98) after a brutal May. The UAE remains a primary U.S. security partner in the Gulf.",
        "lead_articles": [
            ("Iran Halts Communication With U.S. Over Israel\u2019s Lebanon Offensive; Threatens to Close Hormuz", "iran-halts-us-communication-lebanon-offensive-hormuz-threat.html", "June 1, 2026",
             "Iran suspended its U.S. channel over Israel\u2019s Lebanon offensive and threatened to close Hormuz \u2014 reviving the Gulf supply-disruption risk that bypass routes like ADCOP only partly offset."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 1, 2026): The U.S.-Iran negotiating channel froze Monday after Iran suspended communication over Israel\u2019s Lebanon offensive and threatened to close the Strait of Hormuz, reviving the supply-disruption premium. Saudi Arabia, Qatar, and the UAE (former member, departed May 1) are watching a reopening timeline slip. Iran crude loadings fell below 0.3M bpd in May. EIA assessed ~10.5M bpd of Persian Gulf production shut in; energy executives via MUFG warn full normalization may not occur until 2027. Oil rallied Monday (Brent +4% to $94.98) after its worst month since the pandemic.",
        "lead_articles": [
            ("Oil Jumps as Trump Says He \u2018Couldn\u2019t Care Less\u2019 Whether Iran Talks End", "oil-jumps-trump-couldnt-care-less-iran-talks-end.html", "June 1, 2026",
             "Oil rallied Monday as the U.S.-Iran channel froze, erasing hopes for a near-term Hormuz reopening that would let shut-in OPEC barrels return."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 1, 2026): Qatar, a principal mediator alongside Pakistan, is watching the U.S.-Iran channel freeze after Iran suspended communication over Israel\u2019s Lebanon offensive. Tehran threatened to completely close the Strait of Hormuz and open the Bab el-Mandeb front, which would further disrupt Qatari LNG flows. The collapse of the talks erases the near-term path to a 60-day MOU that would have reopened the strait. JKM and TTF benchmarks remain elevated. Trump said late-Monday calls with Netanyahu and Hezbollah secured a halt to the Lebanon shooting.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 1, 2026): Russia remains one of few major producers outside the Persian Gulf disruption zone as the U.S.-Iran channel freezes over Israel\u2019s Lebanon offensive. The collapse of talks and Tehran\u2019s threat to close the Strait of Hormuz revived the supply-disruption premium, sending Brent +4% to $94.98 Monday after its ~19% slide in May. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers. Urals discount dynamics are again in focus as benchmark prices whipsaw.",
        "lead_articles": [
            ("Oil Jumps as Trump Says He \u2018Couldn\u2019t Care Less\u2019 Whether Iran Talks End", "oil-jumps-trump-couldnt-care-less-iran-talks-end.html", "June 1, 2026",
             "Oil rallied Monday as the U.S.-Iran channel froze. The renewed disruption premium affects Urals differential dynamics for one of few producers outside the Gulf zone."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 1, 2026): Brazilian pre-salt production continues to grow as a non-OPEC supply source as the U.S.-Iran channel freezes over Israel\u2019s Lebanon offensive. Tehran\u2019s threat to close the Strait of Hormuz revived the supply premium, sending Brent +4% to $94.98 Monday after a May in which it fell ~19% \u2014 its worst month since the pandemic. The price whipsaw affects pre-salt project economics at the margin. Petrobras Q1 results and pre-salt output milestones remain key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 1, 2026): Nigerian crude remains important to the non-OPEC supply mix as the U.S.-Iran channel freezes over Israel\u2019s Lebanon offensive. Light, sweet Nigerian grades have served as alternatives for refiners losing access to Middle East crude through the conflict. Tehran\u2019s threat to close the Strait of Hormuz and open the Bab el-Mandeb front revived the supply premium, sending Brent +4% to $94.98 Monday. The G7 leaders summit June 15-17 in Evian is expected to address supply-chain diversification.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 1, 2026): Venezuelan production capacity remains a structurally relevant question as the U.S.-Iran channel freezes over Israel\u2019s Lebanon offensive. Tehran\u2019s threat to close the Strait of Hormuz and open the Bab el-Mandeb front revived the supply-disruption premium, sending Brent +4% to $94.98 Monday after its worst month since the pandemic. U.S. sanctions policy on Venezuelan crude remains a relevant input to Atlantic Basin balances as benchmark prices whipsaw.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 1, 2026</div>'''


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
        if "Last reviewed: June 1, 2026" not in txt:
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
