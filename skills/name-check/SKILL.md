---
name: name-check
description: Check a candidate product name against domains (.com via Verisign RDAP; .sa/.ai/.io via whois), the WIPO Global Brand Database (classes 9/35/42) and the Saudi register (SAIP), and record the result in the Dynamo round-table format. Use whenever wassam or any Dynamo agent must say whether a name is free or risky.
---

# name-check

Run the checks in this order, cheapest first. Never report a cell you did not actually check.

## 1. Rejected list
Open the venture profile's rejected names. If the name (any spelling) is there, stop: verdict **drop**, reason "shown
before on <date>".

## 2. .com (Verisign RDAP)
```zsh
curl -s -o /dev/null -w '%{http_code}\n' "https://rdap.verisign.com/com/v1/domain/<name>.com"
```
`404` = free · `200` = taken · anything else = "not checked (HTTP <code>)". About one request per second is fine.

## 3. .sa / .ai / .io (whois, serial, with pauses)
```zsh
whois -h whois.nic.net.sa <name>.sa; sleep 1
whois -h whois.nic.ai <name>.ai;     sleep 1
whois -h whois.nic.io <name>.io
```
"No match", "NOT FOUND", "No Data Found" = free. Parallel calls get rate-limited and return empty: rerun serially.

## 4. WIPO Global Brand Database (browser pane)
- Open https://branddb.wipo.int, search the Arabic word, then each Latin spelling. Filter Nice classes **9, 35, 42**.
- A result URL loads only with the suffix `&_=<unix timestamp>&fg=_void_`; add it if the page stalls.
- Record per hit: mark, owner, country, class, status (active / pending / expired) and the year.
- **Coverage warning (always written in the report):** WIPO has no Saudi national collection. Its GCC coverage is
  Egypt, Kuwait, Oman, Bahrain, Jordan, UAE and Qatar. "WIPO clean" ≠ "Saudi clean".

## 5. Web search
Search `"<Latin>" app`, `"<Latin>" SaaS`, `"<Arabic>" شركة`. Note any live brand, institution or product with the
name, even unregistered.

## 6. SAIP (Saudi Authority for Intellectual Property)
https://ipsearch.saip.gov.sa is geo-blocked outside the Kingdom (DNS resolves, TCP never opens; www.saip.gov.sa itself
loads). Do not retry in a loop. Write "not checked: SAIP geo-blocked; needs a search from inside KSA or a trademark
agent" and list it under open checks.

## 7. Prices (reference, Porkbun 2026-11-17)
.com $11.81/yr · .sa via Saudi registrars · .io $28 first year then $51.80 · .app $8.75 then $14.93 ·
.ai $82.70/yr, 2-year minimum (~$165). Quote the current price if the registrar page is open; otherwise label these
"reference 2026-11".

## 8. Report row
`| # | الاسم | المعنى | Latin | .com | .sa | .ai/.io | WIPO 9/35/42 | المخاطر | الحكم |`
Verdict: **go / caution / drop**. Always end the report with "Open checks:" (SAIP, attorney opinion) and "Not a legal
opinion."
