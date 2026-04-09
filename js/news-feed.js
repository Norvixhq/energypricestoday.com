/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live News Headlines
   
   Pulls live energy headlines from Google News RSS feeds via
   rss2json.com (free, CORS-enabled, no API key required).
   
   SETUP: None. This works immediately on any domain.
   ═══════════════════════════════════════════════════════════════════ */

var NEWS_FEEDS = {
  energy:      'https://news.google.com/rss/search?q=oil+price+OR+crude+oil+OR+energy+market+OR+OPEC&hl=en-US&gl=US&ceid=US:en',
  geopolitics: 'https://news.google.com/rss/search?q=strait+hormuz+OR+red+sea+oil+OR+OPEC+production+OR+oil+sanctions+OR+oil+tanker+attack+OR+refinery+outage+OR+oil+supply+disruption&hl=en-US&gl=US&ceid=US:en',
  natgas:      'https://news.google.com/rss/search?q=natural+gas+price+OR+LNG+OR+Henry+Hub&hl=en-US&gl=US&ceid=US:en',
  renewables:  'https://news.google.com/rss/search?q=renewable+energy+OR+solar+power+OR+wind+energy+OR+nuclear+reactor&hl=en-US&gl=US&ceid=US:en',
  companies:   'https://news.google.com/rss/search?q=ExxonMobil+OR+Chevron+OR+Shell+oil+OR+Saudi+Aramco&hl=en-US&gl=US&ceid=US:en',
  oil:         'https://news.google.com/rss/search?q=crude+oil+production+OR+oil+drilling+OR+Brent+crude+OR+WTI&hl=en-US&gl=US&ceid=US:en',
  rigcount:    'https://news.google.com/rss/search?q=rig+count+OR+Baker+Hughes+OR+drilling+activity&hl=en-US&gl=US&ceid=US:en',
  gasoline:    'https://news.google.com/rss/search?q=gasoline+price+OR+gas+price+gallon+OR+fuel+price&hl=en-US&gl=US&ceid=US:en',
  heating:     'https://news.google.com/rss/search?q=heating+oil+price+OR+diesel+fuel+OR+distillate&hl=en-US&gl=US&ceid=US:en',
};

var RSS2JSON_BASE = 'https://api.rss2json.com/v1/api.json?rss_url=';

function fetchNewsHeadlines(feedUrl, containerId, maxItems) {
  maxItems = maxItems || 6;
  var container = document.getElementById(containerId);
  if (!container) return;

  var url = RSS2JSON_BASE + encodeURIComponent(feedUrl) ;

  fetch(url)
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data.status !== 'ok' || !data.items || data.items.length === 0) {
        console.log('[EPT News] No results');
        return;
      }

      var html = data.items.slice(0, maxItems).map(function(item) {
        var title = item.title || '';
        var link = item.link || '#';
        var pubDate = item.pubDate || '';
        var source = '';

        // Extract source from title (Google News appends " - SourceName")
        var dashIdx = title.lastIndexOf(' - ');
        if (dashIdx > 20) {
          source = title.substring(dashIdx + 3);
          title = title.substring(0, dashIdx);
        }

        var time = pubDate ? formatTimeAgo(pubDate) : '';

        return '<a href="' + escapeAttr(link) + '" target="_blank" rel="noopener noreferrer" class="live-news-card">' +
          (source ? '<div class="live-news-source">' + escapeHtml(source) + '</div>' : '') +
          '<div class="live-news-title">' + escapeHtml(title) + '</div>' +
          (time ? '<div class="live-news-time">' + time + '</div>' : '') +
        '</a>';
      }).join('');

      if (html) {
        container.innerHTML = html;
        var section = document.getElementById('live-headlines-section');
        if (section) section.style.display = '';
      }

      console.log('[EPT News] Loaded ' + data.items.length + ' headlines');
    })
    .catch(function(err) {
      console.log('[EPT News] Error:', err.message);
    });
}

function formatTimeAgo(dateStr) {
  try {
    var then = new Date(dateStr);
    var now = new Date();
    var diff = Math.floor((now - then) / 1000);
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
  var els = document.querySelectorAll('[data-news-topic]');
  els.forEach(function(el) {
    var topic = el.getAttribute('data-news-topic');
    var max = parseInt(el.getAttribute('data-news-max')) || 6;
    loadLiveNews(topic, el.id, max);
  });
});
