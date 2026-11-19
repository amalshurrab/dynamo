# Venture profile · مذكور (Mathkor) — reference implementation

<!-- Filled 2026-11-19 from the Mathkor launch work. This is the worked example the Dynamo agents learn the format from.
     The live copy for the Mathkor venture should sit in the kateb-seo repo at marketing/venture-profile.md. -->

## 1. Identity · الهوية
- **Product name:** مذكور / Mathkor (renamed from «كاتب SEO» on 2026-11-17 because of the Katteb conflict)
- **Domain(s):** mathkor.com (live since 2026-11-18; kattebseo.com 301-redirects with paths kept)
- **One-line promise:** مقالات عربية يكتبها الذكاء الاصطناعي بحيث تظهر في Google وفي إجابات ChatGPT وGemini وClaude وPerplexity.
- **Tagline:** «خلّ الذكاء الاصطناعي يذكرك»
- **Hook line:** «اللي ما ينذكر… ما ينشاف»
- **Category label:** منصة مقالات SEO + GEO بالعربية (GEO = الظهور في إجابات أدوات الذكاء الاصطناعي)
- **Stage:** launch (Flow OS Idea stage; exit rules due ~2026-11-23)
- **Owner / developer:** Nasrallah (nasrallash-farra) · **Marketer / reviewer:** Amal Shurrab · **Decision maker:** Alaa Saqer

## 2. Visual system · النظام البصري
- **Colours:** ink/plum #1F0738 · violet #6A45DC (gradient #9980FE→#5629CE only in the logo mark) · mint #4FDDA6 · off-white #F7F5FC · card border #E6E0F2
- **Fonts:** Cairo (Arabic, 800/900 for headlines) · Inter (Latin)
- **Logo files:** `/Users/amal/Documents/one-studio/Mathkor-brand-logo/` (12 SVG + 22 PNG); social copies in `social/week1/mathkor-logo-color*.svg`, `mathkor-icon-*.svg`
- **Design style:** B2B SaaS for companies. Per post: one Cairo 800 headline, ONE clean product-UI hero (ChatGPT window, article page, KPI card, URL bar) with 24px radius and thin border, ONE mint focus point, small logo bottom-left. Each post has its own composition and one big iconic object; never one template across a week. Grid: violet/white checkerboard; triptychs stay in one row.
- **Never:** gradients on backgrounds, glow, sparkles, orbit swooshes, paper grain, hand-drawn marks, top day/category labels, text-heavy layouts, empty "too plain" layouts.

## 3. Voice · الصوت
- **Formal surfaces:** formal MSA, agency-report tone, numbers first.
- **Social register:** light Saudi («وين اسمك؟», «بكرة», «خلّ»).
- **Bilingual surfaces:** LinkedIn About (AR then EN), website (AR primary, /en secondary, noindex until parity).
- **Always name:** every AI tool: ChatGPT, Gemini, Claude, Perplexity, Google AI. Never only ChatGPT.
- **Banned:** «ابدأ مجانًا», «بلا بطاقة» / «بدون بطاقة» (cheapens the brand); «ليس X بل Y»; «مستخدمي كاتب»; slogans/metaphors («بوابة», «رحلة», «ثورة»); emojis in formal surfaces; naming a target audience in the LinkedIn About.
- **Preferred wording:** the $0 plan is «جرّب أول مقال» / «باقة تجربة: أول مقال قبل الدفع».

## 4. Market · السوق
- **Target segments (test running, pick one in week 3):** 1) Saudi e-commerce stores 2) marketing/SEO agencies 3) service & B2B companies with blogs. 5 interviews + 30 free audits per segment.
- **Buyer and user:** store/agency owner or marketing lead; user = whoever runs the blog.
- **Competitors / comparables:** Katteb (Egypt, Flat6Labs), Jasper, Writesonic, Surfer; Arabic agencies.
- **Evidence we may cite:** Gartner: search-engine volume to drop 25% by 2026 due to AI chatbots; Princeton GEO study: up to ~40% visibility gain from statistics and quotations. Our own 957 articles count (dated 2026-11-12).
- **Evidence we must NOT use:** admin-panel users/sites (friends, studio projects, tests) as market demand; medical as "the market".

## 5. Channels and accounts · القنوات
| Channel | Handle / URL | Owner | Posting time (KSA) | Notes |
|---|---|---|---|---|
| Instagram | instagram.com/mathkor.ai | Amal | 20:00 post, 20:30 story | via Meta Business Suite (business 1875324500568457) |
| Facebook | facebook.com/profile.php?id=61596929990491 («Mathkor مذكور») | Amal | same as IG | cross-posted from Business Suite |
| LinkedIn | linkedin.com/company/mathkor.ai (id 145453834) | Amal | 10:00 until 27 Nov, then alternating 19:30 / 10:00 | single images published as 1080×1350 (landscape blurred in feed) |
| X | not reserved (unknown) | — | — | |
| Website / blog | mathkor.com, /blog (18 articles) | Nasrallah | — | GA4 G-MHH5HHN4SG only |
| Email | info@mathkor.com (not yet created) | Nasrallah | — | no DMARC yet |

## 6. Offer · العرض
- **Plans:** $0 trial (first article before paying), paid plans via Stripe only.
- **Trial wording:** «جرّب أول مقال».
- **Legal status:** an app, not a registered company (no CR, national address or VAT number).
- **Applicable law:** Saudi PDPL and E-Commerce Law for privacy, terms and refund pages.

## 7. Tech · التقنية
- **Repo:** onestudio-co/kateb-seo (read access; main @29b7617 on 2026-11-18) · **Stack:** Laravel 13 + Inertia 3 + React 19 + Stripe · **Hosting:** nginx, Let's Encrypt (valid to 2027-02-16)
- **Analytics present:** GA4 only. No Meta Pixel, LinkedIn Insight, Clarity or conversion events.
- **Known constraints:** public pages (home, pricing, how-it-works, case studies, contact) are client-rendered → empty for AI crawlers; blog has SSR. Live site ran a pre-rebrand build on 2026-11-18 (deploy main first). `url()` takes the webhook host → old domain inside articles.

## 8. Flow OS · فلو أو إس
- **Venture slug:** `lead-ai` · **Portfolio:** One Studio
- **Daily updates:** venture `onestudio`, formal MSA checklist starting `@alaa-saqer`, tags #daily-update #mathkor
- **Open issues:** #227 problem memo (Nasrallah), #228 blog SSR (due 2026-11-30, high), #229 apply Mathkor identity to site (due 2026-11-30)

## 9. Rules learned in this venture · قواعد تعلّمناها هنا
- 2026-11-17: never write «ابدأ مجانًا» or «بلا بطاقة».
- 2026-11-17: name all AI tools, not only ChatGPT.
- 2026-11-18: social = one clever visual idea per post, minimal words, generous white space, calm grid.
- 2026-11-18: style is B2B SaaS, not editorial/freelancer; one product-UI hero + one mint focus point.
- 2026-11-18: one caption per post for ALL platforms, no per-platform split.
- 2026-11-18: no gradients, glows, sparkles or decorative swooshes anywhere.
- 2026-11-19: publish LinkedIn single images as 1080×1350; the landscape 2400×1256 blurs in the feed.
- 2026-11-19: decks for the team are animated, one idea per slide, real screenshots, no "next steps" slide.
