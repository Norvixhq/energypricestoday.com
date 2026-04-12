/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Live Stock Prices via Finnhub
   Free tier: 60 calls/minute, real-time U.S. stock data
   ═══════════════════════════════════════════════════════════════════ */

var FINNHUB_KEY = 'd7dsf2pr01qmm59ebskgd7dsf2pr01qmm59ebsl0';

function fetchStockPrices() {
  var table = document.querySelector('.company-directory-wrap table');
  if (!table) return;
  
  var rows = table.querySelectorAll('tbody tr');
  if (!rows.length) return;

  // Add Stock Price header if not present
  var thead = table.querySelector('thead tr');
  if (thead && !thead.querySelector('.stock-header')) {
    var th = document.createElement('th');
    th.textContent = 'Stock Price';
    th.className = 'stock-header';
    thead.insertBefore(th, thead.children[2]); // After ticker
  }

  rows.forEach(function(row, idx) {
    var tickerCell = row.children[1];
    if (!tickerCell) return;
    var ticker = tickerCell.textContent.trim();
    
    // Skip non-US tickers and private companies
    if (!ticker || ticker === 'Private' || ticker.includes('.') || ticker.includes(':')) {
      // Add empty cell
      if (!row.querySelector('.stock-cell')) {
        var td = document.createElement('td');
        td.className = 'stock-cell';
        td.style.cssText = 'text-align:right;color:var(--text-3);font-size:12px';
        td.textContent = '—';
        row.insertBefore(td, row.children[2]);
      }
      return;
    }

    // Add placeholder cell
    var td = document.createElement('td');
    td.className = 'stock-cell';
    td.style.cssText = 'text-align:right;font-size:13px';
    td.innerHTML = '<span style="color:var(--text-3)">...</span>';
    row.insertBefore(td, row.children[2]);

    // Fetch with delay to respect rate limits (60/min)
    setTimeout(function() {
      fetch('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=' + FINNHUB_KEY)
        .then(function(r) { return r.json(); })
        .then(function(data) {
          if (data && data.c && data.c > 0) {
            var price = data.c.toFixed(2);
            var change = data.dp ? data.dp.toFixed(2) : '0.00';
            var color = parseFloat(change) >= 0 ? '#10b981' : '#ef4444';
            var arrow = parseFloat(change) >= 0 ? '▲' : '▼';
            td.innerHTML = '<strong style="color:var(--text-1)">$' + price + '</strong> <span style="color:' + color + ';font-size:11px">' + arrow + ' ' + change + '%</span>';
          }
        })
        .catch(function() {
          td.innerHTML = '<span style="color:var(--text-3)">—</span>';
        });
    }, idx * 200); // Stagger calls: 200ms apart = 5/sec, well under 60/min
  });
}

document.addEventListener('DOMContentLoaded', function() {
  // Wait for company directory to render, then fetch stock prices
  setTimeout(fetchStockPrices, 1500);
});
