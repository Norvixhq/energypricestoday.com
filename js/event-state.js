/* ═══════════════════════════════════════════════════════════════════
 * event-state.js — Phase 2.4 client-side renderer.
 *
 * Fetches data/state/events.json (produced by resolve_event_state.py)
 * and binds values into DOM elements carrying [data-event-bind].
 *
 * This is the single read-path for every state-dependent module across
 * the site. Nothing that bears on current event state should render from
 * any other source.
 *
 * Binding syntax:
 *   <element data-event-bind="<event_key>.<field>[|<transform>]"
 *            data-event-fallback="<literal fallback text>">
 *     <fallback content>
 *   </element>
 *
 * Available transforms:
 *   lowercase         — lowercase the string
 *   sentence          — "HELLO world" → "Hello world"
 *   date_short        — ISO date → "Apr 21" / "Jan 3"
 *   risk_premium_band — global risk level → "$15-25/bbl" band estimate
 *   truncate:120      — trim to N chars with ellipsis
 *
 * Fallback behavior (in order):
 *   1. If fetch fails or returns non-JSON        → keep DOM untouched
 *   2. If events.json is >12 hours old           → keep DOM untouched
 *   3. If specific event_key missing             → substitute data-event-fallback
 *   4. If field missing on event                 → substitute data-event-fallback
 *   5. If transform throws                       → substitute data-event-fallback
 *
 * The user never sees a broken, empty, or "undefined" element.
 * ═══════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // Figure out the URL prefix based on where the page lives.
  // Works from root, /category/, /articles/, /authors/.
  function resolvePrefix() {
    var path = window.location.pathname;
    if (path.indexOf('/category/') !== -1) return '../';
    if (path.indexOf('/articles/') !== -1) return '../';
    if (path.indexOf('/authors/') !== -1)  return '../';
    return '';
  }

  var STATE_URL = resolvePrefix() + 'data/state/events.json';
  var STALENESS_THRESHOLD_HOURS = 12;

  // ─── Transforms ───────────────────────────────────────────────
  var TRANSFORMS = {
    lowercase: function (v) {
      return (v == null) ? '' : String(v).toLowerCase();
    },
    sentence: function (v) {
      if (v == null) return '';
      var s = String(v).toLowerCase();
      return s.charAt(0).toUpperCase() + s.slice(1);
    },
    date_short: function (v) {
      if (!v) return '';
      try {
        // Accept YYYY-MM-DD or full ISO
        var s = String(v);
        var dt = new Date(s.length === 10 ? s + 'T00:00:00Z' : s);
        if (isNaN(dt.getTime())) return '';
        return dt.toLocaleDateString('en-US', {
          month: 'short',
          day: 'numeric',
          timeZone: 'UTC',
        });
      } catch (e) {
        return '';
      }
    },
    risk_premium_band: function (v) {
      // Global risk level → Brent risk premium band estimate (industry rule of thumb).
      var band = {
        CRITICAL: '$20-30/bbl',
        HIGH:     '$15-25/bbl',
        ELEVATED: '$8-15/bbl',
        LOW:      '$0-5/bbl',
      };
      return band[String(v).toUpperCase()] || '';
    },
    truncate: function (v, arg) {
      if (v == null) return '';
      var n = parseInt(arg, 10) || 120;
      var s = String(v);
      return s.length <= n ? s : s.slice(0, n - 1).trimEnd() + '…';
    },
  };

  function applyTransform(value, transformSpec) {
    if (!transformSpec) return value;
    // Support transform:arg syntax (e.g. "truncate:120")
    var parts = transformSpec.split(':');
    var name = parts[0];
    var arg = parts[1];
    var fn = TRANSFORMS[name];
    if (!fn) return value;
    try {
      return fn(value, arg);
    } catch (e) {
      console.warn('[event-state] transform error', name, e);
      return null;
    }
  }

  // Resolve "hormuz_status.status|lowercase" against events object.
  // Returns either the transformed value or null (caller uses fallback).
  function resolveBinding(events, expr) {
    if (!expr || !events) return null;
    // Split off transform pipe
    var pipeIdx = expr.indexOf('|');
    var path, transform;
    if (pipeIdx > 0) {
      path = expr.slice(0, pipeIdx).trim();
      transform = expr.slice(pipeIdx + 1).trim();
    } else {
      path = expr.trim();
      transform = null;
    }
    // Walk path segments
    var segs = path.split('.');
    if (segs.length < 2) return null;
    var event = events[segs[0]];
    if (!event) return null;
    var value = event;
    for (var i = 1; i < segs.length; i++) {
      if (value == null || typeof value !== 'object') return null;
      value = value[segs[i]];
    }
    if (value == null || value === '') return null;
    if (transform) {
      var out = applyTransform(value, transform);
      return (out == null || out === '') ? null : out;
    }
    return value;
  }

  // Apply bindings to all elements under `root` that have [data-event-bind].
  function applyBindings(events, root) {
    root = root || document;
    var nodes = root.querySelectorAll('[data-event-bind]');
    var bound = 0;
    var fellback = 0;

    for (var i = 0; i < nodes.length; i++) {
      var node = nodes[i];
      var expr = node.getAttribute('data-event-bind');
      var fallback = node.getAttribute('data-event-fallback');

      try {
        var resolved = resolveBinding(events, expr);
        if (resolved == null) {
          // Field missing or transform failed — substitute fallback
          if (fallback != null) {
            node.textContent = fallback;
            fellback++;
          }
          continue;
        }

        // Binding target:
        //   - by default → node.textContent
        //   - if data-event-attr="href" → set that attribute
        //   - if data-event-attr="style.color" → set style property
        var attrTarget = node.getAttribute('data-event-attr');
        if (attrTarget) {
          if (attrTarget.indexOf('style.') === 0) {
            node.style[attrTarget.slice(6)] = String(resolved);
          } else {
            node.setAttribute(attrTarget, String(resolved));
          }
        } else {
          node.textContent = String(resolved);
        }
        bound++;
      } catch (e) {
        console.warn('[event-state] binding failed:', expr, e);
        if (fallback != null) {
          try { node.textContent = fallback; } catch (_) {}
          fellback++;
        }
      }
    }

    if (bound > 0 || fellback > 0) {
      console.debug('[event-state] bound=' + bound + ' fallback=' + fellback);
    }
    // Mark document so validator/nightly audit knows state version applied
    if (events && events.version != null) {
      document.documentElement.setAttribute('data-event-state-version', String(events.version));
    }
    if (events && events.generated_at) {
      document.documentElement.setAttribute('data-event-state-ts', events.generated_at);
    }
  }

  // Staleness guard — don't apply bindings if the state is too old.
  function stateIsFresh(events) {
    if (!events || !events.generated_at) return false;
    try {
      var then = new Date(events.generated_at);
      if (isNaN(then.getTime())) return false;
      var ageHours = (Date.now() - then.getTime()) / 3.6e6;
      return ageHours < STALENESS_THRESHOLD_HOURS;
    } catch (e) {
      return false;
    }
  }

  // ─── Main ─────────────────────────────────────────────────────
  function init() {
    // Only run if the page actually has bindings — avoids fetch on pages
    // that don't need state (articles, trust pages, etc.).
    if (!document.querySelector('[data-event-bind]')) {
      return;
    }

    fetch(STATE_URL, { cache: 'no-store' })
      .then(function (resp) {
        if (!resp.ok) throw new Error('events.json fetch ' + resp.status);
        return resp.json();
      })
      .then(function (payload) {
        var events = (payload && payload.events) ? payload.events : null;
        if (!events) {
          console.debug('[event-state] no events object; fallbacks retained');
          return;
        }
        if (!stateIsFresh(payload)) {
          console.debug('[event-state] state stale (>12h); fallbacks retained');
          return;
        }
        applyBindings(events, document);
      })
      .catch(function (err) {
        // Silent fail — fallbacks already rendered in HTML
        console.debug('[event-state] fetch failed:', err && err.message);
      });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose for manual refresh / debugging
  window.EventState = {
    apply: applyBindings,
    refresh: init,
    url: STATE_URL,
  };
})();
