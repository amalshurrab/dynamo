# Logo brief, vectorisation and package

Source: Mathkor identity work 2026-11-17/18 (`brand/logo-prompt-mathkor-pro.md`, the approved mark vectorised with
Islam Hani, `/Users/amal/Documents/one-studio/Mathkor-brand-logo/` with svg/, png/, preview.html); platform sizes from
LinkedIn, Meta and Apple HIG pages (checked 2026-11-19). last_verified: 2026-11-19

## Writing the brief for an image tool
- Ask for the **symbol only**: "flat vector-style logo mark, single idea, <colours as hex>, plain white background,
  no text, no letters, no gradient, no glow, centred, lots of margin". One idea per prompt; 3–4 prompts = 3–4 directions.
- Never ask the tool for the wordmark. Arabic letters come out wrong; set the wordmark by hand in the chosen font.
- Generate at least 8 candidates per direction; keep the 1–2 that read at thumbnail size when the sheet is zoomed out.

## Vectorise and lock up
- Trace in Illustrator/Figma/Inkscape; simplify to the fewest anchor points; align to a 24-unit grid; check optical
  balance, not mathematical.
- Lock-ups: mark + Arabic wordmark + Latin wordmark (stacked and horizontal), mark alone, wordmark alone. Clear space =
  the mark's height ÷ 4. Minimum size: mark 24px, lock-up 120px wide.
- Colour variants: full colour on light, full colour on dark, white, mono ink.

## Export set
SVG masters for every variant. PNG: 32, 64, 180 (apple-touch), 512, 1024, 2048 for the mark; 1200-wide for lock-ups.
`preview.html` shows all on light and dark. ZIP named `<Venture>-brand-logo.zip`.

## Platform assets
- Avatar: 1024×1024 PNG, mark inside a centred circle of 70% diameter (IG, LinkedIn, FB all crop round).
- LinkedIn banner 2256×382 (content in the middle ~1128×382 band; edges cropped on mobile).
- Facebook cover 1640×624 (mobile shows the centre 640×624); export @2x 3280×1248.
- Favicon: SVG + 32/180/512 PNG + `site.webmanifest`. OG image 1200×630 with the lock-up and tagline.
- Deck/report theme: logo SVG files for the slide master, the colour tokens as CSS variables.
