# Render pipeline: one HTML file → every post in every size

Source: Mathkor campaign sources `social/soon/soon-v3.html`, `social/week1/week1-gpt.html`, `social/month/month.html`,
`social/highlights/render.sh`, `social/week1/build_pdf.py` (One Studio, Nov 2026). last_verified: 2026-11-19

## Source file contract
- One `.html` per campaign. Reads `p` (post number), `f` (`post` | `story` | `li`), optional `s` (carousel slide) from
  the URL. Sets `<html dir="rtl">` **and** `direction:rtl; text-align:right` in CSS (a wrapper may drop the attribute).
- Size by format: `post` 1080×1350 · `story` 1080×1920 · `li` 1200×1200 (or `liw` 2400×1256 when a landscape is
  wanted). The body is exactly that size; nothing scrolls.
- Fonts via Google Fonts (`Cairo`, `Inter`); wait for `document.fonts.ready` or use a virtual-time budget on export.
- Tokens from the venture profile at the top of the CSS: `--ink --primary --accent --bg --border`, font stacks.
- Each post is a block keyed by `p` with its own composition; shared pieces (logo, headline styles) are components.
- Story variants keep the top and bottom 250px free of key content; LinkedIn variants scale type up ~15%.

## Export (headless Chrome, macOS)
```zsh
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CH" --headless=new --hide-scrollbars --virtual-time-budget=6000 \
  --window-size=1080,1350 --screenshot="final/<venture>-<campaign>-1-<slug>-post-1080x1350.png" \
  "file://$PWD/<campaign>.html?p=1&f=post"
```
Loop over posts × formats. Use `--force-device-scale-factor=1` (exact pixels). Verify size with `sips -g pixelWidth -g
pixelHeight` or `file`. Re-export after any CSS change; never hand-edit a PNG.

## Naming
`<venture>-<campaign>-<n>-<slug>-<format>-<WxH>.png`, e.g. `mathkor-w1-2-where-is-your-name-story-1080x1920.png`.
Carousels: `...-<n>-<slug>-s<k>-post-1080x1350.png`. Panorama tiles: `-right`, `-centre`, `-left` (posting order).

## Grid preview
A small HTML/Python step that lays the `post` exports in a 3-column grid, newest first (top-left in LTR terms is the
newest), with the profile's crop (4:5 shown as ~3:4), and screenshots it as `<venture>-<campaign>-instagram-grid.png`.
This is what the reviewer judges rhythm on (checkerboard, triptych rows).

## Design + caption PDF
`build_pdf.py` pattern: read the plan markdown (one `## n. day: title` section per post with a `**الكابشن**` block),
build an HTML with `@page{size:1600px 1060px;margin:0}`, one `<section class="pg">` per post (image left, caption
right), a cover with the schedule table, then print to PDF with headless Chrome `--print-to-pdf`. Output
`<venture>-<campaign>-content.pdf`. Zip `final/` + PDF + grid as `<Venture>-<Campaign>.zip`.

## Highlights and covers
Highlight cover 1080×1920 (centre 1080×1080 is what the circle shows) plus a 1080×1080 export (`&sq=1`). Facebook cover
1640×624 with the mobile safe area (centre 640px wide) and a 2× export. LinkedIn banner 2256×382, content in the middle
band.
