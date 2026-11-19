---
name: site-copy-map
description: Produce a venture's website copy as a numbered, developer-ready file (section → string id → text → location → status), audit the live site against it with a "% applied + violations" report that names the cause of each miss, structure pages and articles so AI answer engines can quote them (keyword in H1, direct answer first, FAQ + Schema, internal links), and write the AR+EN legal page set (privacy, terms, refund with a case table) under Saudi PDPL and E-Commerce Law. Use when muharrir (or any Dynamo agent) writes or checks site copy, blog templates, meta, or legal pages.
---

# site-copy-map

Read `TEAM.md` and the venture profile first (name, bans, trial wording, plans, legal status, law, mailboxes).

## 1. The numbered copy file (`marketing/website/<venture>-website-copy.md`)
```
# نص موقع <venture>
## قواعد عامة            ← ≤ 8 lines: rename map (+ what is NOT the product name), banned phrases to delete
                           everywhere (AR+EN), digits 0-9, logo per background, colours, 301 rule, Organization
                           schema (name / alternateName / former name), "unlisted text stays, rules apply"
## SEO وبيانات المشاركة   ← <title>, meta description 120–160, og:title, og:description, og:site_name
## <section in site order>  ← one block per section (header, hero, proof, demo, articles, features, audiences,
                           how-it-works, pricing, FAQ, testimonials, final CTA, footer, blog template)
**<label = id>:**        ← e.g. **العنوان الرئيسي H1:** ≙ hero.h1 ; text on the next line
> يحذف من هذا القسم: …   ← old strings to remove
| id | text | lives in | status |   ← add after the live check: APPLIED · TODO · VIOLATION · ALREADY ON MAIN
```
Per-page table: URL · title (≤ 60) · description (120–160). Write EN as transcreation. Count strings and sections.

## 2. Live-versus-approved audit
```zsh
curl -s "$URL" | sed 's/<[^>]*>/ /g' > crawler.txt            # what AI crawlers get
"$CH" --headless=new --dump-dom "$URL" | sed 's/<[^>]*>/ /g' > browser.txt   # what people get
grep -c "<approved string>" browser.txt                       # per string → found / missing
grep -nE "ابدأ مجان|بلا بطاقة|بدون بطاقة|<old name>" browser.txt crawler.txt   # violations
```
- `% applied` = found ÷ approved. List misses with the exact live text, and violations with URL + element.
- **Cause per miss** (seen): stale build (fixed on main, not deployed) · database/CMS override beating lang files
  (admin "texts" panel) · hidden-sections setting · plan features stored as JSON · EN translation table missing.
- Owner per cause: copy → muharrir · frontend file → bannaa · SSR/meta/redirect → maher · dashboard → venture owner.
- Report shape: table (Where · Live text · Required · Owner) → `% applied` line → P0 list. If `crawler.txt` is near
  empty for a public page, that is P0 → maher (AI crawlers do not run JavaScript).

## 3. GEO/AEO structure (pages and articles)
Title ≤ 60 with keyword · description 120–160 · one H1 · the first 40 words answer the question · question-shaped H2s
answered in their first sentence · a named source per claim (statistics and quotations raise AI citation) · FAQ of 5–10
buyer questions with `FAQPage` schema · `BlogPosting` + `BreadcrumbList` on articles, `Organization` (name,
alternateName, sameAs, email) site-wide · 2–3 internal links with descriptive anchors · Arabic `alt` on every image ·
one topic per URL. Blog review = technical (server HTML, schema, H1, slugs) · template strings old → new · titles per
slug · duplicates / linking / off-audience · disclaimer wording («كُتب هذا المقال بـ<brand>: بحث، وكتابة، ومراجعة
مصادر، وربط داخلي.», never "shown raw as produced") · 5 next articles mirroring pre-purchase questions.

## 4. Legal page set (AR + EN, 6 files `legal/{ar,en}/{privacy,terms,refund}.md`)
- Facts from the profile only: operator name; registered company → CR, address, VAT; app not registered → omit, never
  invent; payment provider(s); mailboxes `privacy@ billing@ support@`; data actually collected; customer content not used
  for training; governing law and venue (Saudi: PDPL under SDAIA, E-Commerce Law, courts in Riyadh).
- Privacy 14 sections (who we are · data · purposes · your content and AI · cookies and pixels · sharing · transfers
  outside the Kingdom · retention · security · rights incl. complaint to SDAIA · children · links · changes · contact).
- Terms 19 sections (definitions · service · eligibility · plans, trial and payment · cancellation/refunds → policy ·
  ownership and licence · AI-generated content · acceptable use · connected sites · results: no ranking/mention
  guarantee · availability · suspension · disclaimer · liability · indemnity · changes · governing law · general · contact).
- Refund 7 sections with a **case table** (first subscription ≤ 7 days nothing produced → full; with articles → minus
  produced at plan price; renewal unused ≤ 48 h → full; after use/48 h → none; add-on unused ≤ 7 days → full, partly → unused
  part; duplicate charge → full excess; outage > 72 h our fault → days/credit/pro-rata), define "produced", request
  steps (account email, invoice, reply ≤ 2 business days, same method 5–14 business days), not covered, statutory rights.
- Same "last updated" date and contacts across the three; cross-links; a decisions list for the decision maker
  (windows, venue, operator facts); hand-off to bannaa (routes, footer, consent checkbox, sitemap, server titles).
- Mark: `[VIOLATION]` on any banned phrase quoted from the old text; `[DECISION]` on lines needing approval;
  `[COUNSEL]` where exposure is material. This is a compliant draft, not legal advice.

## 5. Deliver
Copy file (+ HTML/PDF for management when asked) · blog review · legal set · live-compliance report · *What changed ·
What was verified · What is open*. Record each reviewer correction as a dated rule in the venture profile.
