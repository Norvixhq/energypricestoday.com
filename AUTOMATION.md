# EnergyPricesToday.com — Automation System

The site publishes itself. Scheduled GitHub Actions run Python scripts
that scrape data sources, refresh content, validate the build, and push
changes back to the repo. GitHub Pages redeploys on each push.

## What runs automatically

| Job | Schedule | What it does |
|---|---|---|
| `update-gas.yml` | 10am, 2pm, 7pm Central daily | Scrapes AAA, updates `GAS_PRICES_BY_STATE` and `US_GAS_NATIONAL` in `js/data.js` |
| `update-news.yml` | Every 4 hours | Fetches Google News RSS for energy topics, refreshes `BREAKING_NEWS`, creates article stubs, and (if API key set) upgrades stubs to full articles via Claude |
| `nightly-audit.yml` | 2am Central daily | Rebuilds slug map, removes orphan articles, refreshes sitemap, runs full validation |

Every job commits + pushes only when content actually changed, so the
repo history stays clean.

## Setup

### 1. Enable GitHub Actions
Actions are enabled by default on public repos. For private repos,
Settings → Actions → General → Allow all actions.

### 2. Give Actions write permission
Settings → Actions → General → Workflow permissions →
**Read and write permissions**. This lets the workflow push back to the repo.

### 3. (Optional — Phase 2) Add Anthropic API key
If you want Claude to generate full article bodies instead of stubs:

1. Get an API key at https://console.anthropic.com
2. Repo Settings → Secrets and variables → Actions → New repository secret
3. Name: `ANTHROPIC_API_KEY`
4. Value: your API key (starts with `sk-ant-...`)

Without this key, articles are created as readable stubs. With it,
they get full 4-paragraph bodies.

**Cost estimate:** With Claude Haiku at default settings, expect
about $2–4/month based on news refresh frequency. Change the `MODEL`
constant in `scripts/generate_articles.py` to use Sonnet or Opus if
you want higher-quality output (roughly $15 or $60/month respectively).

### 4. That's it
Push these files to your repo. The first scheduled run happens on the
next cron tick. You can also trigger any workflow manually:
Actions tab → pick workflow → "Run workflow".

## Running scripts locally

Every script is self-contained Python 3 with no external dependencies
(stdlib + Node.js for JS syntax checking).

```bash
# Update gas prices from AAA
python3 scripts/update_gas_prices.py

# Fetch RSS and refresh breaking news
python3 scripts/update_news.py

# Rebuild the slug map from disk
python3 scripts/rebuild_slug_map.py

# Update sitemap dates
python3 scripts/update_sitemap.py

# Run all integrity checks (does NOT modify anything)
python3 scripts/validate.py

# Remove orphan articles (safety-capped at 30)
python3 scripts/cleanup_orphans.py
```

Exit codes:
- `0` — success (or nothing to do)
- `1` — validation failure / blocked from publishing
- `2` — error

## What each script does in detail

### `update_gas_prices.py`
Fetches `gasprices.aaa.com/state-gas-price-averages/` and the
national averages page. Parses the tables, applies sanity checks
($2–$9 range, 51 states), and rewrites both `GAS_PRICES_BY_STATE`
(51 entries) and `US_GAS_NATIONAL` in `js/data.js`. Skips if AAA
data is unchanged.

### `update_news.py`
Queries Google News RSS for five topics: oil prices, gas prices,
geopolitics, natural gas, and refinery news. Deduplicates by title
similarity, picks the top 8, and rewrites `BREAKING_NEWS`. For every
new headline, ensures an article file exists — creates a stub if not.

### `generate_articles.py`
Finds stub articles (marker-based detection) and regenerates them with
full 4-paragraph bodies using the Anthropic API. Capped at 8 upgrades
per run to control cost. No-ops cleanly if `ANTHROPIC_API_KEY` is not set.

### `rebuild_slug_map.py`
Scans every file in `articles/`, extracts the `<h1>`, and writes a fresh
`js/article-slugs.js`. Validates JS syntax before replacing.

### `update_sitemap.py`
Sets `<lastmod>` on every URL to today. Adds entries for new articles,
removes entries for deleted articles. Validates XML before writing.

### `validate.py`
Runs before every commit. Checks:
- JS syntax on all `js/*.js`
- Every visible title has a matching article file (no 404s)
- Every `href="articles/*.html"` in any HTML resolves
- No literal `\uXXXX` sequences in HTML bodies
- Sitemap dates are valid and not in the future
- FB Pixel / GA4 / FB domain verification still present on homepage
- Gas prices within sanity range
- No empty content arrays

Exits with code 1 and blocks publishing if any check fails.

### `cleanup_orphans.py`
Removes article files not referenced by any content block, HTML link,
or slug map entry. Safety-capped at 30 removals per run. Runs only
in the nightly audit.

### `commit_and_push.py`
Configures git identity for CI, writes a descriptive commit message
based on which files changed, commits, and pushes. Handles rebase
retries on push conflicts.

## Freshness rules

Built into the scripts:

- **Gas prices** refresh 3x/day. AAA updates once per day around 7am ET,
  so the second and third runs are redundancy.
- **Breaking news** refreshes every 4 hours. Each run picks fresh top
  headlines from RSS — stale stories naturally age out.
- **Sitemap dates** refresh every time any content change is published.
- **Orphan articles** get cleaned up nightly (capped to prevent runaway).
- **Article stubs** get upgraded to full content on the next news cycle
  after creation (if API key is set).

## What still needs manual work

The automation handles churn. You still handle:

- **Major redesigns** (category page rebuilds, new sections)
- **Flagship page structural changes** (the big overhauls we've done)
- **Design decisions** (colors, layout, component architecture)
- **Mobile/UX bug investigations**
- **Market driver cards** (`MARKET_DRIVERS` in data.js) — Phase 3 could automate this too

A typical week should now involve zero manual content updates.
Push bug fixes and design improvements as you normally would;
the automation stays out of your way.

## Monitoring

- **Did it run?** Actions tab in GitHub shows every scheduled run with status
- **Did it commit?** `git log --author=energypricestoday-bot --since=7.days` (or whatever your actor is)
- **Did validation fail?** Red X on a workflow run — click in to see which check failed
- **Did the site update?** Every commit triggers GitHub Pages redeploy; check live site

## Failure modes and what happens

| Scenario | What happens |
|---|---|
| AAA changes their HTML structure | `update_gas_prices.py` returns exit 2, no commit, no stale data published |
| Google News RSS is down | `update_news.py` returns exit 2, no commit, existing news remains |
| Anthropic API is down or quota exceeded | Stubs stay as stubs, site still works |
| Validation catches a broken reference | Commit aborted, no push, nothing published |
| Scheduled job fails | Next scheduled run tries again (next gas run in 4-6 hours, next news run in 4 hours) |
| Two jobs try to commit at once | `concurrency` group in each workflow prevents this; later job waits |

## Rollback

Every automated commit is a single atomic git commit. To revert any
automated change:

```bash
git revert <commit-sha>
git push
```

GitHub Pages will redeploy the reverted state. The next scheduled run
will start producing new updates from there.

## Extending

**Adding a new data source?** Add a script in `scripts/`, wire it into
a workflow under `.github/workflows/`. Use the existing scripts as templates.

**Changing the news topics?** Edit the `TOPICS` list at the top of
`scripts/update_news.py`.

**Changing the schedule?** Edit the `cron:` line in the relevant workflow.
GitHub Actions cron is UTC — remember to convert from Central.

**Adding AI-generated market drivers?** Template:
1. Create `scripts/refresh_drivers.py` (pattern from `generate_articles.py`)
2. Add a step in `update-news.yml` that calls it
3. Uses the same `ANTHROPIC_API_KEY` secret
