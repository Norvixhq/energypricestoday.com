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
        "context": "Current state (June 9, 2026): De-escalation has taken hold. After Israel\u2019s Sunday strike on Hezbollah targets in southern Beirut, Iran followed through on its warning and exchanged strikes with Israel over the weekend \u2014 then announced Monday it had ended its military operations, and the two countries agreed Tuesday to halt attacks against each other. President Trump says both are close to a new ceasefire, with progress between Washington and Tehran. Iran warns operations could resume if Israel continues its campaign in Lebanon. Crude round-tripped the episode, falling below $90 after touching $95. The Strait of Hormuz remains closed under the dual U.S.-Iran blockade; Fitch projects it could reopen around the end of July.",
        "lead_articles": [
            ("Iran and Israel Agree to Halt Attacks After Weekend Exchange; Trump Says New Ceasefire Is Close", "iran-israel-agree-halt-attacks-trump-new-ceasefire-close.html", "June 9, 2026",
             "Iran and Israel agreed Tuesday to halt attacks after a weekend exchange of strikes threatened the fragile ceasefire. Trump says both are close to a new ceasefire \u2014 though Iran warns operations resume if Israel continues in Lebanon."),
            ("Oil Falls Below $90 After Touching $95; Crude Surrenders the Escalation Spike", "oil-falls-below-90-after-95-crude-surrenders-escalation-spike.html", "June 9, 2026",
             "Crude round-tripped the escalation: WTI spiked to $95 early Monday before falling below $90 Tuesday as the halt in attacks revived the diplomatic track."),
        ],
    },
    "saudi-arabia.html": {
        "context": "Current state (June 9, 2026): Saudi Arabia is watching de-escalation take hold. Iran and Israel agreed Tuesday to halt attacks after a weekend exchange of strikes, and Trump says both are close to a new ceasefire \u2014 reviving the path toward a phased Hormuz reopening that Fitch now pegs around the end of July. OPEC+ approved a July quota increase of 188,000 bpd despite persistent supply risks. Saudi production remains near its lowest since 1990 with ~10.5M bpd of Gulf output shut in; Aramco CEO Amin Nasser has warned normalization slips to 2027 if reopening is delayed past mid-June \u2014 a deadline now passing. Crude fell below $90 as the escalation premium unwound.",
        "lead_articles": [
            ("Oil Falls Below $90 After Touching $95; Crude Surrenders the Escalation Spike", "oil-falls-below-90-after-95-crude-surrenders-escalation-spike.html", "June 9, 2026",
             "Crude surrendered the weekend\u2019s escalation spike as Iran and Israel halted attacks. OPEC+ approved a July quota increase of 188,000 bpd; Fitch sees possible 4Q26 oversupply once Hormuz reopens."),
            ("Iran and Israel Agree to Halt Attacks After Weekend Exchange; Trump Says New Ceasefire Is Close", "iran-israel-agree-halt-attacks-trump-new-ceasefire-close.html", "June 9, 2026",
             "The halt in attacks revives the diplomatic path toward reopening the strait \u2014 the trigger for restoring shut-in Saudi barrels to the market."),
        ],
    },
    "uae.html": {
        "context": "Current state (June 9, 2026): The UAE, which formally departed OPEC effective May 1, is watching de-escalation take hold. Iran and Israel agreed Tuesday to halt attacks after a weekend exchange, and Trump says both are close to a new ceasefire \u2014 reviving the path toward a Hormuz reopening that Fitch pegs around the end of July. ADCOP pipeline continues to carry available bypass volumes that don\u2019t transit the strait, which remains closed under the dual U.S.-Iran blockade. Crude fell below $90 as the escalation premium unwound. The UAE remains a primary U.S. security partner in the Gulf.",
        "lead_articles": [
            ("Iran and Israel Agree to Halt Attacks After Weekend Exchange; Trump Says New Ceasefire Is Close", "iran-israel-agree-halt-attacks-trump-new-ceasefire-close.html", "June 9, 2026",
             "De-escalation revives the reopening path \u2014 relief for bypass-constrained Gulf exporters once the strait reopens; Fitch pegs that around the end of July."),
            ("UAE Nuclear Facility Attacked Over Weekend in Persian Gulf Escalation", "uae-nuclear-facility-attacked-weekend-persian-gulf-escalation.html", "May 18, 2026",
             "Energy infrastructure across the Persian Gulf came under attack, including a nuclear facility in the United Arab Emirates."),
        ],
    },
    "opec-members.html": {
        "context": "Current state (June 9, 2026): OPEC+ approved a July quota increase of 188,000 bpd despite persistent supply risks \u2014 modest barrels into a market where ~10.5M bpd of Persian Gulf production remains shut in. De-escalation took hold this week: Iran and Israel agreed Tuesday to halt attacks, and Trump says both are close to a new ceasefire. Fitch projects Hormuz could reopen around the end of July and warns rapid capacity recovery plus a more aggressive OPEC+ policy could recreate an oversupply by 4Q26, with Brent averaging $87 for full-year 2026. Crude fell below $90 as the escalation premium unwound; Chinese imports pulled back aggressively.",
        "lead_articles": [
            ("Oil Falls Below $90 After Touching $95; Crude Surrenders the Escalation Spike", "oil-falls-below-90-after-95-crude-surrenders-escalation-spike.html", "June 9, 2026",
             "OPEC+ approved a July quota increase of 188,000 bpd as crude surrendered the weekend\u2019s escalation spike; Fitch flags possible 4Q26 oversupply once the strait reopens."),
            ("UAE Officially Departs OPEC Effective May 1; EIA Cuts 2027 Spare Capacity Forecast", "uae-officially-departs-opec-effective-may-1-eia-cuts-spare-capacity.html", "May 13, 2026",
             "The EIA\u2019s May Short-Term Energy Outlook incorporates the UAE\u2019s departure from OPEC, effective May 1, 2026."),
        ],
    },
    "qatar.html": {
        "context": "Current state (June 9, 2026): Qatar, a principal mediator alongside Pakistan, is watching de-escalation take hold. Iran and Israel agreed Tuesday to halt attacks after a weekend exchange, and Trump says both are close to a new ceasefire \u2014 reviving the diplomatic path toward a Hormuz reopening that would allow Qatari LNG exports to resume; Fitch pegs that around the end of July. The strait remains closed under the dual U.S.-Iran blockade, and the EIA notes global LNG prices remain elevated on reduced Hormuz flows. JKM and TTF benchmarks stay elevated. Iran\u2019s caveat \u2014 operations resume if Israel continues in Lebanon \u2014 keeps the Lebanon track in focus for Doha.",
        "lead_articles": [],
    },
    "russia.html": {
        "context": "Current state (June 9, 2026): Russia remains one of few major producers outside the Persian Gulf disruption zone as de-escalation takes hold. Iran and Israel agreed Tuesday to halt attacks, and crude round-tripped the weekend\u2019s escalation \u2014 WTI below $90 after touching $95. OPEC+ approved a July quota increase of 188,000 bpd, and Fitch flags possible 4Q26 oversupply once Hormuz reopens (~end of July in its view), with Brent averaging $87 for 2026 \u2014 a softer price backdrop for Urals differentials. The U.S. previously issued a waiver permitting the sale of Russian crude already loaded onto tankers. Chinese imports pulled back aggressively.",
        "lead_articles": [
            ("Oil Falls Below $90 After Touching $95; Crude Surrenders the Escalation Spike", "oil-falls-below-90-after-95-crude-surrenders-escalation-spike.html", "June 9, 2026",
             "Crude surrendered the escalation spike as attacks halted; Fitch sees Brent averaging $87 for 2026 with possible 4Q26 oversupply \u2014 a softer backdrop for Urals differentials."),
        ],
    },
    "brazil.html": {
        "context": "Current state (June 9, 2026): Brazilian pre-salt production continues to grow as a non-OPEC supply source as de-escalation takes hold in the Middle East. Iran and Israel agreed Tuesday to halt attacks, and crude fell below $90 after the weekend\u2019s brief spike to $95. Fitch cites strong non-OPEC supply growth \u2014 of which Brazil is a leading contributor \u2014 among the factors that could recreate an oversupply by 4Q26 once Hormuz reopens, with Brent averaging $87 for 2026. The softer price path tightens pre-salt project economics at the margin. Petrobras output milestones remain key watchpoints.",
        "lead_articles": [],
    },
    "nigeria.html": {
        "context": "Current state (June 9, 2026): Nigerian crude remains important to the non-OPEC supply mix as de-escalation takes hold. Light, sweet Nigerian grades have served as alternatives for refiners losing access to Middle East crude through the conflict \u2014 a premium position that softens as the reopening path revives. Iran and Israel agreed Tuesday to halt attacks; crude fell below $90 after the weekend spike, and Fitch sees Brent averaging $87 for 2026. The G7 leaders summit June 15-17 in Evian is expected to address supply-chain diversification.",
        "lead_articles": [],
    },
    "venezuela.html": {
        "context": "Current state (June 9, 2026): Venezuelan production capacity remains a structurally relevant question as de-escalation takes hold in the Middle East. Iran and Israel agreed Tuesday to halt attacks, and crude fell below $90 after the weekend\u2019s brief spike to $95 \u2014 with Fitch projecting Brent averaging $87 for 2026 and possible oversupply by 4Q26 once Hormuz reopens. A softer price path reduces the urgency of marginal Atlantic Basin barrels. U.S. sanctions policy on Venezuelan crude remains a relevant input as benchmark prices swing.",
        "lead_articles": [],
    },
}

LAST_REVIEWED_BLOCK = '''<div style="margin-top:8px;display:inline-flex;align-items:center;gap:8px;font-family:var(--font-body);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.08em;color:var(--text-3);padding:6px 12px;background:var(--surface-2);border:1px solid var(--border);border-radius:4px"><span style="width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block"></span>Last reviewed: June 9, 2026</div>'''


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
        if "Last reviewed: June 9, 2026" not in txt:
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
