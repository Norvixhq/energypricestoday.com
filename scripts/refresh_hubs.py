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
        "context": "Current state (June 22, 2026): The interim peace is holding, but the formal one slipped. The signing ceremony set for Geneva on June 19 was abruptly postponed \u2014 Switzerland said the B\u00FCrgenstock talks would not proceed and VP Vance no longer traveled. Mediators Qatar and Pakistan said the U.S. and Iran instead agreed on a roadmap to a final deal within 60 days, with technical talks continuing this week. The interim memorandum that took effect June 18 remains in force, but Trump has threatened renewed strikes and Iran accused Washington of failing to ensure a Lebanon ceasefire, saying talks would focus only on implementing the MOU, not its nuclear program. Tankers are crossing Hormuz again (12M+ barrels overnight) and Treasury issued a 60-day license authorizing the sale of Iranian oil.",
        "lead_articles": [
            ("Geneva Signing Ceremony Postponed; U.S. and Iran Turn to a 60-Day Roadmap", "geneva-signing-ceremony-postponed-us-iran-60-day-roadmap.html", "June 22, 2026",
             "The formal Geneva ceremony set for June 19 was called off; mediators said the sides agreed on a roadmap to a final deal within 60 days. The interim deal holds, but Trump has threatened renewed strikes."),
            ("Crude Holds Near Multi-Month Lows as the Physical Reopening of Hormuz Lags", "crude-holds-multi-month-lows-hormuz-reopening-lags-wti-7482-brent-7790.html", "June 22, 2026",
             "Oil held near multi-month lows as a holding interim peace met a slow physical reopening. Treasury issued a 60-day license authorizing the sale of Iranian oil."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 22, 2026): The interim U.S.-Iran deal is holding and Saudi barrels are beginning to move \u2014 three Saudi supertankers carrying about 6 million barrels exited the Strait of Hormuz after weeks of waiting. But the formal Geneva signing set for June 19 was postponed for a 60-day roadmap, and traffic remains a fraction of the prewar norm with 500+ vessels still waiting. Crude held near multi-month lows (Brent $77.90), down ~36% from the conflict peak. OPEC Secretary General Al Ghais rejected IEA glut forecasts; the trajectory of Saudi crude allocations to Chinese refiners in 2H26 will be a key indicator of how Riyadh manages Iranian volume recovery without triggering a price collapse.",
        "lead_articles": [
            ("Crude Holds Near Multi-Month Lows as the Physical Reopening of Hormuz Lags", "crude-holds-multi-month-lows-hormuz-reopening-lags-wti-7482-brent-7790.html", "June 22, 2026",
             "Three Saudi supertankers exited Hormuz as the deal held, but traffic stays far below normal; OPEC\u2019s Al Ghais rejected IEA glut forecasts as the market recalibrates."),
            ("Geneva Signing Ceremony Postponed; U.S. and Iran Turn to a 60-Day Roadmap", "geneva-signing-ceremony-postponed-us-iran-60-day-roadmap.html", "June 22, 2026",
             "The path to a permanent settlement lengthened to a 60-day roadmap, leaving Riyadh to manage Iranian volume recovery against a softer price backdrop."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 22, 2026): The interim U.S.-Iran deal is holding and tankers are crossing the Strait of Hormuz again, easing the bypass pressure that had elevated the ADCOP pipeline for the UAE, which formally departed OPEC effective May 1. But the formal Geneva signing set for June 19 was postponed for a 60-day roadmap, and traffic remains far below the prewar norm with 500+ vessels still waiting and mine-clearing weeks away. Crude held near multi-month lows (Brent $77.90). The UAE remains a primary U.S. security partner in the Gulf as attention shifts to the pace of normalization and the durability of a deal Trump has threatened to abandon over a Lebanon ceasefire dispute.",
        "lead_articles": [
            ("Geneva Signing Ceremony Postponed; U.S. and Iran Turn to a 60-Day Roadmap", "geneva-signing-ceremony-postponed-us-iran-60-day-roadmap.html", "June 22, 2026",
             "Tankers are crossing Hormuz again, easing bypass pressure on routes like ADCOP, but the formal signing slipped to a 60-day roadmap as normalization lags."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 22, 2026): With the interim U.S.-Iran deal holding and the strait reopening, OPEC has pushed back on the glut narrative. Secretary General Haitham Al Ghais said the group does not expect oil demand to peak in the foreseeable future and rejected IEA forecasts of a future supply surplus, citing fundamentals. Crude held near multi-month lows (Brent $77.90), down ~36% from the conflict peak, and Treasury issued a 60-day license authorizing Iranian oil sales. The bloc faces decisions on how quickly to restore shut-in capacity without accelerating a 2027 oversupply, with Saudi allocations to Asian refiners a key leading indicator. The formal Geneva signing was postponed for a 60-day roadmap.",
        "lead_articles": [
            ("OPEC Pushes Back on Peak-Demand and Glut Forecasts as Market Recalibrates", "geneva-signing-ceremony-postponed-us-iran-60-day-roadmap.html", "June 22, 2026",
             "OPEC chief Al Ghais rejected IEA glut forecasts and forecasts of a near-term demand peak; the deal held but the formal signing slipped to a 60-day roadmap."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 22, 2026): Qatar, a lead mediator alongside Pakistan, helped broker the 60-day roadmap the U.S. and Iran turned to after the formal Geneva signing set for June 19 was postponed. The interim deal is holding and LNG and oil tankers are transiting Hormuz again \u2014 a France-flagged LNG carrier passed through this week \u2014 though traffic remains far below normal with 500+ vessels still waiting. Global LNG benchmarks should ease as Qatari cargoes resume to Asian and European buyers, but mine-clearing and insurer caution could slow the restart. Crude held near multi-month lows as the market recalibrates around the pace of normalization.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 22, 2026): The interim U.S.-Iran deal is holding and crude has held near multi-month lows (Brent $77.90, down ~36% from the conflict peak) \u2014 a softer price backdrop for Russian Urals differentials. Treasury issued a 60-day license authorizing Iranian oil sales, adding a competing barrel to the market. OPEC\u2019s Al Ghais rejected IEA glut forecasts, but analysts warn Mideast supply near prewar levels partly reflects inventory liquidation rather than restored production. Russia remains one of few major producers outside the Gulf disruption zone, but the unwinding war premium erodes the scarcity that had supported its export revenues. The formal Geneva signing was postponed for a 60-day roadmap.",
        "lead_articles": [
            ("Crude Holds Near Multi-Month Lows as the Physical Reopening of Hormuz Lags", "crude-holds-multi-month-lows-hormuz-reopening-lags-wti-7482-brent-7790.html", "June 22, 2026",
             "Crude held near multi-month lows as the deal held and Treasury authorized Iranian oil sales \u2014 a softer backdrop for Urals differentials as competing barrels return."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 22, 2026): The interim U.S.-Iran deal is holding and crude has held near multi-month lows (Brent $77.90). Brazilian pre-salt output continues to grow as a non-OPEC source; the IEA cites strong non-OPEC growth \u2014 of which Brazil is a leading contributor \u2014 among factors that could tip the market into a 2027 surplus, though OPEC\u2019s Al Ghais rejected that view. The softer price path tightens pre-salt economics at the margin, a reversal from the wartime premium. The formal Geneva signing was postponed for a 60-day roadmap as the market shifts focus from war risk to the pace of supply normalization and the demand outlook.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 22, 2026): The interim U.S.-Iran deal is holding and crude has held near multi-month lows (Brent $77.90). Light, sweet Nigerian grades had served as alternatives for refiners losing Middle East crude during the conflict \u2014 a premium that fades as Gulf barrels return and Treasury authorizes Iranian oil sales. OPEC\u2019s Al Ghais pushed back on glut forecasts, but the softer price environment pressures Nigerian fiscal math as the war premium unwinds. The formal Geneva signing was postponed for a 60-day roadmap, leaving the market focused on the pace of normalization and the demand outlook.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 22, 2026): The interim U.S.-Iran deal is holding and crude has held near multi-month lows (Brent $77.90, down ~36% from the peak). The softer price path reduces the pull on marginal Atlantic Basin barrels that had gained relevance during the wartime disruption, and Treasury\u2019s 60-day license authorizing Iranian oil sales adds competing supply. U.S. sanctions policy on Venezuelan crude remains a key variable as the market shifts from scarcity to a potential 2027 surplus \u2014 a view OPEC\u2019s Al Ghais disputes. Venezuelan production capacity stays structurally constrained. The formal Geneva signing was postponed for a 60-day roadmap.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 22, 2026</div>'''


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
        if "Last reviewed: June 22, 2026" not in txt:
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
