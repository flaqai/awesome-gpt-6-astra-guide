# Authorship and provenance / 创作与来源记录

[English](../README.md) · [中文](../README_zh.md) · [Asset manifest](../assets/screenshots/manifest.json)

## What changed on 2026-09-08

The current guide replaces its three community artwork screenshots with independently designed budget, storyboard, and release reports. The new visual system, paper-circuit illustrations, fictional input data, and calculation/rendering code were written for this repository. This is a change in subject matter, implementation, and teaching method, rather than a recoloring or renaming of someone else's work.

| Material | Origin and scope |
| --- | --- |
| `examples/field_lab.py` | New standard-library implementation of budget calculations, frame intervals, evidence comparisons, and SVG rendering |
| `examples/fixtures/studio-brief.json` | Original fictional teaching data; no customer data or model response |
| `assets/originals/*.svg` | Direct generator output; editable vectors with no embedded external artwork |
| `assets/screenshots/*.png` | Actual browser captures of those local SVGs |
| Python and JavaScript API clients | Guide-authored teaching clients; updated to analyze original lab evidence. Standard request fields and endpoint names follow official API documentation |
| README gallery and practice cases | Rewritten around the original lab; community links are now separate reading material |
| External references | Authors and original links remain attributed; this project does not claim ownership of linked works |

The earlier reference repository was used for discovering community examples. [Source records](sources.md) retain that history. The language navigation and flaq.ai background reference [Backlink Skills](https://github.com/flaqai/backlink_skills). Neither repository supplies the new lab's code or artwork. The standard OpenAI API schema is kept intact for compatibility; disguising API field names would break the examples rather than add originality.

The shipped original code and assets are covered by [MIT](../LICENSE). External works and trademarks retain their own rights. Old screenshots may remain in Git history; this change replaces the current files and does not rewrite history. The file manifest documents reproducibility, not an independent legal determination of authorship.

## 中文说明

这次差异化包含原创主题、数据、计算逻辑、视觉布局、程序绘图以及配套练习。首页不再用外部作者作品作为本项目的展示图；外部案例仅保留署名链接，避免把别人的成果换上自己的品牌。API 协议字段和官方资料链接继续保留，不为追求表面差异破坏兼容性。

这些改动有助于清楚说明本项目独立完成了什么，但不保证不会发生相似性争议或收到投诉。后续加入外部素材时，仍需记录其来源和适用许可。
