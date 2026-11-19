---
name: strategy-memo
description: Write a venture's go-to-market strategy documents in One Studio's agency-report style: the segment scoring matrix, the 90-day plan with channel gates, the three Idea-stage exit documents (problem memo with external why-now, buyer count with source, top-3 risky assumptions with dated tests), Lean Canvas edits for Flow OS, and the weekly KPI review. Use whenever mukhattit, or any Dynamo agent, must produce or update strategy text.
---

# strategy-memo

## Style (non-negotiable)
Formal Modern Standard Arabic. Plain section labels («الملخص التنفيذي», «الشرائح المرشّحة», «مؤشرات الأداء الرئيسية»).
Lead every section with the number. No slogans, metaphors, "ليس X بل Y", dramatic half-sentences or emojis. No
"بيانات مطلوبة / من يوفره" columns and no "صالح للنشر" labels; list only what is still needed. No security notes.
Numbers carry a source and date or `[تقدير]` with the method.

## 1. Segment scoring matrix
Columns: الشريحة · شدة الألم (×3) · سهولة الوصول (×2) · الاستعداد للدفع (×3) · العدد التقريبي ومصدره (×1) · ملاءمة
المنتج (×2) · المجموع الموزون. Write the decision rule and the decision date ABOVE the table. Every count has a source
line under it (registry, platform merchant count, directory export, LinkedIn filter count, with the date).

## 2. The 90-day plan
Sections in this order: الملخص التنفيذي · الوضع الحالي · الشرائح ومصفوفة التقييم · مدخلات التموضع · القنوات بالترتيب
(each with its gate number) · خطة 12 أسبوعًا (week · goal · activities · owner · KPI · gate) · الفرضيات والاختبارات ·
مؤشرات الأداء (≤5) · الميزانية والافتراضات · القرارات المطلوبة · خطة العمل التنفيذية (the detailed task list).
Rule: one channel at a time. The plan names the number that opens the next channel.

## 3. Idea-stage exit documents (Flow OS)
**مذكرة المشكلة:** المشكلة بكلمات المشتري · من يعاني منها · ماذا يفعلون اليوم · «لماذا الآن» بحقيقة خارجية مؤرّخة
(تغيير منصة، تنظيم، رقم منشور) · ما الذي نختبره أولًا. One page.
**عدد المشترين التقريبي:** الشريحة · الطريقة · الرقم · المصدر · التاريخ · التحفّظ.
**أخطر ثلاث فرضيات:** table: الفرضية · لماذا خطرة · الاختبار · حدّ النجاح · التاريخ · المسؤول · النتيجة. Thresholds are
written before the test runs. Results are logged in Flow OS as evidence (`add_evidence` / `add_rule_proof`) by
mudawwin after the reviewer's yes.

## 4. Lean Canvas update protocol
Read the current canvas (`get_lean_canvas`). Propose edits as a diff: block · current text · proposed text · basis.
Only the reviewer approves; mudawwin applies via `update_canvas_item` / `set_lean_canvas_uvp` and records the date.

## 5. Weekly KPI review
```
المراجعة الأسبوعية · الأسبوع <n> · <from–to>
| المؤشر | المخطّط | الفعلي | الفرق | الملاحظة |
الاختبارات المغلقة: <assumption → pass/fail with the number>
القرار المقترح: <one decision> · الأساس: <evidence>
تعديلات الخطة: <lines moved, cut or added>
بريفات الأسبوع: <agent → task → done-when>
```
Append the decision to `marketing/strategy/decisions-log.md` (date · decision · who decided · basis).

## Gates
Two routes first for any big choice; the owner picks. Internal/friendly data is never market evidence. Every claim has a
source or an `[estimate]` label. The reviewer approves before anything reaches Flow OS.
