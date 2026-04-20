/* ═══════════════════════════════════════════════════════════════════
 * news-feed.js — Path B: cache-first headline loader.
 *
 * Previous behavior: fetched rss2json.com first, fell back to server-side
 * cache. That worked until rss2json started rate-limiting (422 errors).
 *
 * New behavior: reads data/sources/headlines-{topic}.json FIRST — our own
 * cache, refreshed every 15 minutes by scripts/observers/fetch_headlines.py.
 * rss2json.com is demoted to emergency fallback only, used if the cache
 * hasn't been generated yet (e.g. first 15 min after repo push).
 *
 * Topic → cache file mapping:
 *   energy      → headlines-energy.json
 *   geopolitics → headlines-geopolitics.json
 *   oil         → headlines-oil.json
 *   gasoline    → headlines-gasoline.json
 *   natgas / natural gas → headlines-natgas.json
 *   heating / diesel     → headlines-heating.json
 *   rigcount    → headlines-rigcount.json
 *   renewables  → headlines-renewables.json
 *   companies   → headlines-companies.json
 *   breaking    → headlines-breaking.json
 *
 * Module containers use: <div data-news-topic="<topic>" data-news-max="<N>">
 *
 * Fallback chain:
 *   1. Our own cache (data/sources/headlines-<topic>.json)
 *   2. rss2json.com (emergency legacy fallback)
 *   3. Empty container with "Headlines temporarily unavailable"
 * ═══════════════════════════════════════════════════════════════════ */

// Topic aliases — accepts both short keys and human-friendly names
var TOPIC_ALIAS = {
  'natural gas': 'natgas',
  'diesel':      'heating',
};

// Legacy rss2json URL map, used only as emergency fallback
var NEWS_FEEDS = {
  energy:      'https://news.google.com/rss/search?q=oil+prices+energy+market&hl=en-US&gl=US&ceid=US:en',
  geopolitics: 'https://news.google.com/rss/search?q=Iran+ceasefire+oil+OR+OPEC+oil+OR+Middle+East+energy&hl=en-US&gl=US&ceid=US:en',
  natgas:      'https://news.google.com/rss/search?q=natural+gas+price+LNG&hl=en-US&gl=US&ceid=US:en',
  renewables:  'https://news.google.com/rss/search?q=renewable+energy+solar+wind&hl=en-US&gl=US&ceid=US:en',
  companies:   'https://news.google.com/rss/search?q=ExxonMobil+Chevron+Shell+Aramco&hl=en-US&gl=US&ceid=US:en',
  oil:         'https://news.google.com/rss/search?q=crude+oil+Brent+WTI&hl=en-US&gl=US&ceid=US:en',
  rigcount:    'https://news.google.com/rss/search?q=oil+rig+count+drilling&hl=en-US&gl=US&ceid=US:en',
  gasoline:    'https://news.google.com/rss/search?q=gas+prices+gasoline+fuel&hl=en-US&gl=US&ceid=US:en',
  heating:     'https://news.google.com/rss/search?q=heating+oil+diesel+fuel&hl=en-US&gl=US&ceid=US:en',
  breaking:    'https://news.google.com/rss/search?q=oil+energy+breaking+news&hl=en-US&gl=US&ceid=US:en',
};

var RSS2JSON_BASE = 'https://api.rss2json.com/v1/api.json?rss_url=';

// ─── Path resolution (works from any depth) ──────────────────────
function cachePathPrefix() {
  if (window.location.pathname.indexOf('/category/') !== -1) return '../';
  if (window.location.pathname.indexOf('/articles/') !== -1) return '../';
  if (window.location.pathname.indexOf('/authors/') !== -1)  return '../';
  return '';
}

function normalizeTopic(topic) {
  if (!topic) return 'energy';
  var t = String(topic).toLowerCase().trim();
  return TOPIC_ALIAS[t] || t;
}

function cacheUrlForTopic(topic) {
  return cachePathPrefix() + 'data/sources/headlines-' + normalizeTopic(topic) + '.json';
}

// ─── Rendering ───────────────────────────────────────────────────
function renderHeadlines(container, stories, maxItems) {
  if (!stories || !stories.length) {
    container.innerHTML = '<div style="color:var(--text-3);font-size:12px;padding:12px 16px">Headlines temporarily unavailable</div>';
    return;
  }
  container.innerHTML = stories.slice(0, maxItems).map(function(item) {
    var title = item.title || '';
    var link = item.url || item.link || '#';
    var source = item.source || '';
    // rss2json includes source in " - Source" suffix on title; strip it
    if (!source && title) {
      var dashIdx = title.lastIndexOf(' - ');
      if (dashIdx > 20) {
        source = title.substring(dashIdx + 3);
        title = title.substring(0, dashIdx);
      }
    }
    var tsRaw = item.published_at || item.pubDate || '';
    var time = tsRaw ? formatTimeAgo(tsRaw) : '';
    return '<a href="' + escapeAttr(link) + '" target="_blank" rel="noopener noreferrer" class="live-news-card">' +
      (source ? '<div class="live-news-source">' + escapeHtml(source) + '</div>' : '') +
      '<div class="live-news-title">' + escapeHtml(title) + '</div>' +
      (time ? '<div class="live-news-time">' + time + '</div>' : '') +
    '</a>';
  }).join('');
}

// ─── Cache-first loader ──────────────────────────────────────────
function loadFromCache(topic, containerId, maxItems) {
  var container = document.getElementById(containerId);
  if (!container) return Promise.reject('no container');
  var url = cacheUrlForTopic(topic);

  return fetch(url, { cache: 'no-store' })
    .then(function(res) {
      if (!res.ok) throw new Error('cache ' + res.status);
      return res.json();
    })
    .then(function(data) {
      var stories = (data && data.stories) || [];
      if (!stories.length) throw new Error('cache empty');
      renderHeadlines(container, stories, maxItems);
      return { source: 'cache', count: stories.length };
    });
}

// ─── rss2json emergency fallback ─────────────────────────────────
function loadFromRss2Json(topic, containerId, maxItems) {
  var container = document.getElementById(containerId);
  if (!container) return Promise.reject('no container');
  var feedUrl = NEWS_FEEDS[normalizeTopic(topic)] || NEWS_FEEDS.energy;
  var url = RSS2JSON_BASE + encodeURIComponent(feedUrl);

  return fetch(url)
    .then(function(res) {
      if (!res.ok) throw new Error('rss2json ' + res.status);
      return res.json();
    })
    .then(function(data) {
      if (data.status !== 'ok' || !data.items || !data.items.length) {
        throw new Error('rss2json empty');
      }
      renderHeadlines(container, data.items, maxItems);
      return { source: 'rss2json', count: data.items.length };
    });
}

// ─── Main loader — cache first, rss2json fallback ────────────────
function loadLiveNews(topic, containerId, maxItems) {
  maxItems = maxItems || 6;
  loadFromCache(topic, containerId, maxItems)
    .catch(function(cacheErr) {
      console.debug('[news-feed] cache miss for', topic, '→ trying rss2json:', cacheErr && (cacheErr.message || cacheErr));
      return loadFromRss2Json(topic, containerId, maxItems);
    })
    .catch(function(fallbackErr) {
      console.debug('[news-feed] both sources failed for', topic, fallbackErr && (fallbackErr.message || fallbackErr));
      var container = document.getElementById(containerId);
      if (container) {
        container.innerHTML = '<div style="color:var(--text-3);font-size:12px;padding:12px 16px">Headlines temporarily unavailable</div>';
      }
    });
}

// ─── Legacy no-op (retained so any stale caller still works) ─────
// Phase 2.4's event-state.js owns the banner's top_story binding; the
// homepage's inline rotator (in index.html) handles multi-headline rotation
// from cache. This function used to call rss2json directly — now safely a no-op.
function updateBreakingBanner() { /* no-op */ }

// ─── Utilities ───────────────────────────────────────────────────
function formatTimeAgo(dateStr) {
  try {
    var then = new Date(dateStr);
    var diff = Math.floor((new Date() - then) / 1000);
    if (isNaN(diff) || diff < 0) return '';
    if (diff < 120) return 'Just now';
    if (diff < 3600) return Math.floor(diff / 60) + 'm ago';
    if (diff < 86400) return Math.floor(diff / 3600) + 'h ago';
    if (diff < 604800) return Math.floor(diff / 86400) + 'd ago';
    return then.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  } catch (e) { return ''; }
}

function escapeHtml(str) {
  var d = document.createElement('div');
  d.textContent = str;
  return d.innerHTML;
}

function escapeAttr(str) {
  return String(str).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;');
}

// ─── Auto-discovery on DOM ready ─────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
  var els = document.querySelectorAll('[data-news-topic]');
  Array.prototype.forEach.call(els, function(el) {
    var topic = el.getAttribute('data-news-topic');
    var max = parseInt(el.getAttribute('data-news-max'), 10) || 6;
    if (el.id) {
      loadLiveNews(topic, el.id, max);
      // Refresh every 15 minutes to stay in sync with autopilot cadence
      setInterval(function() { loadLiveNews(topic, el.id, max); }, 15 * 60 * 1000);
    }
  });
});

// Expose for manual debugging / refresh
window.NewsFeed = {
  loadLiveNews: loadLiveNews,
  loadFromCache: loadFromCache,
  loadFromRss2Json: loadFromRss2Json,
};
