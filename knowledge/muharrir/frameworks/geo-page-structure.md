# GEO / AEO page structure and the blog review checklist

Source: Mathkor blog review (18 articles, 2026-11-17) and week-1 «تشريح مقال مذكور» post; Google Search Central
guidance on structured data and AI features; Princeton GEO study (arXiv 2311.09735: statistics, quotations and citations
raise visibility in generative engines by up to ~40%). last_verified: 2026-11-19

## A page that an answer engine can quote
- **Reaches the crawler as HTML.** If `curl` shows a title and an empty `<div id="app">`, ChatGPT, Claude and Perplexity
  see nothing: flag P0 and hand to maher (SSR). Google runs JavaScript; the others mostly do not.
- **Title ≤ 60 chars with the keyword**, description 120–160 chars, one H1 that matches the title's promise.
- **Direct answer first:** the first 40 words answer the page's question in plain terms. Then the detail.
- **Question-shaped H2s**, each answered in its first sentence.
- **Evidence:** a named source per empirical claim (organisation + year), statistics and short quotations.
- **FAQ block** of 5–10 real buyer questions with `FAQPage` schema; `BlogPosting` (headline, date, image, publisher) and
  `BreadcrumbList` on articles; `Organization` with `name`, `alternateName`, `sameAs`, `email` site-wide.
- **Internal links** to 2–3 sibling pages with descriptive anchors; descriptive Arabic `alt` on every image.
- **One topic per URL.** Two articles answering the same query compete; merge or differentiate.

## Blog review checklist
1. Technical: server HTML non-empty per article; schema present; one H1; no duplicated sections; slugs are Latin and
   readable (a transliterated Arabic slug → rename + 301).
2. Template strings: title patterns, breadcrumb, disclaimer line, "last updated" label, CTA box, internal labels that
   should be hidden from readers (e.g. the keyword "entry" line).
3. Titles: ≤ 60 chars, keyword first, no year unless the piece is dated by nature; one new title per slug in a table.
4. Content: duplicate topics, weak internal linking, off-audience pieces, outdated counts ("7 articles" when 18 exist).
5. Disclaimer wording for AI-written content: state what the product did (research, writing, source review, internal
   linking) rather than "generated, shown as it came out of the line".
6. Next five articles: each mirrors a question the buyer asks before buying (does ChatGPT mention my brand? why my
   competitor and not me? how to write an article AI cites? how to measure AI visibility?).
