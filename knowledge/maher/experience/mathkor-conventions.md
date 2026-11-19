# Experience log · Mathkor (reference implementation)

Source: Mathkor domain move (2026-11-18), site handoff Part B and C (2026-11-19), the independent check the same day,
Kateb-SEO workspace.

- [VENTURE-CONVENTION] 2026-11-18 · The blog had SSR (Blade copy) and scored SEO 100, but home, pricing, how-it-works,
  case studies and contact were client-rendered and empty for AI crawlers. SSR was "silently off": inertia-laravel
  enables it by default, but no bundle existed. Nothing blocked it; it was never set up.
- [VENTURE-CONVENTION] 2026-11-18 · Root cause of 248 old-domain links inside articles: the pipeline used `url()`, which
  takes the incoming webhook's host. Fixed with a config-based `SiteUrl` helper plus a `mathkor:replace-domain` backfill.
- [VENTURE-CONVENTION] 2026-11-18 · Redirect chains: `http://www`, `https://www.kattebseo.com/...` and the old slug
  `ahmy-seo-fy-almkalat` took two hops. Required: one hop to the final URL, paths kept.
- [VENTURE-CONVENTION] 2026-11-18 · Mail: MX pointed at Namecheap forwarding (`eforward*`), no mailbox, no DKIM/DMARC.
  Decision path: Google Workspace (or Zoho free), aliases, Resend for app mail, SPF merged, DMARC `p=none` first.
- [VENTURE-CONVENTION] 2026-11-19 · Independent check: SSR bundle on main (`efaa2ab`) but no `<h1>` in any raw public
  page: the renderer process was never started on the server. DNS unchanged. `/build/assets` still without
  `Cache-Control`. Lesson: separate "code on main" from "live", and list operations steps per owner.
- [VENTURE-CONVENTION] 2026-11-19 · Keep `SESSION_COOKIE=kateb-seo-session` and `CACHE_PREFIX` unless the owner accepts a
  one-time logout of every user; changing them is a destructive step, asked explicitly.
- [VENTURE-CONVENTION] 2026-11-19 · Five grounding links were opaque `vertexaisearch` redirect tokens: match on anchor
  text, not URL. `dl.acm.org`, `nelc.gov.sa`, `dga.gov.sa` return 403 to bots only: leave them.
- [VENTURE-CONVENTION] 2026-11-19 · `/en/blog/*` were 18 Arabic duplicates declared `lang="en"` with self-canonicals:
  `noindex,follow` + canonical to the Arabic URL, out of the sitemap, hreflang only when a real translation exists.
