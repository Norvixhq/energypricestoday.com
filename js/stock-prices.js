// Stock price loader for Company News directory tables
// Uses Finnhub API for U.S.-listed tickers; marks others as "Not Available"
(function(){
  var FINNHUB_KEY = 'd7dsf2pr01qmm59ebskgd7dsf2pr01qmm59ebsl0';
  var US_TICKERS = ['XOM','CVX','COP','EOG','DVN','FANG','SLB','HAL','BKR','LNG','MPC','VLO','PSX','SU','CNQ','YPF','PBR','EC','WDS','SHEL','TTE','BP','EQNR'];
  var FETCH_TIMEOUT = 8000; // 8 seconds before giving up

  function fetchWithTimeout(url, ms) {
    return new Promise(function(resolve, reject) {
      var timer = setTimeout(function(){ reject(new Error('timeout')); }, ms);
      fetch(url).then(function(r){
        clearTimeout(timer);
        resolve(r);
      }).catch(function(err){
        clearTimeout(timer);
        reject(err);
      });
    });
  }

  function markNotAvailable(el) {
    el.innerHTML = '<span style="color:var(--text-3);font-size:11px">Not Available</span>';
  }

  function renderPrice(el, price, pct) {
    var color = pct >= 0 ? '#10b981' : '#ef4444';
    var arrow = pct >= 0 ? '▲' : '▼';
    el.innerHTML = '<strong style="color:var(--text-1)">$' + price.toFixed(2) + '</strong> <span style="color:' + color + ';font-size:10px;font-weight:600">' + arrow + pct.toFixed(2) + '%</span> <span style="display:inline-block;width:6px;height:6px;background:#10b981;border-radius:50%;margin-left:4px;animation:pulse-live 2s infinite"></span>';
  }

  function loadStockPrices() {
    var spans = document.querySelectorAll('[data-ticker]');
    if (!spans.length) return;

    // Build a map: ticker -> array of DOM nodes (same ticker may appear in multiple tables)
    var byTicker = {};
    spans.forEach(function(span) {
      var t = span.getAttribute('data-ticker');
      if (!byTicker[t]) byTicker[t] = [];
      byTicker[t].push(span);
    });

    // For each unique ticker: if in US_TICKERS, try to fetch; otherwise mark Not Available
    Object.keys(byTicker).forEach(function(ticker, idx) {
      var nodes = byTicker[ticker];
      if (US_TICKERS.indexOf(ticker) === -1) {
        nodes.forEach(markNotAvailable);
        return;
      }
      // Stagger requests by 120ms to avoid rate-limit bursts
      setTimeout(function() {
        fetchWithTimeout('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=' + FINNHUB_KEY, FETCH_TIMEOUT)
          .then(function(r){ return r.json(); })
          .then(function(data) {
            if (data && typeof data.c === 'number' && data.c > 0) {
              var pct = typeof data.dp === 'number' ? data.dp : 0;
              nodes.forEach(function(n){ renderPrice(n, data.c, pct); });
            } else {
              nodes.forEach(markNotAvailable);
            }
          })
          .catch(function(){
            nodes.forEach(markNotAvailable);
          });
      }, idx * 120);
    });

    // Safety net: any element still showing "Loading..." after 12s gets marked Not Available
    setTimeout(function() {
      document.querySelectorAll('[data-ticker]').forEach(function(span) {
        if (span.innerHTML.indexOf('Loading') !== -1) {
          markNotAvailable(span);
        }
      });
    }, 12000);
  }

  // Expose globally
  window.loadStockPrices = loadStockPrices;

  // Inject pulse animation
  var s = document.createElement('style');
  s.textContent = '@keyframes pulse-live{0%,100%{opacity:1}50%{opacity:0.3}}';
  document.head.appendChild(s);

  // Auto-run on DOM ready if tables exist
  document.addEventListener('DOMContentLoaded', function() {
    setTimeout(loadStockPrices, 400);
  });
})();
