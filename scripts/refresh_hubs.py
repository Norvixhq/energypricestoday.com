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
        "context": "Current state (June 13, 2026): A peace deal may be hours away \u2014 or a claim that outran the diplomacy. Pakistani Prime Minister Sharif says the U.S. and Iran reached a final, agreed-upon text, the \u201CIslamabad declaration,\u201D with an electronic signing expected within ~24 hours and a Geneva ceremony to follow, attended by VP Vance. But the claim is contested: a source close to Iran\u2019s negotiating team told Fars that the Sunday-Geneva signing report is \u201Ccompletely false,\u201D and both Trump and Vance disputed leaked details, stressing Iran receives no cash merely for signing. No text is confirmed signed by both sides. The U.S. framework would reopen Hormuz, lift the blockade, dismantle Iran\u2019s nuclear program and remove enriched uranium; an Iranian version is more favorable to Tehran. Both commit to reopening the strait within 30 days of a final deal.",
        "lead_articles": [
            ("Pakistan Says U.S. and Iran Reach a Final Text \u2014 the Islamabad Declaration; Signing Expected Within Hours", "pakistan-us-iran-final-text-islamabad-declaration-signing-expected.html", "June 13, 2026",
             "PM Sharif says the two sides reached a final text, with electronic signing likely within 24 hours and a Geneva ceremony to follow \u2014 though Iran\u2019s team calls the Sunday-Geneva claim \u201Ccompletely false\u201D and Trump and Vance dispute leaked details."),
            ("Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", "crude-holds-three-month-low-markets-closed-wti-8488-brent-8733.html", "June 13, 2026",
             "Oil markets are closed for the weekend after crude fell to a three-month low Friday. Monday\u2019s open hinges on whether a memorandum is actually signed."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 13, 2026): Saudi Arabia is watching a possible signing this weekend. Pakistan says the U.S. and Iran reached a final text (the \u201CIslamabad declaration\u201D), with a Geneva signing expected, though Iran\u2019s team and U.S. officials dispute leaked details and no text is confirmed signed. Both draft frameworks commit to reopening the Strait of Hormuz within 30 days of a final deal \u2014 the trigger for restoring shut-in Saudi barrels. Crude settled Friday at a three-month low (Brent $87.33), the $87 level Fitch projects for full-year 2026. OPEC this week cut its 2026 demand-growth forecast to 970,000 bpd; Fitch warns rapid capacity recovery could tip the market into oversupply by 4Q26.",
        "lead_articles": [
            ("Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", "crude-holds-three-month-low-markets-closed-wti-8488-brent-8733.html", "June 13, 2026",
             "Crude sits at a three-month low as a U.S.-Iran signing nears; OPEC cut its 2026 demand view and Fitch flags possible 4Q26 oversupply once Hormuz reopens and Saudi barrels return."),
            ("Pakistan Says U.S. and Iran Reach a Final Text \u2014 the Islamabad Declaration; Signing Expected Within Hours", "pakistan-us-iran-final-text-islamabad-declaration-signing-expected.html", "June 13, 2026",
             "A confirmed deal reopening Hormuz within 30 days would let Saudi Arabia rebuild export volumes from production near its lowest since 1990."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 13, 2026): The UAE, which formally departed OPEC effective May 1, is watching a possible weekend signing. Pakistan says a final text (the \u201CIslamabad declaration\u201D) is reached, with a Geneva ceremony expected, though the claim is contested and no text is confirmed signed. Both draft frameworks commit to reopening the Strait of Hormuz within 30 days of a final deal; a reopening would relieve the bypass pressure on routes like the ADCOP pipeline. Crude settled Friday at a three-month low (Brent $87.33). The UAE remains a primary U.S. security partner in the Gulf as the diplomacy moves toward a possible signature.",
        "lead_articles": [
            ("Pakistan Says U.S. and Iran Reach a Final Text \u2014 the Islamabad Declaration; Signing Expected Within Hours", "pakistan-us-iran-final-text-islamabad-declaration-signing-expected.html", "June 13, 2026",
             "A confirmed deal reopening Hormuz within 30 days would relieve bypass pressure on routes like ADCOP and let Gulf exporters normalize flows."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 13, 2026): OPEC this week cut its 2026 world oil demand-growth forecast to 970,000 bpd from 1.17 million \u2014 a second straight downward revision \u2014 while projecting a 2027 rebound of 1.73 million bpd. The cut lands as a U.S.-Iran signing may be hours away: Pakistan says a final text (the \u201CIslamabad declaration\u201D) is reached, with a Geneva ceremony expected, though the claim is contested. Both drafts commit to reopening the Strait of Hormuz within 30 days of a final deal. Crude settled Friday at a three-month low (Brent $87.33), the $87 level Fitch projects for 2026; Fitch warns rapid capacity recovery, strong non-OPEC growth, and a more aggressive OPEC+ policy could recreate an oversupply by 4Q26.",
        "lead_articles": [
            ("Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", "crude-holds-three-month-low-markets-closed-wti-8488-brent-8733.html", "June 13, 2026",
             "OPEC cut its 2026 demand-growth forecast to 970,000 bpd as crude held at a three-month low; Fitch flags possible 4Q26 oversupply once Hormuz reopens and shut-in Gulf barrels return."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 13, 2026): Qatar, a principal mediator alongside Pakistan, is watching a possible weekend signing. Pakistan says the U.S. and Iran reached a final text (the \u201CIslamabad declaration\u201D), with a Geneva ceremony expected, though the claim is contested and no text is confirmed signed. Both drafts commit to reopening the Strait of Hormuz within 30 days of a final deal \u2014 the trigger for Qatari LNG exports, which transit the strait, to resume. Global LNG benchmarks remain elevated on reduced Hormuz flows; a reopening would ease them. Crude settled Friday at a three-month low as markets closed for the weekend.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 13, 2026): Russia remains one of few major producers outside the Persian Gulf disruption zone as a U.S.-Iran signing may near. Pakistan says a final text (the \u201CIslamabad declaration\u201D) is reached, with a Geneva ceremony expected, though the claim is contested. Both drafts commit to reopening the Strait of Hormuz within 30 days of a final deal. Crude settled Friday at a three-month low (Brent $87.33), the $87 level Fitch projects for 2026 \u2014 a softer backdrop for Urals differentials, compounded by OPEC\u2019s cut to its 2026 demand-growth view. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers.",
        "lead_articles": [
            ("Crude Holds Near a Three-Month Low With Markets Closed; WTI $84.88, Brent $87.33", "crude-holds-three-month-low-markets-closed-wti-8488-brent-8733.html", "June 13, 2026",
             "Crude held at a three-month low as a U.S.-Iran signing neared; OPEC cut its 2026 demand view and Fitch sees Brent averaging $87 for 2026 \u2014 a softer backdrop for Urals differentials."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 13, 2026): Brazilian pre-salt production continues to grow as a non-OPEC supply source as a U.S.-Iran signing may near. Pakistan says a final text (the \u201CIslamabad declaration\u201D) is reached, with a Geneva ceremony expected, though the claim is contested. Both drafts commit to reopening the Strait of Hormuz within 30 days. Crude settled Friday at a three-month low (Brent $87.33). Fitch cites strong non-OPEC supply growth \u2014 of which Brazil is a leading contributor \u2014 among the factors that could recreate an oversupply by 4Q26 once Hormuz reopens, a view reinforced by OPEC\u2019s downgraded 2026 demand outlook.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 13, 2026): Nigerian crude remains important to the non-OPEC supply mix as a U.S.-Iran signing may near. Light, sweet Nigerian grades served as alternatives for refiners losing Middle East crude during the conflict \u2014 a premium that fades as the reopening path firms. Pakistan says a final text (the \u201CIslamabad declaration\u201D) is reached, with a Geneva ceremony expected, though contested; crude settled Friday at a three-month low. The G7 leaders summit June 15-17 in France is expected to address supply-chain diversification, near where a signing ceremony may be held.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 13, 2026): Venezuelan production capacity remains a structurally relevant question as a U.S.-Iran signing may near. Pakistan says a final text (the \u201CIslamabad declaration\u201D) is reached, with a Geneva ceremony expected, though the claim is contested. Both drafts commit to reopening the Strait of Hormuz within 30 days. Crude settled Friday at a three-month low (Brent $87.33); OPEC cut its 2026 demand-growth view, and Fitch projects possible oversupply by 4Q26 once flows normalize \u2014 a softer price path that reduces the pull on marginal Atlantic Basin barrels. U.S. sanctions policy on Venezuelan crude remains a relevant input.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 13, 2026</div>'''


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
        if "Last reviewed: June 13, 2026" not in txt:
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
        # Defensively strip any ORPHANED markers left by past manual edits (prevents
        # mismatched START/END counts from corrupting future strip passes).
        txt = txt.replace(LEAD_START, '').replace(LEAD_END, '')

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
