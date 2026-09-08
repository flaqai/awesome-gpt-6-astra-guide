# 可以直接运行的代码示例

[中文首页](../README_zh.md) · [English](../README.md) · [设置 API key](../docs/quickstart.md#用-api-开始)

这些是本仓库编写的教学示例，不是社区作品源码。Python 文件使用标准库，JavaScript 文件使用 Node.js 内置 `fetch`；不用安装 SDK。首页另有一个官方 Python SDK 风格的最小示例。

**要求**：Python 3.10+ 或 Node.js 20+；真实调用需要 `OPENAI_API_KEY` 和模型权限。所有命令在仓库根目录运行。

| 模式 | 输入 | 输出 | 如何验收 |
| --- | --- | --- | --- |
| `text` | 中文任务描述 | 文本与 token 用量 | 是否符合条数、目标和约束 |
| `vision` | 本地 PNG / JPEG / WebP | 截图的布局与组件分析 | 将每条结论与原图比对 |
| `research` | 默认的官方文档研究问题 | 文本与 API 返回的引用链接 | 打开链接，核对结论是否有支持 |
| `extract` | 模拟会议记录 | 严格 JSON 结构 | 行动、负责人是否正确；缺失截止时间为 null |

## 01 · 文本与需求拆解

```bash
python3 examples/astra.py text --prompt '将咖啡店预约页面拆成 5 个可验收功能。'
```

入口：[astra.py](astra.py) 中的 `build_request()`。模型不会运行生成的代码；得到文本之后，再交给开发环境实施。

## 02 · 看图分析

```bash
python3 examples/astra.py vision \
  --image assets/screenshots/iphone-archive.png \
  --prompt '列出截图中可见的按钮和布局，给出制作类似界面的组件树。不要推断未展示的交互。'
```

示例把本地图片编码成 data URL，放在 `input_image` 中。真实请求会上传这张图片。10 MB 是本示例的自设限制，不是官方上限。[官方图片输入说明](https://developers.openai.com/api/docs/guides/images-vision)

**验收**：组件树能对应到截图，且没有声称看到了未展示的数据库、交互或其他页面。想复刻 UI，继续使用 [网页工作流](../docs/workflows.md#workflow-web)。

## 03 · 带来源的联网研究

```bash
python3 examples/astra.py research --output outputs/research-response.json
```

工具配置核心：

```python
{"type": "web_search", "filters": {"allowed_domains": [
    "developers.openai.com", "platform.openai.com", "learn.chatgpt.com"
]}}
```

本例只检索 OpenAI 官方站点；修改研究领域时，也要修改域名过滤。本例收集 `output_text.annotations` 中的 `url_citation`，在终端追加来源，完整响应保留原始标注位置。做网页展示时，应把引用放到对应结论附近。[官方 Web search 指南](https://developers.openai.com/api/docs/guides/tools-web-search)

**验收**：至少核对一条原始来源；若无引用，则不能当作已完成的有据研究。搜索工具和文本处理可能分别产生费用。

## 04 · 从会议记录提取 JSON

```bash
python3 examples/astra.py extract
```

期望结构示意（这是人工编写的格式示例，非实测回答）：

```json
{
  "items": [
    {"task": "整理首页截图", "owner": "小林", "deadline": "周五前"},
    {"task": "检查移动端", "owner": "小周", "deadline": null}
  ]
}
```

Responses API 用 `text.format` 设置 `json_schema`，并使用 `strict: true`。Schema 要求字段完整，用 `null` 表达未知内容，不把缺失信息编出来。结构约束不等于事实正确，仍需核对原文。[官方 Structured Outputs 文档](https://developers.openai.com/api/docs/guides/structured-outputs)

## 05 · JavaScript

```bash
node examples/quickstart.mjs --dry-run
node examples/quickstart.mjs
```

入口：[quickstart.mjs](quickstart.mjs)。只在 Node.js 服务端环境运行，不要将 API key 放进网页前端。

## 离线检查与真实调用的区别

所有 Python 模式都支持 `--dry-run`；视觉模式仍需一个真实本地文件，但不输出 base64 内容、不发送网络请求。它只验证请求构造，不验证服务器接受请求。

```bash
python3 examples/astra.py extract --dry-run
python3 -m unittest discover -s tests -v
```

离线测试覆盖结果解析、拒绝、截断、缺密钥和 HTTP 错误等边界。没有真实 API 结果截图，也没有性能或费用实测。详见 [验证记录](../docs/verification.md)。
