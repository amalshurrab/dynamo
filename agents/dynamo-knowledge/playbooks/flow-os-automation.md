# Running the team as a Flow OS automation

Source: Flow OS automation palette read on 2026-11-19 (`get_automation_palette`): built-in steps trigger (manual /
event / schedule), condition, transform, delay, approval ("Ask a person": prompt, approverUserId), foreach, agent ("Ask an
agent": agentId, prompt), http, plus action steps for Flow OS capabilities. last_verified: 2026-11-19

## Why an automation
"Call the team" in Flow OS = one button on the venture that starts a graph of agent steps with approval gates, instead
of thirteen chats. The graph is owned by a person (automations are per person) and scoped to a venture; a copy per
venture, or one studio-wide graph that takes the venture as input.

## Prerequisites
1. The Dynamo agents exist in Flow OS (import from the repo) and are **live** (agent steps need a live agentId).
2. The venture has a `marketing/venture-profile.md` or the intake step creates one.
3. The reviewer's user id for the approval steps (the venture's marketer; fallback the venture Owner).

## Graph: "الدينامو · برنامج" (manual trigger with input)
```
trigger.manual (input: request text, programme shape, cadence)
→ agent dynamo        prompt: "Intake + programme for venture {venture}: {input}. Return the programme table."
→ approval            prompt: "اعتمد البرنامج؟" (approverUserId = reviewer)
→ [wave 1, parallel]  agent mukhattit | agent wassam …   (branches per programme shape)
→ approval            "قرارات البوابة 1"
→ [wave 2, parallel]  agent rawi | agent lawwan | agent muharrir …
→ approval            "قرارات البوابة 2"
→ … 
→ agent mudawwin      prompt: "Consolidate all outputs; draft the report and the Flow OS update."
→ approval            "انشر التحديث؟"
→ action post_status_update / publish_venture_update
```
Each agent step's prompt carries the earlier steps' outputs by reference (`{{steps.<id>.output}}` as the editor shows).
Approval steps park the run until the reviewer answers in Flow OS; nothing outside Flow OS is touched by the graph
(publishing to social platforms stays with nashir in a browser session the reviewer opens).

## Variants
- **Event trigger:** `cap.add_venture_member.done` or `notification.venture.stage_changed` → run the intake wave only and
  post "الدينامو جاهز لهذا المشروع" with the profile draft.
- **Schedule trigger:** Thursday 16:00 (`0 16 * * 4`) → agent mudawwin weekly team report → approval → post.
- **Narrow runs:** one button per programme shape (content month, site readiness) so a venture picks what it needs.

## What Claude Code does meanwhile
Until the agents are live, the same programme runs in Claude Code: the `dynamo` agent dispatches the specialists with the
Agent tool (one call per specialist per wave, in the same message), with the reviewer answering the gates in chat.
