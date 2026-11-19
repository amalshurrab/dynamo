# Check order and round table

Source: Mathkor naming work, 2026-11-12 → 2026-11-17 (Kateb-SEO CLAUDE.md, renaming research section); Verisign RDAP
and WIPO Global Brand Database behaviour as observed on those dates. last_verified: 2026-11-19

## Order (cheapest and most decisive first)
1. **Rejected list** in the venture profile. A name shown before is dead, in any spelling.
2. **.com** via Verisign RDAP: `curl -s -o /dev/null -w '%{http_code}' https://rdap.verisign.com/com/v1/domain/<name>.com`
   → `404` free, `200` taken. Fast, no rate limit seen at ~1 request/second.
3. **.sa / .ai / .io** via whois, one at a time with `sleep 1` between calls (parallel runs get rate-limited):
   `whois -h whois.nic.net.sa <name>.sa`, `whois -h whois.nic.ai <name>.ai`, `whois -h whois.nic.io <name>.io`.
   "No match" / "not found" = free.
4. **WIPO Global Brand Database** (branddb.wipo.int) in the browser pane: search the Arabic word AND each Latin
   spelling; filter Nice classes 9, 35, 42. Result pages only load when the URL carries `&_=<timestamp>&fg=_void_`.
   Record: hit count, owner, country, class, status (active / pending / expired). WIPO's coverage list has Egypt,
   Kuwait, Oman, Bahrain, Jordan, UAE and Qatar but **no Saudi national collection**.
5. **Web search** for the Latin spelling plus "app", "SaaS", "شركة": catches unregistered brands and institutions.
6. **SAIP** (Saudi register, ipsearch.saip.gov.sa): geo-blocked from outside the Kingdom (DNS resolves, TCP never
   opens). Ask someone inside KSA to run the search, or use a trademark agent. Until then the cell reads "not checked".

## Prices (Porkbun, checked 2026-11-17)
.com $11.81/yr · .io $28 first year then $51.80 · .app $8.75 then $14.93 · .ai $82.70/yr with a 2-year minimum (~$165).
Marketers usually prefer .com; .ai only when the profile allows the cost.

## Round table (one per round, markdown)
| # | الاسم | المعنى | Latin | .com | .sa | .ai/.io | WIPO 9/35/42 | المخاطر | الحكم |
Verdict vocabulary: **go** (all green, risks "none found"), **caution** (one yellow cell, say which), **drop** (reason).
Under the table: the top pick in two sentences, then "open checks" (SAIP, attorney).

## Decision record
When a name is chosen write: date · Arabic · Latin · domains to reserve (with prices) · handles to check (IG, LinkedIn,
X, Facebook) · documents to rename · who reserves (the reviewer/owner, never the agent).
