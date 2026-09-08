# 从零开始使用 GPT-6 Astra

[中文首页](../README_zh.md) · [English](../README.md) · [查看案例](cases.md) · [代码说明](../examples/README.md)

## 不用写代码

**先看模型是否可选。** 登录你正在使用的 ChatGPT / Codex 产品，在可用模型列表中确认 GPT-6 Astra。入口和可见选项随产品、账号与发布阶段变化；找不到时先查账号权限，不要把其他模型的结果标成 Astra。产品操作以 [官方入门文档](https://learn.chatgpt.com/docs/quickstart) 为准。

1. 新建任务。第一次先选一个小目标，如一页活动方案或一个待办页面。
2. 选 Astra；若能设置推理强度，普通练习先用较低强度，复杂任务再提高。
3. 加入材料：目标用户、参考图片、已有文件、截止时间、输出格式。
4. 发送“目标 + 材料 + 约束 + 交付物 + 验收标准”。[工作流](workflows.md) 有完整模板。
5. 检查实际成果，再反馈需要改变的部分。不要只看“已经完成”的文字总结。

**预期结果**：你拿到可以阅读、打开或运行的成果。若只收到计划，追加：“请按上面的范围继续完成，交付文件，并说明实际检查结果。”

### 在 Codex 里做第一个项目

打开一个空的项目文件夹，发送：

```text
在当前项目里做一个本地待办页面。
功能：新增、完成、删除待办，刷新后保留记录。
外观：中文，浅色，手机上单列显示；优先使用项目已有技术。
交付：源文件、启动步骤、一张实际运行截图。
验收：新增“买咖啡”后能勾选、删除；刷新后数据仍存在。
先完成最小版本；常规设计细节由你决定并说明。
```

你需要做的是打开成果、逐项点击验收。如果浏览器或文件工具未启用，模型只能给出代码和操作说明；需要在产品环境中提供相应工具，才能代你运行。

## 用 API 开始

API 适合把 Astra 接入自己的脚本或应用。使用有模型权限的 OpenAI API 项目和密钥，并确认计费设置；不要默认聊天订阅包含 API 额度。[官方 API 快速开始](https://developers.openai.com/api/docs/quickstart)

### 1. 准备环境

下载本仓库，进入仓库目录。完整 Python 示例只用标准库，要求 Python 3.10+；JavaScript 示例要求 Node.js 20+。不需要同时安装两种环境。

```bash
python3 --version
# 使用 JavaScript 才需要下面这条
node --version
```

Windows 可用 `python` 代替 `python3`。后面的所有相对路径都以仓库根目录为起点。

### 2. 先免费预览请求

```bash
python3 examples/astra.py text --dry-run
```

**预期结果**：终端显示包含 `model: gpt-6-astra`、`input` 和 `reasoning` 的 JSON。此模式不联网、不需要密钥，也不会返回模型答案。它帮助你看清即将发送的内容。

### 3. 设置密钥

macOS / Linux，可用隐藏输入方式设置，避免把密钥写入命令历史：

```bash
# 启动 Bash，以下提示符语法按 Bash 执行
bash
read -r -s -p 'OpenAI API key: ' OPENAI_API_KEY
export OPENAI_API_KEY
```

Windows PowerShell：

```powershell
$astraSecureKey = Read-Host 'OpenAI API key' -AsSecureString
$env:OPENAI_API_KEY = [System.Net.NetworkCredential]::new('', $astraSecureKey).Password
```

密钥仅在当前终端会话及其子进程生效。不要放进浏览器代码、截图或提交到 Git；本示例不自动读取 `.env` 文件。

### 4. 发出第一次请求

```bash
python3 examples/astra.py text
# 或者使用 JavaScript 版本
node examples/quickstart.mjs
```

**预期结果**：打印中文回答，并在终端显示 token 用量。实际措辞每次可能不同。请求可能需要一段时间；本示例超时设为 180 秒，不自动重试。

### 5. 替换成自己的任务

```bash
python3 examples/astra.py text \
  --prompt '为个人作品集网站写一份需求清单，包括首页、案例和联系方式。' \
  --output outputs/portfolio-response.json
```

`--output` 保存完整 API 响应，文件已存在会报错，避免覆盖之前的成果。可用它检查 `status`、`output` 和 `usage`。

### 6. 看图、联网和结构化提取

```bash
# 图片会发送到 OpenAI API；先使用仓库里的公开案例截图
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png

# 联网检索 OpenAI 官方文档，输出引用来源
python3 examples/astra.py research

# 把模拟会议记录提取成 JSON
python3 examples/astra.py extract
```

更详细的输入、输出和验收方法见 [代码示例](../examples/README.md)。

## 推理强度怎么选

本指南建议：简单分类、短文本先试 `low`；有多个约束的任务再试 `medium` 或 `high`；确有复杂推理需求时评估 `xhigh` / `max`。不要把更高强度视为必然更好，比较结果、用时与费用。

Astra API 支持的强度是 `low`、`medium`、`high`、`xhigh`、`max`。`none` / `minimal` 不适用。Responses API 使用 `reasoning.effort`；Astra 工具调用使用 Responses。不要照搬旧示例中的 `temperature`、`top_p` 等参数。[官方迁移与参数指南](https://developers.openai.com/api/docs/guides/latest-model)

```bash
python3 examples/astra.py text --effort medium --max-output-tokens 8192
```

`max_output_tokens` 还需要给推理留空间，不能理解成最终可见回答的字数。过小会导致输出未完成。提高预算前先检查错误，而不是无限增加预算。

## 常见问题

| 现象 | 先检查什么 | 怎么处理 |
| --- | --- | --- |
| `缺少 OPENAI_API_KEY` | 是否在同一个终端设置了环境变量 | 重新设置，或先用 `--dry-run` |
| 401 | key 是否有效 | 在 API 项目里检查密钥；不要发给他人排错 |
| 403 / 404 | 项目和模型权限 | 确认该项目能使用 `gpt-6-astra`；不静默换模型 |
| 400 | 参数或输入格式 | 保留最小请求，检查推理强度及图片格式 |
| 429 | 用量额度、余额或速率限制 | 检查控制台；稍后再试，不循环猛重试 |
| 响应 `incomplete` | 输出预算及结束原因 | 查看 `incomplete_details`；缩小任务或适度提高预算 |
| 连接失败 / 超时 | 网络与服务状态 | 检查网络；超时不代表服务器未处理，重复提交可能再次计费 |
| 联网回答没来源 | 是否启用了 `web_search`，是否返回引用 | 检查完整响应；要求检索，不能把模型记忆当来源 |
| 模型说生成了文件但找不到 | 是否真的提供了文件工具 | API 文字响应不会自动写文件；用应用程序保存结果 |
| 3D 页面空白 | 浏览器的 WebGL / WebGPU 支持与资源加载 | 换兼容环境或先看案例截图 |

### 费用怎么估算

以首页所列标准文本费率为例，假设一次请求的**实际计费用量**为 2,000 输入 tokens、1,000 输出 tokens，无缓存和工具调用：

```text
2,000 / 1,000,000 × $10 + 1,000 / 1,000,000 × $50 = $0.07
```

这是费率计算示例，不是某个任务的实测价格。完整费用还可能包含推理 token、图片输入、工具、长上下文及服务模式差异。API 响应中的 `usage` 和账单才是核对依据。[模型计价说明](https://developers.openai.com/api/docs/models/gpt-6-astra)

建议先用一个小输入、一张图和较低推理强度评估；满意后再扩大任务。
