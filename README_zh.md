# GPT-6 Astra 中文上手指南

由 **[flaq.ai](https://flaq.ai/) 团队整理的最新 GPT-6 Astra 实用指引**：从第一条指令，到看图分析、联网研究、制作网页、游戏与 3D 场景，帮助你完成第一个可检查的成果。

<!-- languages:start -->
[English](README.md) · **简体中文** · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

**资料核对：2026-09-08** · flaq.ai 团队整理 · 非 OpenAI 官方文档

README 提供 12 种语言，默认首页为英文。深入教程与示例诊断信息目前为简体中文。教程与练习由 flaq.ai 团队整理；案例保留原作者与出处，不代表作者公开了制作提示词，也不保证复现其完整作品。

## 从这里开始

| 你想做什么 | 建议入口 | 完成后得到什么 |
| --- | --- | --- |
| 不写代码，先试用 | [零基础入门](docs/quickstart.md#不用写代码) | 一份可检查的任务成果 |
| 用代码调用 Astra | [API 快速开始](docs/quickstart.md#用-api-开始) | 第一次 Python / JavaScript 请求 |
| 看有哪些强大玩法 | [12 个精选案例](docs/cases.md) | 原帖、作品、复现练习与验收要求 |
| 复制指令开始做 | [6 套实战工作流](docs/workflows.md) | 网页、游戏、3D、视频、研究和代码审查提示词 |
| 看图、研究、提取 JSON | [代码示例说明](examples/README.md) | 4 种 Python 调用模式 |
| 解决报错与控制成本 | [排错与费用](docs/quickstart.md#常见问题) | 权限、限流、输出截断等问题的处理方法 |

## Astra 是什么

GPT-6 Astra 是 OpenAI 面向复杂任务的模型，适用于推理、编程、研究，以及结合工具的多步骤工作。它可以接收文字和图片、输出文字；浏览器、代码运行和图像生成等能力需要相应工具或产品环境。

| 项目 | 官方文档所列信息 |
| --- | --- |
| API 模型名 | `gpt-6-astra` |
| 上下文窗口 | 1,050,000 tokens |
| 最大输出 | 128,000 tokens |
| 知识截止 | 2026-04-30；新信息需要检索 |
| 推理强度 | `low`、`medium`、`high`、`xhigh`、`max` |
| 输入 / 输出 | 文字和图片输入；文字输出 |
| 标准文本价格 | 每百万 tokens：输入 $10，缓存输入 $1，输出 $50 |

规格来自 [官方模型页](https://developers.openai.com/api/docs/models/gpt-6-astra)。价格和权限可能变化；超过 272K 输入 tokens 的长请求有不同费率，工具调用另计，详见官方页面。产品订阅与 API 使用权限应分别确认。

“能制作视频”通常指组织工具完成工作，例如规划分镜、编写动画代码、调用素材工具、渲染和剪辑，不等于 Astra 模型端点原生接收或输出视频。

## 一眼看看可以做什么

### 从参考图到 Blender 模型

![Tom Krcha 蒸汽火车作品在参考仓库中的真实页面截图](assets/screenshots/steam-train-reference.png)

Tom Krcha 的作品展示。截图采集自参考仓库，模型与预览属于原作者。[原帖](https://x.com/tomkrcha/status/2095756085890310311) · [学习路线](docs/cases.md#case-04)

### 可交互的 iPhone 历史档案

![Interactive iPhone History 在线页面实拍](assets/screenshots/iphone-archive.png)

bluedev 的在线作品。[在线体验](https://iphone-archive.vercel.app/) · [原帖](https://x.com/blueemi99/status/2096917792737911131) · [案例解析](docs/cases.md#case-07)

### 首尔三维地图

![Seoul 3D Atlas 城市与日落模式实拍](assets/screenshots/seoul-atlas.png)

synabreu 的在线作品，已检查 City 标签与 Sunset 模式切换。[在线体验](https://seoul-3d-atlas.synabreu.chatgpt.site/) · [原帖](https://x.com/synabreu/status/2096557555086725159)

更多截图见 [精选案例](docs/cases.md) 和 [截图来源清单](assets/screenshots/README.md)。

## 第一个练习：把任务说清楚

在产品中选择你有权限使用的 Astra 模型，粘贴下面的指令：

```text
请帮我把咖啡店活动想法整理成可执行方案。
背景：周末两天，已有门店和社交账号，预算上限 2000 元。
目标：让首次到店的顾客愿意再次光顾。
交付：活动规则、两天执行清单、预算表、三条宣传文案。
约束：不要虚构门店数据；缺少的普通信息做合理假设并标明。
验收：预算合计不超过上限；每个行动有负责人角色和时间。
```

检查结果后，再追加：“把执行清单改成只需要两位店员的版本，保留预算上限。”从小成果开始，练习补充要求和迭代。

## 最小代码示例

安装官方 Python SDK：`python3 -m pip install -U openai`。按 [快速开始](docs/quickstart.md#用-api-开始) 设置 `OPENAI_API_KEY`，再运行：

```python
from openai import OpenAI

client = OpenAI()
response = client.responses.create(
    model="gpt-6-astra",
    reasoning={"effort": "low"},
    input="用三个步骤解释：第一次使用 AI 编程，如何验收生成的代码？",
    max_output_tokens=4096,
)
print(response.output_text)
```

这是教学最小示例。完整示例支持离线预览、失败处理和用量显示，根据 [官方快速开始](https://developers.openai.com/api/docs/quickstart) 编写。本次未进行付费 API 调用，不把模拟测试称为模型效果验证。

```bash
# Python 3.10+，完整示例只用标准库，无需安装依赖
python3 examples/astra.py text --dry-run
python3 examples/astra.py text
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
```

这些示例直接调用 **OpenAI API**，使用 OpenAI 密钥；Flaq.ai 的模型目录与接口配置需另外确认。

## 怎么让复杂任务更容易成功

1. **给材料**：参考截图、现有文件、目标用户和约束，比“高级一点”有用。
2. **先做小版本**：网页先做好一个页面，游戏先做好一个关卡，3D 先确定比例。
3. **写清交付物**：文件名、格式、启动方式、截图、检查结果。
4. **指定验收**：按钮可点击、总价能复算、模型可编辑，而不只是画面好看。
5. **根据证据迭代**：反馈截图、错误信息和期望行为，每次集中修一类问题。

这些是本指南的教学建议。异步工具调用、执行中调整指令等进阶能力请看 [官方模型使用指南](https://developers.openai.com/api/docs/guides/latest-model)，它们需要应用端配合。

## 资料与贡献

- [官方来源与核对说明](docs/sources.md)
- [验证记录](docs/verification.md)
- [贡献说明](CONTRIBUTING.md)
- 原创文档和代码沿用 [MIT License](LICENSE)；第三方案例、品牌、截图内作品和外链代码保留各自权利，不因本仓库许可证而重新授权。

## 关于 flaq.ai

[flaq.ai](https://flaq.ai/) 为 AI Agent 和生产应用提供图片、视频、音乐及语言模型的统一 API 接入。我们整理这份最新指引，希望通过可运行的示例、真实截图和清晰的验收方法，让更多人理解、尝试并评估 AI 的实际能力。

团队开源工作流：[Backlink Skills](https://github.com/flaqai/backlink_skills)。

## 联盟营销与合作支持

欢迎创作者、开发者和教育者加入 **[Flaq.ai 联盟营销计划](https://flaq.ai/zh/affiliate-program/)**，通过自己的推广链接，在教程、评测和集成指南中推荐 Flaq.ai。

- 推荐用户的首笔有效付费订单：**20% 佣金**。
- 后续有效付费订单：**10% 佣金**。
- 有效订单归因窗口：推荐用户**注册后 60 天内**。

登录后完善联盟资料，即可在联盟中心创建推广链接、跟踪推荐并设置收款方式。分享推广链接时应明确披露联盟关系。有效订单、审核和结算以现行 [联盟协议](https://flaq.ai/affiliate-agreement/) 为准，不保证收益。

**[访问 flaq.ai](https://flaq.ai/) · [加入联盟营销计划](https://flaq.ai/zh/affiliate-program/)**
