/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Engine
   
   OilPriceAPI.com — 5-minute updates from CME/ICE
   Single set of API calls shared across ALL page components.
   ═══════════════════════════════════════════════════════════════════ */

var OILPRICE_API_KEY = 'f719bf8a7ff3844d0a5436da144bc985db3acf2431ddf3095702b1c5f4926e5a';

var API_CODES = {
  'WTI Crude':     'WTI_USD',
  'Brent Crude':   'BRENT_CRUDE_USD',
  'Natural Gas':   'NATURAL_GAS_USD',
  'Gasoline RBOB': 'GASOLINE_USD',
  'Heating Oil':   'HEATING_OIL_USD',
  'Diesel ULSD':   'DIESEL_USD',
  'Jet Fuel':      'JET_FUEL_USD',
  'Coal':          'COAL_USD',
};

// Batch fetch — fires all requests in parallel, applies once all complete
function fetchLivePrices() {
  var names = Object.keys(API_CODES);
  var pending = names.length;
  var results = {};

  names.forEach(function(name) {
    fetch('https://api.oilpriceapi.com/v1/prices/latest?by_code=' + API_CODES[name], {
      headers: { 'Authorization': 'Token ' + OILPRICE_API_KEY }
    })
    .then(function(r) { return r.json(); })
    .then(function(d) {
      if (d.status === 'success' && d.data && d.data.price) {
        results[name] = parseFloat(d.data.price);
      }
    })
    .catch(function() {})
    .finally(function() {
      if (--pending === 0) applyAll(results);
    });
  });
}

function applyAll(results) {
  var count = 0;

  // 1. Update COMMODITIES (homepage hero, ticker, market table)
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) {
      var livePrice = results[c.name];
      if (livePrice) {
        var oldPrice = c.price || livePrice;
        c.change = +(livePrice - oldPrice).toFixed(3);
        c.pct = oldPrice ? +((livePrice - oldPrice) / oldPrice * 100).toFixed(2) : 0;
        c.price = livePrice;
        c.loading = false;
        c.spark = [livePrice*.97,livePrice*.98,livePrice*.99,livePrice*.995,livePrice*.998,livePrice,livePrice];
        count++;
      }
      // Murban = Brent + $1.76
      if (c.name === 'Murban Crude' && results['Brent Crude']) {
        c.price = +(results['Brent Crude'] + 1.76).toFixed(2);
        c.loading = false;
        c.spark = [c.price*.97,c.price*.98,c.price*.99,c.price*.995,c.price*.998,c.price,c.price];
        count++;
      }
    });
  }

  // 2. Update OIL_PRICE_SECTIONS Futures & Indexes rows (oil-prices page)
  if (typeof OIL_PRICE_SECTIONS !== 'undefined' && OIL_PRICE_SECTIONS[0]) {
    OIL_PRICE_SECTIONS[0].rows.forEach(function(row) {
      if (row.apiCode) {
        // Map apiCode back to name
        var apiName = null;
        Object.keys(API_CODES).forEach(function(n) {
          if (API_CODES[n] === row.apiCode) apiName = n;
        });
        var livePrice = apiName ? results[apiName] : null;
        if (livePrice) {
          row.change = +(livePrice - row.price).toFixed(2);
          row.pct = +((livePrice - row.price) / row.price * 100).toFixed(2);
          row.price = livePrice;
          row.live = true;
        }
      }
    });
  }

  console.log('[EPT] Live prices applied: ' + count + ' commodities + oil table');

  // 3. Re-render ALL displays
  if (typeof renderHeroPrices === 'function') renderHeroPrices();
  if (typeof renderTicker === 'function') renderTicker();

  // Market table (homepage)
  var mkt = document.getElementById('home-market-table');
  if (mkt && typeof renderMarketTable === 'function') renderMarketTable('home-market-table', true);

  // Hero benchmark cards (oil-prices, markets, rig-count pages)
  var hero = document.getElementById('hero-benchmarks');
  if (hero && typeof sparkline === 'function' && typeof priceChange === 'function') {
    hero.innerHTML = COMMODITIES.slice(0,5).map(function(c) {
      if (c.price === null) return '<div class="price-card price-card-loading"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span></div><div class="price-card-value" style="color:var(--text-3);font-size:15px">Updating\u2026</div><div class="price-card-footer"><span class="price-card-unit">'+c.unit+'</span></div></div>';
      return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span>'+sparkline(c.spark,c.change>=0?'#10b45c':'#dc3545')+'</div><div class="price-card-value">$'+c.price.toFixed(2)+'</div><div class="price-card-footer">'+priceChange(c.change,c.pct)+'<span class="price-card-unit">'+c.unit+'</span></div></div>';
    }).join('');
  }

  // Oil prices Futures & Indexes table re-render
  var sec0 = document.getElementById('price-section-0');
  if (sec0 && typeof OIL_PRICE_SECTIONS !== 'undefined') {
    var tbody = sec0.querySelector('tbody');
    if (tbody) {
      tbody.innerHTML = OIL_PRICE_SECTIONS[0].rows.map(function(r) {
        var cls = r.change >= 0 ? 'up' : 'down';
        var tag = r.live ? ' <span style="color:var(--green);font-size:9px;vertical-align:super">LIVE</span>' : '';
        return '<tr><td>'+r.name+tag+'</td><td class="table-price">$'+r.price.toFixed(2)+'</td><td><span class="change '+cls+'">'+(r.change>=0?'+':'')+r.change.toFixed(2)+'</span></td><td><span class="change '+cls+'">'+(r.change>=0?'+':'')+r.pct.toFixed(2)+'%</span></td></tr>';
      }).join('');
    }
  }
}

// Boot
document.addEventListener('DOMContentLoaded', function() {
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) { if (c.price !== null) c.loading = false; });
  }
  fetchLivePrices();
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
