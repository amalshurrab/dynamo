---
name: social-render
description: Export social designs from a parameterised HTML source at exact pixel sizes with headless Chrome, build the Instagram grid preview and the design+caption PDF, and zip the deliverable. Use whenever a Dynamo agent (lawwan, naqqash, mudawwin) needs PNG/PDF exports of an HTML design.
---

# social-render

Turn `<campaign>.html?p=N&f=post|story|li[&s=K]` into review-ready files.

## 1. Export PNGs
```zsh
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
render() { # render <p> <f> <W> <H> <out>
  "$CH" --headless=new --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=6000 \
    --window-size=$3,$4 --screenshot="$5" "file://$PWD/$SRC?p=$1&f=$2" 2>/dev/null
}
SRC=week1.html; mkdir -p final
for p in 1 2 3 4 5 6; do
  render $p post  1080 1350 "final/${V}-${C}-${p}-${SLUG[$p]}-post-1080x1350.png"
  render $p story 1080 1920 "final/${V}-${C}-${p}-${SLUG[$p]}-story-1080x1920.png"
  render $p li    1200 1200 "final/${V}-${C}-${p}-${SLUG[$p]}-li-1200x1200.png"
done
```
- Linux: `google-chrome` or `chromium` with the same flags. Fonts must be loadable (Google Fonts online, or local).
- Verify every file: `sips -g pixelWidth -g pixelHeight final/*.png | grep -c pixelWidth` equals the expected count.
- Open 2–3 exports and look: cut-off text, LTR fallback, logo position, safe zones, the «و»+Latin glitch.

## 2. Grid preview
Write `grid.html` that places the `post` PNGs in a 3-column RTL grid (newest first), each cropped to 3:4 as the profile
does, with 4px gaps on a white background; screenshot it at 1080 wide (`--window-size=1080,<rows*480>`), save as
`<venture>-<campaign>-instagram-grid.png`.

## 3. Design + caption PDF
From the plan markdown (one `## n. <day>: <title>` per post, caption under `**الكابشن**`), generate `pdf.html`:
`@page{size:1600px 1060px;margin:0}`, `.pg{width:1600px;height:1060px;display:flex}`, image left (~900px tall), caption
right in Cairo 19px/1.7, a cover page with the schedule table. Then:
```zsh
"$CH" --headless=new --print-to-pdf="<venture>-<campaign>-content.pdf" --no-pdf-header-footer "file://$PWD/pdf.html"
```
Check page count = posts + 1.

## 4. Deliver
`zip -r <Venture>-<Campaign>.zip final <venture>-<campaign>-content.pdf <venture>-<campaign>-instagram-grid.png`.
Report: files count per format, PDF pages, anything not verified.

## Gotchas
- A published Artifact or any wrapper may drop `dir="rtl"` on `<html>`: set `direction:rtl;text-align:right` in CSS too.
- Wrap "60+"-style numbers in `<bdi dir="ltr">`.
- `--virtual-time-budget` lets web fonts load; without it the first export may use a fallback font.
- Chrome print breaks `vw`-based layouts: for decks, screenshot each slide and bind the PNGs through an HTML page with
  `@page{size:<W>px <H>px}`.
