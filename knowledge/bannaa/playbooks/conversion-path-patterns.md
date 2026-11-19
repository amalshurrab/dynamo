# Conversion-path patterns for a SaaS marketing site

Source: Mathkor handoff Part F (F3–F8, 2026-11-19) and its independent check `handoff-check-2026-11-19.md`; Laravel
+ Inertia + React stack, patterns stated stack-neutral. last_verified: 2026-11-19

## Footer (F3 pattern)
One brand config (`brand.json` or equivalent) holds `email`, `social: {instagram, linkedin, facebook, x}`, legal links.
The footer renders what exists; the `Organization` JSON-LD gets `email` and `sameAs` from the same config, so the site
and the schema never disagree. Env fallback for envs without the config file. Verified social URLs come from nashir.

## Legal pages system (F4 pattern)
`content/legal/{ar,en}/{privacy,terms,refund}.md` → one controller that reads the file for the current locale →
one page component rendering markdown with the site layout → routes `/privacy /terms /refund` and `/en/...` → sitemap
entries for both locales → server-side `<title>` per page (lang file `legal.php`) → footer links. Why P0: payment
gateways, Google OAuth consent screen, Meta/LinkedIn ads, and company buyers require them.

## Register → plan → checkout (F5 pattern)
- Do not rebuild what exists: find the "intended plan" mechanism first (session, signed param).
- `?plan=<slug>` shows a banner with the plan name and price on the register page («اخترت باقة النمو: 29 USD شهريًا…»).
- After email verification, auto-start checkout when the plan came from pricing (skip the extra click); the flash must
  survive onboarding redirects (check the middleware chain).
- Consent checkbox «أوافق على شروط الاستخدام وسياسة الخصوصية» validated server-side; store `terms_accepted_at`.
- Niche/segment order on the form follows the venture's target segments (profile section 4).
- **First-touch attribution:** on first visit, store `utm_*`, `gclid/fbclid/li_fat_id`, landing path and referrer in a
  cookie; on register (email or Google), copy them onto the user row (`signup_*` columns, one migration). Marketing can
  then answer "where did paying users come from".

## Contact form (F6 pattern)
Fields that qualify a lead: name, email, WhatsApp (optional), website, business type (segments from the profile),
message. Migration extends the table; a notification mails the venture inbox (queue `mail` must have a worker); success
copy without banned phrases; an admin list with the new columns. Verify: submit → row → email in the inbox.

## WhatsApp and booking (F7 pattern)
Env `WHATSAPP_NUMBER` (international, no +) and `BOOKING_URL`; a floating button and a pricing-page booking button
render only when set; respect the sticky mobile CTA height. Verify: empty env → nothing rendered; set → `wa.me` link.

## Post-deploy check (what the independent check found)
Code live ≠ behaviour live: database text overrides (`/admin/texts`) beat lang files; hidden-section settings hide the
new CTA; env-driven features stay invisible until C4 values exist; SSR bundle on main but the process not running.
Always check from outside (curl, dump-dom, network tab) and name the cause per gap.
