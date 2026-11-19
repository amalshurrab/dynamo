---
name: publish-schedule
description: Publish and schedule approved social content on Instagram + Facebook (Meta Business Suite) and LinkedIn company pages, in the venture's time zone, with the browser upload method that works, calendar-adjusted captions, and a row-by-row verification. Use when a Dynamo agent (nashir) has approved files and captions to post or schedule, or a queue to audit.
---

# publish-schedule

Preconditions: the reviewer said yes on every file + caption; the reviewer opened Business Suite and the LinkedIn page
admin in the browser (Claude in Chrome). You never type passwords or codes. If a login screen appears, stop and ask.

## 1. Plan table first
One row per date × platform × type: date, local time, platform, type, file path, WxH, caption (date-adjusted), notes.
- Times in the venture's time zone (profile). Default pattern: feed post at HH:00, its story at HH:30, LinkedIn at the
  profile's time. One feed post per day.
- Calendar words: a caption written as "tomorrow/yesterday" relative to another post gets «بكرة»/«أمس»/the date fixed to
  the scheduled day. Log every change for rawi.
- Links: Instagram link goes in bio or first comment (publish-day task); LinkedIn link in the first comment.
- Sizes: IG/FB post 1080×1350, story 1080×1920, LinkedIn single image 1080×1350 (landscape blurs), carousel slides all
  1080×1350 in order.
- Not schedulable → publish-day list: first comments, poll stickers (IG app), LinkedIn polls (native post type).

## 2. Meta Business Suite (IG + FB)
1. Planner → Create post. Select both the Instagram account and the Facebook page.
2. Attach media. The file input is hidden; with Claude in Chrome use `file_upload` after hooking the input:
   ```js
   const i=[...document.querySelectorAll('input[type=file]')].pop(); i.style.display='block'; i.removeAttribute('hidden'); i.id='dyn-upload';
   ```
   then `file_upload` on `#dyn-upload` (for a carousel, select all slides in order in one upload, 2–10 images).
3. Caption: click the text box, then `document.execCommand('insertText', false, CAPTION)` so Arabic RTL and line breaks
   are kept (typing character by character breaks RTL; pasting may drop line breaks).
4. Schedule → set date and time → Schedule. Confirm the toast/"Scheduled" state before the next row.
5. Stories: Create story → attach the 1080×1920 file → schedule at HH:30 of the same day (Business Suite schedules
   stories; stickers are app-only).
6. Repeat per row. Every 10 rows, open the Scheduled list and reconcile counts.

## 3. LinkedIn company page
1. Admin view → Start a post → attach the 1080×1350 image (or all carousel slides as a multi-image post, or a PDF as a
   document post) → caption via `execCommand('insertText')` → clock icon → date/time (page time zone) → Schedule.
2. Polls: create as a native poll post; the image version goes to IG/FB only.
3. Open Posts → Scheduled and reconcile after each batch of 5.

## 4. Verify (mandatory, after scheduling)
- Rows per platform = days planned; stories = days; no date with two rows of one type on one platform.
- Spot-open 3 rows per platform: media count, size, caption first line and calendar words, time.
- Save `marketing/social/<campaign>/publishing-log.md`: the verified table + verification timestamp + publish-day list.

## 5. Publish day
First-comment links within 10 minutes; stickers/polls natively; confirm visibility; record URLs in the log.

## Known edges
- Business Portfolio limit on a personal account: create the page from the profile, then add it to an existing team
  portfolio and connect Instagram there.
- A session expiring mid-queue: stop, ask the reviewer to sign in, re-verify the last 3 rows before continuing.
- Highlights: publish the slides as stories in group order; the reviewer pins them in the app (covers 1080×1920, the
  centre square shows).
- Never delete or move an existing row without a fresh yes that names the row.
