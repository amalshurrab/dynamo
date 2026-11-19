# Experience log · Mathkor (reference implementation)

Source: Mathkor site handoff Part F, the developer's 26 commits (2026-11-19) and the independent check, Kateb-SEO
workspace.

- [VENTURE-CONVENTION] 2026-11-18 · Read the repo at a pinned sha (29b7617) and compare with the live site first: the
  live build predated the rebrand merge, so many "copy bugs" were already fixed on main. Step 0 became "deploy main".
- [VENTURE-CONVENTION] 2026-11-18 · Strings live in three places: `resources/js/lang/{ar,en}/*.ts`, the `plans.features`
  JSON in the database (admin `/admin/plans`), and `ui_translations` for EN plan features. A copy fix can be a data fix.
- [VENTURE-CONVENTION] 2026-11-19 · Database overrides in `/admin/texts` win over lang files; six old hero/testimonial
  overrides kept the old copy alive after deploy. Hidden-sections settings hid `final-cta`, `sticky-cta`, `beyond`,
  `search-surfaces`. Both are admin-panel fixes, flagged to the owner, not code.
- [VENTURE-CONVENTION] 2026-11-19 · `?plan=` already had an "intended plan" mechanism; the handoff added only a read-only
  peek, the banner, consent (`terms_accepted_at`) and auto-start checkout. Do not rebuild what exists.
- [VENTURE-CONVENTION] 2026-11-19 · First-touch attribution stored on the user (`2026_11_19_000002_add_signup_fields_to_users`),
  copied on both email and Google registration.
- [VENTURE-CONVENTION] 2026-11-19 · Env-driven features (WhatsApp, booking, pixels, Turnstile) shipped hidden; the
  independent check found them invisible because C4 env values were never set. Say this explicitly in the handoff summary.
- [VENTURE-CONVENTION] 2026-11-19 · Twelve consolidated ASSUMPTIONS at the end of Part F (DB not reachable, lang key
  names, middleware chain, queue worker) saved the developer from blind pastes.
- [VENTURE-CONVENTION] 2026-11-19 · The developer applies one section per commit with the id in the message
  (`F3: footer…`); the check later maps commits to sections. Keep ids stable.
