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
        "context": "Current state (June 3, 2026): Signals from Washington and Tehran are diverging. President Trump pushed back Tuesday on reports that U.S.-Iran communications had broken down, calling them \"false and erroneous,\" and said a memorandum of understanding to reopen the Strait of Hormuz could be reached within the next week \u2014 while seeking written commitments from Iran on nuclear concessions. Secretary of State Rubio told the Senate that Iran has agreed to negotiate aspects of its nuclear program it previously refused to discuss. Iran\u2019s Fars news agency countered that the two sides had not exchanged messages for several days, the last being Tehran\u2019s \"clear message\" over Lebanon. CENTCOM said it repelled Iranian missiles and drones Tuesday; Iran is still seeking a halt to Israel\u2019s campaign against Hezbollah.",
        "lead_articles": [
            ("Trump Pushes Back on Reports U.S.-Iran Talks Collapsed; Says Hormuz MOU Could Come Within a Week", "trump-pushes-back-talks-collapse-hormuz-mou-within-week.html", "June 3, 2026",
             "Trump called reports of a breakdown \"false and erroneous\" and said a Hormuz MOU could come within a week, seeking written nuclear commitments. Rubio told the Senate Iran agreed to negotiate aspects of its nuclear program."),
            ("Brent Climbs Toward $98 for a Third Straight Session as Risk Premium Returns", "brent-climbs-toward-98-third-straight-session-risk-premium.html", "June 3, 2026",
             "Oil rose a third straight session as uncertainty over the talks kept a risk premium in the market. CENTCOM said it defeated multiple Iranian missiles and drones and launched defensive strikes."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 3, 2026): Saudi Arabia is watching a contested U.S.-Iran negotiating track. Trump says a memorandum of understanding to reopen the Strait of Hormuz could come within a week, while Iranian media cast doubt; Rubio told the Senate Iran agreed to negotiate aspects of its nuclear program. Saudi Aramco CEO Amin Nasser has warned market normalization is pushed to 2027 if reopening is delayed past mid-June \u2014 a deadline now imminent. Saudi production remains at the lowest level since 1990. Oil rose a third straight session (Brent toward $98, WTI ~$96) as the risk premium returned after May\u2019s near-19% slide.",
        "lead_articles": [
            ("Brent Climbs Toward $98 for a Third Straight Session as Risk Premium Returns", "brent-climbs-toward-98-third-straight-session-risk-premium.html", "June 3, 2026",
             "Oil rose a third straight session as uncertainty over U.S.-Iran talks kept a risk premium in the market. API data showed a sixth straight weekly crude draw if the EIA confirms."),
            ("Trump Pushes Back on Reports U.S.-Iran Talks Collapsed; Says Hormuz MOU Could Come Within a Week", "trump-pushes-back-talks-collapse-hormuz-mou-within-week.html", "June 3, 2026",
             "A Hormuz MOU could come within a week, Trump says \u2014 the deadline Aramco\u2019s Nasser flagged as the line past which market normalization slips to 2027."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 3, 2026): The UAE, which formally departed OPEC effective May 1, is watching a contested U.S.-Iran track. Trump says a Hormuz MOU could come within a week and pushed back on reports the channel collapsed; Iranian media cast doubt, and Rubio reported progress on nuclear talks. CENTCOM repelled Iranian missiles and drones Tuesday and Israel kept striking southern Lebanon, keeping Gulf spillover risk live. ADCOP pipeline continues to carry available bypass volumes that don\u2019t transit Hormuz. Oil rose a third straight session (Brent toward $98). The UAE remains a primary U.S. security partner in the Gulf.",
        "lead_articles": [
            ("Trump Pushes Back on Reports U.S.-Iran Talks Collapsed; Says Hormuz MOU Could Come Within a Week", "trump-pushes-back-talks-collapse-hormuz-mou-within-week.html", "June 3, 2026",
             "Trump says a Hormuz MOU could come within a week, while Iranian media cast doubt. A reopening would relieve the bypass pressure on routes like ADCOP."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 3, 2026): A contested U.S.-Iran track has revived the supply-disruption premium. Trump says a memorandum of understanding to reopen the Strait of Hormuz could come within a week; Iranian media cast doubt; Rubio told the Senate Iran agreed to negotiate aspects of its nuclear program. Saudi Arabia, Qatar, and the UAE (former member, departed May 1) are watching the reopening timeline. EIA assessed ~10.5M bpd of Persian Gulf production shut in; energy executives via MUFG warn full normalization may not occur until 2027. Oil rose a third straight session (Brent toward $98) and API reported a sixth straight weekly U.S. crude draw if confirmed.",
        "lead_articles": [
            ("Brent Climbs Toward $98 for a Third Straight Session as Risk Premium Returns", "brent-climbs-toward-98-third-straight-session-risk-premium.html", "June 3, 2026",
             "Oil rose a third straight session as uncertainty over the U.S.-Iran talks kept a risk premium in the market that keeps shut-in OPEC barrels off the table."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 3, 2026): Qatar, a principal mediator alongside Pakistan, is watching a contested U.S.-Iran track. Trump says a memorandum of understanding to reopen the Strait of Hormuz could come within a week, which would allow Qatari LNG exports to resume; Iranian media cast doubt, and Rubio reported progress on nuclear talks. Israel kept striking southern Lebanon Tuesday, a day after Trump asked Netanyahu not to attack Beirut, keeping the Lebanon and Hormuz tracks entangled. JKM and TTF benchmarks remain elevated.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 3, 2026): Russia remains one of few major producers outside the Persian Gulf disruption zone as a contested U.S.-Iran track keeps a risk premium in oil. Trump says a Hormuz MOU could come within a week; Iranian media cast doubt. Oil rose a third straight session, Brent toward $98 and WTI ~$96, recovering part of May\u2019s near-19% slide. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers. Urals discount dynamics remain in focus as benchmark prices whipsaw.",
        "lead_articles": [
            ("Brent Climbs Toward $98 for a Third Straight Session as Risk Premium Returns", "brent-climbs-toward-98-third-straight-session-risk-premium.html", "June 3, 2026",
             "Oil rose a third straight session as uncertainty over U.S.-Iran talks kept a risk premium in the market, affecting Urals differential dynamics."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 3, 2026): Brazilian pre-salt production continues to grow as a non-OPEC supply source as a contested U.S.-Iran track keeps a risk premium in oil. Trump says a Hormuz MOU could come within a week; Iranian media cast doubt. Oil rose a third straight session, Brent toward $98, recovering part of May\u2019s near-19% slide \u2014 its worst month since the pandemic. The price whipsaw affects pre-salt project economics at the margin. Petrobras Q1 results and pre-salt output milestones remain key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 3, 2026): Nigerian crude remains important to the non-OPEC supply mix as a contested U.S.-Iran track keeps a risk premium in oil. Light, sweet Nigerian grades have served as alternatives for refiners losing access to Middle East crude through the conflict. Trump says a Hormuz MOU could come within a week; Iranian media cast doubt. Oil rose a third straight session, Brent toward $98. The G7 leaders summit June 15-17 in Evian is expected to address supply-chain diversification.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 3, 2026): Venezuelan production capacity remains a structurally relevant question as a contested U.S.-Iran track keeps a risk premium in oil. Trump says a Hormuz MOU could come within a week; Iranian media cast doubt. Oil rose a third straight session, Brent toward $98, recovering part of May\u2019s near-19% slide. U.S. sanctions policy on Venezuelan crude remains a relevant input to Atlantic Basin balances as benchmark prices whipsaw.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 3, 2026</div>'''


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
        if "Last reviewed: June 3, 2026" not in txt:
            # Find the close of the lead p tag inside .article-body
            lead_pattern = re.compile(
                r'(<p style="font-size:16\.5px;line-height:1\.7;color:var\(--text-2\)">[^<]*?</p>)',
                re.DOTALL
            )
            new_txt, n = lead_pattern.subn(r'\1\n          ' + LAST_REVIEWED_BLOCK, txt, count=1)
            if n > 0:
                txt = new_txt

        # 3) Daily lead articles REPLACE prior daily leads (no accumulation).
        #    Prior prepends are wrapped in <!--DAILY_LEADS_START-->...<!--DAILY_LEADS_END-->.
        #    Strip any existing marked block first, then inject today's (also marked).
        LEAD_START = "<!--DAILY_LEADS_START-->"
        LEAD_END = "<!--DAILY_LEADS_END-->"

        # Count how many rows are currently inside an existing marker block (to decrement the count)
        prior_block = re.search(re.escape(LEAD_START) + r'(.*?)' + re.escape(LEAD_END), txt, re.DOTALL)
        prior_lead_count = 0
        if prior_block:
            prior_lead_count = prior_block.group(1).count('<article class="hub-article-row">')
            # Remove the entire prior marked block (and trailing whitespace)
            txt = re.sub(re.escape(LEAD_START) + r'.*?' + re.escape(LEAD_END) + r'\s*', '', txt, flags=re.DOTALL)

        added = 0
        if data["lead_articles"]:
            new_articles_html = "\n            ".join(
                render_article_row(t, s, d, e) for t, s, d, e in data["lead_articles"]
            )
            block = LEAD_START + "\n            " + new_articles_html + "\n            " + LEAD_END + "\n            "
            list_open_pattern = re.compile(
                r'(<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">[^<]*</p>\s*<div>\s*)',
                re.DOTALL
            )
            new_txt, n = list_open_pattern.subn(r'\1' + block, txt, count=1)
            if n > 0:
                txt = new_txt
                added = len(data["lead_articles"])

        # 4) Reconcile the displayed article count: subtract prior leads, add today's.
        count_pattern = re.compile(r'<p style="color:var\(--text-3\);font-size:13px;margin:0 0 20px">(\d+) articles, most recent first\.')
        m = count_pattern.search(txt)
        if m:
            new_count = int(m.group(1)) - prior_lead_count + added
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
