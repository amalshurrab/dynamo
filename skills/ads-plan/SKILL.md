---
name: ads-plan
description: Plan, approve, set up and report paid campaigns for a venture (Meta, LinkedIn, Google, X, TikTok, Snapchat) with realistic budgets and expected ranges. Use whenever mulin, or any Dynamo agent, needs a campaign plan document, a per-platform access checklist, a tracking prerequisite check, or the weekly ads performance report. Spend never moves without the owner's written yes.
---

# ads-plan

## 1. Campaign plan document (`marketing/ads/<campaign>/plan.md`)
```
# <venture> · <campaign name> · <month>
Objective: <awareness | traffic | leads | conversions>  → KPI: <metric> target range <low–high> [estimate]
Audience: <who> · size read from platform: <n> · exclusions: <customers, staff>
Platform mix: <platform %> … (why each, one line)
Budget: SAR <monthly> (+15% VAT) = SAR <daily> split <per platform/ad set> · flight <from–to>
Creatives (from lawwan / rawi): <n> variants per ad set · sizes <1080×1080, 1080×1350, 1200×628…> · text limits <…>
Tracking prerequisites: pixel/tag ✓/✗ · events ✓/✗ · UTMs <pattern> · landing page mudaqqiq P0 clear ✓/✗
Expected results [estimate]: impressions <low–high> · clicks <low–high> · results <low–high> · cost/result <low–high>
Assumptions: <CPM/CPL ranges used and their basis, landing conversion %, market, language, duration>
Stop rule: <condition that pauses the campaign without waiting for the weekly call>
Approval: owner <name> · date · amount SAR <total>   ← nothing launches without this line filled by the owner
```
Platform mix guide: B2B decision makers → LinkedIn first, Google Search second; Saudi store owners → Meta first; consumer
→ Meta/Snapchat/TikTok. X for awareness only. Ranges: see `mulin-knowledge/frameworks/platform-fit-and-benchmarks.md`.

## 2. Access checklist (roles, never credentials)
| Platform | Role for the reviewer | Also needed |
|---|---|---|
| Meta | Ad account *Advertiser*, Page *Content*, Pixel shared | Business Portfolio, payment by owner, domain verified |
| LinkedIn | Campaign Manager *Campaign Manager*, Page *Content admin* | Insight Tag on the domain |
| Google Ads | *Standard* user or MCC link | conversions in the same account, billing by owner |
| TikTok / Snapchat / X | Ads manager *Operator* | pixel/tag installed |
Record granted roles and dates in the venture profile §5. If a platform tool is available in the session (Meta Ads
tools, ad studios), it may read and prepare; spend still needs the owner's yes.

## 3. Set-up and verification
Create everything **paused**. Read back and fill: campaign · ad set · ad · objective · audience size · placements ·
daily budget · schedule · creative file · URL+UTM · event · status. Fix mismatches, screenshot the summary, then ask for
the go date.

## 4. Weekly performance report (formal MSA, numbers first)
```
الأسبوع <n> · <from–to> · الإنفاق: <SAR actual> من <SAR planned>
| الحملة/المجموعة | الظهور | النقرات | CTR | CPC | النتائج | تكلفة النتيجة | مقابل الخطة |
التغيير المقترح لهذا الأسبوع: <one change> · الأثر المتوقع: <range> · يحتاج موافقة: نعم/لا
الإجمالي منذ البداية: <spend / results / cost per result> · سقف الميزانية المتبقي: <SAR>
```
Hand the table to mudawwin for the Thursday report.

## Gates
- No tracking for the bought result → no launch. No approval line → no launch. A spend change → a new yes.
- Expected results are ranges with assumptions; never a single promised figure.
- Payment methods and sign-ins are the owner's; the agent works inside the opened session only.
