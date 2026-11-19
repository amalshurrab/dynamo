# Platform fit by buyer, and budget ranges that are honest

Source: practitioner ranges for MENA/KSA from public benchmark round-ups (WordStream, Statista and regional agency
reports read 2026-11-19) and the platforms' own minimums; all figures are `[estimate]` ranges, not promises, and must be
re-verified against the venture's first two weeks of data. last_verified: 2026-11-19

## Where the buyer is
| Buyer | First platform | Second | Avoid at launch |
|---|---|---|---|
| Marketing / SEO agency owner, B2B decision maker | LinkedIn (job title + company size) | Google Search (intent keywords) | TikTok, Snapchat |
| Saudi e-commerce store owner | Meta (Instagram interests, Salla/Zid lookalikes) | Google Search | LinkedIn (low volume) |
| Service company with a blog | Google Search | LinkedIn | Snapchat |
| Consumer app | Meta, Snapchat, TikTok | Google App campaigns | LinkedIn |

## Budget ranges, KSA, B2B SaaS, Arabic creatives `[estimate]`
| Platform | CPM (SAR) | CPC (SAR) | CPL, soft lead (SAR) | Note |
|---|---|---|---|---|
| Meta (IG+FB) | 15–45 | 1.5–5 | 25–90 | learning phase needs ~50 results/week per ad set |
| LinkedIn | 90–220 | 12–35 | 120–400 | minimum ~SAR 40/day per campaign; small audiences cost more |
| Google Search | n/a | 4–20 | 60–250 | depends on keyword intent; Arabic long-tail cheaper |
| X | 10–30 | 1–4 | weak for B2B | brand awareness only |
| TikTok / Snapchat | 8–25 | 0.8–3 | consumer only | not for B2B SaaS at launch |

Rules of thumb: a monthly budget under SAR 3,000 buys one platform and one objective; under SAR 1,500 buys a learning
test, not results. State this to the owner before they decide. VAT (15% in KSA) is added by the platform on top.

## Expected results format
Always: `impressions ≈ budget ÷ CPM × 1000` and `results ≈ budget ÷ CPL`, both as low–high ranges using the table,
then the assumptions line: "assumes the landing page converts 2–4% of clicks, Arabic creatives, KSA only, 4 weeks."

## Tracking stack
Meta Pixel + Conversions API (server-side, via the backend) · LinkedIn Insight Tag + conversion rules · Google tag with
conversion actions · GA4 events mirrored (sign_up, begin_checkout, purchase, generate_lead) · UTM naming:
`utm_source=<platform>&utm_medium=paid&utm_campaign=<campaign>&utm_content=<creative>`.
