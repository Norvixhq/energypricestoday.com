/* Live News Headlines via Google News RSS + rss2json.com */

var NEWS_FEEDS = {
  energy:      'https://news.google.com/rss/search?q=oil+prices+energy+market&hl=en-US&gl=US&ceid=US:en',
  geopolitics: 'https://news.google.com/rss/search?q=oil+geopolitics+OPEC+sanctions&hl=en-US&gl=US&ceid=US:en',
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

  container.innerHTML = '<div style="color:var(--text-3);font-size:12px;padding:12px 16px">Loading headlines...</div>';

  fetch(url)
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data.status !== 'ok' || !data.items || data.items.length === 0) {
        container.innerHTML = '<div style="color:var(--text-3);font-size:12px;padding:12px 16px">Headlines temporarily unavailable</div>';
        return;
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
      }
    })
    .catch(function() {});
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
