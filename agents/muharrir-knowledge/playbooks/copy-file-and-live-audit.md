# The numbered copy file and the live-versus-approved audit

Source: Mathkor `mathkor-website-copy.md` (14 sections, 144 strings, 2026-11-17), `mathkor-launch-readiness.md`
section 4 and `handoff-check-2026-11-19.md` (One Studio). last_verified: 2026-11-19

## Shape of the copy file
1. **General rules** first (8 lines max): rename map (old → new, and which occurrences are NOT the product name),
   banned phrases to delete everywhere, digit style, logo file per background, brand colours, 301 rule on a domain move,
   Organization schema (`name`, `alternateName`, former name), and "any text not listed stays as is, with the rules
   above applied".
2. **SEO and sharing block**: `<title>`, meta description (120–160 chars), `og:title`, `og:description`, `og:site_name`,
   plus a per-page title/description table.
3. **One block per section in the site's order** (header, hero, proof bar, demo, articles, Arabic-first, audiences,
   how it works, pricing, FAQ, testimonials, final CTA, footer, blog template). Each string: a bold label that doubles
   as its id (`**العنوان الرئيسي H1:**` ≙ `hero.h1`), the text on its own line, and a "delete from this section" note
   where old strings must go.
4. **Status column** after the live check: APPLIED · TODO · VIOLATION · ALREADY ON MAIN (code is right, build is stale).

## Live audit method
- Fetch each public page twice: `curl -s URL` (what crawlers see) and headless Chrome `--dump-dom` (what people see).
  Strip tags, search each approved string; record found / missing / replaced-by-what.
- Count: applied ÷ approved = `% applied`; list the misses with the exact live text; list violations (banned phrases,
  old name) with URL and element.
- Find the **cause** of each miss before reporting it. Seen causes: a stale build (code on main, not deployed); a
  database text override that wins over lang files (admin "texts" panel); a hidden-sections setting; a plan feature
  stored as JSON in the database; an EN translation missing in a `ui_translations` table.
- Hand each cause to its owner: copy → muharrir, frontend file → bannaa, SSR/meta/redirect → maher, dashboard setting →
  the venture owner (name the exact panel).
- Report shape: a 4-column table (Where · Live text · Required · Owner), then the `% applied` line, then the P0 list.
