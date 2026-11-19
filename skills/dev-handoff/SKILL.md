---
name: dev-handoff
description: Write a complete, ordered developer handoff for a venture's website (the shape of MATHKOR-SITE-DEV-HANDOFF.md): read the real repo at a pinned sha, compare the live build with main, then deliver Part F (frontend), Part B (backend/SSR/performance/mail) and Part C (content, external settings, final .env), each section with quoted current code, replacement, file paths, env, migrations and a verify step, plus an execution order and a WhatsApp-ready summary for the developer. Use when bannaa or maher hands code to a venture's developer; never touches production.
---

# dev-handoff

Read `TEAM.md` and the venture profile (repo, stack, hosting, brand bans, plans). Inputs: the audit (mudaqqiq), the
copy file and legal pages (muharrir), the tracking plan, verified social URLs (nashir).

## 0. Read before writing
1. Pin the repo: `git rev-parse HEAD` (or the API's latest commit) → record `sha`, date, last merge message. Every quote
   is "as of `<sha>`".
2. Live versus main: `curl -s $URL` + headless `--dump-dom`, compare strings and sections with the code on `main`.
   What is fixed on main but not deployed → **Step 0: deploy `main`**, sections marked **ALREADY ON MAIN** (verify only).
3. Locate where things really live: lang files vs database/CMS overrides, layout file, routes/middleware, brand config,
   analytics plumbing, boot script/process manager, nginx or CDN config, mail config. Note what you could NOT see.

## 1. File shape (`marketing/website/<VENTURE>-SITE-DEV-HANDOFF.md`)
```
# <Venture>: complete site handoff for the developer
> For <developer>: hand this to your AI coding assistant. Written against <repo> @ <sha> (<date>), checked against <live URL>.
## How to use this file          ← branch name; one section → verify → commit "<ID>: title"; "current code" = quoted,
                                   replace by intent if it differs; ASSUMPTION must be checked; brand rules for any text
                                   (bans, name all AI tools, trial wording); legal facts; `lint && build && test` before push
## Step 0: deploy current main
## Execution order               ← table: # · ID · What · Priority (P0/P1/P2), dependencies first
# Part F: frontend and app       ← F1 copy fixes (status per string) · F2 CTA · F3 footer+sameAs · F4 legal pages system ·
                                   F5 register → plan → checkout + consent + attribution · F6 contact form · F7 WhatsApp/
                                   booking · F8 tracking + track() + funnel events
## Env summary · ## Migrations added · ## Open ASSUMPTIONs (consolidated)
# Part B: backend, infrastructure and performance
                                 ← B1 robots.txt from APP_URL · B2 llms.txt · B3 replace-domain + root cause · B4 SSR all
                                   public pages (+ persistent process, fallback) · B5 per-page meta · B6 secondary locale
                                   noindex/canonical/hreflang/sitemap · B7 nginx cache, HSTS, one-hop redirects · B8 images
                                   WebP/srcset/dimensions/alt backfill · B9 link guard · B10 Turnstile · B11 mail + DNS ·
                                   B12 performance
## Commands added · ## Open ASSUMPTIONs
# Part C: content, external settings and env
                                 ← C1 legal content files (exact) · C2 dead-link replacement map (checked 200, anchor-text
                                   match for opaque redirects, bot-only 403 hosts left alone) · C3 dashboard steps in
                                   dependency order (mailbox → sender → DNS → mail-tester → Search Console → Bing → OAuth →
                                   payment: public details, descriptor, webhook URL, test purchase per plan → pixels →
                                   GA4 stream/key events/unwanted referrals → Turnstile → Flow OS issues) · C4 final .env
                                   (placeholders) + cache clears
```

## 2. Section template (every F/B section)
```
## <ID> <Title>
**Read:** what the repo/live site shows now (file, lines, observed behaviour, measured numbers).
**Files:** paths touched / created.
Current code:            ```<lang> …quoted as found… ```
Replace with:            ```<lang> …``` + one-line reason. (**ASSUMPTION:** … check with …)
**Env / migration / lang keys:** placeholders, both locales.
**Verify:**              ```zsh curl / dig / browser path / DB row / devtools request → expected output ```
```
Rules: quote then replace, never "add something like"; one section = one commit with the ID; every section has a verify;
env values are placeholders; no secrets, keys or internal hosts the repo did not already publish; brand bans never enter
a string; above-the-fold elements never start at `opacity:0`; SSR is a marketing requirement (AI crawlers do not run
JavaScript) and goes in the P0 order; destructive steps (cookie rename, content rewrite) carry a backup step and need the
owner's explicit yes.

## 3. Never touch production
You write commands; the developer runs them. You verify from outside (`curl -sI`, `--dump-dom`, `dig`, Lighthouse,
devtools) and never through server access, `.env`, a database or a dashboard. Operations steps go to the owner as a
numbered list in dependency order with a one-line check each.

## 4. Post-deploy check
When told "it is live": re-run every verify, map commits to section IDs, produce a table (Step · ID · Status ✅/🟡/⚠️/❌/❔ ·
Evidence) and a "what's left, in priority order" list naming the cause per gap (stale build, DB override, hidden section,
process not started, env empty, DNS unchanged). "Code on main" is not "live".

## 5. Developer summary (WhatsApp-ready, ≤ 12 lines)
What the file is · where it is · step 0 · the P0 IDs in order · the steps outside the code that only they can do ·
how to tell us it is done. End the handoff with *What changed · What was verified · What is open*.
