# Experience log · Mathkor (reference implementation)

Source: audit of mathkor.com on 2026-11-18 (evening) and the developer handoff `website/MATHKOR-SITE-DEV-HANDOFF.md`.

- [VENTURE-CONVENTION] 2026-11-18 · Denominators: 46 sitemap pages, 174 links, 238 images, 3 Lighthouse runs (home,
  pricing, GEO article), 135 approved strings. Results: 112/135 copy applied (83%), 25 dead links (5 of them expired AI
  grounding links), 110 images without alt, 248 old-domain references inside articles, blog SEO 100, accessibility 98–100,
  home FCP 4.8s, article LCP 12.4s, 2.1 MB, 77 assets without cache headers.
- [VENTURE-CONVENTION] 2026-11-18 · The live site still ran a build from before the rebrand merge, so several copy
  violations were already fixed on `main`. Rule: compare live against the repo's default branch before filing copy items;
  "deploy main" can be step 0.
- [VENTURE-CONVENTION] 2026-11-18 · Root cause of the old domain inside articles: `url()` used the incoming webhook host.
  Rule: look for the generator, not only the symptom.
- [VENTURE-CONVENTION] 2026-11-18 · `?plan=` was ignored on register ("you will start on the free plan"), losing a paying
  customer's decision. Rule: always walk pricing → signup → checkout with the plan parameter.
- [VENTURE-CONVENTION] 2026-11-18 · Copy violations found live: «ليست مجرد… بل», «بلا بطاقة دفع», «مستخدمي كاتب». The
  banned list came from the venture profile; the audit only reports violations, muharrir rewrites.
- [VENTURE-CONVENTION] 2026-11-18 · Owners in the report: Nasr (code and server), Amal (marketing and accounts), Alaa
  (decisions: case-study wording, official WhatsApp number). Deadlines: P0 before 24 Nov, P1 before 30 Nov.
- [VENTURE-CONVENTION] 2026-11-18 · The report replaced an earlier task list (`mathkor-dev-tasks-2026-11-19.md`) and said
  so in its header, to avoid two live lists.
