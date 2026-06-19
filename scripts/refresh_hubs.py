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
        "context": "Current state (June 18, 2026): The war is ending. The U.S. and Iran signed an interim peace agreement that took effect June 18, formally closing the three-month conflict. Presidents Trump and Pezeshkian, with VP Vance and parliament speaker Qalibaf, electronically signed the memorandum on June 15; Trump signed at the G7 in France, and a formal Geneva ceremony is set for June 19. Iran agreed not to produce or acquire nuclear weapons and to dilute its enriched uranium, which the IAEA will verify; the U.S. agreed to release $25 billion in frozen Iranian assets contingent on compliance, with officials stressing no cash has changed hands. Under Article 5, Iran will guarantee free passage for commercial vessels through the Strait of Hormuz for 60 days. Risk remains: Iran warns an Israeli move on Lebanon would violate the deal.",
        "lead_articles": [
            ("U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", "us-iran-sign-peace-deal-interim-agreement-takes-effect-ending-war.html", "June 18, 2026",
             "The interim accord took effect June 18; Trump and Pezeshkian signed electronically June 15, with a Geneva ceremony June 19. Iran will forgo nuclear weapons and dilute enriched uranium; the U.S. will release $25 billion in frozen assets on compliance."),
            ("Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", "crude-falls-multi-month-lows-supply-returns-wti-7583-brent-7841.html", "June 18, 2026",
             "Oil tumbled as the deal took effect and Hormuz reopens under a 60-day free-passage clause; the IEA sees a possible significant supply surplus by 2027."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz under a 60-day free-passage clause and clearing the way for shut-in Saudi barrels to return. Crude tumbled to multi-month lows (Brent $78.41), and the IEA said the market could move into a significant supply surplus by 2027 as Gulf production resumes. Saudi output had fallen to near its lowest since 1990 during the closure; the kingdom now faces the opposite challenge of ramping back into a market where OPEC has cut its 2026 demand-growth view and a glut could form. Mine-clearing and infrastructure repairs mean the return of full Saudi flows will be gradual.",
        "lead_articles": [
            ("Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", "crude-falls-multi-month-lows-supply-returns-wti-7583-brent-7841.html", "June 18, 2026",
             "Crude tumbled as the peace deal took effect; the IEA sees a possible 2027 supply surplus as Saudi and other Gulf barrels return through a reopening Hormuz."),
            ("U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", "us-iran-sign-peace-deal-interim-agreement-takes-effect-ending-war.html", "June 18, 2026",
             "The reopening of Hormuz under a 60-day free-passage clause clears the way for shut-in Saudi production to return to the market."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz under a 60-day free-passage clause. For the UAE, which formally departed OPEC effective May 1, the reopening relieves the bypass pressure that had elevated the role of the ADCOP pipeline during the closure. Crude tumbled to multi-month lows (Brent $78.41), and the IEA sees a possible 2027 supply surplus as Gulf flows normalize. The UAE remains a primary U.S. security partner in the Gulf as attention shifts from wartime disruption to the logistics of restarting normal tanker traffic, which experts say could take weeks given mine-clearing and insurer caution.",
        "lead_articles": [
            ("U.S. and Iran Sign Peace Deal; Interim Agreement Takes Effect, Ending the War", "us-iran-sign-peace-deal-interim-agreement-takes-effect-ending-war.html", "June 18, 2026",
             "The reopening of Hormuz relieves the bypass pressure on routes like ADCOP and lets Gulf exporters normalize flows over the coming weeks."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz and shifting the supply outlook from scarcity to a potential glut. The IEA said the market could move into a significant supply surplus by 2027 as disrupted Gulf barrels return; OPEC last week cut its own 2026 world oil demand-growth forecast to 970,000 bpd, a second straight downward revision. Crude tumbled to multi-month lows (Brent $78.41), well below the $87 Fitch had projected for full-year 2026. The bloc now faces decisions on how quickly to restore shut-in capacity without accelerating a 2027 oversupply, with prices already pricing the end of the war premium.",
        "lead_articles": [
            ("Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", "crude-falls-multi-month-lows-supply-returns-wti-7583-brent-7841.html", "June 18, 2026",
             "The IEA sees a possible 2027 supply surplus as Gulf barrels return through a reopening Hormuz; OPEC last week cut its 2026 demand-growth forecast to 970,000 bpd."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz under a 60-day free-passage clause \u2014 the trigger for Qatari LNG exports, which transit the strait, to resume. Global LNG benchmarks had remained elevated on reduced Hormuz flows; a reopening should ease them as cargoes return to Asian and European buyers. Crude tumbled to multi-month lows on the deal, and the IEA sees a possible 2027 supply surplus. As a principal mediator alongside Pakistan, Qatar\u2019s diplomatic role gives way to its commercial stake in a swift, durable reopening, though mine-clearing and insurer caution could slow the LNG restart by weeks.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz and pushing crude to multi-month lows (Brent $78.41) \u2014 a softer price backdrop for Russian Urals differentials. The IEA sees a possible significant supply surplus by 2027 as Gulf barrels return alongside strong non-OPEC growth, and OPEC cut its 2026 demand-growth view. Russia remains one of few major producers outside the Persian Gulf disruption zone, but the end of the war erodes the scarcity premium that had supported its export revenues. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers.",
        "lead_articles": [
            ("Crude Falls to Multi-Month Lows as Supply Returns: WTI Near $75.83, Brent $78.41", "crude-falls-multi-month-lows-supply-returns-wti-7583-brent-7841.html", "June 18, 2026",
             "Crude tumbled as the peace deal took effect and Hormuz reopens; the IEA sees a possible 2027 surplus \u2014 a softer backdrop for Urals differentials."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz and pushing crude to multi-month lows (Brent $78.41). Brazilian pre-salt production continues to grow as a non-OPEC supply source; the IEA cites strong non-OPEC growth \u2014 of which Brazil is a leading contributor \u2014 among the factors that could tip the market into a significant supply surplus by 2027 as Gulf barrels return. The softer price path tightens pre-salt project economics at the margin, a reversal from the wartime premium that had supported Brazilian output through the spring. Petrobras output milestones remain key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz and pushing crude to multi-month lows (Brent $78.41). Light, sweet Nigerian grades had served as alternatives for refiners losing Middle East crude during the conflict \u2014 a premium that now fades as Gulf barrels return and the IEA flags a possible 2027 supply surplus. The G7 summit in France, where Trump signed the deal, was expected to address energy-supply diversification. Nigeria faces a softer price environment as the war premium unwinds and the market refocuses on demand growth and non-OPEC supply.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 18, 2026): The U.S.-Iran interim peace deal took effect June 18, reopening the Strait of Hormuz and pushing crude to multi-month lows (Brent $78.41), with the IEA projecting a possible significant supply surplus by 2027. For Venezuela, the softer price path reduces the pull on marginal Atlantic Basin barrels that had gained relevance during the wartime disruption. U.S. sanctions policy on Venezuelan crude remains a key variable as benchmarks fall and the market shifts from scarcity to potential oversupply. Venezuelan production capacity stays structurally constrained regardless of the improved geopolitical backdrop.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 18, 2026</div>'''


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
        if "Last reviewed: June 18, 2026" not in txt:
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
