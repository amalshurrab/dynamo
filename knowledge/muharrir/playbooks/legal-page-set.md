# Legal page set for a Saudi-market SaaS (privacy · terms · refund), AR + EN

Source: Mathkor legal content in `MATHKOR-SITE-DEV-HANDOFF.md` Part C1 (2026-11-19), written under the Personal Data
Protection Law (PDPL, SDAIA) and the E-Commerce Law and its implementing regulations. last_verified: 2026-11-19

## Before writing
Take from the venture profile: operator name (AR + Latin), legal status (registered company with CR, national address,
VAT → show them; an app not yet registered → omit them, never invent), payment provider(s), contact mailboxes
(privacy@, billing@, support@), data actually collected (account, connected sites, Search Console if linked, payment via
the provider, analytics pixels), whether customer content trains models (usually: no), governing law and venue.

## Privacy policy (14 sections)
Who we are · Data we collect · Why we use it · Your content and AI (ownership stays with the customer; not used for
model training; third-party model providers process it to produce the output) · Cookies and measurement tools (name
GA4, pixels, Clarity; consent where required) · Who we share with (hosting, payment provider, model providers, email) ·
Transfers outside the Kingdom (PDPL conditions) · Retention · Security · Your rights (access, correction, deletion,
withdraw consent, complain to SDAIA) · Children (not for under 18) · Links to other sites · Changes · Contact.

## Terms of use (19 sections)
Definitions · The service · Eligibility and account · Plans, trial and payment (trial wording from the profile; renewal;
price changes with notice; provider named) · Cancellation and refunds (points to the refund policy) · Ownership and
licence (articles belong to the customer once produced) · AI-generated content (review before publishing; no guarantee
of accuracy) · Acceptable use · Connected sites and third-party services · Results (no ranking or mention guarantee) ·
Availability · Suspension and termination · Disclaimer · Limitation of liability · Indemnity · Changes · Governing law
and disputes (Saudi law, competent courts in Riyadh unless the profile says otherwise) · General · Contact.

## Cancellation and refund policy (7 sections, table-based)
Trial plan (no fees) · Cancelling (any time; stays active to period end; no fee) · When a refund applies as a **table**:
first paid subscription within 7 days and nothing produced → full; within 7 days with articles produced → minus the
produced articles at plan price; renewal charged and unused, requested within 48 h → full; renewal after use or after
48 h → none; add-on packs unused within 7 days → full, partly used → unused part; duplicate or wrong charge → full
excess; outage over 72 h by our fault → extra days, credit or pro-rata refund. Define "produced" (completed and
available, published or not, because production has a real cost) · How to request (from the account email, invoice,
reply within 2 business days, refund to the same method via the provider in 5–14 business days) · Not covered (breach,
no ranking/mention achieved, late requests except what the law requires) · Statutory rights preserved · Contact.

## Delivery
Six files `legal/{ar,en}/{privacy,terms,refund}.md`, each with `آخر تحديث / Last updated`, cross-links between the three,
a decisions list for the decision maker (windows, venue, operator facts), and a hand-off to bannaa: routes `/privacy
/terms /refund` (+ `/en/...`), footer links, register consent checkbox «بإنشاء الحساب أنت توافق على شروط الاستخدام
وسياسة الخصوصية», sitemap entries, server-side titles. Why P0: payment gateways, Google OAuth consent screen, Meta and
LinkedIn ads and lead forms, and company buyers all require them.
