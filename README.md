# الدينامو · Dynamo

**الدينامو** فريق تسويق كامل من ثلاثة عشر وكيلًا متخصصًا يعملون بالتوازي لأي venture في One Studio، ومراجِعة بشرية واحدة تعتمد أو ترفض. بُني من العمل الحقيقي على «مذكور» (17–19 نوفمبر 2026)، وكل وكيل يحمل خبرته المكتوبة من ذلك العمل، من دون أن يحمل المشروع نفسه في نواته.

**Dynamo** is a thirteen-agent marketing team for One Studio ventures: strategy, naming, identity, social design, captions, site copy, frontend, backend/SSR, technical audit, publishing, paid ads, direct outreach, and reporting. Every agent first reads the venture (Flow OS, GitHub, site, socials) and asks the owner only what it could not read. It was distilled from the Mathkor launch work. Every agent is venture-neutral and reads one small venture profile before it works.

## الفريق · The team

| # | الوكيل | Slug | الدور |
|---|---|---|---|
| 1 | وسّام | `wassam` | باحث الأسماء والعلامات التجارية |
| 2 | نقّاش | `naqqash` | مصمم الهوية والشعار ونظام التصميم |
| 3 | لوّان | `lawwan` | مصمم السوشال (شهر كامل بثلاث مقاسات) |
| 4 | راوي | `rawi` | الكابشنات والنبذات وخطة المحتوى |
| 5 | محرّر | `muharrir` | نصوص الموقع والمدوّنة والصفحات القانونية |
| 6 | بنّاء | `bannaa` | مطوّر الواجهة (كود جاهز للتسليم) |
| 7 | ماهر | `maher` | مطوّر الخادم: SSR والأداء والبريد |
| 8 | مُدقّق | `mudaqqiq` | المراجع التقني والتسويقي للموقع (P0/P1/P2) |
| 9 | ناشر | `nashir` | النشر والجدولة، وموديريتور الحساب: حالة يومية وتقرير نتائج أسبوعي |
| 10 | مدوّن | `mudawwin` | التقارير، التحديث اليومي، وتقرير الفريق كل خميس 16:00 |
| 11 | مُعلن | `mulin` | الإعلانات المدفوعة: الحملات والميزانية والنتائج المتوقعة، بموافقة المالك |
| 12 | مُخطّط | `mukhattit` | الاستراتيجية والاستهداف: الشرائح، الفرضيات، القنوات، خطة 90 يومًا |
| 13 | سفير | `safeer` | التواصل المباشر: قوائم العملاء، الرسائل، المقابلات، المتابعة |

التعريفات بالعربية: [`dynamo-agents-v2.md`](dynamo-agents-v2.md) (الحالية، 13 وكيلًا) و[`dynamo-agents-v1.md`](dynamo-agents-v1.md) (الأصل). القواعد المشتركة التي يقرأها كل وكيل: [`TEAM.md`](TEAM.md).

## كيف يستخدمه أي venture · How a venture uses it

1. **ملف هوية وقواعد المشروع.** انسخي [`venture-profile.template.md`](venture-profile.template.md) إلى مستودع الـ venture باسم `marketing/venture-profile.md` واملئيه. مثال مكتمل: [`ventures/mathkor.md`](ventures/mathkor.md). كل وكيل يقرأه قبل أي عمل.
2. **داخل Claude Code (الطريقة الأسرع).** من مجلد الـ venture:
   ```bash
   /path/to/dynamo/scripts/install.sh /path/to/venture
   ```
   ينسخ الوكلاء إلى `.claude/agents/` والمهارات إلى `.claude/skills/`. بعدها: «شغّلي لوّان على خطة الشهر» أو `Agent(subagent_type=lawwan)`.
3. **داخل Flow OS.** `discover_agent_repo` على هذا المستودع، ثم `import_agents_from_repo` للوكلاء المطلوبين، ثم `attach_imported_agent_to_venture`. يظهرون على كرت الطاقم موقوفين إلى أن يُشغَّلوا. التحديثات اللاحقة عبر `check_agent_import_updates` ثم `adopt_agents_from_repo`.

## بنية المستودع · Layout

```
dynamo/
├── README.md · TEAM.md · dynamo-agents-v1.md
├── venture-profile.template.md      ← ما يملؤه كل venture
├── ventures/mathkor.md              ← المثال المرجعي المكتمل
├── agents/<slug>.md                 ← تعريف كل وكيل (frontmatter متوافق مع Flow OS)
├── agents/<slug>-knowledge/         ← INDEX.md + playbooks/ + experience/ + frameworks/
├── examples/<slug>-starter-prompts.yaml
├── skills/<skill>/SKILL.md          ← مهارات مشتركة (render, publish, audit, report…)
└── scripts/install.sh
```

## الشخصيات · Characters

`characters/`: ورقة شخصية لكل وكيل (`CHARACTERS.md`)، الأفاتارات `png/<slug>-512.png`، المصدر `svg/`، صفحة الفريق `dynamo-team-2400x1256.png`، والمولّد `build_characters.py` (يعيد رسم الـ 13 بأسلوب واحد: فلات بلا خطوط حبر، لوحة One Studio، لمسة برتقالية واحدة).

## ملاحظة الاستيراد إلى Flow OS

`discover_agent_repo` يحتاج أن يقرأ المستودع. وهو اليوم **خاص** تحت `amalshurrab/dynamo`، فالقراءة ترفض (`no_access`). الحلول: جعله عامًا، أو تثبيت تطبيق GitHub الخاص بالستوديو على الحساب، أو نقله إلى `onestudio-co`. قرار المالكة.

## قواعد الملكية · Ownership

- المالكة والمراجِعة: Amal Shurrab. أي تعديل على وكيل يمرّ من هنا ثم يُزامَن إلى Flow OS.
- ما يتعلمه الفريق في venture يُسجَّل في `agents/<slug>-knowledge/experience/` موسومًا `[VENTURE-CONVENTION]` مع التاريخ، ولا يُدمج في النواة إلا إذا ثبت أنه عام.
- الأسماء العشرة قابلة للمراجعة. الـ slug ثابت حتى تُقرَّر الأسماء النهائية.
