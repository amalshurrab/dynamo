# Experience log · Mathkor (reference implementation)

Source: reviewer (Amal Shurrab) and owner (Nasrallah) feedback and site checks, 2026-11-17 → 2026-11-19, Kateb-SEO
workspace.

- [VENTURE-CONVENTION] 2026-11-17 · Site copy is delivered as one file, section by section in the site's order, with
  general rules on top; the developer applies it without questions. 14 sections, 144 strings.
- [VENTURE-CONVENTION] 2026-11-17 · «ابدأ مجانًا», «بلا بطاقة دفع», «تسجيل فوري بدون بطاقة», «ابدأ الآن واختر الدفع لاحقًا»
  are deleted everywhere, AR and EN. The $0 plan is «باقة التجربة: أول مقال قبل الدفع».
- [VENTURE-CONVENTION] 2026-11-17 · Hero H1 is the tagline «خلّ الذكاء الاصطناعي يذكرك.», eyebrow is the list of engines
  «Google · ChatGPT · Gemini · Claude · Perplexity». The old «ليست مجرد أداة… بل منظومة» was rejected as AI-sounding.
- [VENTURE-CONVENTION] 2026-11-17 · Rename sweep: «كاتب SEO» and «كاتب» as the product name → «مذكور»; «كاتب AI» in the
  FAQ and «كاتب» meaning "the writer" inside articles are NOT the product name and stay.
- [VENTURE-CONVENTION] 2026-11-17 · Blog disclaimer became «كُتب هذا المقال بمذكور: بحث، وكتابة، ومراجعة مصادر، وربط داخلي.»;
  the internal "entry keyword" line is hidden from readers; "تحليل:" became «آخر تحديث:».
- [VENTURE-CONVENTION] 2026-11-18 · Live audit: 112 of 135 strings applied (83%). Causes found later: a pre-rebrand build
  still live, then database overrides in `/admin/texts` winning over the new lang files, and hidden sections in the admin
  panel. Always find the cause, not only the miss.
- [VENTURE-CONVENTION] 2026-11-19 · Legal pages written for an app that is not a registered company: no CR, national
  address or VAT; operator named «مذكور»; Stripe only; disputes in Riyadh; refund policy as a case table.
- [VENTURE-CONVENTION] 2026-11-18 · Case-study and testimonial wording needs Alaa's decision before publishing; the
  home page's "7 articles" count was stale (18 exist).
