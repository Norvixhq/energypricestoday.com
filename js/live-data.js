/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Engine
   
   PRIMARY: OilPriceAPI (5-min CME/ICE data)
   FALLBACK: Reference prices after 5-second timeout
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

// Reference prices — used as fallback if API fails
var REF_PRICES = {
  'WTI Crude':     { price: 98.72, change: 0.85, pct: 0.87 },
  'Brent Crude':   { price: 96.51, change: 0.59, pct: 0.62 },
  'Natural Gas':   { price: 2.672, change: 0.002, pct: 0.07 },
  'Gasoline RBOB': { price: 3.018, change: 0.018, pct: 0.58 },
  'Heating Oil':   { price: 3.975, change: 0.038, pct: 0.97 },
  'Murban Crude':  { price: 99.62, change: 1.98, pct: 2.03 },
  'Diesel ULSD':   { price: 3.91, change: 0.03, pct: 0.77 },
  'Jet Fuel':      { price: 4.23, change: 0.05, pct: 1.20 },
  'Coal':          { price: 107.70, change: -2.10, pct: -1.91 },
};

var apiResolved = false;

function fetchLivePrices() {
  var names = Object.keys(API_CODES);
  var pending = names.length;
  var liveMap = {};

  names.forEach(function(name) {
    fetch('https://api.oilpriceapi.com/v1/prices/latest?by_code=' + API_CODES[name], {
      headers: { 'Authorization': 'Token ' + OILPRICE_API_KEY }
    })
    .then(function(r) { return r.json(); })
    .then(function(d) {
      if (d.status === 'success' && d.data && d.data.price) {
        liveMap[name] = parseFloat(d.data.price);
        liveMap[API_CODES[name]] = parseFloat(d.data.price);
      }
    })
    .catch(function() {})
    .finally(function() {
      if (--pending === 0) {
        apiResolved = true;
        if (Object.keys(liveMap).length > 0) {
          console.log('[EPT] API success — ' + Object.keys(liveMap).length + ' prices');
          applyPrices(liveMap, true);
        } else {
          console.log('[EPT] API returned no data — using reference prices');
          applyPrices(null, false);
        }
      }
    });
  });
}

// Fallback timer — if API doesn't respond in 5 seconds, use reference prices
function startFallbackTimer() {
  setTimeout(function() {
    if (!apiResolved) {
      console.log('[EPT] API timeout — using reference prices');
      applyPrices(null, false);
    }
  }, 5000);
}

function applyPrices(liveMap, isLive) {
  if (typeof COMMODITIES === 'undefined') return;

  COMMODITIES.forEach(function(c) {
    var src = (liveMap && liveMap[c.name]) ? { price: liveMap[c.name], change: 0, pct: 0 } : REF_PRICES[c.name];
    if (!src) return;
    c.price = src.price;
    c.change = (liveMap && liveMap[c.name]) ? 0 : src.change;
    c.pct = (liveMap && liveMap[c.name]) ? 0 : src.pct;
    c.loading = false;
    c.spark = [c.price*.97,c.price*.98,c.price*.99,c.price*.995,c.price*.998,c.price,c.price];

    // Murban derived from Brent
    if (c.name === 'Murban Crude' && liveMap && liveMap['Brent Crude']) {
      c.price = +(liveMap['Brent Crude'] + 1.76).toFixed(2);
      c.spark = [c.price*.97,c.price*.98,c.price*.99,c.price*.995,c.price*.998,c.price,c.price];
    }
  });

  // Update OIL_PRICE_SECTIONS Futures table
  if (typeof OIL_PRICE_SECTIONS !== 'undefined' && OIL_PRICE_SECTIONS[0]) {
    OIL_PRICE_SECTIONS[0].rows.forEach(function(row) {
      if (row.apiCode && liveMap && liveMap[row.apiCode]) {
        var np = liveMap[row.apiCode];
        row.change = +(np - row.price).toFixed(2);
        row.pct = row.price > 0 ? +((np - row.price) / row.price * 100).toFixed(2) : 0;
        row.price = np;
        row.live = true;
      }
      if (row.name === 'Murban Crude' && liveMap && liveMap['BRENT_CRUDE_USD']) {
        var np2 = +(liveMap['BRENT_CRUDE_USD'] + 1.76).toFixed(2);
        row.change = +(np2 - row.price).toFixed(2);
        row.pct = row.price > 0 ? +((np2 - row.price) / row.price * 100).toFixed(2) : 0;
        row.price = np2;
        row.live = true;
      }
    });
  }

  // Re-render everything
  renderAll();
}

function renderAll() {
  if (typeof renderHeroPrices === 'function') renderHeroPrices();
  if (typeof renderTicker === 'function') renderTicker();
  
  var mkt = document.getElementById('home-market-table');
  if (mkt && typeof renderMarketTable === 'function') renderMarketTable('home-market-table', true);

  var hero = document.getElementById('hero-benchmarks');
  if (hero && typeof sparkline === 'function' && typeof priceChange === 'function') {
    hero.innerHTML = COMMODITIES.slice(0,5).map(function(c) {
      if (c.price === null) return '<div class="price-card price-card-loading"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span></div><div class="price-card-value" style="color:var(--text-3);font-size:15px">Updating\u2026</div><div class="price-card-footer"><span class="price-card-unit">'+c.unit+'</span></div></div>';
      return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span>'+sparkline(c.spark,c.change>=0?'#10b45c':'#dc3545')+'</div><div class="price-card-value">$'+c.price.toFixed(2)+'</div><div class="price-card-footer">'+priceChange(c.change,c.pct)+'<span class="price-card-unit">'+c.unit+'</span></div></div>';
    }).join('');
  }

  // Re-render oil prices table
  var sectionsEl = document.getElementById('price-sections');
  if (sectionsEl && typeof OIL_PRICE_SECTIONS !== 'undefined') {
    sectionsEl.innerHTML = OIL_PRICE_SECTIONS.map(function(s, i) {
      var header = '<div id="price-section-' + i + '" style="scroll-margin-top:100px;margin-bottom:32px">' +
        '<div style="display:flex;align-items:center;gap:8px;margin-bottom:12px">' +
        (s.flag ? '<span style="font-size:22px">' + s.flag + '</span>' : '') +
        '<h2 style="font-size:17px;margin:0">' + s.title + '</h2>' +
        (s.subtitle ? '<span style="color:var(--text-3);font-size:12px;font-weight:500">(' + s.subtitle + ')</span>' : '') +
        '</div>';
      var table = '<div class="market-table-wrap"><table class="market-table">' +
        '<thead><tr><th style="text-align:left">Blend / Index</th><th>Price</th><th>Change</th><th>% Change</th></tr></thead><tbody>';
      table += s.rows.map(function(r) {
        var cls = r.change >= 0 ? 'up' : 'down';
        var tag = r.live ? ' <span style="color:#10b981;font-size:9px;font-weight:700;vertical-align:super">LIVE</span>' : '';
        return '<tr><td>'+r.name+tag+'</td><td class="table-price">$'+r.price.toFixed(2)+'</td><td><span class="change '+cls+'">'+(r.change>=0?'+':'')+r.change.toFixed(2)+'</span></td><td><span class="change '+cls+'">'+(r.change>=0?'+':'')+r.pct.toFixed(2)+'%</span></td></tr>';
      }).join('');
      table += '</tbody></table></div></div>';
      return header + table;
    }).join('');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  fetchLivePrices();
  startFallbackTimer();
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
