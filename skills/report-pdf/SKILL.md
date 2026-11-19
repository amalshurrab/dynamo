---
name: report-pdf
description: Build management reports, one-page CEO summaries and team decks as branded RTL HTML and export them to PDF with headless Chrome at fixed page sizes; includes the slide-screenshot binding method for vw-based decks and the RTL safety rules. Use when a Dynamo agent (mudawwin, or any agent delivering a PDF) must produce a report, summary or deck PDF.
---

# report-pdf

## 1. Detailed management report (A4 portrait or 1600×1060 landscape)
Structure: cover (logo, title, date, one scope line; no "prepared by/for" line) → summary page (KPI tiles + status table)
→ one page per theme (numbers, one real screenshot with caption, files, verification) → open items table (item, owner,
date) → footer on every page (venture, date, page). Formal MSA, numbers first, venture colours and fonts.

HTML skeleton (A4):
```html
<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800;900&family=Inter:wght@700;900&display=swap" rel="stylesheet">
<style>
@page{size:A4;margin:0} *{box-sizing:border-box;margin:0;padding:0}
html,body{direction:rtl;text-align:right;font-family:Cairo;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.pg{width:210mm;height:297mm;padding:18mm 17mm 16mm;page-break-after:always;position:relative;overflow:hidden}
.pg:last-child{page-break-after:auto}
.k .v{font:900 26pt/1 Inter;direction:ltr;text-align:right}   /* numbers LTR inside RTL */
table{width:100%;border-collapse:collapse} td,th{text-align:right;vertical-align:top}
</style></head><body>…</body></html>
```
Export:
```zsh
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CH" --headless=new --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf="<venture>-report-<YYYY-MM-DD>.pdf" "file://$PWD/report.html"
```
Check: page count, fonts rendered (not fallback), images present, no page overflow (`overflow:hidden` hides it: inspect).

## 2. One-page CEO summary
Same tokens, one `.pg`: logo, title, date, 6–10 short outcome lines, 2–3 open decisions with owner. No technical detail,
no paths, no KPI tiles that need explaining. Export the same way; 1 page.

## 3. Team deck (HTML slides, often `vw`-based and animated)
Chrome print breaks `vw` layouts. Do not print. Instead:
1. Make a copy of the deck that hides `.nav` and `.count` (or any chrome) and disables auto-advance.
2. Screenshot every slide:
   ```zsh
   for n in {1..N}; do "$CH" --headless=new --hide-scrollbars --force-device-scale-factor=2 --window-size=1600,900 \
     --virtual-time-budget=6000 --screenshot="slides/$n.png" "file://$PWD/deck-print.html#$n"; done
   ```
   For animated scenes, screenshot the final state (add `?final=1` handling in the copy that jumps to the end state).
3. Bind: `bind.html` with `@page{size:1600px 900px;margin:0}` and one `<img>` per page sized 1600×900 →
   `--print-to-pdf="<venture>-deck.pdf"`. Page count = N.

## 4. RTL safety (applies to every HTML export and every published Artifact)
- A wrapper may drop `dir="rtl"` from `<html>`: set `direction:rtl;text-align:right` on `html, body` and the stage in CSS,
  and set `document.documentElement.dir='rtl'` in JS too.
- Wrap mixed-direction tokens ("60+", "1080×1350", "#228") in `<bdi dir="ltr">`; right-align numeric tiles.
- Test inside a plain LTR wrapper page before publishing.
- Never attach «و» to a Latin word; restructure the sentence.

## 5. Delivery
File names ASCII and dated: `<venture>-report-<YYYY-MM-DD>.pdf`, `<venture>-summary-<YYYY-MM-DD>.pdf`,
`<venture>-deck-<YYYY-MM-DD>.pdf`. Keep the HTML source next to the PDF in `marketing/reports/<date>/`. Report page count
and anything not verified (e.g. a screenshot taken mid-animation).
