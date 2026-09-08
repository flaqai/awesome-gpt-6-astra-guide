# دليل GPT-6 Astra العملي

أحدث دليل عملي لـ GPT-6 Astra من إعداد **فريق [flaq.ai](https://flaq.ai/)**، ويشمل أساسيات النموذج، وخطوات البدء، وأمثلة برمجية قابلة للتشغيل، ومسارات عمل إبداعية، ولقطات شاشة حقيقية.

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · **العربية**
<!-- languages:end -->

آخر مراجعة: 2026-09-08. هذا دليل مستقل أعدّه الفريق، وليس وثائق OpenAI الرسمية. تتوفر ملفات README بـ 12 لغة، بينما الدروس التفصيلية ورسائل التشخيص متاحة حاليًا بالصينية المبسطة.

[البدء](docs/quickstart.md) · [12 حالة استخدام](docs/cases.md) · [6 مسارات عمل](docs/workflows.md) · [أمثلة برمجية](examples/README.md)

## ما هو Astra؟

Astra نموذج من OpenAI للاستدلال المعقد والبرمجة والبحث والمهام متعددة الخطوات. يستقبل نصوصًا وصورًا ويُخرج نصوصًا. يتطلب التصفح وتشغيل البرامج وإنتاج الفيديو أدوات مناسبة في التطبيق الذي تستخدمه.

| النموذج | `gpt-6-astra` |
| --- | --- |
| السياق | 1,050,000 tokens |
| الحد الأقصى للمخرجات | 128,000 tokens |
| مستوى الاستدلال | `low` · `medium` · `high` · `xhigh` · `max` |

[وثائق النموذج الرسمية](https://developers.openai.com/api/docs/models/gpt-6-astra) · [الإعدادات والميزات المتقدمة](https://developers.openai.com/api/docs/guides/latest-model)

## ابدأ دون كتابة كود

اختر Astra في منتج تملك صلاحية استخدامه، وأرفق المواد المطلوبة، وابدأ بنتيجة صغيرة. مثال:

```text
خطط لفعالية لمدة يومين في مقهى بميزانية 2000 يوان وموظفين اثنين. قدم القواعد والجدول الزمني وتفاصيل الميزانية وثلاث رسائل ترويجية. تحقق من مجموع التكاليف ووضح الافتراضات.
```

## شغّل المثال الأول

استخدم Python 3.10+ أو Node.js 20+ من المجلد الرئيسي للمستودع. تعتمد البرامج المرفقة على المكتبات المدمجة ولا تتطلب تثبيت حزم. عاين الطلب مجانًا أولًا:

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

قبل الاستدعاء الحقيقي، اضبط `OPENAI_API_KEY` في الطرفية باستخدام مفتاح مشروع OpenAI يملك وصولًا إلى Astra. راجع [خطوات الإعداد](docs/quickstart.md#用-api-开始). لا تضع المفاتيح في الكود أو الصور. لا يتصل `--dry-run` بالشبكة، أما الطلبات الحقيقية فتترتب عليها رسوم. تستخدم الأمثلة OpenAI API مباشرة؛ تحقق بشكل منفصل من توفر النموذج لدى Flaq.ai.

```bash
python3 examples/astra.py text --prompt 'خطط لفعالية لمدة يومين في مقهى بميزانية 2000 يوان وموظفين اثنين. قدم القواعد والجدول الزمني وتفاصيل الميزانية وثلاث رسائل ترويجية. تحقق من مجموع التكاليف ووضح الافتراضات.'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[أمثلة برمجية](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## مشروعات ولقطات شاشة حقيقية

التُقطت الصور التالية من المتصفح فعلًا. تبقى حقوق الأعمال لأصحابها، ولم تُعَدْ صناعة المشروعات كاملةً هنا.

![قطار Tom Krcha البخاري: لقطة للصفحة التي تعرض معاينة صاحب العمل.](assets/screenshots/steam-train-reference.png)

قطار Tom Krcha البخاري: لقطة للصفحة التي تعرض معاينة صاحب العمل. [المنشور الأصلي](https://x.com/tomkrcha/status/2095756085890310311)

![iPhone Archive من bluedev: صفحة عامة فُتحت في المتصفح.](assets/screenshots/iphone-archive.png)

iPhone Archive من bluedev: صفحة عامة فُتحت في المتصفح. [المنشور الأصلي](https://x.com/blueemi99/status/2096917792737911131) · [المشروع المباشر](https://iphone-archive.vercel.app/)

![Seoul 3D Atlas من synabreu: تم التحقق من التبديل إلى City وSunset.](assets/screenshots/seoul-atlas.png)

Seoul 3D Atlas من synabreu: تم التحقق من التبديل إلى City وSunset. [المنشور الأصلي](https://x.com/synabreu/status/2096557555086725159) · [المشروع المباشر](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[مصادر الصور](assets/screenshots/README.md) · [12 حالة استخدام](docs/cases.md)

## مسارات عمل عملية

أنشئ أصغر نسخة تعمل، ثم حسّنها بناءً على الصور والأخطاء ومعايير القبول. اطلب ملفات قابلة للتحرير وتعليمات تشغيل ولقطات للنتيجة الفعلية.

[6 مسارات عمل](docs/workflows.md)

## التحقق والمساهمة

نجحت الأمثلة في 17 اختبارًا دون اتصال. لم تُنفذ استدعاءات API مدفوعة أو إعادة إنتاج كاملة للمشروعات. [سجل التحقق](docs/verification.md) · [المصادر](docs/sources.md) · [المساهمة](CONTRIBUTING.md). المحتوى والكود الأصليان تحت ترخيص [MIT](LICENSE)، مع احتفاظ مواد الأطراف الأخرى بحقوقها.

## عن flaq.ai

توفر [flaq.ai](https://flaq.ai/) واجهة API موحدة للوصول إلى نماذج الصور والفيديو والموسيقى واللغة لوكلاء الذكاء الاصطناعي والتطبيقات الإنتاجية. يشارك فريقنا طرقًا عملية من خلال هذا الدليل. مسارات عمل مفتوحة المصدر: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## التسويق بالعمولة ودعم الشركاء

يمكن للمبدعين والمطورين والمعلمين الانضمام إلى [برنامج Flaq.ai للتسويق بالعمولة](https://flaq.ai/affiliate-program/) ومشاركة الدروس والمراجعات وأدلة التكامل باستخدام رابط الإحالة الخاص بهم.

عمولة **20%** على أول طلب مدفوع صالح للمستخدم المُحال، و**10%** على الطلبات التالية. يجب أن تقع الطلبات المؤهلة خلال **60 يومًا بعد تسجيل المستخدم المُحال**.

سجّل الدخول وأكمل ملفك لإدارة الروابط وتتبع الإحالات وإعداد الدفعات. أفصح بوضوح عن علاقة التسويق بالعمولة عند المشاركة. تخضع الأهلية والمراجعة والصرف لـ[الاتفاقية السارية](https://flaq.ai/affiliate-agreement/)، ولا توجد ضمانات للأرباح.
