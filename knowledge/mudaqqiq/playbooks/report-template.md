# Launch-readiness report template

Source: `website/mathkor-launch-readiness.md` (One Studio, 2026-11-18), the shape the reviewer and owner accepted.
last_verified: 2026-11-19

## Header block
```
# <Venture>: جاهزية الموقع لاستقبال العملاء
**تاريخ الفحص:** <date, time of day>.
**ما شمله الفحص:** (bullets, each with its count)
- كل الصفحات الـ<N> في الـsitemap.
- <N> رابطًا. · <N> صورة. · Lighthouse على الجوال (<pages>). · DNS والبريد وSSL وترويسات الأمان.
- تجربة صفحات التسجيل والأسعار والتواصل في المتصفح. · مقارنة الموقع بملف النص المعتمد `<file>`.
**الهدف:** <the campaign date and what every visitor must be able to do>.
```

## Summary table
`| المجال | الحالة | الملاحظة |` with ✅ / ⚠️ / ❌ and one line of fact per row. Rows: domain and redirects, SSL, blog
SEO, accessibility, old-domain leftovers, main pages for crawlers (SSR), mobile speed, mailbox, legal pages, approved
copy applied %, signup and payment path, tracking, Search Console and Bing.

## Priorities block
P0 before the campaign date · P1 within the following week · P2 continuous. Owners listed by first name with their lane
(code and server / marketing and accounts / decision).

## Item format (numbered, grouped by part)
```
## <n>. <title> — <owner> (<secondary owner if any>)
**الوضع الحالي:** facts with numbers and the exact current string or record.
**المطلوب:** numbered steps, exact target values (records, strings, files).
**للتحقق:** a command or a visible check, e.g. `curl -s https://<domain>/llms.txt | grep -c <old-domain>   # المطلوب: 0`
```

## Copy-compliance table
`| المكان | الحالي على الموقع | المطلوب |`, one row per violation, bold on the approved string. Close with the fixed
rule in one line (banned phrases, in both languages).

## Final checklist
`- [ ]` per deliverable under P0 / P1 / acquisition system, in the exact wording the developer will tick.

## Verification command set
```zsh
curl -s https://D/sitemap.xml | grep -oE '<loc>[^<]+' | wc -l            # pages
curl -sI https://D | grep -iE 'strict-transport|x-frame|content-security'  # headers
curl -s https://D/pricing | grep -oE '<h1[^>]*>[^<]+'                       # crawler view (empty = CSR)
curl -s https://D/robots.txt; curl -s https://D/llms.txt | grep -c OLD      # old domain leftovers
dig +short MX D; dig +short TXT D | grep spf; dig +short TXT _dmarc.D
echo | openssl s_client -connect D:443 -servername D 2>/dev/null | openssl x509 -noout -dates
npx lighthouse https://D --preset=perf --form-factor=mobile --output=json --quiet --chrome-flags="--headless"
```
