#!/usr/bin/env python3
"""
Hub refresh — update country/topic hubs with current verified context.

For each hub, replaces the "Current Context" box content with current
(May 18, 2026) framing, and adds a "Last reviewed" indicator.

All content is grounded in real, verified May 17-18 reporting.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"

# ─── Per-hub current context (verified May 17, 2026) ──────────────────
HUBS = {
    "iran.html": {
        "context": "Current state (May 18, 2026): Iran's revised peace proposal — delivered today via Pakistan — includes transferring its 60%-enriched uranium stockpile to Russia (not the U.S.), dropping financial-compensation demands, and gradually reopening Hormuz in exchange for U.S. lifting the blockade. Washington rejected the Russia destination, suggesting an unspecified third country. Axios sources characterized the revisions as \"token\" improvements. Trump: \"For Iran, the clock is ticking, and they better get moving FAST, or there won't be anything left of them.\" G7 finance ministers meeting in Paris today; Bessent urging sanctions alignment. WTI $108-$105 whipsaw session.",
        "lead_articles": [
            ("Iran's Revised Peace Proposal: Transfer Enriched Uranium to Russia, Drop Financial Demands", "iran-revised-peace-proposal-uranium-russia-drop-financial-demands.html", "May 18, 2026",
             "Iranian media reported today that Tehran's revised peace proposal — delivered via Pakistan — includes transferring its 60%-enriched uranium stockpile to Russia, a significant shift from Iran's prior position. Iran also dropped its demand for direct U.S. financial compensation."),
            ("IRGC Redefines Strait of Hormuz as 'Vast Operational Area'", "irgc-redefines-hormuz-vast-operational-area.html", "May 17, 2026",
             "Islamic Revolutionary Guard Corps Navy spokesperson Mohammad Akbarzadeh announced Iran has redefined the Strait of Hormuz as a \"vast operational area\" rather than the traditional narrow corridor."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (May 18, 2026): Saudi Aramco CEO Amin Nasser warned investors on the company's Q1 earnings call: \"If the Strait of Hormuz opens today, it will still take months for the market to rebalance, and if its opening is delayed by a few more weeks, then normalization will last into 2027.\" Saudi production remains at the lowest level since 1990. G7 finance ministers meet in Paris today; Bessent urging sanctions alignment. EIA assesses Iraq, Saudi Arabia, Kuwait, UAE, Qatar, and Bahrain collectively shut in 10.5 million bpd in April, peaking near 10.8 million bpd in May. The kingdom is now the central OPEC voice following the UAE's May 1 departure.",
        "lead_articles": [
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack over the weekend, including a nuclear facility in the United Arab Emirates. Saudi Aramco CEO Amin Nasser warned investors market normalization is pushed to 2027 if Hormuz reopening is delayed past mid-June."),
            ("G7 Finance Ministers Convene in Paris with Iran War, Hormuz Closure Topping Agenda", "g7-finance-ministers-convene-paris-iran-war-hormuz-may-18.html", "May 18, 2026",
             "G7 finance ministers and central bank governors gathered in Paris on Monday May 18 to address the economic fallout of the Iran war. French FM Lescure hosting; Bessent urging Iran sanctions alignment."),
        ],
    },
    "uae.html": {
        "context": "Current state (May 18, 2026): A UAE nuclear facility was attacked over the weekend, adding to concerns over regional stability and potential further supply disruptions. The UAE formally departed OPEC effective May 1, 2026 after weeks of missile and drone attacks from Iran. EIA's May STEO incorporates the change, cutting OPEC's 2027 spare capacity forecast to 2.5M bpd from 3.8M prior. ADCOP pipeline carrying available bypass volumes. The UAE remains a primary U.S. security partner in the Gulf and attended today's G7 Paris meeting as an invited guest.",
        "lead_articles": [
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack over the weekend, including a nuclear facility in the United Arab Emirates. The attack comes as the UAE has positioned itself as a primary U.S. security partner in the Gulf."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The UAE announced its departure from OPEC, effective May 1, 2026. EIA's May STEO incorporates the change. Because the UAE held substantial spare capacity, OPEC's 2027 spare capacity forecast is cut to 2.5 million bpd from 3.8 million prior."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (May 18, 2026): Saudi Aramco CEO Nasser told investors on the Q1 call that Hormuz reopening past mid-June pushes market normalization to 2027. The UAE formally departed OPEC effective May 1, 2026, reducing the producer group's composition and structural capacity. EIA's May STEO cut OPEC's 2027 spare capacity forecast to 2.5 million bpd from 3.8 million prior. Saudi Arabia informed OPEC its output fell to the lowest level since 1990. EIA assesses 10.5 million bpd of Persian Gulf production was shut in during April. Brent traded between $111 and $102 in Monday's whipsaw session.",
        "lead_articles": [
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA's May Short-Term Energy Outlook released May 12 incorporates the UAE's departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (May 18, 2026): Qatari LNG exports remain disrupted as part of the broader Persian Gulf shutdown that began in late February. EIA's May STEO notes global LNG prices remain elevated as a result of reduced energy flows through the Strait of Hormuz, with a wide U.S.&ndash;international price spread persisting. JKM and TTF benchmarks elevated as Asian importers outbid European utility buyers for U.S. cargoes. Qatar's economy minister attended the G7 Paris meeting today as an invited guest. U.S. LNG export terminals running near capacity.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (May 18, 2026): Russia is now centrally positioned in the U.S.-Iran negotiations as Iran's revised proposal — delivered today via Pakistan — includes transferring 60%-enriched uranium to Russian custody. Kremlin spokesman Peskov: \"This proposal was made by President Putin in conversations with both the United States and regional states. The offer still stands, but has not been acted upon.\" Washington rejected the Russia destination, suggesting an unspecified third country. Russia remains one of few major producers operating outside the Persian Gulf disruption zone.",
        "lead_articles": [
            ("Iran's Revised Peace Proposal: Transfer Enriched Uranium to Russia, Drop Financial Demands", "iran-revised-peace-proposal-uranium-russia-drop-financial-demands.html", "May 18, 2026",
             "Iranian media reported today that Tehran's revised peace proposal includes transferring its 60%-enriched uranium stockpile to Russia. The U.S. rejected the destination, suggesting a third country."),
        ],
    },
    "brazil.html": {
        "context": "Current state (May 18, 2026): Brazilian pre-salt production continues to grow, an increasingly important non-OPEC supply source as Persian Gulf flows remain heavily disrupted. With OPEC's 2027 spare capacity forecast cut to 2.5M bpd from 3.8M prior, Brazil and other non-OPEC producers are receiving heightened market attention. Brazil's finance minister attended the G7 Paris meeting today as an invited guest. Petrobras Q1 results and pre-salt output milestones are the key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (May 18, 2026): Nigerian crude is increasingly important to the non-OPEC supply mix as Persian Gulf production remains heavily disrupted. Light, sweet Nigerian grades serve as alternatives for refiners losing access to Middle East crude. Pipeline security, oil-theft enforcement, and African Atlantic Basin flows are the principal watchpoints. The G7 leaders summit June 15-17 in Evian is expected to address rare-earths and supply-chain diversification in detail.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (May 18, 2026): Venezuelan production capacity remains a structurally relevant question as global spare capacity has tightened sharply: EIA's May STEO cut OPEC 2027 spare capacity to 2.5M bpd from 3.8M prior following the UAE's departure. Aramco CEO Nasser's 2027 normalization warning underscores the structural tightness. U.S. sanctions policy on Venezuelan crude continues as a relevant input to Atlantic Basin supply balance.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: May 18, 2026</div>'''


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
        if "Last reviewed: May 18, 2026" not in txt:
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
