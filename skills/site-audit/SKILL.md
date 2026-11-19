---
name: site-audit
description: Full launch-readiness audit of a venture's public website, in a fixed order, with a number and evidence per finding and a P0/P1/P2 report with owners and deadlines. Use when a Dynamo agent (mudaqqiq, or maher/bannaa re-verifying) must audit or re-audit a site before traffic is sent to it.
---

# site-audit

Inputs from the venture profile: domain `D`, old domain `OLD` (if any), approved-copy file, banned words, owners, campaign
date, expected tags. Work in the scratchpad; save every raw output. Every finding = count + evidence + owner + priority.

## 0. Inventory (denominators first)
```zsh
curl -s https://D/sitemap.xml | grep -oE '<loc>[^<]+' | sed 's/<loc>//' > pages.txt; wc -l pages.txt
for u in $(cat pages.txt); do curl -s "$u" > "p_$(echo $u | md5).html"; done
grep -ohE 'href="[^"#]+"' p_*.html | sort -u | wc -l          # links
grep -ohE '<img[^>]+>' p_*.html | wc -l                       # images
```
Record: pages, links, images. Missing from the sitemap but linked (e.g. /contact)? Note it.

## 1. Crawl, redirects, old domain
- `curl -sI http://D`, `https://www.D`, `https://OLD/<path>`: expect one hop to `https://D/<same path>` (301).
- `curl -s https://D/robots.txt`, `/llms.txt`, `/sitemap.xml`: count `OLD` occurrences; target 0.
- `grep -c OLD p_*.html | awk -F: '{s+=$2} END{print s}'`: old-domain references inside content.
- Per-page `<title>` and `<meta name=description>`: count duplicates (`grep -h '<title>' p_*.html | sort | uniq -c`).
- Language duplicates (`/en/...`): canonical, hreflang or noindex present?

## 2. Links: dead and expired
For every unique absolute link: `curl -s -o /dev/null -w '%{http_code} %{redirect_url}\n' -L --max-time 15 URL`.
Classify: 404/410 dead · 5xx server · timeout · 200 but expired pattern (grounding-api-redirect, utm-laden trackers,
shorteners). Table: URL, status, page(s) found on, class, replacement if known.

## 3. Images
`grep -ohE '<img[^>]+>' p_*.html | grep -vc 'alt="[^"]'` = images without alt. Also: count without width/height,
formats (`.png|.jpg` vs `.webp`), and the 10 heaviest by `curl -sI | grep -i content-length`.

## 4. Mobile Lighthouse (3 pages: home, pricing, one article)
```zsh
npx lighthouse https://D --form-factor=mobile --screenEmulation.mobile --output=json --output-path=lh-home.json --quiet --chrome-flags="--headless"
jq '.categories|map_values(.score*100)' lh-home.json; jq '.audits["first-contentful-paint"].displayValue, .audits["largest-contentful-paint"].displayValue, .audits["total-byte-weight"].displayValue, .audits["uses-long-cache-ttl"].details.items|length' lh-home.json
```
Report FCP, LCP, weight, count of assets without long cache, Performance / SEO / Accessibility scores.

## 5. DNS and mail
`dig +short MX D` · `dig +short TXT D | grep -i spf` (exactly one) · `dig +short TXT _dmarc.D` · DKIM selector if known.
Is there a real mailbox behind info@ (forwarding-only MX such as `eforward*.registrar-servers.com` = no)? Transactional
sender domain in the app's mail config (ask bannaa/maher or check a signup email's From).

## 6. SSL and security headers
`echo | openssl s_client -connect D:443 -servername D 2>/dev/null | openssl x509 -noout -issuer -dates`
`curl -sI https://D | grep -iE 'strict-transport-security|content-security-policy|x-frame-options|x-content-type|referrer-policy|set-cookie'`
Note HSTS presence, cookie name leaking the framework, bot protection on forms (Turnstile/reCAPTCHA markup).

## 7. Crawler view without JavaScript
For each public page: `curl -s URL | grep -oE '<h1[^>]*>[^<]+|<p[^>]*>[^<]{40,}' | head -3`. Empty while the browser
shows content = client-side rendered = invisible to GPTBot/ClaudeBot/PerplexityBot. Also check JSON-LD presence
(`grep -c 'application/ld+json'`). List pages per state: SSR / CSR / partial.

## 8. Copy compliance
Load the approved-copy file (numbered strings). For each string, grep the live HTML (normalise whitespace and
diacritics). Output: applied N / total M (%), missing list, and a violations table for banned words and old names:
`grep -ohE 'ابدأ مجانًا|بلا بطاقة|بدون بطاقة|ليست? مجرد|<old name>' p_*.html | sort | uniq -c`.

## 9. Live conversion tests (browser pane opened by the reviewer; never type a password or real card)
- Pricing → "choose plan" → signup: is the plan carried (`?plan=`) and shown? After signup, does checkout open?
- Checkout in the provider's test mode only, or stop at the checkout screen: brand name, descriptor, currency.
- Contact form: required fields, delivery address, confirmation; WhatsApp button and booking link present and working.
- Signup email: sender address and domain, lands in inbox or spam (mail-tester score if a test address is available).

## 10. Tracking actually installed
In the browser: Network filter `collect|tr?id=|px.ads.linkedin|clarity`; or grep the HTML for `G-`, `fbq(`, `_linkedin_partner_id`,
`clarity`. Trigger signup and plan selection and record which events fire. Check UTM persistence (land with
`?utm_source=test`, sign up, confirm it is stored, via the developer if needed).

## 11. Acquisition system (marketer's side)
Mailbox and aliases, lead log, post-signup message sequence, outreach script per segment, free-audit template, weekly
numbers sheet, Search Console and Bing verified, bio links with UTM.

## 12. Report
Write `marketing/website/<venture>-launch-readiness.md` using `${CLAUDE_PLUGIN_ROOT}/knowledge/mudaqqiq/playbooks/report-template.md`:
scope with counts, summary table (✅/⚠️/❌), P0 (before campaign date) / P1 (+1 week) / P2, each item with current
state, required change, owner, and a `للتحقق` command; copy-compliance table; final `- [ ]` checklist. Hand code items to
bannaa/maher, copy to muharrir, bugs to fahis, numbers to mudawwin. State explicitly what was not tested.

## Re-audit
Same denominators, same order, same commands. Report deltas (25 → 3 dead links) and close items only with the
verification output pasted.
