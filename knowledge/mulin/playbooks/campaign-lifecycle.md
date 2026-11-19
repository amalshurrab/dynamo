# Campaign lifecycle: readiness → two plans → approval → set-up → verify → weekly loop

Source: Dynamo team conventions (TEAM.md §0, §1, §3a, §8a) and nashir's verification discipline; platform mechanics
from Meta Business Help, LinkedIn Campaign Manager Help and Google Ads Help (read 2026-11-19). last_verified: 2026-11-19

## 0. Readiness (no money yet)
| Check | Pass condition | Owner |
|---|---|---|
| Pixel / tag installed | Meta Pixel + CAPI, LinkedIn Insight Tag, Google tag fire on all public pages | bannaa |
| Conversion events | sign-up, trial start, purchase, contact as named events; test fires visible in each platform | bannaa / maher |
| UTM discipline | every ad URL carries source/medium/campaign/content; GA4 shows them | mulin |
| Landing page | mudaqqiq P0 list is empty for the destination page; mobile LCP acceptable | mudaqqiq |
| Legal | privacy page live (platform policy requires it), terms, refund | muharrir |
| Accounts | ad account, page, Business Portfolio, LinkedIn page admin, Google Ads account exist | owner |
| Payment | added by the owner, with a monthly cap set in the platform | owner |

## 1. Two plans, side by side
Each plan is one page: objective, platform(s), audiences, monthly budget and daily split, flight dates, creatives
needed, expected ranges `[estimate]` with basis, stop rule, what it bets on. Typical pair for a B2B SaaS launch:
- **A. One platform, deep:** 100% on the platform where the buyer is (LinkedIn for agencies/B2B leads; Meta for store
  owners), two audiences × two creatives, four weeks.
- **B. Test and learn:** 60/40 across two platforms for two weeks, then consolidate on the winner for two weeks.
The owner picks. Record the choice and the date in the venture profile.

## 2. The approved plan document
Saved at `marketing/ads/<campaign>/plan.md`. Fields: campaign name, objective, KPI and target range, platform,
audiences (with sizes read from the platform), placements, daily budget, total cap, dates, creatives (file names from
lawwan, copy from rawi, text limits), tracking (events, UTMs), expected results (range + assumptions), stop rule (e.g.
"pause if CPL > 2× the upper estimate after 1,000 impressions and 7 days"), approval line: owner name, date, amount.

## 3. Access checklist (roles only, never credentials)
- **Meta:** Business Portfolio → add the reviewer as *Advertiser* on the ad account and *Content* on the Page; Pixel
  shared to the ad account; payment method added by the owner.
- **LinkedIn:** Campaign Manager account → reviewer as *Campaign Manager*; Page → *Content admin*; Insight Tag domain
  verified.
- **Google Ads:** owner's account linked under the studio MCC or reviewer added as *Standard* user; conversions set in
  the same account; billing by the owner.
- **TikTok / Snapchat / X:** Business Center or Ads Manager member with *Operator*/*Campaign manager* role.
Write the granted roles with the date in the venture profile §5.

## 4. Set-up and verification
Set up inside the session the owner opened. Everything paused. Then read back and fill the set-up table: campaign, ad
set, ad, objective, audience size, placements, daily budget, schedule, creative file, destination URL with UTM,
tracking event, status. Any mismatch with the plan is fixed before the go date. Screenshot the summary for the record.

## 5. Weekly loop (agreed day, same hour)
1. Pull spend, impressions, clicks, CTR, CPC, results, cost per result per ad set and ad.
2. Compare to the plan ranges. Mark each line: on track / watch / stop rule hit.
3. Decide **one** change (pause the worst creative, shift budget to the best ad set, new creative request).
4. Propose it with the expected effect; apply only after the owner's yes. Spend changes always need a yes.
5. Report (weekly format in `ads-plan` skill) and hand numbers to mudawwin.
