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
        "context": "Current state (June 7, 2026): Escalation has re-intensified. Israel struck Iranian-backed Hezbollah military targets in southern Beirut on Sunday in response to Hezbollah firing missiles into northern Israel \u2014 a dangerous moment for the U.S.-Iran peace talks. Before the strike, Iran\u2019s Islamic Revolutionary Guard Corps warned via state media that if Israel hit Beirut, Iran would launch strikes against Israel and could halt negotiations with Washington. Over the weekend, U.S. and Iranian forces exchanged strikes near the Strait of Hormuz: CENTCOM intercepted a wave of Iranian missiles and drones, struck Iranian coastal radar sites, and downed six drones in two days, while Iran fired \"warning\" shots near the strait. President Trump nonetheless said talks were progressing well.",
        "lead_articles": [
            ("Israel Strikes Hezbollah Targets in Southern Beirut, Imperiling U.S.-Iran Talks", "israel-strikes-southern-beirut-imperiling-us-iran-talks.html", "June 7, 2026",
             "Israel struck Hezbollah targets in southern Beirut Sunday. Iran\u2019s IRGC had warned it would strike Israel and could halt negotiations with the U.S. if Beirut were hit \u2014 a dangerous moment for the talks and the tenuous ceasefire."),
            ("U.S. and Iran Exchange Strikes Near Hormuz; CENTCOM Downs Drones, Hits Coastal Radar", "us-iran-exchange-strikes-hormuz-centcom-downs-drones-coastal-radar.html", "June 7, 2026",
             "U.S. and Iranian forces exchanged strikes near the strait over the weekend; CENTCOM downed six Iranian drones and struck coastal radar sites, while Iran fired \"warning\" shots tied to U.S. naval repositioning."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 7, 2026): Saudi Arabia is watching a sharp re-escalation. Israel struck Hezbollah targets in southern Beirut on Sunday, and Iran had warned it would retaliate and could halt U.S. talks if Beirut were hit; over the weekend U.S. and Iranian forces exchanged strikes near the Strait of Hormuz, with a strike also hitting Kuwait International Airport \u2014 a sign of widening Gulf spillover. Saudi Aramco CEO Amin Nasser has warned market normalization slips to 2027 if reopening is delayed past mid-June. Saudi production remains at the lowest level since 1990. Brent slid to ~$93 Friday on weak Chinese demand even as it held 3\u20134% higher for the week.",
        "lead_articles": [
            ("U.S. and Iran Exchange Strikes Near Hormuz; CENTCOM Downs Drones, Hits Coastal Radar", "us-iran-exchange-strikes-hormuz-centcom-downs-drones-coastal-radar.html", "June 7, 2026",
             "U.S. and Iranian forces exchanged strikes near Hormuz over the weekend; a strike also hit Kuwait International Airport, underscoring the conflict\u2019s widening spillover across the Gulf."),
            ("Israel Strikes Hezbollah Targets in Southern Beirut, Imperiling U.S.-Iran Talks", "israel-strikes-southern-beirut-imperiling-us-iran-talks.html", "June 7, 2026",
             "Israel\u2019s strike on southern Beirut Sunday raised the risk of a wider escalation that would keep Saudi shut-in barrels off the market."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 7, 2026): The UAE, which formally departed OPEC effective May 1, is watching a sharp re-escalation. Israel struck Hezbollah targets in southern Beirut on Sunday, and Iran had warned it would retaliate and could halt U.S. talks if Beirut were hit; over the weekend U.S. and Iranian forces exchanged strikes near the Strait of Hormuz, with a strike hitting Kuwait International Airport \u2014 a reminder that Gulf spillover risk is live. ADCOP pipeline continues to carry available bypass volumes that don\u2019t transit Hormuz. Brent slid to ~$93 Friday on weak Chinese demand. The UAE remains a primary U.S. security partner in the Gulf.",
        "lead_articles": [
            ("U.S. and Iran Exchange Strikes Near Hormuz; CENTCOM Downs Drones, Hits Coastal Radar", "us-iran-exchange-strikes-hormuz-centcom-downs-drones-coastal-radar.html", "June 7, 2026",
             "U.S. and Iranian forces exchanged strikes near Hormuz over the weekend; a strike hit Kuwait International Airport \u2014 a reminder that bypass routes like ADCOP only partly offset the Gulf disruption."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 7, 2026): A sharp re-escalation has revived the supply-disruption risk. Israel struck Hezbollah targets in southern Beirut on Sunday, with Iran having warned it would retaliate and could halt U.S. talks if Beirut were hit; over the weekend U.S. and Iranian forces exchanged strikes near the Strait of Hormuz. Saudi Arabia, Qatar, and the UAE (former member, departed May 1) are watching the reopening timeline slip. EIA assessed ~10.5M bpd of Persian Gulf production shut in; the next EIA Short-Term Energy Outlook is due June 9. Brent slid to ~$93 Friday on weak Chinese demand even as it held 3\u20134% higher for the week.",
        "lead_articles": [
            ("U.S. and Iran Exchange Strikes Near Hormuz; CENTCOM Downs Drones, Hits Coastal Radar", "us-iran-exchange-strikes-hormuz-centcom-downs-drones-coastal-radar.html", "June 7, 2026",
             "U.S. and Iranian forces exchanged strikes near Hormuz over the weekend, reviving the supply-disruption risk that keeps shut-in OPEC barrels off the market."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 7, 2026): Qatar, a principal mediator alongside Pakistan, is watching a sharp re-escalation that threatens the diplomacy. Israel struck Hezbollah targets in southern Beirut on Sunday, and Iran had warned it would retaliate and could halt U.S. talks if Beirut were hit; over the weekend U.S. and Iranian forces exchanged strikes near the Strait of Hormuz, which would further disrupt Qatari LNG flows if it widens. Hezbollah rejected the latest U.S.-brokered ceasefire. JKM and TTF benchmarks remain elevated. Trump still says talks are progressing well.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 7, 2026): Russia remains one of few major producers outside the Persian Gulf disruption zone as escalation re-intensifies. Israel struck Hezbollah targets in southern Beirut on Sunday and U.S. and Iranian forces exchanged strikes near the Strait of Hormuz over the weekend, reviving the supply-disruption risk. Brent slid to ~$93 Friday on weak Chinese demand \u2014 crude imports at a ten-year low \u2014 even as it held 3\u20134% higher for the week. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers. Urals discount dynamics remain in focus as benchmark prices swing.",
        "lead_articles": [
            ("U.S. and Iran Exchange Strikes Near Hormuz; CENTCOM Downs Drones, Hits Coastal Radar", "us-iran-exchange-strikes-hormuz-centcom-downs-drones-coastal-radar.html", "June 7, 2026",
             "U.S. and Iranian forces exchanged strikes near Hormuz over the weekend, reviving a supply-disruption risk that affects Urals differential dynamics for producers outside the Gulf zone."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 7, 2026): Brazilian pre-salt production continues to grow as a non-OPEC supply source as escalation re-intensifies in the Middle East. Israel struck Hezbollah targets in southern Beirut on Sunday and U.S. and Iranian forces exchanged strikes near the Strait of Hormuz over the weekend. Brent slid to ~$93 Friday on weak Chinese demand even as it held 3\u20134% higher for the week. The price swings affect pre-salt project economics at the margin. Petrobras Q1 results and pre-salt output milestones remain key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 7, 2026): Nigerian crude remains important to the non-OPEC supply mix as escalation re-intensifies. Light, sweet Nigerian grades have served as alternatives for refiners losing access to Middle East crude through the conflict. Israel struck Hezbollah targets in southern Beirut on Sunday and U.S. and Iranian forces exchanged strikes near the Strait of Hormuz over the weekend. Brent slid to ~$93 Friday on weak Chinese demand. The G7 leaders summit June 15-17 in Evian is expected to address supply-chain diversification.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 7, 2026): Venezuelan production capacity remains a structurally relevant question as escalation re-intensifies in the Middle East. Israel struck Hezbollah targets in southern Beirut on Sunday and U.S. and Iranian forces exchanged strikes near the Strait of Hormuz over the weekend, reviving the supply-disruption risk. Brent slid to ~$93 Friday on weak Chinese demand even as it held 3\u20134% higher for the week. U.S. sanctions policy on Venezuelan crude remains a relevant input to Atlantic Basin balances as benchmark prices swing.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 7, 2026</div>'''


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
        if "Last reviewed: June 7, 2026" not in txt:
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
