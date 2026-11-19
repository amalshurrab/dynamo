---
name: venture-intake
description: First step of every Dynamo agent on a new venture. Read everything that can be read (Flow OS venture, GitHub repo, live site, social accounts, existing profile) before asking the owner anything, then ask at most five pre-filled questions and write or update marketing/venture-profile.md. Use whenever an agent starts work for a venture it has no profile for, or the profile is older than 30 days.
---

# venture-intake

Founders often cannot state their marketing needs. The agent's job is to find out, not to ask them to explain.

## 1. Read before you ask (20–30 minutes, no questions yet)

**Flow OS** (onestudio MCP; say what you read, never paste it):
- `venture_brief` and `get_venture` → stage, owner, team, description, tagline, avatar colour.
- `get_lean_canvas` → problem, segments, UVP, channels, revenue, unfair advantage.
- `list_stage_rules` → the exit rules the venture must meet (they shape what marketing must prove).
- `list_issues {summary:true, compact:true}` and `list_status_updates` → what is being built, what is blocked, deadlines.
- `list_marketing`, `list_learnings` for the venture → existing assets, decisions, lessons.
- `get_venture_settings` / `venture_web_traffic` where allowed → analytics, domains.

**GitHub** (`gh api`, read-only):
- README, CLAUDE.md/AGENTS.md, docs/, any `marketing/` folder, the public pages' copy, i18n files (banned words, tone),
  analytics and pixel ids in the code, sitemap and robots, legal pages, pricing config, payment provider, stack.
- Last 30 commits: what the developer is working on right now.

**Live surfaces** (browser pane or `curl`):
- The site: hero, offer, pricing, trial wording, footer links, languages, what a crawler sees without JavaScript.
- Social accounts: handles, bios, last post date, cadence, visual style, follower counts (as a dated snapshot).
- Competitors named anywhere above: their positioning line and one screenshot each.

**Existing profile:** `marketing/venture-profile.md` if present. Note every field that is empty, stale or contradicts
what you read.

## 2. Draft the profile yourself

Fill `venture-profile.template.md` from what you read. Mark each value with its source in a trailing comment
(`<!-- Flow OS lean canvas 2026-11-19 -->`, `<!-- repo i18n/ar.json -->`, `<!-- assumed -->`). Where you had to guess,
write your best guess and tag it `[assumed]` with one line of reasoning.

## 3. Ask at most five questions, pre-filled

One message to the owner. Each question states what you found and asks for a yes or a correction:
- "قرأت إن الشريحة المستهدفة هي X من Lean Canvas بتاريخ …، لسا صح؟"
- "ما لقيت ممنوعات لفظية مكتوبة. اقترحت هذه الثلاث بناءً على نبرة الموقع: … توافق؟"
Never send a blank questionnaire. Never ask what you could have read. If the owner cannot answer, keep your proposal
tagged `[assumed]` and move on; the reviewer can change it later.

## 4. Write the profile and get a yes

Save to `<venture repo>/marketing/venture-profile.md` (or the path the reviewer gives). Show the owner the filled
profile, not the template. Record the date in "Rules learned". Only then start the actual task.

## 5. Re-intake triggers
A profile older than 30 days, a name or identity change, a new segment decision, a new channel, or a rule from the
reviewer. Update the profile; do not fork it.

## Output of the skill
- `marketing/venture-profile.md` filled, every field sourced or `[assumed]`.
- A 10-line intake summary to the reviewer: stage, promise, segments, channels, assets that exist, the three biggest
  gaps, and the five questions (or "no questions needed").
