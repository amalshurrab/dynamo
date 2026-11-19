# Domain move pipeline and the mail + DNS sequence

Source: Mathkor move kattebseo.com → mathkor.com (2026-11-18), handoff B3, B7, B11, C3 and
`mathkor-launch-readiness.md` sections 1, 5–8, 17 (2026-11-19). last_verified: 2026-11-19

## Domain move
1. **Redirects first, one hop, paths kept:** `http://`, `www.`, old domain and old `www.` each → `https://NEW/<path>`
   directly. Old slugs that changed (e.g. a transliterated Arabic slug) → the new slug in the same hop. Verify with
   `curl -sIL` and count the hops.
2. **App URL and generated files:** `APP_URL=https://NEW`; `robots.txt` (`Sitemap:` line) and `llms.txt` built from it;
   clear config and cache.
3. **Stored content root cause:** find where the old host was baked into stored HTML. In Mathkor the pipeline used
   `url()`, which takes the incoming request's host, so webhook-produced articles carried the old domain (248
   occurrences). Fix the writer (a `SiteUrl` helper from config), then backfill with a command (`<app>:replace-domain`,
   dry-run first, counts per table, legacy hosts list).
4. **Endpoints that do not follow redirects:** payment webhooks POST; a webhook still pointing at the old host breaks
   silently. Update it in the provider dashboard.
5. **Search engines:** Search Console domain property for the new host, submit the sitemap, Change of address from the
   old property (needs the 301s live), URL inspection on the top pages; Bing import + Site Move; OAuth consent screen
   domains and redirect URIs; cookie and cache prefixes (changing the session cookie name logs everyone out once: ask).
6. **Schema:** `Organization.name` = new, `alternateName` = Latin, former name noted, `sameAs` to the social URLs.

## Mail and DNS (in this order)
1. **Mailbox:** forwarding is not enough (cannot reply from `info@`). Google Workspace or Zoho; create `info@`, aliases
   `hello@ support@ billing@ privacy@ security@ dmarc@ no-reply@`; set the provider's MX, remove registrar forwarding MX.
2. **Transactional sender:** Resend/Postmark/SES; verify the domain (adds DKIM); `MAIL_FROM_ADDRESS=no-reply@NEW`,
   `MAIL_FROM_NAME` = brand, global reply-to `support@NEW` (mailables' own reply-to still wins).
3. **SPF:** exactly one TXT record including every sender: `v=spf1 include:_spf.google.com include:<provider> ~all`.
4. **DKIM:** per provider from its panel. 5. **DMARC:** `_dmarc TXT "v=DMARC1; p=none; rua=mailto:dmarc@NEW"` for two
   weeks, then `p=quarantine`.
6. **Verify:** `dig MX/TXT`; a mail from `info@` lands in a Gmail inbox with SPF/DKIM/DMARC PASS in "Show original";
   registration triggers a verify-email from `no-reply@`; the contact form notification reaches `info@`;
   mail-tester.com ≥ 9/10.

## Operations hand-steps (owner), dependency order
Workspace → transactional provider → DNS → mail-tester → Search Console → Bing → OAuth consent → payment dashboard
(public details, descriptor, webhook URL, one test purchase per plan) → ad pixels and Clarity → GA4 stream URL, key
events, unwanted referrals → Turnstile keys → final `.env` → `config:clear route:clear view:clear cache:clear
queue:restart`.
