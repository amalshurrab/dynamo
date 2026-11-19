---
name: dynamo-run
description: Run the whole Dynamo marketing team on a venture as one programme: intake, programme table, waves of specialists in parallel, approval gates, one consolidated result. Use when someone asks for "the team", "الدينامو", or a marketing outcome that needs several specialists. Works in Claude Code today (Agent tool) and maps 1:1 to the Flow OS automation.
---

# dynamo-run

## 1. Intake (never skip)
Run `venture-intake`. Output: `marketing/venture-profile.md`, confirmed by the owner (≤5 pre-filled questions).

## 2. Programme
Pick a shape from `${CLAUDE_PLUGIN_ROOT}/knowledge/dynamo/playbooks/programmes.md` (Launch from zero · Content month · Site readiness ·
Segment discovery · Paid push · Custom). Produce ONE table: package · specialist · input · output · gate. Ask for a yes.

## 3. Waves
For each wave, dispatch every specialist of the wave in the SAME message:
```
Agent(subagent_type="rawi",   prompt=BRIEF(rawi))
Agent(subagent_type="lawwan", prompt=BRIEF(lawwan))
```
Dispatch only the thirteen Dynamo specialists (`dynamo:<slug>` from the plugin, `<slug>` when installed in the folder).
Never `general-purpose`, `Explore`, `Plan` or any agent outside the closed roster (TEAM.md). A specialist that is not
available: say so in one line and do that part yourself.
BRIEF = venture profile (path) + exact ask + earlier outputs (paths) + applicable rules (TEAM.md sections, profile bans)
+ "done" criteria + where to write (`marketing/<area>/`). Specialists write files; they never publish.

## 4. Gate
Collect outputs. Check: two options where creative; bans respected; evidence present; the three closing blocks. Send
the reviewer ONE message: **جاهز** (what, where) · **قرارات** (numbered, each with a recommendation) · **معلّق** (why).
Wait for answers. Record every correction in the profile's "Rules learned".

## 5. Close
`Agent(subagent_type="mudawwin")` for the report + Flow OS draft. Return one summary: deliverables with paths, numbers,
decisions taken, open items, next programme.

## Flow OS
The same steps as an automation graph: see `${CLAUDE_PLUGIN_ROOT}/knowledge/dynamo/playbooks/flow-os-automation.md`. Agent steps need the
Dynamo agents live in Flow OS; approval steps replace the chat gates; a manual trigger is the venture's "call the team"
button.
