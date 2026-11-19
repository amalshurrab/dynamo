---
name: caption-system
description: Write and check social captions and content-plan files the Dynamo way: one caption per post for all platforms, hook under 125 characters with the keyword, numbered practical tip, comment/save CTA, 3–5 hashtags, named sources, banned-words and mandatory-mentions check against the venture profile, Arabic typography rules, and the plan markdown format the PDF builder and the publisher read. Use whenever rawi or any Dynamo agent writes or reviews captions, bios or a content plan.
---

# caption-system

## 1. Load the rules (from the venture profile)
Before writing, copy into your working notes: banned words/phrases (exact strings), mandatory mentions (e.g. all AI
tools by name), social register/dialect, brand lines (tagline, hook line), link placement, allowed sources, forbidden
evidence. Every caption is checked against this list before it is shown.

## 2. Caption shape (one text, every platform)
```
<Hook ≤125 chars, keyword inside, no emoji>

<Body: 1 numbered practical point, or 3 short lines; concrete nouns; one named source if a claim needs it>

<Close: one ask — comment with …, save this, tell us …>
#tag1 #tag2 #tag3 #tag4
```
- 600–1,200 characters total. Link never inside the caption («الرابط في البايو» / first comment).
- 3–5 hashtags, one line, brand tag last.
- Sequencing words when published daily: «بكرة», «أمس», «(2/3)».

## 3. Checks (run mechanically)
```zsh
# banned strings: exit 1 if any appears
grep -nE 'ابدأ مجان|بلا بطاقة|بدون بطاقة|ليس .* بل ' plan.md && echo "BANNED FOUND" || echo "bans ok"
# «و» glued to a Latin word
grep -nE 'و[A-Za-z]' plan.md && echo "FIX و+Latin" || echo "و ok"
# hook length (first line after **الكابشن**)
awk '/\*\*الكابشن\*\*/{getline; print length($0)": "$0}' plan.md
# hashtag count per post
grep -nE '^#' plan.md | awk -F'#' '{print NF-1": "$0}'
```
Adapt the banned-strings regex to the venture profile. Then read for: a sentence that fits any company (delete), a
claim with no source (add or delete), a promise of results (delete), the mandatory mentions (present), dialect
consistency, no emoji in formal surfaces.

## 4. Plan file format (read by build_pdf.py and by nashir)
```
# <Venture>: خطة محتوى <الفترة>

## 1. الأحد 22 نوفمبر: <العنوان>
**الشكل:** بوست + ستوري + لينكدإن   **المحور:** <pillar>
**السطر على الصورة:** <one line for lawwan>
**الكابشن**
<caption exactly as published>
---
```
`## n. <day>: <title>` per post, `**الكابشن**` block = the published text, `---` closes the post. Carousels add
`**الشرائح:**` (one line per slide); polls add `**السؤال:**` and `**الخيارات:**`.

## 5. Bios (character limits, checked 2026-11-19)
Instagram 150 · Facebook 255 · LinkedIn tagline 120 · LinkedIn About 2,000 · X 160. Count with
`python3 -c "import sys;print(len(open(sys.argv[1],encoding='utf-8').read().strip()))" bio.txt`.

## 6. Deliver
Plan file + a summary table (day · title · format · pillar · hook) + the list of rules applied. End with *What
changed · What was verified · What is open*.
