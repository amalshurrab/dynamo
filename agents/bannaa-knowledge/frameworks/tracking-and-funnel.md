# Tracking stack and funnel event table

Source: Mathkor handoff F8 and C3.8–11 (2026-11-19); GA4 key events and unwanted-referrals documentation (Google);
Meta Pixel, LinkedIn Insight Tag and Microsoft Clarity setup docs. last_verified: 2026-11-19

## Stack
- **GA4** (`G-…`): already present on most sites; make the stream URL the new domain; mark key events; add
  `checkout.stripe.com` (or the payment host) to unwanted referrals so purchases are not attributed to the gateway.
- **Meta Pixel** (`META_PIXEL_ID`), **LinkedIn Insight Tag** (`LINKEDIN_PARTNER_ID`, conversion ids per event),
  **Microsoft Clarity** (`CLARITY_PROJECT_ID`). All env-driven; the layout bootstraps them only when set; page views fire
  on client-side navigation (Inertia/Next router events), not only on first load.
- One `track(event, props)` helper fans out to all four; server-side aliases map existing backend events to the same
  names. Consent gating for ad pixels is a product/legal decision, flagged, not silently decided in code.

## Funnel events (name → fires where → GA4 key event)
| Event | Where | Key event |
|---|---|---|
| `analyze_site` | hero/CTA "analyze my site" submit | yes |
| `sign_up` | account created (email or Google) | yes |
| `generate_lead` | contact form stored | yes |
| `begin_checkout` | checkout session created | yes |
| `purchase` | payment webhook marks plan active (server) | yes |
| `first_article_published` | pipeline publishes the first article (server) | optional |
| `upgrade_completed` | plan upgrade webhook (server) | optional |

## Verify
`fbq`, `_linkedin_partner_id`/`snap.licdn`, `clarity.ms` present in the HTML only when ids are set; devtools network
shows each pixel's request on page view and on `sign_up`; GA4 DebugView lists the events; LinkedIn conversion ids
mapped per event. Dashboards (pixel creation, domain verification, OAuth consent, Stripe public details) are hand steps
for the owner, listed in order of dependency.
