---
name: flow-os-update
description: Write and post Flow OS surfaces for a venture's marketing work: the daily update checklist on the studio venture, venture update posts, Big Shift cards, developer issues with owner and deadline, and Lean Canvas or stage-rule evidence edits, always drafted first and posted only after the reviewer's yes. Use when a Dynamo agent (mudawwin) must report work into Flow OS.
---

# flow-os-update

Rule zero: every surface is drafted and shown to the reviewer; nothing is posted, created or edited on Flow OS before an
explicit yes on that draft. The reviewer approves content; the venture's decision maker approves decisions.

## 1. Daily update (studio venture, e.g. `onestudio`, not `one-studio`)
Format:
```
@alaa-saqer
- [x] <one formal MSA fact, past tense, with a number or a named deliverable>
- [x] ...
- [ ] <next step, one line, owner implied by the venture>
#daily-update #<venture-tag>
```
- Formal MSA only. One fact per line. No sub-bullets, no parenthetical reasons, no team-member names, no emojis, no
  casual words, never "Thursday deck / عرض الخميس".
- Covers all fronts the marketer works on; when only this venture's lines are produced, hand them as lines to merge.
- Post with `post_status_update` (venture slug from the profile) after the yes.

## 2. Venture update post (the venture itself, e.g. `lead-ai`)
Title + 3–8 formal lines, one official post per decision (rename, identity approval, launch). No names, no emojis, no
security or credential notes. Post via `publish_venture_update` after the yes. A rejected topic is not re-proposed.

## 3. Big Shift card (weekly studio meeting)
`log_big_shift_card`: one "automated" card and one "vo_step" card per person, text ≤ 500 characters, formal MSA, numbers
first (what was automated, how many outputs, what it replaced). Editable until Thursday 10:00 Riyadh; after that it saves
to the next week. Draft → yes → log before the lock. Evidence: issue numbers or links.

## 4. Issue for the developer / owner
`create_issue` on the venture: title (imperative), context (2–3 lines with the finding and its evidence), acceptance
criteria (`- [ ]` lines a tester can tick), owner, due date (absolute), priority, links to the audit or handoff file.
One issue per deliverable; no bundles. Example titles: «SSR لكل الصفحات العامة», «تطبيق هوية <venture> على الموقع».

## 5. Lean Canvas, venture details, stage rules
- Venture details: name, tagline, description, colour, avatar (`update_venture_details`, `set_venture_avatar`).
- Lean Canvas: UVP (`set_lean_canvas_uvp`), channels and other boxes (`update_canvas_item` / `add_canvas_item`).
- Stage exit rules: `list_stage_rules` then `add_rule_proof` with the evidence the rule asks for (problem memo with an
  external "why now", buyer count for one segment with its source, top-3 risky assumptions each with a dated test).
Each edit is shown as before/after text to the reviewer first.

## 6. Checks before posting
- Bans from the venture profile applied (banned phrases, old product name, metaphors, "ليس X بل Y").
- Dates absolute. Numbers present. No names in formal posts. No security notes.
- Right venture slug and right surface. Read back the posted item once and record its URL in the day's log.
