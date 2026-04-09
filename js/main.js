/* ═══════════════════════════════════════════════════════════════════
   EnergyPricesToday.com — Main JavaScript
   Shared components, icons, and utilities
   ═══════════════════════════════════════════════════════════════════ */

// ─── SVG ICONS (inline, no dependencies) ─────────────────────────
const ICONS = {
  zap: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
  "trending-up": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>',
  "trending-down": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 17 13.5 8.5 8.5 13.5 2 7"/><polyline points="16 17 22 17 22 11"/></svg>',
  "chevron-right": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>',
  "chevron-down": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
  "arrow-right": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>',
  activity: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/></svg>',
  "bar-chart": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>',
  newspaper: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8"/><path d="M15 18h-5"/><path d="M10 6h8v4h-8V6Z"/></svg>',
  globe: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>',
  building: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>',
  sun: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>',
  flame: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>',
  thermometer: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/></svg>',
  droplets: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z"/><path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97"/></svg>',
  fuel: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" x2="15" y1="22" y2="22"/><line x1="4" x2="14" y1="9" y2="9"/><path d="M14 22V4a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v18"/><path d="M14 13h2a2 2 0 0 1 2 2v2a2 2 0 0 0 2 2a2 2 0 0 0 2-2V9.83a2 2 0 0 0-.59-1.42L18 5"/></svg>',
  "line-chart": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>',
  "hard-hat": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 18a1 1 0 0 0 1 1h18a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1v2z"/><path d="M10 15V6.5a3.5 3.5 0 0 1 7 0V15"/><path d="M7 15v-3a6.5 6.5 0 0 1 13 0v3"/></svg>',
  atom: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="1"/><path d="M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5Z"/><path d="M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5Z"/></svg>',
  wind: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/><path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/></svg>',
  leaf: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.9C15.5 4.9 20 .5 20 .5s1 4.9-1.5 10.5A7 7 0 0 1 11 20z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>',
  users: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
  factory: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/><path d="M17 18h1"/><path d="M12 18h1"/><path d="M7 18h1"/></svg>',
  layout: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><line x1="3" x2="21" y1="9" y2="9"/><line x1="9" x2="9" y1="21" y2="9"/></svg>',
  menu: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>',
  x: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>',
  mail: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
  bell: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/></svg>',
  user: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
  image: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/></svg>',
  "check-circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
  share: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"/><polyline points="16 6 12 2 8 6"/><line x1="12" x2="12" y1="2" y2="15"/></svg>',
  twitter: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/></svg>',
  linkedin: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>',
  youtube: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/></svg>',
  folder: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/></svg>',
  search: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
  anchor: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22V8"/><path d="M5 12H2a10 10 0 0 0 20 0h-3"/><circle cx="12" cy="5" r="3"/></svg>',
  ship: '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 21c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1 .6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M19.38 20A11.6 11.6 0 0 0 21 14l-9-4-9 4c0 2.9.94 5.34 2.81 7.76"/><path d="M19 13V7a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v6"/><path d="M12 10v4"/><path d="M12 2v3"/></svg>',
};

function icon(name, size) {
  const s = size || 18;
  const svg = ICONS[name] || ICONS.folder;
  return svg.replace(/width="24"/g, `width="${s}"`).replace(/height="24"/g, `height="${s}"`);
}

// ─── SPARKLINE SVG GENERATOR ─────────────────────────────────────
function sparkline(data, color, w, h) {
  w = w || 80; h = h || 28;
  if (!data || data.length < 2) return '';
  const min = Math.min(...data), max = Math.max(...data), range = max - min || 1;
  const pts = data.map((v, i) => `${(i / (data.length - 1)) * w},${h - ((v - min) / range) * (h - 4) - 2}`).join(' ');
  return `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" style="display:block"><polyline points="${pts}" fill="none" stroke="${color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
}

// ─── PRICE CHANGE HTML ───────────────────────────────────────────
function priceChange(change, pct) {
  if (change === null || change === undefined) return '<span style="color:var(--text-3)">—</span>';
  const up = change >= 0;
  const cls = up ? 'up' : 'down';
  const ico = up ? 'trending-up' : 'trending-down';
  return `<span class="change ${cls}">${icon(ico, 13)} ${up ? '+' : ''}${change.toFixed(2)} (${up ? '+' : ''}${pct.toFixed(2)}%)</span>`;
}

// ─── CATEGORY PILL ───────────────────────────────────────────────
function catPill(cat, slug) {
  if (slug) return `<a class="cat-pill" href="category/${slug}.html">${cat}</a>`;
  return `<span class="cat-pill">${cat}</span>`;
}

// ─── HEADER ──────────────────────────────────────────────────────
function renderHeader(activePage) {
  const nav = [
    { label: 'Home', href: 'index.html' },
    { label: 'Gas Prices', href: 'category/gas-prices.html' },
    { label: 'Oil Prices', href: 'oil-prices.html' },
    { label: 'Geopolitics', href: 'category/geopolitics.html' },
    { label: 'Markets', href: 'markets.html', dropdown: [
      { label: 'Crude Oil', href: 'category/crude-oil.html' },
      { label: 'Natural Gas', href: 'category/natural-gas.html' },
      { label: 'Heating Oil', href: 'category/heating-oil.html' },
      { label: 'Oil Futures', href: 'oil-futures.html' },
    ]},
    { label: 'Rig Count', href: 'rig-count.html' },
    { label: 'Company News', href: 'category/company-news.html' },
    { label: 'Energy', href: 'category/energy.html' },
    { label: 'Alt Energy', href: 'category/alternative-energy.html', dropdown: [
      { label: 'Nuclear', href: 'category/nuclear.html' },
      { label: 'Solar', href: 'category/solar.html' },
      { label: 'Wind', href: 'category/wind.html' },
      { label: 'Renewables', href: 'category/renewable-energy.html' },
    ]},
    { label: 'About', href: 'about.html' },
    { label: 'Contact', href: 'contact.html' },
  ];

  // Fix paths for pages in subdirectories
  const inSub = window.location.pathname.includes('/category/') || window.location.pathname.includes('/authors/') || window.location.pathname.includes('/articles/');
  const prefix = inSub ? '../' : '';

  const navLinks = nav.map(n => {
    const href = prefix + n.href;
    const isActive = window.location.pathname.endsWith(n.href) || (activePage && n.href.includes(activePage));
    if (n.dropdown) {
      const subs = n.dropdown.map(s => `<a href="${prefix + s.href}">${s.label}</a>`).join('');
      return `<div class="nav-dropdown-wrap">
        <a class="nav-link${isActive ? ' active' : ''}" href="${href}">${n.label} ${icon('chevron-down', 12)}</a>
        <div class="nav-dropdown">${subs}</div>
      </div>`;
    }
    return `<a class="nav-link${isActive ? ' active' : ''}${n.label === 'Geopolitics' ? ' nav-link-geo' : ' nav-link-energy'}" href="${href}">${n.label}</a>`;
  }).join('');

  const mobileLinks = nav.map(n => {
    const href = prefix + n.href;
    let cls = '';
    if (n.label === 'Geopolitics') cls = ' mobile-geo';
    else cls = ' mobile-energy';
    if (n.dropdown) {
      const subs = n.dropdown.map(s => `<a class="sub" href="${prefix + s.href}">${s.label}</a>`).join('');
      return `<div class="mobile-dropdown-group">
        <div class="mobile-dropdown-header">
          <a href="${href}" class="${cls}">${n.label}</a>
          <button class="mobile-dropdown-toggle" onclick="this.parentElement.parentElement.classList.toggle('open')" aria-label="Expand">${icon('chevron-down', 16)}</button>
        </div>
        <div class="mobile-dropdown-items">${subs}</div>
      </div>`;
    }
    return `<a href="${href}" class="${cls}">${n.label}</a>`;
  }).join('');

  document.getElementById('site-header').innerHTML = `
    <div class="header-inner">
      <a class="logo" href="${prefix}index.html">
        <img src="${prefix}images/logo.png" alt="EnergyPricesToday.com" class="logo-img shimmer-subtle">
      </a>
      <nav class="nav-desktop">${navLinks}</nav>
      <div class="header-actions">
        <button class="header-search-btn" onclick="toggleSearch()" aria-label="Search">${icon('search', 18)}</button>
        <button class="mobile-toggle" onclick="toggleMobileNav()" aria-label="Menu">${icon('menu', 24)}</button>
      </div>
    </div>
    <div class="market-ticker-strip" id="ticker-strip">
      <div class="ticker-scroll-area">
        <div class="ticker-track" id="ticker-track"></div>
      </div>

    </div>
    <div class="mobile-nav" id="mobile-nav">${mobileLinks}</div>
    <div class="search-overlay" id="search-overlay">
      <div class="search-overlay-inner">
        <div class="search-box">
          ${icon('search', 20)}
          <input type="text" id="search-input" placeholder="Search markets, news, and analysis..." autocomplete="off">
          <button onclick="toggleSearch()" class="search-close-btn">${icon('x', 18)}</button>
        </div>
        <div class="search-hints">
          <span class="search-hint-label">Popular:</span>
          <a href="${prefix}category/oil-prices.html" class="search-hint-tag">Oil Prices</a>
          <a href="${prefix}category/natural-gas.html" class="search-hint-tag">Natural Gas</a>
          <a href="${prefix}category/geopolitics.html" class="search-hint-tag">Geopolitics</a>
          <a href="${prefix}markets.html" class="search-hint-tag">Markets</a>
          <a href="${prefix}category/alternative-energy.html" class="search-hint-tag">Alt Energy</a>
        </div>
      </div>
    </div>
  `;

  // Scroll listener
  window.addEventListener('scroll', () => {
    document.getElementById('site-header').classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });
}

function toggleMobileNav() {
  const nav = document.getElementById('mobile-nav');
  const btn = document.querySelector('.mobile-toggle');
  const backdrop = document.getElementById('mobile-backdrop');
  const open = nav.classList.toggle('open');
  if (backdrop) backdrop.classList.toggle('open', open);
  btn.innerHTML = open ? icon('x', 24) : icon('menu', 24);
  document.body.style.overflow = open ? 'hidden' : '';
}

// Close mobile nav via backdrop or close button
document.addEventListener('click', function(e) {
  if (e.target.id === 'mobile-backdrop' || e.target.id === 'mobile-close' || e.target.closest('#mobile-close')) {
    var nav = document.getElementById('mobile-nav');
    var backdrop = document.getElementById('mobile-backdrop');
    if (nav) nav.classList.remove('open');
    if (backdrop) backdrop.classList.remove('open');
    var btn = document.querySelector('.mobile-toggle');
    if (btn) btn.innerHTML = icon('menu', 24);
    document.body.style.overflow = '';
  }
});

// ─── SEARCH OVERLAY ──────────────────────────────────────────────
function toggleSearch() {
  var overlay = document.getElementById('search-overlay');
  if (!overlay) return;
  var open = overlay.classList.toggle('open');
  if (open) {
    document.body.style.overflow = 'hidden';
    setTimeout(function() {
      var input = document.getElementById('search-input');
      if (input) input.focus();
    }, 150);
  } else {
    document.body.style.overflow = '';
  }
}

// ─── MARKET TICKER STRIP ─────────────────────────────────────────
function renderTicker() {
  var track = document.getElementById('ticker-track');
  if (!track || typeof COMMODITIES === 'undefined') return;
  var items = COMMODITIES.filter(function(c) { return c.price !== null; }).map(function(c) {
    var cls = c.change >= 0 ? 'up' : 'down';
    var arrow = c.change >= 0 ? '▲' : '▼';
    return '<span class="ticker-item">' +
      '<span class="ticker-name">' + c.name + '</span>' +
      '<span class="ticker-price">$' + c.price.toFixed(2) + '</span>' +
      '<span class="ticker-change ' + cls + '">' + arrow + ' ' + (c.change >= 0 ? '+' : '') + c.pct.toFixed(2) + '%</span>' +
    '</span>';
  }).join('<span class="ticker-sep">·</span>');
  // Triplicate for seamless continuous loop
  track.innerHTML = items + items + items;
}

// ─── NEWSLETTER SIGNUP ───────────────────────────────────────────
function initNewsletter() {
  var form = document.getElementById('newsletter-form');
  if (!form) return;
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    var wrap = document.getElementById('newsletter-wrap');
    if (wrap) {
      wrap.innerHTML = '<div style="text-align:center;padding:20px">' +
        icon('check-circle', 32) +
        '<p style="color:#22c55e;font-size:15px;font-weight:600;margin-top:12px">You\'re subscribed!</p>' +
        '<p style="color:#9ca3af;font-size:13px">We\'ll send you market updates — no spam, ever.</p></div>';
    }
  });
}

// ─── FOOTER ──────────────────────────────────────────────────────
function renderFooter() {
  const inSub = window.location.pathname.includes('/category/') || window.location.pathname.includes('/authors/') || window.location.pathname.includes('/articles/');
  const p = inSub ? '../' : '';

  document.getElementById('site-footer').innerHTML = `
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="${p}index.html"><img src="${p}images/logo.png" alt="EnergyPricesToday.com" class="footer-logo-img"></a>
          <p>Modern energy market intelligence — live pricing, analysis, and news without the clutter.</p>
        </div>
        <div class="footer-columns">
          <div>
            <div class="footer-heading">Markets</div>
            <div class="footer-links">
              <a href="${p}oil-prices.html">Oil Prices</a>
              <a href="${p}category/natural-gas.html">Natural Gas</a>
              <a href="${p}category/gas-prices.html">Gas Prices</a>
              <a href="${p}category/heating-oil.html">Heating Oil</a>
              <a href="${p}oil-futures.html">Oil Futures</a>
              <a href="${p}markets.html">All Markets</a>
            </div>
          </div>
          <div>
            <div class="footer-heading">Coverage</div>
            <div class="footer-links">
              <a href="${p}category/energy.html">Energy</a>
              <a href="${p}category/geopolitics.html">Geopolitics</a>
              <a href="${p}category/company-news.html">Company News</a>
              <a href="${p}rig-count.html">Rig Count</a>
              <a href="${p}category/alternative-energy.html">Alternative Energy</a>
              <a href="${p}category/crude-oil.html">Crude Oil</a>
            </div>
          </div>
          <div>
            <div class="footer-heading">Company</div>
            <div class="footer-links">
              <a href="${p}about.html">About Us</a>
              <a href="${p}contact.html">Contact</a>
              <a href="${p}site-news.html">Site News</a>
              <a href="${p}editorial-policy.html">Editorial Policy</a>
              <a href="${p}corrections-policy.html">Corrections Policy</a>
              <a href="${p}privacy.html">Privacy Policy</a>
              <a href="${p}disclaimer.html">Disclaimer</a>
              <a href="${p}terms.html">Terms</a>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 EnergyPricesToday.com &middot; All rights reserved &middot; Market data for informational purposes only</p>
      </div>
    </div>
  `;
}

// ─── MARKET TABLE ────────────────────────────────────────────────
function renderMarketTable(containerId, compact) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const tabs = Object.keys(FULL_PRICES);
  let activeTab = tabs[0];

  function buildTable() {
    const data = FULL_PRICES[activeTab] || [];
    const rows = (compact ? data.slice(0, 5) : data).map(c => {
      if (c.price === null || c.price === undefined) {
        return `<tr>
          <td>${c.name}</td>
          <td class="table-price" style="color:var(--text-3)">Updating\u2026</td>
          <td><span style="color:var(--text-3)">\u2014</span></td>
          <td><span style="color:var(--text-3)">\u2014</span></td>
          <td></td>
          <td class="table-unit">${c.unit}</td>
        </tr>`;
      }
      const color = c.change >= 0 ? '#22c55e' : '#ef4444';
      return `<tr>
        <td>${c.name}</td>
        <td class="table-price">$${c.price.toFixed(2)}</td>
        <td><span class="change ${c.change >= 0 ? 'up' : 'down'}">${c.change >= 0 ? '+' : ''}${c.change.toFixed(2)}</span></td>
        <td><span class="change ${c.pct >= 0 ? 'up' : 'down'}">${c.pct >= 0 ? '+' : ''}${c.pct.toFixed(2)}%</span></td>
        <td style="text-align:right">${sparkline(c.spark, color, 60, 24)}</td>
        <td class="table-unit">${c.unit}</td>
      </tr>`;
    }).join('');

    const tabsHtml = tabs.map(t =>
      `<button class="market-tab${t === activeTab ? ' active' : ''}" data-tab="${t}">${t}</button>`
    ).join('');

    container.innerHTML = `
      <div class="market-tabs">${tabsHtml}</div>
      <div class="market-table-wrap">
        <table class="market-table">
          <thead><tr>
            <th style="text-align:left">Commodity</th><th>Price</th><th>Change</th><th>% Change</th><th>Chart</th><th>Unit</th>
          </tr></thead>
          <tbody>${rows}</tbody>
        </table>
        ${compact ? '<div class="table-footer">Showing top ' + (FULL_PRICES[activeTab]||[]).slice(0,5).filter(c=>c.price!==null).length + ' — Updated ' + new Date().toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric'}) + '</div>' : ''}
      </div>
    `;

    container.querySelectorAll('.market-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        activeTab = btn.dataset.tab;
        buildTable();
      });
    });
  }

  buildTable();
}

// ─── CONTACT FORM ────────────────────────────────────────────────
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    document.getElementById('contact-form-wrap').innerHTML = `
      <div class="success-card">
        ${icon('check-circle', 40)}
        <h3>Message Sent</h3>
        <p>Thank you for reaching out. We'll get back to you shortly.</p>
      </div>
    `;
  });
}

// ─── READING PROGRESS BAR ────────────────────────────────────────
function initReadingProgress() {
  const bar = document.querySelector('.reading-progress-bar');
  if (!bar) return;
  window.addEventListener('scroll', () => {
    const h = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = h > 0 ? `${(window.scrollY / h) * 100}%` : '0%';
  }, { passive: true });
}

// ─── INIT ────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  renderHeader();
  renderFooter();
  renderTicker();
  initContactForm();
  initNewsletter();
  initReadingProgress();
});

// ─── LOAD MORE ARTICLES ──────────────────────────────────────────
var EXTRA_ARTICLES = [
  { title: "OPEC+ Considers Easing Production Cuts in Q4 2026", author: "Staff", date: "Mar 28, 2026", readTime: "5 min" },
  { title: "China's Strategic Petroleum Reserve Purchases Slow in March", author: "Staff", date: "Mar 27, 2026", readTime: "4 min" },
  { title: "U.S. Shale Operators Report Highest Well Productivity on Record", author: "Staff", date: "Mar 26, 2026", readTime: "6 min" },
  { title: "IEA Warns of Potential Supply Shortfall in Late 2026", author: "Staff", date: "Mar 25, 2026", readTime: "5 min" },
  { title: "European Refiners Boost Margins With Russian Crude Alternatives", author: "Staff", date: "Mar 24, 2026", readTime: "4 min" },
  { title: "Brazil's Pre-Salt Output Reaches 4 Million Barrels Per Day Milestone", author: "Staff", date: "Mar 23, 2026", readTime: "5 min" },
  { title: "Natural Gas Flaring Reduction Efforts Gain Momentum in Permian", author: "Staff", date: "Mar 22, 2026", readTime: "4 min" },
  { title: "India Diversifies Crude Imports Away From Middle East Dependence", author: "Staff", date: "Mar 21, 2026", readTime: "5 min" },
  { title: "Global Oil Tanker Rates Spike on Red Sea Rerouting Congestion", author: "Staff", date: "Mar 20, 2026", readTime: "4 min" },
  { title: "Electric Vehicle Sales Growth Slows in Europe But Accelerates in Asia", author: "Staff", date: "Mar 19, 2026", readTime: "6 min" },
];

function initLoadMore() {
  var btn = document.querySelector('.btn-load-more');
  if (!btn) return;
  var loaded = 0;
  var listEl = document.getElementById('article-list');
  
  btn.addEventListener('click', function() {
    if (!listEl) return;
    var batch = EXTRA_ARTICLES.slice(loaded, loaded + 4);
    if (batch.length === 0) {
      btn.textContent = 'All articles loaded';
      btn.style.opacity = '0.5';
      btn.style.pointerEvents = 'none';
      return;
    }
    batch.forEach(function(a) {
      var div = document.createElement('a');
      div.href = articleUrl(a.title);
      div.className = 'article-list-item';
      div.innerHTML = '<div class="article-list-thumb" style="background:linear-gradient(135deg,rgba(61,143,212,0.08),rgba(212,122,12,0.05))"></div>' +
        '<div><h3>' + a.title + '</h3>' +
        '<div class="article-meta-sm"><span>' + a.author + '</span><span>' + a.date + '</span><span>' + a.readTime + '</span></div></div>';
      listEl.appendChild(div);
    });
    loaded += batch.length;
    if (loaded >= EXTRA_ARTICLES.length) {
      btn.textContent = 'All articles loaded';
      btn.style.opacity = '0.5';
      btn.style.pointerEvents = 'none';
    }
  });
}

document.addEventListener('DOMContentLoaded', function() {
  initLoadMore();
});
