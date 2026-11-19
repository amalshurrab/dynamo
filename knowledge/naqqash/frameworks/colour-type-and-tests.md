# Colour roles, type pairing and the three tests

Source: Mathkor official identity (2026-11-17), the reviewer's design lessons (2026-11-18), WCAG 2.1 contrast thresholds.
last_verified: 2026-11-19

## Colour roles (always five, as hex)
`--ink` (text), `--primary` (brand colour, solid blocks), `--accent` (one highlight colour, used once per surface),
`--bg` (page/off-white), `--border` (thin lines on cards). Optional `--primary-dark` for dark posts.
Rules: a gradient only inside the mark; body text ≥ 4.5:1 on `--bg`; headline ≥ 3:1; accent is a focus device, never a
fill for large areas; dark surfaces use `--primary` or `--ink`, not black.
Example (Mathkor): ink #1F0738 · primary #6A45DC · accent #4FDDA6 · bg #F7F5FC · border #E6E0F2.

## Type pairing for Arabic-first brands
- Arabic headline face with real heavy weights: Cairo 800/900, Tajawal 800, IBM Plex Sans Arabic 700, Almarai 800.
- Latin companion: Inter (neutral, tabular numerals). Keep the Latin a touch smaller than the Arabic at the same
  nominal size.
- Line-height 1.25–1.35 for Arabic headlines, 1.7 for body. Never fake-bold a light cut.
- Watch for the «و» + Latin ligature glitch in Cairo; never attach و to a Latin word.

## The three tests before anything is shown
1. **32px test:** the mark alone at 32px on light and dark. If it turns to mush, simplify.
2. **Avatar test:** inside a circle at 110px (as IG/LinkedIn show it). The mark must stay inside the circle with air.
3. **Header test:** the horizontal lock-up at 140px wide in a site header next to a nav. Must read instantly.
Plus: greyscale (idea survives without colour) and a side-by-side with the three closest competitors' logos.

## Register: companies vs consumers
B2B SaaS wants calm: flat, geometric, one accent, generous space. "Freelancer" signals to avoid: hand-drawn strokes,
paper grain, many details, every space filled, playful tilts. Consumer brands may loosen this; the profile decides.
