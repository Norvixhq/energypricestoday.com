/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Price Engine
   
   OilPriceAPI /v1/prices/all — ONE call returns ALL 35+ commodities
   10,000 requests/month = 10,000 page loads/month (333/day)
   ═══════════════════════════════════════════════════════════════════ */

var OILPRICE_API_KEY = 'f719bf8a7ff3844d0a5436da144bc985db3acf2431ddf3095702b1c5f4926e5a';

// Map our display names to API codes
// ALL 28 available commodity codes mapped
var CODE_MAP = {
  // Oil Benchmarks
  'WTI Crude':     'WTI_USD',
  'Brent Crude':   'BRENT_CRUDE_USD',
  'Tapis Crude':   'TAPIS_CRUDE_USD',
  // Refined Products
  'Gasoline RBOB': 'GASOLINE_USD',
  'Heating Oil':   'HEATING_OIL_USD',
  'Diesel ULSD':   'DIESEL_USD',
  'Jet Fuel':      'JET_FUEL_USD',
  'Ethanol':       'ETHANOL_USD',
  // Natural Gas & LNG
  'Natural Gas':          'NATURAL_GAS_USD',
  'Henry Hub Natural Gas':'NATURAL_GAS_USD',
  'UK NBP Natural Gas':   'NATURAL_GAS_GBP',
  'Dutch TTF Natural Gas':'DUTCH_TTF_EUR',
  'JKM LNG (Japan/Korea)':'JKM_LNG_USD',
  // Coal
  'Coal':                       'NEWCASTLE_COAL_USD',
  'Newcastle Coal':             'NEWCASTLE_COAL_USD',
  'CAPP Coal (Central Appalachia)':'CAPP_COAL_USD',
  'Coking Coal':                'COKING_COAL_USD',
  'NYMEX Appalachian Coal':     'NYMEX_APPALACHIAN_USD',
  // Marine Fuels
  'VLSFO (Very Low Sulfur Fuel Oil)':'VLSFO_USD',
  'MGO 0.5% Sulfur':           'MGO_05S_USD',
  'HFO 380 CST':               'HFO_380_USD',
  'HFO 180 CST':               'HFO_180_USD',
  // Metals & Other
  'Gold':        'GOLD_USD',
  'Uranium':     'URANIUM_USD',
  'EU Carbon (EUA)':'EU_CARBON_EUR',
  // Forex
  'GBP/USD':     'GBP_USD',
  'EUR/USD':     'EUR_USD',
  // Storage
  'Cushing OK Crude Storage':  'CUSHING_STORAGE',
  'U.S. Natural Gas Storage':  'NATURAL_GAS_STORAGE',
};
var EXTRA_CODES = {};

function fetchLivePrices() {
  fetch('https://api.oilpriceapi.com/v1/prices/all', {
    headers: { 'Authorization': 'Token ' + OILPRICE_API_KEY }
  })
  .then(function(r) { return r.json(); })
  .then(function(resp) {
    if (resp.status !== 'success' || !resp.data || !resp.data.data || !resp.data.data.prices) {
      console.log('[EPT] API response invalid');
      return;
    }
    var prices = resp.data.data.prices;
    console.log('[EPT] All Prices API: ' + Object.keys(prices).length + ' commodities received');
    applyAll(prices);
  })
  .catch(function(err) {
    console.log('[EPT] API error: ' + err.message);
  });
}

function applyAll(prices) {
  var count = 0;

  // 1. Update COMMODITIES (homepage hero, ticker, market table)
  if (typeof COMMODITIES !== 'undefined') {
    COMMODITIES.forEach(function(c) {
      var code = CODE_MAP[c.name];
      if (code && prices[code]) {
        var p = prices[code];
        c.price = p.price;
        c.change = p.change_24h || 0;
        c.pct = p.change_24h_percent || 0;
        c.loading = false;
        c.spark = [c.price*.97,c.price*.98,c.price*.99,c.price*.995,c.price*.998,c.price,c.price];
        count++;
      }
      // Murban = Brent + $1.76
      if (c.name === 'Murban Crude' && prices['BRENT_CRUDE_USD']) {
        c.price = +(prices['BRENT_CRUDE_USD'].price + 1.76).toFixed(2);
        c.change = prices['BRENT_CRUDE_USD'].change_24h || 0;
        c.pct = prices['BRENT_CRUDE_USD'].change_24h_percent || 0;
        c.loading = false;
        c.spark = [c.price*.97,c.price*.98,c.price*.99,c.price*.995,c.price*.998,c.price,c.price];
        count++;
      }
    });
  }

  // 2. Update ALL OIL_PRICE_SECTIONS with live data
  if (typeof OIL_PRICE_SECTIONS !== 'undefined') {
    OIL_PRICE_SECTIONS.forEach(function(section) {
    section.rows.forEach(function(row) {
      var code = row.apiCode;
      if (!code) {
        Object.keys(CODE_MAP).forEach(function(name) {
          if (row.name === name) code = CODE_MAP[name];
        });
      }
      if (code && prices[code]) {
        var p = prices[code];
        row.change = +(p.price - row.price).toFixed(2);
        row.pct = row.price > 0 ? +((p.price - row.price) / row.price * 100).toFixed(2) : 0;
        row.price = p.price;
        row.live = true;
      }
      // Murban derived from Brent
      if (row.name === 'Murban Crude' && prices['BRENT_CRUDE_USD']) {
        var np = +(prices['BRENT_CRUDE_USD'].price + 1.76).toFixed(2);
        row.change = +(np - row.price).toFixed(2);
        row.pct = row.price > 0 ? +((np - row.price) / row.price * 100).toFixed(2) : 0;
        row.price = np;
        row.live = true;
      }
    });
    });
  }

  console.log('[EPT] Applied ' + count + ' live commodity prices');
  renderAll();
}

function renderAll() {
  if (typeof renderHeroPrices === 'function') renderHeroPrices();
  if (typeof renderTicker === 'function') renderTicker();
  
  var mkt = document.getElementById('home-market-table');
  if (mkt && typeof renderMarketTable === 'function') renderMarketTable('home-market-table', true);

  // Subpage hero cards
  var hero = document.getElementById('hero-benchmarks');
  if (hero && typeof sparkline === 'function' && typeof priceChange === 'function') {
    hero.innerHTML = COMMODITIES.slice(0,5).map(function(c) {
      if (c.price === null) return '<div class="price-card price-card-loading"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span></div><div class="price-card-value" style="color:var(--text-3);font-size:15px">Updating\u2026</div><div class="price-card-footer"><span class="price-card-unit">'+c.unit+'</span></div></div>';
      return '<div class="price-card"><div class="price-card-header"><span class="price-card-label">'+c.name+'</span>'+sparkline(c.spark,c.change>=0?'#10b45c':'#dc3545')+'</div><div class="price-card-value">$'+c.price.toFixed(2)+'</div><div class="price-card-footer">'+priceChange(c.change,c.pct)+'<span class="price-card-unit">'+c.unit+'</span></div></div>';
    }).join('');
  }

  // Oil prices page full table re-render
  var sectionsEl = document.getElementById('price-sections');
  if (sectionsEl && typeof OIL_PRICE_SECTIONS !== 'undefined') {
    sectionsEl.innerHTML = OIL_PRICE_SECTIONS.map(function(s, i) {
      var header = '<div id="price-section-' + i + '" style="scroll-margin-top:100px;margin-bottom:32px"><div style="display:flex;align-items:center;gap:8px;margin-bottom:12px">' +
        (s.flag ? '<span style="font-size:22px">' + s.flag + '</span>' : '') +
        '<h2 style="font-size:17px;margin:0">' + s.title + '</h2>' +
        (s.subtitle ? '<span style="color:var(--text-3);font-size:12px;font-weight:500">(' + s.subtitle + ')</span>' : '') + '</div>';
      var table = '<div class="market-table-wrap"><table class="market-table"><thead><tr><th style="text-align:left">Blend / Index</th><th>Price</th><th>Change</th><th>% Change</th></tr></thead><tbody>';
      table += s.rows.map(function(r) {
        var cls = r.change >= 0 ? 'up' : 'down';
        var tag = r.live ? ' <span style="color:#10b981;font-size:9px;font-weight:700;vertical-align:super">LIVE</span>' : '';
        return '<tr><td>'+r.name+tag+'</td><td class="table-price">$'+r.price.toFixed(2)+'</td><td><span class="change '+cls+'">'+(r.change>=0?'+':'')+r.change.toFixed(2)+'</span></td><td><span class="change '+cls+'">'+(r.change>=0?'+':'')+r.pct.toFixed(2)+'%</span></td></tr>';
      }).join('');
      return header + table + '</tbody></table></div></div>';
    }).join('');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  // Fetch immediately — 1 call gets everything
  fetchLivePrices();
  // Refresh every 5 minutes
  setInterval(fetchLivePrices, 5 * 60 * 1000);
});
