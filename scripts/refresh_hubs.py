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
        "context": "Current state (July 7, 2026): The reopening hit its most serious test yet. Iran attacked the Qatari LNG tanker Al-Rekayyat near the Strait of Hormuz and a second vessel was struck by a projectile, and the U.S. revoked the license authorizing Iran to sell its oil, stressing the memorandum of understanding is performance-based. Oil jumped \u2014 Brent settled +3% at $74.16 and popped to $76 after hours \u2014 but stayed near four-month lows as OPEC+ added barrels. The two sides also disagree over the use of funds covered under the MOU. The nuclear and sanctions questions remain unresolved as the fragile peace faces renewed strain.",
        "lead_articles": [
            ("Iran Strikes Qatari LNG Tanker Near Hormuz as U.S. Revokes Oil-Sale License", "iran-strikes-qatari-lng-tanker-hormuz-us-revokes-oil-sale-license.html", "July 7, 2026",
             "Iran attacked the Qatari LNG tanker Al-Rekayyat and a second vessel was hit by a projectile; the U.S. revoked Iran\u2019s oil-sale license in response, sending oil sharply higher."),
            ("Oil Jumps on Hormuz Tanker Attacks but Holds Near Four-Month Lows", "oil-jumps-hormuz-tanker-attacks-holds-near-four-month-lows.html", "July 7, 2026",
             "Brent settled 3% higher at $74.16 after the attacks, but crude stayed near four-month lows as OPEC+ added barrels and Saudi discounted to Asia."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (July 7, 2026): Saudi Arabia is driving the bearish supply story even as security risk re-rates. Over the weekend OPEC+, led by Riyadh, approved a 188,000 bpd quota increase for next month, and Saudi Aramco cut its Arab Light price for Asian buyers by $11 a barrel to a $1.50 discount \u2014 the first discount since the price wars of 2020 and 2015 \u2014 signaling a pivot to volume and market share. Saudi exports are approaching pre-war levels. That backdrop kept crude near four-month lows even after Iran struck a Qatari LNG tanker near Hormuz and the U.S. revoked Iran\u2019s oil-sale license, sending prices briefly higher.",
        "lead_articles": [
            ("OPEC+ Approves 188,000 bpd Quota Increase as Saudi Cuts Arab Light to Asia", "opec-plus-approves-188000-bpd-quota-increase-saudi-cuts-arab-light.html", "July 7, 2026",
             "OPEC+ raised quotas by 188,000 bpd for next month while Saudi Aramco cut Arab Light to Asian buyers by $11 \u2014 its first discount since 2020 \u2014 keeping the supply picture bearish."),
            ("Oil Jumps on Hormuz Tanker Attacks but Holds Near Four-Month Lows", "oil-jumps-hormuz-tanker-attacks-holds-near-four-month-lows.html", "July 7, 2026",
             "Saudi exports near pre-war levels and the OPEC+ quota hike kept crude near four-month lows even after the tanker attacks drove a sharp intraday rally."),
        ],
    },
    "uae.html": {
        "context": "Current state (July 7, 2026): The UAE has fully restored its shipping flows as the Gulf supply recovery continues, part of a bearish backdrop that kept crude near four-month lows even after Iran struck a Qatari LNG tanker near Hormuz and the U.S. revoked Iran\u2019s oil-sale license this week. Having formally departed OPEC effective May 1, the UAE is now boosting supply outside the cartel\u2019s quota framework just as OPEC+ approved a further 188,000 bpd increase and Saudi Aramco discounted Arab Light to Asia. The UAE remains a primary U.S. security partner, and resumed Hormuz traffic \u2014 with supertankers exiting via a route near Iran \u2014 has relieved the bypass pressure that had elevated the ADCOP pipeline.",
        "lead_articles": [
            ("Oil Jumps on Hormuz Tanker Attacks but Holds Near Four-Month Lows", "oil-jumps-hormuz-tanker-attacks-holds-near-four-month-lows.html", "July 7, 2026",
             "The UAE has fully restored shipping flows, part of a supply wave that kept crude near four-month lows even as Hormuz tanker attacks re-rated the security risk."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (July 7, 2026): OPEC+ policy is the dominant bearish force. Over the weekend the group approved a 188,000 bpd quota increase for next month, continuing to unwind long-standing curbs, and Saudi Aramco cut Arab Light to Asian buyers by $11 to a $1.50 discount \u2014 its first discount since 2020. But cohesion is under strain: Iraq has reportedly sought a higher quota and told the group it could leave if its demands are not met, raising the prospect of another exit after the UAE departed in May. Crude sits near four-month lows even after Iran struck a Qatari LNG tanker near Hormuz and the U.S. revoked Iran\u2019s oil-sale license this week.",
        "lead_articles": [
            ("OPEC+ Approves 188,000 bpd Quota Increase as Saudi Cuts Arab Light to Asia", "opec-plus-approves-188000-bpd-quota-increase-saudi-cuts-arab-light.html", "July 7, 2026",
             "OPEC+ raised quotas by 188,000 bpd while Saudi cut Arab Light to Asia by $11; Iraq is pressing for a higher quota and hinting it could follow the UAE out."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (July 7, 2026): Qatar is at the center of today\u2019s escalation. Iran attacked the Qatari LNG tanker Al-Rekayyat as it transited near the Strait of Hormuz, an incident Qatar\u2019s Ministry of Foreign Affairs confirmed, and a second vessel was struck by a projectile. The attacks sent oil sharply higher \u2014 Brent settled +3% at $74.16 \u2014 and prompted the U.S. to revoke Iran\u2019s oil-sale license. As one of the world\u2019s largest LNG exporters, Qatar\u2019s cargoes transit Hormuz, and the strike renews questions among shipowners about the durability of the U.S.-Iran agreement even as overall traffic keeps recovering, with supertankers exiting via a route near Iran.",
        "lead_articles": [
            ("Iran Strikes Qatari LNG Tanker Near Hormuz as U.S. Revokes Oil-Sale License", "iran-strikes-qatari-lng-tanker-hormuz-us-revokes-oil-sale-license.html", "July 7, 2026",
             "Iran attacked the Qatari LNG tanker Al-Rekayyat near Hormuz, confirmed by Qatar\u2019s foreign ministry; the U.S. revoked Iran\u2019s oil-sale license in response."),
        ],
    },
    "russia.html": {
        "context": "Current state (July 7, 2026): Crude sits near four-month lows even after a security-driven spike this week, when Iran struck a Qatari LNG tanker near Hormuz and the U.S. revoked Iran\u2019s oil-sale license (Brent settled +3% at $74.16). The bearish backdrop \u2014 an OPEC+ 188,000 bpd quota increase and a Saudi Arab Light discount to Asia \u2014 keeps pressure on Russian Urals differentials as competing barrels return. Russia remains one of few major producers outside the Gulf disruption zone, but the evaporated war premium erodes the scarcity that had supported its export revenues. The market\u2019s focus is now on how fast returning Gulf barrels and higher OPEC+ quotas rebuild global inventories.",
        "lead_articles": [
            ("Oil Jumps on Hormuz Tanker Attacks but Holds Near Four-Month Lows", "oil-jumps-hormuz-tanker-attacks-holds-near-four-month-lows.html", "July 7, 2026",
             "Crude held near four-month lows despite the Hormuz tanker attacks, a soft backdrop for Urals differentials as OPEC+ adds barrels and Saudi discounts to Asia."),
        ],
    },
    "brazil.html": {
        "context": "Current state (July 7, 2026): Crude sits near four-month lows even after Iran struck a Qatari LNG tanker near Hormuz and the U.S. revoked Iran\u2019s oil-sale license this week, briefly lifting prices. Brazilian pre-salt output continues to grow as a non-OPEC source; the IEA cites strong non-OPEC growth \u2014 of which Brazil is a leading contributor \u2014 among factors that could tip the market into a 2027 surplus, a view OPEC\u2019s Al Ghais rejects. With OPEC+ adding barrels and Saudi discounting Arab Light to Asia, the softer price path tightens pre-salt economics at the margin. The market\u2019s focus has shifted to the demand outlook and how the Hormuz security risk resolves.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (July 7, 2026): Crude sits near four-month lows even after a security-driven spike this week tied to the Hormuz tanker attacks and the U.S. revocation of Iran\u2019s oil-sale license. Light, sweet Nigerian grades had served as alternatives for refiners losing Middle East crude during the conflict \u2014 a premium that has faded as Gulf barrels return and OPEC+ adds supply. Saudi Aramco\u2019s $11 cut to Arab Light for Asia underscores the competitive pressure on West African crude. The softer price environment strains Nigerian fiscal math, and the market is focused on the demand outlook and the pace of the Gulf supply ramp.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (July 7, 2026): Crude sits near four-month lows even after Iran struck a Qatari LNG tanker near Hormuz and the U.S. revoked Iran\u2019s oil-sale license this week. The softer price path reduces the pull on marginal Atlantic Basin barrels that had gained relevance during the wartime disruption, and returning Gulf supply \u2014 an OPEC+ quota increase, a Saudi discount to Asia \u2014 adds competing volume. U.S. sanctions policy on Venezuelan crude remains a key variable as the market shifts from scarcity toward a potential 2027 surplus. Venezuelan production capacity stays structurally constrained regardless of the improved geopolitical backdrop.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: July 7, 2026</div>'''


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
        if "Last reviewed: July 7, 2026" not in txt:
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
