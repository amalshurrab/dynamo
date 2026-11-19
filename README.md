# الدينامو · Dynamo

**الدينامو** فريق تسويق كامل من ثلاثة عشر وكيلًا متخصصًا يعملون بالتوازي لأي venture في One Studio، ومراجِعة بشرية واحدة تعتمد أو ترفض. بُني من العمل الحقيقي على «مذكور» (17–19 نوفمبر 2026)، وكل وكيل يحمل خبرته المكتوبة من ذلك العمل، من دون أن يحمل المشروع نفسه في نواته.

**Dynamo** is a thirteen-agent marketing team for One Studio ventures: strategy, naming, identity, social design, captions, site copy, frontend, backend/SSR, technical audit, publishing, paid ads, direct outreach, and reporting. Every agent first reads the venture (Flow OS, GitHub, site, socials) and asks the owner only what it could not read. It was distilled from the Mathkor launch work. Every agent is venture-neutral and reads one small venture profile before it works.

## نقطة الدخول الواحدة · One entry point

لا أحد يستدعي وكيلًا واحدًا. يستدعي **الدينامو** (`agents/dynamo.md`، قائد الفريق): يفهم المشروع، يحوّل الطلب إلى برنامج بجدول (حزمة · وكيل · مدخل · مخرج · بوابة)، يشغّل الوكلاء الـ 13 على موجات متوازية، يوقف عند بوابات موافقة المراجِعة، ويعيد نتيجة واحدة. أشكال البرامج في `knowledge/dynamo/playbooks/programmes.md`، وتشغيله في Claude Code عبر المهارة `dynamo-run`، وفي Flow OS كأتمتة (زر «شغّل الدينامو» على الـ venture ← خطوات وكلاء ← خطوات موافقة) موصوفة في `knowledge/dynamo/playbooks/flow-os-automation.md`.

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

## التطبيق · The app

**الطريقة الأسهل:** صفحة واحدة على claude.ai فيها الـ 13 شخصية؛ تختار واحدًا وتتحدث معه بشخصيته، وهو يقرأ ملف مشروعك المحفوظ في الصفحة. المصدر في `app/` (يُنشر كـ Artifact مع `agents/*.md` والأفاتارات كملفات مرافقة). الرابط الحالي: https://claude.ai/artifact/3JiJx9nNntTDWpDH3C84Mm (خاص حتى تشاركه المالكة).
- المحادثة تستخدم حساب Claude الخاص بالزائر (يوافق مرة واحدة).
- ملفات المشاريع والمحادثات تُحفظ في مخزن الصفحة؛ محادثات كل شخص خاصة به.
- زر «اقرأ من Flow OS» يعمل لمالكة الصفحة داخل تطبيق Claude فقط (قيد المنصة)؛ الباقون يلصقون ما يعرفونه.
- الوكلاء هنا يكتبون ويخططون ويراجعون؛ التنفيذ الذي يحتاج ملفات أو نشرًا أو كودًا يُكمَل في Claude Code بالطريقة أدناه.

## كيف تستدعيه من Claude · Calling the team from Claude

**من Claude Code، كـ plugin (الطريقة الموصى بها لكل فريق One Studio):** أمران، مرة واحدة، على أي جهاز، ويعمل في كل مشاريعك:

```bash
claude plugin marketplace add onestudio-co/dynamo
```

```bash
claude plugin install dynamo@dynamo
```

أو من داخل جلسة Claude Code: `/plugin marketplace add onestudio-co/dynamo` ثم `/plugin install dynamo@dynamo`. (في Claude Code 2.1.292 وما بعد يكفي أمر واحد: `claude plugin install dynamo --marketplace onestudio-co/dynamo`.)
بعدها افتح **جلسة جديدة** (الـ plugins تُحمَّل عند بدء الجلسة) واكتب:

```
/dynamo:dynamo بدي أطلق منتجي خلال أسبوعين
```

أو ببساطة «شغّل الدينامو على مشروعي». القائد يفهم ويخطّط ويوزّع ويرجع بنتيجة واحدة، ويسألك عند كل بوابة. الوكلاء يظهرون باسم `dynamo:<slug>` والمهارات باسم `/dynamo:<skill>`.

- **التحديث:** `claude plugin update dynamo@dynamo` (كل commit على `main` هو إصدار جديد؛ لا يلزم رقم نسخة). ثم `/reload-plugins` أو جلسة جديدة.
- **لمستودع فريق** (حتى يُفعَّل تلقائيًا لكل من يفتحه): أضف إلى `.claude/settings.json` في المستودع:
  ```json
  { "extraKnownMarketplaces": { "dynamo": { "source": { "source": "github", "repo": "onestudio-co/dynamo" } } },
    "enabledPlugins": { "dynamo@dynamo": true } }
  ```
  وكل عضو يشغّل مرة واحدة `claude plugin install dynamo@dynamo --scope project`.
- **ربط Flow OS** (اختياري): اربط MCP الستوديو في Claude Code حتى يقرأ الفريق مشروعك من Flow OS. بدونه يشتغل الفريق من المستودع والموقع وما تكتبه له.
- **بديل بلا plugin:** `git clone https://github.com/onestudio-co/dynamo.git` ثم `dynamo/scripts/install.sh /path/to/venture` (ينسخ الوكلاء إلى `.claude/agents/`، المهارات إلى `.claude/skills/`، والمعرفة وقواعد الفريق إلى `.claude/dynamo/`). الأمر يصير `/dynamo` بلا بادئة. أعد تشغيله للتحديث.

**من Flow OS** (بعد الترقية لـ«حيّ»): اكتب `@dynamo` في شات مذكور أو في شات خاص معه. لا تحتاج مفتاح Claude؛ الوكلاء يعملون على حساب Flow OS. يلزم أن تكون عضوًا داخليًا في Flow OS وعضوًا في الـ venture.

**من claude.ai** (صفحة الفريق): رابط يُشارك معك؛ المحادثة على حسابك في claude.ai، ولا يلزم ربط بـ Flow OS.

## كيف يستخدمه أي venture · How a venture uses it

1. **ملف هوية وقواعد المشروع.** انسخي [`venture-profile.template.md`](venture-profile.template.md) إلى مستودع الـ venture باسم `marketing/venture-profile.md` واملئيه. مثال مكتمل: [`ventures/mathkor.md`](ventures/mathkor.md). كل وكيل يقرأه قبل أي عمل.
2. **داخل Claude Code.** ثبّت الـ plugin كما في القسم السابق (أو `scripts/install.sh` كبديل). بعدها: «شغّلي لوّان على خطة الشهر» أو `Agent(subagent_type="dynamo:lawwan")`.
3. **داخل Flow OS.** `discover_agent_repo` على هذا المستودع، ثم `import_agents_from_repo` للوكلاء المطلوبين، ثم `attach_imported_agent_to_venture`. يظهرون على كرت الطاقم موقوفين إلى أن يُشغَّلوا. التحديثات اللاحقة عبر `check_agent_import_updates` ثم `adopt_agents_from_repo`.

## بنية المستودع · Layout

```
dynamo/
├── .claude-plugin/plugin.json       ← بيان الـ plugin
├── .claude-plugin/marketplace.json  ← الـ marketplace (نفس المستودع، source "./")
├── README.md · TEAM.md · dynamo-agents-v2.md
├── venture-profile.template.md      ← ما يملؤه كل venture
├── ventures/mathkor.md              ← المثال المرجعي المكتمل
├── agents/<slug>.md                 ← تعريف كل وكيل فقط (frontmatter متوافق مع Flow OS)
├── knowledge/<slug>/                ← INDEX.md + playbooks/ + experience/ + frameworks/
├── examples/<slug>-starter-prompts.yaml
├── skills/<skill>/SKILL.md          ← مهارات مشتركة (render, publish, audit, report…)
├── characters/                      ← الأفاتارات وصفحة الفريق
├── app/                             ← مصدر صفحة claude.ai
└── scripts/install.sh               ← البديل بلا plugin
```

> `agents/` يحوي ملفات الوكلاء فقط: Claude Code يقرأ هذا المجلد كله (بما فيه المجلدات الفرعية) كوكلاء، لذلك المعرفة في `knowledge/` والوكلاء يشيرون لها عبر `${CLAUDE_PLUGIN_ROOT}/knowledge/<slug>/`.

## الشخصيات · Characters

`characters/`: ورقة شخصية لكل وكيل (`CHARACTERS.md`)، الأفاتارات `png/<slug>-512.png`، المصدر `svg/`، صفحة الفريق `dynamo-team-2400x1256.png`، والمولّد `build_characters.py` (يعيد رسم الـ 13 بأسلوب واحد: فلات بلا خطوط حبر، لوحة One Studio، لمسة برتقالية واحدة).

## ملاحظة الاستيراد إلى Flow OS

المستودع **عام** منذ 2026-11-19، و`discover_agent_repo` يقرأه (14 وكيلًا، 15 مهارة). Flow OS يقرأ `agents/*.md` و`skills/*/SKILL.md` فقط، فنقل المعرفة إلى `knowledge/` لا يؤثر عليه.

## قواعد الملكية · Ownership

- المالكة والمراجِعة: Amal Shurrab. أي تعديل على وكيل يمرّ من هنا ثم يُزامَن إلى Flow OS.
- ما يتعلمه الفريق في venture يُسجَّل في `knowledge/<slug>/experience/` موسومًا `[VENTURE-CONVENTION]` مع التاريخ، ولا يُدمج في النواة إلا إذا ثبت أنه عام.
- الأسماء العشرة قابلة للمراجعة. الـ slug ثابت حتى تُقرَّر الأسماء النهائية.
