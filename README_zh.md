# GPT-6 Astra 中文上手指南

由 **[flaq.ai](https://flaq.ai/) 团队整理的最新 GPT-6 Astra 实用指引**：从第一条指令，到看图分析、联网研究、制作网页、游戏与 3D 场景，帮助你完成第一个可检查的成果。

<!-- languages:start -->
[English](README.md) · **简体中文** · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

**资料核对：2026-09-08** · flaq.ai 团队整理 · 非 OpenAI 官方文档

README 提供 12 种语言，默认首页为英文。深入教程与示例诊断信息目前为简体中文。教程与练习由 flaq.ai 团队整理；案例保留原作者与出处，不代表作者公开了制作提示词，也不保证复现其完整作品。

## 从这里开始：选一个入口

**可以在 ChatGPT、Codex 客户端、Codex CLI 中直接使用 GPT-6 Astra。** 先用 ChatGPT 账号登录、选择 Astra、发送任务，无需先配置 API key。能否选择 Astra 及使用额度取决于账号、工作区和开放阶段。[官方模型说明](https://learn.chatgpt.com/docs/models)

| 目标 | 推荐入口 | 第一步 |
| --- | --- | --- |
| 看图、方案、研究、整理文件 | ChatGPT / Work | 选择 Astra，添加图片或文件 |
| 做网页、修改本地项目、玩 Blender | Codex 客户端 | 打开本地项目文件夹，选择 Astra |
| 在终端读代码、改文件、运行工具 | Codex CLI | 在项目目录执行 `codex -m gpt-6-astra` |

### ChatGPT：上传一张图就开始

1. 登录 ChatGPT 网页或客户端，需要研究和完整交付物时选择 **Work**。
2. 在模型／**Power** 选择器里选择 **Astra**；如有 **Advanced**，展开核对具体型号。
3. 上传本仓库的预算截图，发送：

```text
请复算这张预算图，比较 24 人和 32 人两种情况，固定成本保持不变。
列出总支出、剩余金额，并判断是否满足预算 10% 的预留目标。
交付计算过程与两条调整建议；看不清的数字不要猜。
```

验收：24 人剩 432 元；32 人仅剩 16 元，未达到预留目标。[详细操作](docs/quickstart.md#chatgpt)

### Codex 客户端：打开项目，让它动手

1. 登录 Codex 客户端；统一桌面应用可从产品菜单切换到 **Codex**。
2. 新建项目或打开本仓库所在的本地文件夹，新建任务并选择 **Astra**。
3. 发送下面的指令，再点击它交付的文件检查：

```text
阅读当前仓库说明，运行 examples/field_lab.py，输出到新的目录。
打开预算、分镜和验收报告，解释结果，再生成 32 人的对照版本。
交付文件路径和实际检查结果；缺少环境就说明，不把计划说成已执行。
```

想做 3D，直接让它按 [Blender 趣味指引](docs/blender-playbook.md) 检查环境、运行原创机器人脚本并验收。MCP 或 Computer Use 按任务需要配置。[客户端详细步骤](docs/quickstart.md#codex-app)

### Codex CLI：登录后像聊天一样使用

先按 [官方安装页](https://learn.chatgpt.com/docs/cli) 安装 Codex CLI，再进入你的项目目录执行：

```bash
codex -m gpt-6-astra
```

首次选择 **Sign in with ChatGPT**，在浏览器完成登录。在 Codex 交互界面输入 `/model` 核对 Astra，输入 `/status` 查看会话配置，然后直接描述任务。退出后可在项目目录用 `codex resume --last` 继续。

```bash
# 在本仓库根目录运行，带上原创预算图
codex -m gpt-6-astra -i assets/screenshots/workshop-budget.png "核对预算图与 examples/fixtures/studio-brief.json 是否一致。"
```

[安装、登录、模型选择与排错完整指引](docs/quickstart.md#codex-cli)。没有 Astra 时先检查更新与账号权限，命令不能绕过开放限制。无需 API key 不等于不消耗账号额度。

## 运行本项目原创实验

三套独立编写的练习共用一份虚构工作室资料。下图是本地程序生成 SVG 报告后取得的真实浏览器截图，不是第三方作品或 Astra API 实测输出。

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![工作坊预算：支出 2,168 元，预留 432 元。](assets/screenshots/workshop-budget.png)

工作坊预算：支出 2,168 元，预留 432 元。

![分镜时间轴：20 秒、30 fps，连续 600 帧。](assets/screenshots/craft-storyboard.png)

分镜时间轴：20 秒、30 fps，连续 600 帧。

![发布验收：5 项虚构检查通过 3 项，2 项待修复。](assets/screenshots/release-review.png)

发布验收：5 项虚构检查通过 3 项，2 项待修复。

[源码、复现步骤与练习](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

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

## API：需要接入自己的产品时再看

日常聊天、项目制作和终端协作先用上面的三条入口。开发自己的应用时，再看 [API 进阶说明](docs/api.md) 和 [Python / JavaScript 示例](examples/README.md)。

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

## 玩点有趣的：让小机器人自己组装

新增六种原创 Blender 练习：桌面机器人、零件组装、迷你阅读角、纸电路短片、蘑菇吉祥物与场景找茬。提供中英文提示词、工具准备、帧数验收和原创脚本。脚本仅通过 Python 语法检查，尚未在 Blender 中实跑，未新增模型实测截图。

[打开 Blender 趣味指引](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

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

## 引用来源与创作启发

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

公众号：数字生命卡兹克；作者：卡兹克、可达；2026-09-08。用于工具协作与分阶段创作的选题启发；不转载文章图片或长提示词。
