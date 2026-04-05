/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live News & Data Ingestion
   
   This module pulls real headlines from NewsAPI and displays them
   as attributed source cards that link to the original publisher.
   
   ═══════════════════════════════════════════════════════════════════
   
   SETUP:
   
   1. NEWS HEADLINES (Free)
      Go to https://newsapi.org/register
      Get a free API key (100 requests/day — plenty for hourly updates)
      Paste it below where it says NEWSAPI_KEY
      
      IMPORTANT: NewsAPI free tier only works on localhost.
      For production, you need the paid plan ($449/mo) OR
      use a Cloudflare Worker as a proxy (free tier works).
      I've included the Cloudflare Worker code at the bottom.
   
   2. MARKET PRICES (Free)  
      The EIA API key goes in live-data.js (separate file)
      Register at https://www.eia.gov/opendata/register.php
   
   WHAT THIS DOES:
   - Fetches energy/oil/gas headlines from real publishers
   - Displays them as cards with SOURCE NAME, headline, timestamp
   - Links to the ORIGINAL article (not copied)
   - Refreshes every 30 minutes
   - Falls back to static content if API is unavailable
   
   WHAT THIS DOES NOT DO:
   - Does NOT copy/republish article text
   - Does NOT scrape full articles
   - Does NOT rewrite other people's content
   
   This is the "headline ingestion + source attribution" model
   that is safe for SEO and copyright.
   ═══════════════════════════════════════════════════════════════════ */

// ─── CONFIGURATION ───────────────────────────────────────────────
var NEWS_CONFIG = {
  // Paste your NewsAPI key here (get one free at newsapi.org/register)
  apiKey: '',
  
  // Or if using a Cloudflare Worker proxy, put the worker URL here instead
  // and leave apiKey blank. The worker handles the API key server-side.
  proxyUrl: '',
  
  // How often to refresh (milliseconds). 30 min = 1800000
  refreshInterval: 30 * 60 * 1000,
  
  // Search queries for different sections
  queries: {
    energy:      'oil price OR crude oil OR energy market OR OPEC',
    geopolitics: 'oil sanctions OR energy geopolitics OR pipeline OR OPEC meeting',
    natgas:      'natural gas price OR LNG OR Henry Hub',
    renewables:  'renewable energy OR solar power OR wind energy OR nuclear energy',
    companies:   'ExxonMobil OR Shell OR Chevron OR BP OR TotalEnergies OR Saudi Aramco',
  },
  
  // Max headlines per query
  pageSize: 8,
};

// ─── FETCH HEADLINES ─────────────────────────────────────────────
function fetchNewsHeadlines(query, containerId, maxItems) {
  maxItems = maxItems || 6;
  var container = document.getElementById(containerId);
  if (!container) return;
  
  // Determine URL
  var url = '';
  if (NEWS_CONFIG.proxyUrl) {
    // Use Cloudflare Worker proxy (recommended for production)
    url = NEWS_CONFIG.proxyUrl + '?q=' + encodeURIComponent(query) + '&pageSize=' + NEWS_CONFIG.pageSize;
  } else if (NEWS_CONFIG.apiKey) {
    // Direct NewsAPI call (only works on localhost with free tier)
    url = 'https://newsapi.org/v2/everything?q=' + encodeURIComponent(query) +
          '&language=en&sortBy=publishedAt&pageSize=' + NEWS_CONFIG.pageSize +
          '&apiKey=' + NEWS_CONFIG.apiKey;
  } else {
    // No API configured — show setup message in console only
    console.log('[EPT News] No NewsAPI key or proxy configured. Using static content.');
    console.log('[EPT News] Get a free key at https://newsapi.org/register');
    return;
  }
  
  fetch(url)
    .then(function(res) { return res.json(); })
    .then(function(data) {
      if (data.status !== 'ok' || !data.articles || data.articles.length === 0) {
        console.log('[EPT News] No results for: ' + query);
        return;
      }
      
      var html = data.articles.slice(0, maxItems).map(function(article) {
        var source = article.source && article.source.name ? article.source.name : 'Source';
        var title = article.title || '';
        var url = article.url || '#';
        var time = article.publishedAt ? formatTimeAgo(article.publishedAt) : '';
        
        // Clean title — some APIs append " - SourceName" at the end
        if (title.indexOf(' - ') > -1) {
          title = title.substring(0, title.lastIndexOf(' - '));
        }
        
        return '<a href="' + url + '" target="_blank" rel="noopener noreferrer" class="live-news-card">' +
          '<div class="live-news-source">' + escapeHtml(source) + '</div>' +
          '<div class="live-news-title">' + escapeHtml(title) + '</div>' +
          '<div class="live-news-time">' + time + '</div>' +
        '</a>';
      }).join('');
      
      container.innerHTML = html;
      console.log('[EPT News] Loaded ' + data.articles.length + ' headlines for: ' + query);
    })
    .catch(function(err) {
      console.log('[EPT News] Fetch error for ' + query + ':', err.message);
    });
}

// ─── UTILITIES ───────────────────────────────────────────────────
function formatTimeAgo(isoString) {
  var now = new Date();
  var then = new Date(isoString);
  var diff = Math.floor((now - then) / 1000);
  
  if (diff < 60) return 'Just now';
  if (diff < 3600) return Math.floor(diff / 60) + 'm ago';
  if (diff < 86400) return Math.floor(diff / 3600) + 'h ago';
  if (diff < 604800) return Math.floor(diff / 86400) + 'd ago';
  return then.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
}

function escapeHtml(str) {
  var div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

// ─── AUTO-INIT ───────────────────────────────────────────────────
// Call this from any page to load live headlines into a container
// Example: loadLiveNews('energy', 'live-headlines-container', 6);
function loadLiveNews(topic, containerId, maxItems) {
  var query = NEWS_CONFIG.queries[topic] || topic;
  fetchNewsHeadlines(query, containerId, maxItems);
  
  // Auto-refresh
  setInterval(function() {
    fetchNewsHeadlines(query, containerId, maxItems);
  }, NEWS_CONFIG.refreshInterval);
}


/* ═══════════════════════════════════════════════════════════════════
   CLOUDFLARE WORKER CODE
   
   Deploy this as a Cloudflare Worker to proxy NewsAPI requests.
   This keeps your API key server-side and works on production.
   
   Steps:
   1. Go to dash.cloudflare.com → Workers & Pages → Create Worker
   2. Paste this code
   3. Add your NewsAPI key as an environment variable: NEWSAPI_KEY
   4. Deploy
   5. Copy the worker URL (e.g., https://news-proxy.your-subdomain.workers.dev)
   6. Paste it into NEWS_CONFIG.proxyUrl above
   
   ─── WORKER CODE (copy everything between the === lines) ═══════
   
   export default {
     async fetch(request, env) {
       const url = new URL(request.url);
       const query = url.searchParams.get('q') || 'oil price';
       const pageSize = url.searchParams.get('pageSize') || '8';
       
       const apiUrl = `https://newsapi.org/v2/everything?q=${encodeURIComponent(query)}&language=en&sortBy=publishedAt&pageSize=${pageSize}&apiKey=${env.NEWSAPI_KEY}`;
       
       const response = await fetch(apiUrl);
       const data = await response.json();
       
       return new Response(JSON.stringify(data), {
         headers: {
           'Content-Type': 'application/json',
           'Access-Control-Allow-Origin': 'https://energypricestoday.com',
           'Cache-Control': 'public, max-age=900', // cache 15 min
         },
       });
     },
   };
   
   ═══════════════════════════════════════════════════════════════════ */
