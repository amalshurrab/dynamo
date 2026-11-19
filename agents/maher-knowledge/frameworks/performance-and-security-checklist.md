# Performance and security checklist with targets

Source: Mathkor Lighthouse mobile run (2026-11-18: home performance 0 with no measurable LCP, FCP 4.8 s, 2,363 DOM
nodes; pricing 73, LCP 4.7 s; GEO article 62, LCP 12.4 s, 2.1 MB) and handoff B7, B8, B12; web.dev Core Web Vitals
thresholds. last_verified: 2026-11-19

## Targets
Mobile performance ≥ 80 on home, pricing and one article; LCP < 2.5 s; FCP < 1.8 s; DOM < 1,500 nodes; built assets
cached one year; HTML never cached stale.

## Checklist
| Area | Check | Fix |
|---|---|---|
| Asset cache | `curl -sI /build/assets/app-*.js` has `Cache-Control` | nginx `location ~* ^/(build|images)/ { expires 1y; add_header Cache-Control "public, immutable"; }` |
| Hero LCP | H1/subtitle start at `opacity:0` (unmeasurable LCP; SSR ships it hidden) | slide-only motion above the fold; fade only below |
| Images | JPG heroes ~300 KB, no `srcset`, no width/height, 110 of 238 without alt | WebP variants `{base}.w{480,768,1200}.webp`, `srcset`, dimensions, `loading="lazy"` below the fold, `fetchpriority="high"` on the hero, alt backfill (fix `?? ''` bugs that pass empty alts) |
| JavaScript | 130–150 KB unused; 13 eager landing sections | route-level chunks; lazy-load the interactive demo and marquees after first paint |
| DOM | demo renders every locale sample invisibly | build on demand |
| Redirect hops | `curl -sIL http://www.DOMAIN` shows 2+ hops | one-hop map at the edge |
| HSTS | header missing | `Strict-Transport-Security: max-age=31536000; includeSubDomains` |
| Headers | nosniff, referrer-policy, X-Frame-Options | keep; CSP optional later; `/.well-known/security.txt` with `security@` |
| Bots on forms | no challenge on register/contact | Cloudflare Turnstile, server-verified, env-driven |
| Links | expiring grounding redirects and 404s inside articles | resolve at generation time (link guard), one-off fix command with an anchor-text map for opaque redirect URLs; leave bot-only 403 hosts alone |
| Certificates | renewal for the new domain | confirm certbot timer covers the new host |

## Method
Lighthouse mobile on three pages before and after, same device profile; keep the JSON; report a table with the delta and
the cause per change. `[estimate]` for Lighthouse "savings" until re-measured.
