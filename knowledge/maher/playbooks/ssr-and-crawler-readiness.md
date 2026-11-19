# SSR and crawler readiness for public pages

Source: Mathkor handoff B1, B2, B4, B5, B6 (2026-11-19) and `handoff-check-2026-11-19.md`; Inertia SSR docs; Google
Search Central on JavaScript rendering. last_verified: 2026-11-19

## Why (marketing framing)
Google renders JavaScript; ChatGPT, Claude and Perplexity crawlers mostly do not. A client-rendered page reaches them as
a title plus an empty `<div id="app">` with the text inside a JSON `data-page` attribute. When someone asks "what is X,
how much does it cost", the engine has nothing to quote. For a product that promises AI visibility this is a P0 defect.

## Diagnose
```zsh
for p in / /pricing /how-it-works /contact /en; do
  printf "%-16s " $p; curl -s https://DOMAIN$p | sed -n '/<div id="app"/,$p' | sed 's/<[^>]*>//g' | wc -w; done
curl -s https://DOMAIN/ | grep -c '<h1'          # expect 1
curl -s https://DOMAIN/robots.txt; curl -s https://DOMAIN/llms.txt | grep -c OLDDOMAIN   # expect 0
```
A page with ~0 words is client-rendered.

## Fix (Inertia pattern; Next/Nuxt have the same shape)
1. Add the SSR entry (`resources/js/ssr.tsx`): same providers as the client app (i18n, query client), title rule kept in
   sync, no DOM reads. Add the `ssr` input to the bundler and a build script.
2. Public routes only: exclude dashboards and auth pages (`Inertia::disableSsr()` / per-route flag). Blog pages that
   already have a Blade/HTML copy keep it.
3. Run the renderer persistently: a self-restarting loop in the boot script, or a supervisor/systemd program. When it is
   down the app falls back to client rendering (`throw_on_error=false`), so the site never breaks. Restart it after each
   build.
4. Guard components that read `window`/`document` during render (`typeof window !== 'undefined'`, or move to effects).
   Watch the log for `SsrRenderFailed`.
5. Per-page server-side `<title>` and description (120–160 chars) from one `PublicPageMeta` map, de-duplicated with the
   client title rule; `/contact` and legal pages in the sitemap.
6. Secondary locale without real translations: `noindex,follow`, canonical to the primary URL, `hreflang` only where both
   versions exist, removed from the sitemap.
7. `robots.txt` and `llms.txt` generated from the app URL, never hard-coded; `llms.txt` lists only crawlable URLs.

## Verify
Word counts in the hundreds per public page; `<h1>` = 1; dashboard returns 302 with no SSR attempt; renderer health
endpoint OK; titles differ per page; the secondary-locale duplicates carry `noindex` + canonical. The independent check
found the bundle on main but the process not started: "code on main" is not "live", so verify from outside after deploy.
