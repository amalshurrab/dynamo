# Priority rules, AI-crawler visibility, deliverability and legal pages

Source: Mathkor audit 2026-11-18 and its developer handoff; Google Search Central and Lighthouse docs; dmarc.org; Saudi
PDPL and E-Commerce Law summaries (checked 2026-11-19). last_verified: 2026-11-19

## P0 / P1 / P2
- **P0 (before the first visitor):** no mailbox behind the published address; legal pages 404 (payment providers,
  Google OAuth consent, Meta and LinkedIn ads all require them); plan choice lost between pricing and signup; banned or
  old-name copy on the home page; robots/llms/sitemap pointing at an old domain; old-domain links inside content; site not
  in Search Console or Bing; no conversion tracking; main pages empty for crawlers.
- **P1 (within a week):** mobile performance below 80, no long cache on static assets, no WebP/srcset, dead links,
  images without alt, duplicate language paths without hreflang, shared titles across pages, no HSTS, no bot protection,
  multi-hop redirects, a contact form with required fields that scare leads, no WhatsApp or booking entry.
- **P2 (continuous):** duplicate articles to merge, new articles, per-segment landing pages, a lead-magnet tool, CSP and
  security.txt, cookie naming.

## AI-crawler visibility
- GPTBot, ClaudeBot, PerplexityBot and Google-Extended fetch HTML and do not execute JavaScript. A client-rendered page
  arrives as a shell; the text sits in a JSON attribute (`data-page`) that is not treated as content.
- Test: `curl -s URL | grep -oE '<h1[^>]*>[^<]+'`. Empty on a page that shows a headline in the browser = CSR.
- Fix lane: server-side rendering for every public page (maher), kept running by a supervisor; components touching
  `window` wrapped in mount hooks.
- `llms.txt` lists the pages an assistant should read; every URL must be on the live domain and allowed in robots.txt.
- Expired AI-grounding links (`vertexaisearch.cloud.google.com/grounding-api-redirect/...`) inside articles die within
  weeks; the content pipeline must resolve them to the final URL before publishing.

## Mail deliverability minimum
One MX provider with a real mailbox (forwarding alone cannot reply); exactly one SPF record including every sender;
DKIM from each provider; DMARC starting at `p=none` with `rua=`, moved to `p=quarantine` after two clean weeks;
transactional mail from `no-reply@<domain>` with the brand as the display name; aliases hello@, support@, billing@. Pass
criterion: mail-tester 9/10 or more, and a test signup email landing in a Gmail inbox.

## Legal and trust pages (KSA)
Privacy policy, terms of use, cancellation and refund policy, in Arabic and English, linked in the footer, with a consent
line at signup. Must state: content ownership, no training on customer data, data collected (site, Search Console if
connected, payment), cancellation at any time, refund rule, governing law. If the venture is an app and not a registered
company, say so rather than inventing a CR, VAT number or address.

## Measurement minimum before paid traffic
GA4 with conversion events (signup, plan selected, checkout started, payment), Meta Pixel, LinkedIn Insight Tag,
Clarity for session replay, UTM captured and stored on the account at first touch.
