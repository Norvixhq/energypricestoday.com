/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Data Module
   
   FREE API SETUP:
   1. Go to https://www.eia.gov/opendata/register.php
   2. Register for a free API key (instant, no payment)
   3. Paste your key below where it says YOUR_KEY_HERE
   4. That's it — prices will update automatically
   
   The EIA API is run by the U.S. government and is 100% free.
   It covers WTI, Brent, Henry Hub, gasoline, heating oil, and more.
   Data updates daily (not intraday — for that you'd need a paid API).
   
   If no API key is set or the API fails, the site falls back to
   the mock data in data.js so it always looks good.
   ═══════════════════════════════════════════════════════════════════ */

var EIA_API_KEY = ''; // ← Paste your free EIA key here

// EIA series IDs for major benchmarks
var EIA_SERIES = {
  'WTI Crude':     'PET.RWTC.D',
  'Brent Crude':   'PET.RBRTE.D',
  'Natural Gas':   'NG.RNGWHHD.D',
  'Gasoline RBOB': 'PET.EER_EPMRU_PF4_RGC_DPG.D',
  'Heating Oil':   'PET.EER_EPD2F_PF4_RGC_DPG.D',
};

// Fetch live prices from EIA API
function fetchLivePrices() {
  if (!EIA_API_KEY || EIA_API_KEY === 'YOUR_KEY_HERE' || EIA_API_KEY === '') {
    console.log('[EPT] No EIA API key configured — using mock data. Get a free key at https://www.eia.gov/opendata/register.php');
    return;
  }

  console.log('[EPT] Fetching live prices from EIA API...');

  var seriesEntries = Object.entries(EIA_SERIES);
  var completed = 0;
  var updates = {};

  seriesEntries.forEach(function(entry) {
    var name = entry[0];
    var seriesId = entry[1];
    var url = 'https://api.eia.gov/v2/seriesid/' + seriesId + '?api_key=' + EIA_API_KEY + '&num=2';

    fetch(url)
      .then(function(res) { return res.json(); })
      .then(function(data) {
        if (data && data.response && data.response.data && data.response.data.length >= 2) {
          var latest = parseFloat(data.response.data[0].value);
          var prev = parseFloat(data.response.data[1].value);
          var change = latest - prev;
          var pct = prev > 0 ? (change / prev) * 100 : 0;
          updates[name] = { price: latest, change: change, pct: pct };
          console.log('[EPT] ' + name + ': $' + latest.toFixed(2) + ' (' + (change >= 0 ? '+' : '') + change.toFixed(2) + ')');
        }
      })
      .catch(function(err) {
        console.log('[EPT] Failed to fetch ' + name + ':', err.message);
      })
      .finally(function() {
        completed++;
        if (completed === seriesEntries.length) {
          applyLiveUpdates(updates);
        }
      });
  });
}

// Apply fetched prices to the COMMODITIES array and re-render
function applyLiveUpdates(updates) {
  var count = 0;
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) {
      if (updates[c.name]) {
        c.price = updates[c.name].price;
        c.change = updates[c.name].change;
        c.pct = updates[c.name].pct;
        count++;
      }
    });
  }

  if (count > 0) {
    console.log('[EPT] Applied ' + count + ' live price updates');
    // Re-render hero prices if on homepage
    var heroEl = document.getElementById('hero-prices');
    if (heroEl && typeof renderHeroPrices === 'function') {
      renderHeroPrices();
    }
    // Re-render ticker
    if (typeof renderTicker === 'function') {
      renderTicker();
    }
  }
}

// Auto-fetch on page load if key is set
document.addEventListener('DOMContentLoaded', function() {
  // Small delay to let main rendering finish first
  setTimeout(fetchLivePrices, 1500);

  // Refresh every 5 minutes
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
