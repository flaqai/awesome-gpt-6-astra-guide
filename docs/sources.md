# 来源与核对方法

[中文首页](../README_zh.md) · [English](../README.md)

核对日期：**2026-09-08**。官方资料优先用于模型、API 和产品事实；社区目录用于发现作品；在线页面用于核对视觉展示。下表中的页面均已通过网页工具读取，参考目录另进行了浏览器实时核对。

| 来源 | 用途 |
| --- | --- |
| [GPT-6 Astra 官方模型页](https://developers.openai.com/api/docs/models/gpt-6-astra) | 模型标识、输入输出、上下文、价格 |
| [官方模型使用指南](https://developers.openai.com/api/docs/guides/latest-model) | 推理强度、参数兼容、进阶能力 |
| [API 快速开始](https://developers.openai.com/api/docs/quickstart) | 第一次调用、SDK 用法 |
| [产品快速开始](https://learn.chatgpt.com/docs/quickstart) | ChatGPT / Codex 产品入口；原 developers.openai.com/codex/quickstart 重定向至此 |
| [图片与视觉](https://developers.openai.com/api/docs/guides/images-vision) | `input_image` 与 base64 图片输入 |
| [Web search](https://developers.openai.com/api/docs/guides/tools-web-search) | 搜索工具、域名过滤、引用 |
| [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | `text.format`、严格 JSON Schema |
| [参考案例目录](https://github.com/magiccreator-ai/awesome-gpt-6-astra) | 发现作品、作者、原帖与外链 |

## 案例发现记录（仅用于溯源）

早期案例发现记录对应社区目录提交 [90cbefd](https://github.com/magiccreator-ai/awesome-gpt-6-astra/commit/90cbefd35c9fc5e3cd2e3c3ba55f8e15975fc498)。这里保留来源路径，以便核对早期案例的发现出处；旧截图已从当前目录移除。本指南的品牌介绍、教程组织与多语言 README 由 flaq.ai 团队负责。

[社区延伸阅读](community-references.md) 保留原帖链接，供读者直接查看作者说明。本次没有逐一读取所有 X 原帖；不把目录转述升级成独立验证，也没有照搬整份目录。制作耗时、帧率、物体数量和“一次提示完成”等说法不作为本指南的能力保证。

## 三类内容如何区分

1. **官方事实**：附对应官方页面，随来源更新。
2. **社区作品**：保留作者和来源，注明本次核对范围。
3. **教学内容**：本仓库的提示词、步骤、验收方法和代码为原创练习；示意输出显式标记，不伪装成真实调用结果。

`latest-model` 是动态地址，未来内容可能变化。阅读旧版本指南时，应重新核对模型名和参数。API 文档中的支持能力，也不等于你当前账号已获得全部产品入口或工具权限。

## 多语言与 flaq.ai 说明

- [Backlink Skills](https://github.com/flaqai/backlink_skills)：参考语言切换方式与 flaq.ai 的统一 API 介绍；本指南默认语言为英文。
- [Flaq.ai 联盟计划](https://flaq.ai/affiliate-program/) / [中文页面](https://flaq.ai/zh/affiliate-program/)：核对加入入口、首单 20%、后续订单 10% 和注册后 60 天归因窗口。
- [联盟协议](https://flaq.ai/affiliate-agreement/)：核对订单资格、审核、结算及联盟关系披露。

上述联盟页面与协议于 2026-09-08 读取；各语言 README 使用同一规则摘要，具体以官方现行条款为准。README 链接是公开入口，没有虚构专属推广码或替任何人注册联盟账户。Flaq.ai 团队署名由项目维护者要求加入；示例仍直接调用 OpenAI API，不据此声称 Flaq.ai 已支持 Astra。

## 当前原创实验

当前展示使用本项目的原创数据、计算程序、SVG 和浏览器截图，详见 [创作记录](originality.md) 与 [截图清单](../assets/screenshots/README.md)。这些截图不是付费 API 结果或第三方作品。

## 新增：Blender 趣味创作来源（2026-09-08）

- [《用GPT-6 Astra操控Blender玩3D，保姆级教程来了。》](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)：公众号数字生命卡兹克，署名卡兹克、可达。已在浏览器中读取正文、标题和作者。用于 [趣味指引](blender-playbook.md) 的工具协作思路，不转载其图片或长提示词，不把作者的耗时、额度和演示结果升级为本项目实测。
- [Blender Lab MCP Server](https://www.blender.org/lab/mcp-server/)：已读取，确认 Blender 5.1+、扩展、客户端与服务端的要求。
- [Blender 命令行参数](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)：已读取，确认后台脚本执行和 Python 错误退出码参数。
- [OpenAI Computer Use](https://learn.chatgpt.com/docs/computer-use) 与 [MCP 指引](https://learn.chatgpt.com/zh-Hans/docs/extend/mcp)：核对客户端插件与工具连接方式。

新增桌面机器人脚本由本指南独立编写，仅验证 Python 语法，未在 Blender 实跑。所有语言 README 底部都保留微信原文链接、署名与引用范围。

## 客户端优先入门更新（2026-09-08）

[官方模型选择](https://learn.chatgpt.com/docs/models)、[产品快速开始](https://learn.chatgpt.com/docs/quickstart)、[Codex CLI](https://learn.chatgpt.com/docs/cli) 已读取，用于核对 ChatGPT / Work、桌面 Codex、Astra 选择器和 CLI 的 ChatGPT 登录路线。`codex -m gpt-6-astra` 来自官方模型页；`-m`、`-i`、`resume --last` 同时与本机 CLI 帮助核对。没有据此保证所有账号已开放 Astra，也未进行新的付费会话验证。

首页不再将 API key、JSON 参数和 token 计费作为入门要求；这些内容保留在 [API 进阶说明](api.md)。微信文章继续位于所有 README 底部，作为 Blender 创作启发来源。

## X 社区检索（2026-09-22）

新增 [X 使用场景指引](x-playbook.md) 与 [结构化来源清单](research/x-sources-2026-09-22.json)。直接读取七条 X 原帖及部分作者回复，按创作者演示、品牌展示、推广内容、研究主张和个人经验标明来源性质。八项练习中，字幕和调色引用同一原帖，不计作独立交叉验证。

查询包括 `GPT-6 Astra`、`from:JaydenCoach Astra`、`"Astra" (Excel OR spreadsheet OR slides)`。网页搜索只用于发现线索；最终收录均回到 X 阅读正文。历史研究条目的作者以实际原帖显示的 `@deredleritt3r` 为准，未沿用报道中的旧用户名链接。

日期分别记录原帖显示日期与读取日期。本次没有核验付费服务、视频全部内容、性能或研究结论，没有下载第三方媒体和源码。新增提示词、虚构库存数据及验收方法是本指南原创教学内容，不是原作者提示词。
