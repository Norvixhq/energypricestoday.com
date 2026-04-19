/* Live News Headlines via Google News RSS + rss2json.com */

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

function fetchNewsHeadlines(feedUrl, containerId, maxItems) {
  maxItems = maxItems || 8;
  var container = document.getElementById(containerId);
  if (!container) return;

  var url = RSS2JSON_BASE + encodeURIComponent(feedUrl);

  // container starts empty — no loading indicator

  fetch(url)
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data.status !== 'ok' || !data.items || data.items.length === 0) {
        throw new Error('rss2json empty response');
      }

      container.innerHTML = data.items.slice(0, maxItems).map(function(item) {
        var title = item.title || '';
        var link = item.link || '#';
        var source = '';
        var dashIdx = title.lastIndexOf(' - ');
        if (dashIdx > 20) {
          source = title.substring(dashIdx + 3);
          title = title.substring(0, dashIdx);
        }
        var time = item.pubDate ? formatTimeAgo(item.pubDate) : '';
        return '<a href="' + escapeAttr(link) + '" target="_blank" rel="noopener noreferrer" class="live-news-card">' +
          (source ? '<div class="live-news-source">' + escapeHtml(source) + '</div>' : '') +
          '<div class="live-news-title">' + escapeHtml(title) + '</div>' +
          (time ? '<div class="live-news-time">' + time + '</div>' : '') +
        '</a>';
      }).join('');
    })
    .catch(function(err) {
      // PHASE 2.1 FALLBACK: pull from server-side cache written by fetch_headlines.py
      // This ensures modules never go blank when rss2json fails or rate-limits.
      loadHeadlinesFromCache(containerId, maxItems);
    });
}

// Derive the cache topic key from the feed URL we were asked to fetch.
// NEWS_FEEDS keys ("energy", "oil", ...) map 1:1 to cache filenames.
function topicKeyFromFeedUrl(feedUrl) {
  for (var key in NEWS_FEEDS) {
    if (NEWS_FEEDS[key] === feedUrl) return key;
  }
  return 'energy'; // default
}

// Fetch from server-side cache (data/sources/headlines-{topic}.json).
// This is the Phase 2.1 fallback that guarantees headline modules never go blank.
function loadHeadlinesFromCache(containerId, maxItems) {
  var container = document.getElementById(containerId);
  if (!container) return;

  // Find the data-news-topic attribute on the container (or its parent) to resolve topic
  var el = container.hasAttribute('data-news-topic') ? container : container.closest('[data-news-topic]');
  var topic = el ? el.getAttribute('data-news-topic') : 'energy';

  // Resolve cache URL — works from any depth (root, /category/, /articles/)
  var pathDepth = window.location.pathname.split('/').filter(Boolean).length;
  var prefix = '';
  if (window.location.pathname.indexOf('/category/') !== -1) prefix = '../';
  else if (window.location.pathname.indexOf('/articles/') !== -1) prefix = '../';
  else if (window.location.pathname.indexOf('/authors/') !== -1) prefix = '../';

  var cacheUrl = prefix + 'data/sources/headlines-' + topic + '.json';

  fetch(cacheUrl)
    .then(function(res) { return res.ok ? res.json() : Promise.reject('cache miss'); })
    .then(function(data) {
      var stories = (data && data.stories) || [];
      if (!stories.length) {
        container.innerHTML = '<div style="color:var(--text-3);font-size:12px;padding:12px 16px">Headlines temporarily unavailable</div>';
        return;
      }
      container.innerHTML = stories.slice(0, maxItems).map(function(item) {
        var title = item.title || '';
        var link = item.url || '#';
        var source = item.source || '';
        var time = item.published_at ? formatTimeAgo(item.published_at) : '';
        return '<a href="' + escapeAttr(link) + '" target="_blank" rel="noopener noreferrer" class="live-news-card">' +
          (source ? '<div class="live-news-source">' + escapeHtml(source) + '</div>' : '') +
          '<div class="live-news-title">' + escapeHtml(title) + '</div>' +
          (time ? '<div class="live-news-time">' + time + '</div>' : '') +
        '</a>';
      }).join('');
    })
    .catch(function() {
      container.innerHTML = '<div style="color:var(--text-3);font-size:12px;padding:12px 16px">Headlines temporarily unavailable</div>';
    });
}

// Update breaking news banner with latest headline
function updateBreakingBanner() {
  var url = RSS2JSON_BASE + encodeURIComponent(NEWS_FEEDS.energy);
  fetch(url)
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data.status === 'ok' && data.items && data.items.length > 0) {
        var item = data.items[0];
        var title = item.title || '';
        var link = item.link || '#';
        var dashIdx = title.lastIndexOf(' - ');
        if (dashIdx > 20) title = title.substring(0, dashIdx);

        var textEl = document.querySelector('.breaking-text');
        var linkEl = document.querySelector('.breaking-link');
        if (textEl) textEl.textContent = title;
        if (linkEl) linkEl.href = link;
        return;
      }
      throw new Error('rss2json empty');
    })
    .catch(function() {
      // Fallback to server-side cache — the homepage banner specifically pulls 'energy'
      fetch('data/sources/headlines-energy.json')
        .then(function(r){ return r.ok ? r.json() : null; })
        .then(function(data) {
          if (!data || !data.stories || !data.stories.length) return;
          var s = data.stories[0];
          var textEl = document.querySelector('.breaking-text');
          var linkEl = document.querySelector('.breaking-link');
          if (textEl && s.title) textEl.textContent = s.title;
          if (linkEl && s.url) linkEl.href = s.url;
        })
        .catch(function(){});
    });
}

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
  return str.replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;');
}

function loadLiveNews(topic, containerId, maxItems) {
  var feedUrl = NEWS_FEEDS[topic] || NEWS_FEEDS.energy;
  fetchNewsHeadlines(feedUrl, containerId, maxItems);
  setInterval(function() {
    fetchNewsHeadlines(feedUrl, containerId, maxItems);
  }, 15 * 60 * 1000);
}

document.addEventListener('DOMContentLoaded', function() {
  // Auto-discover news containers
  var els = document.querySelectorAll('[data-news-topic]');
  els.forEach(function(el) {
    var topic = el.getAttribute('data-news-topic');
    var max = parseInt(el.getAttribute('data-news-max')) || 6;
    loadLiveNews(topic, el.id, max);
  });
  
  // Update breaking banner every 30 minutes
  if (document.querySelector('.breaking-banner')) {
    updateBreakingBanner();
    setInterval(updateBreakingBanner, 30 * 60 * 1000);
  }
});
