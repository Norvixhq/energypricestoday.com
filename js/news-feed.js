/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — GDELT News Feed
   
   Pulls live energy headlines from GDELT — 100% free, no API key,
   no registration, no commercial restrictions, works on production.
   
   SETUP: None. This works immediately. Just deploy your site.
   
   HOW IT WORKS:
   - Calls GDELT's free Doc API to search for energy/oil/gas headlines
   - Displays them as attributed source cards linking to original publisher
   - Refreshes every 15 minutes automatically
   - Falls back gracefully if GDELT is temporarily unavailable
   
   GDELT monitors news from nearly every country in 100+ languages
   and updates every 15 minutes. No rate limits for this usage level.
   ═══════════════════════════════════════════════════════════════════ */

var GDELT_CONFIG = {
  // Base URL for GDELT Doc 2.0 API
  baseUrl: 'https://api.gdeltproject.org/api/v2/doc/doc',
  
  // Refresh interval (15 minutes)
  refreshInterval: 15 * 60 * 1000,
  
  // Search queries mapped to site sections
  queries: {
    energy:      'oil price OR crude oil OR energy market OR OPEC OR petroleum',
    geopolitics: 'oil sanctions OR energy geopolitics OR strait hormuz OR OPEC meeting OR pipeline conflict',
    natgas:      'natural gas price OR LNG export OR Henry Hub OR liquefied natural gas',
    renewables:  'renewable energy OR solar power OR wind energy OR nuclear reactor OR clean energy',
    companies:   'ExxonMobil OR Chevron OR Shell oil OR BP energy OR Saudi Aramco OR TotalEnergies',
    oil:         'crude oil production OR oil drilling OR Brent crude OR WTI crude OR oil refinery',
    gasoline:    'gasoline price OR gas price per gallon OR fuel price OR RBOB gasoline',
    heating:     'heating oil price OR diesel fuel OR distillate OR home heating',
    rigcount:    'rig count OR oil drilling rig OR Baker Hughes OR drilling activity',
  },
  
  // Max articles per request
  maxRecords: 10,
};

// ─── FETCH FROM GDELT ────────────────────────────────────────────
function fetchGdeltHeadlines(query, containerId, maxItems) {
  maxItems = maxItems || 6;
  var container = document.getElementById(containerId);
  if (!container) return;
  
  var url = GDELT_CONFIG.baseUrl +
    '?query=' + encodeURIComponent(query) +
    '&mode=ArtList' +
    '&maxrecords=' + GDELT_CONFIG.maxRecords +
    '&sort=DateDesc' +
    '&format=json' +
    '&sourcelang=eng';
  
  // Use CORS proxy for cross-origin GDELT requests
  var corsUrl = 'https://api.allorigins.win/raw?url=' + encodeURIComponent(url);
  
  fetch(corsUrl)
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (!data.articles || data.articles.length === 0) {
        console.log('[EPT] No GDELT results for: ' + query);
        return;
      }
      
      var seen = {};
      var articles = data.articles.filter(function(a) {
        // Deduplicate by domain
        var domain = extractDomain(a.url || '');
        if (seen[domain]) return false;
        seen[domain] = true;
        return true;
      }).slice(0, maxItems);
      
      var html = articles.map(function(article) {
        var title = article.title || '';
        var url = article.url || '#';
        var source = article.domain || extractDomain(url);
        var dateStr = article.seendate || '';
        var time = dateStr ? formatTimeAgo(dateStr) : '';
        
        // Clean source domain into readable name
        source = cleanSourceName(source);
        
        // Clean title — remove trailing " - Source Name" patterns
        if (title.lastIndexOf(' - ') > 20) {
          title = title.substring(0, title.lastIndexOf(' - '));
        }
        if (title.lastIndexOf(' | ') > 20) {
          title = title.substring(0, title.lastIndexOf(' | '));
        }
        
        return '<a href="' + escapeAttr(url) + '" target="_blank" rel="noopener noreferrer" class="live-news-card">' +
          '<div class="live-news-source">' + escapeHtml(source) + '</div>' +
          '<div class="live-news-title">' + escapeHtml(title) + '</div>' +
          (time ? '<div class="live-news-time">' + time + '</div>' : '') +
        '</a>';
      }).join('');
      
      if (html) {
        container.innerHTML = html;
        // Show parent section if it was hidden
        var section = container.closest('[style*="display:none"], [style*="display: none"]');
        if (section) section.style.display = '';
      }
      
      console.log('[EPT] Loaded ' + articles.length + ' headlines for: ' + query.substring(0, 30) + '...');
    })
    .catch(function(err) {
      console.log('[EPT] GDELT fetch error:', err.message);
    });
}

// ─── HELPERS ─────────────────────────────────────────────────────
function extractDomain(url) {
  try {
    return new URL(url).hostname.replace('www.', '');
  } catch (e) {
    return url.split('/')[2] || 'source';
  }
}

function cleanSourceName(domain) {
  // Map common domains to clean names
  var names = {
    'reuters.com': 'Reuters',
    'apnews.com': 'AP News',
    'bloomberg.com': 'Bloomberg',
    'cnbc.com': 'CNBC',
    'cnn.com': 'CNN',
    'bbc.com': 'BBC',
    'bbc.co.uk': 'BBC',
    'nytimes.com': 'New York Times',
    'washingtonpost.com': 'Washington Post',
    'wsj.com': 'Wall Street Journal',
    'ft.com': 'Financial Times',
    'theguardian.com': 'The Guardian',
    'foxnews.com': 'Fox News',
    'foxbusiness.com': 'Fox Business',
    'nbcnews.com': 'NBC News',
    'abcnews.go.com': 'ABC News',
    'aljazeera.com': 'Al Jazeera',
    'oilprice.com': 'OilPrice',
    'rigzone.com': 'Rigzone',
    'spglobal.com': 'S&P Global',
    'platts.com': 'S&P Platts',
    'argusmedia.com': 'Argus Media',
    'energynow.com': 'EnergyNow',
    'naturalgasintel.com': 'NGI',
    'ogj.com': 'Oil & Gas Journal',
    'worldoil.com': 'World Oil',
    'upstreamonline.com': 'Upstream',
    'hellenicshippingnews.com': 'Hellenic Shipping',
    'maritime-executive.com': 'Maritime Executive',
    'yahoo.com': 'Yahoo',
    'finance.yahoo.com': 'Yahoo Finance',
    'marketwatch.com': 'MarketWatch',
    'investing.com': 'Investing.com',
    'nasdaq.com': 'Nasdaq',
    'barrons.com': "Barron's",
    'seekingalpha.com': 'Seeking Alpha',
  };
  
  if (names[domain]) return names[domain];
  
  // Auto-clean: remove TLD, capitalize
  var parts = domain.replace(/\.(com|org|net|co\.uk|io)$/i, '').split('.');
  var name = parts[parts.length - 1];
  return name.charAt(0).toUpperCase() + name.slice(1);
}

function formatTimeAgo(gdeltDate) {
  // GDELT dates come as "YYYYMMDDTHHmmssZ" format
  try {
    var d = gdeltDate.replace(/(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})Z/, '$1-$2-$3T$4:$5:$6Z');
    var then = new Date(d);
    var now = new Date();
    var diff = Math.floor((now - then) / 1000);
    
    if (isNaN(diff) || diff < 0) return '';
    if (diff < 120) return 'Just now';
    if (diff < 3600) return Math.floor(diff / 60) + 'm ago';
    if (diff < 86400) return Math.floor(diff / 3600) + 'h ago';
    if (diff < 604800) return Math.floor(diff / 86400) + 'd ago';
    return then.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
  } catch (e) {
    return '';
  }
}

function escapeHtml(str) {
  var div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

function escapeAttr(str) {
  return str.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/'/g, '&#39;').replace(/</g, '&lt;');
}

// ─── PUBLIC API ──────────────────────────────────────────────────
// Call from any page: loadLiveNews('energy', 'container-id', 6)
function loadLiveNews(topic, containerId, maxItems) {
  var query = GDELT_CONFIG.queries[topic] || topic;
  
  // Fetch immediately
  fetchGdeltHeadlines(query, containerId, maxItems);
  
  // Then refresh on interval
  setInterval(function() {
    fetchGdeltHeadlines(query, containerId, maxItems);
  }, GDELT_CONFIG.refreshInterval);
}

// Auto-initialize any elements with data-news-topic attribute
document.addEventListener('DOMContentLoaded', function() {
  var els = document.querySelectorAll('[data-news-topic]');
  els.forEach(function(el) {
    var topic = el.getAttribute('data-news-topic');
    var max = parseInt(el.getAttribute('data-news-max')) || 6;
    loadLiveNews(topic, el.id, max);
  });
});
