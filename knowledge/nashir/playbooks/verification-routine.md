# Verification routine and publish-day checklist

Source: Mathkor scheduling 2026-11-18/19 (48 IG+FB post rows, 48 story rows, 24 LinkedIn rows verified).
last_verified: 2026-11-19

## Queue table schema (one row per date × platform × type)
| date | time (local) | platform | type (post/story/carousel/li) | file | WxH | caption state (as approved / date-adjusted) | status (scheduled/published) | url | notes |

## After scheduling
1. Open Business Suite → Planner (month view) and the Scheduled list; open LinkedIn page → Posts → Scheduled.
2. Count rows per platform and compare with the plan: IG posts = days, FB posts = days, stories = days, LI = days.
3. Duplicates: sort by date; any date with two rows of the same type on one platform is a stop condition.
4. Spot-open 3 rows per platform: media count (carousel = all slides, in order), size (1080×1350 post, 1080×1920
   story), caption's first line and relative words, time and time zone.
5. Save the verified table in `marketing/social/<campaign>/publishing-log.md` with the verification date.

## Publish day
- First-comment link (not schedulable) within 10 minutes of publishing.
- Poll stickers on stories (Instagram app only) and LinkedIn polls (create natively, not as an image).
- Confirm the post is visible on the public profile; record the URL.
- Re-share to the FB page or personal profiles only if the plan says so.

## When the reviewer reports a quality problem
Check the rendition the platform serves (open the image in a new tab: width served, blur). If the file is right and the
rendition is wrong, switch to the size the platform shows at full quality (LinkedIn: portrait 1080×1350) and re-create
the affected rows; log the count changed.
