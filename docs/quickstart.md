# 直接使用 GPT-6 Astra：ChatGPT、Codex 客户端、Codex CLI

[中文首页](../README_zh.md) · [English](../README.md) · [趣味 Blender](blender-playbook.md) · [原创练习](cases.md)

**先登录账号、选择 Astra、发送任务即可开始。** 下面以 ChatGPT 账号登录为主，不要求先申请 API key、安装 Python SDK 或编写接口请求。模型选项、额度和工具权限取决于账号、工作区及开放阶段。核对日期：2026-09-08。[官方模型与可用入口](https://learn.chatgpt.com/docs/models)

| 你想做什么 | 建议入口 | 准备材料 |
| --- | --- | --- |
| 看图、做方案、研究、整理文档 | ChatGPT；需要完整交付物时选择 Work | 图片、文件、目标与限制 |
| 修改本地项目、制作页面、运行 Blender 脚本 | Codex 客户端／桌面应用里的 Codex | 一个本地项目文件夹 |
| 已习惯终端，希望读代码、改文件、运行命令 | Codex CLI | 本地项目目录及已安装的工具 |

<a id="不用写代码"></a>
<a id="chatgpt"></a>

## 1. 在 ChatGPT 中使用

1. 打开 ChatGPT 网页或客户端，用自己的 ChatGPT 账号登录。方案、资料分析和交付文件类任务可在新对话中选择 **Work**。
2. 打开对话的模型／**Power** 选择器，选择包含 **Astra** 的选项；如果界面提供 **Advanced**，可展开查看具体模型。确认选择的是 Astra，再开始任务。不同版本不一定显示完全相同的按钮名称。[官方模型选择说明](https://learn.chatgpt.com/docs/models)
3. 用附件按钮添加图片或文件，或直接粘贴材料。第一次可以上传本仓库的 `assets/screenshots/workshop-budget.png`。
4. 复制下面的任务，发送后检查回答中的数字；继续在同一对话里提出改动。

```text
请检查我上传的工作坊预算图，先读出人数、各项费用、总支出和预留金。
逐项复算，并说明是否满足预算的 10% 预留目标。
再分析人数从 24 增加到 32 时会发生什么，固定费用不变。
交付：两种人数的对照表、计算过程、两条调整建议。
看不清的数字请标明，不要猜。
```

**怎么验收**：24 人应支出 2,168 元、剩余 432 元；32 人应支出 2,584 元、剩余 16 元。后者虽未超预算，却不满足 10% 预留目标。

**继续追问**：“保持 32 人和 10% 预留目标，其他费用不变，预算至少要提高到多少？按整元向上取整。”可用 `2584 / 0.9` 对照，整元预算至少为 2,872 元。

ChatGPT 网页不会仅凭一条文字请求连接到你电脑上的 Blender。要操作本地文件或软件，继续使用下面的本地项目入口和已配置的工具。[官方产品入门](https://learn.chatgpt.com/docs/quickstart)

<a id="codex-app"></a>

## 2. 在 Codex 客户端中使用

1. 打开 Codex 客户端并登录 ChatGPT 账号。如果你的版本是统一的 ChatGPT 桌面应用，从产品切换菜单选择 **Codex**。
2. 新建项目或打开文件夹，选择本仓库 `awesome-gpt-6-astra-guide` 所在目录。让当前任务工作在这个本地项目里，而不是仅贴一个 GitHub 链接。
3. 新建任务，在模型／Power 选择器中选择 **Astra**；需要时在 Advanced 中核对具体型号。先用界面默认的推理设置即可。
4. 发送下面的任务。Codex 会在可用工具及权限范围内读取文件和执行命令，按界面提示处理实际需要的授权。

```text
先阅读当前项目的 README 和运行说明。
运行 examples/field_lab.py，输出到一个新的 outputs 子目录，避免覆盖旧结果。
打开生成的预算、分镜和验收报告，说明三个结果分别意味着什么。
再生成一个 32 人的对照版本，解释预留金为何不达标。
交付：可打开的文件路径、实际检查结果，以及无法完成的步骤。
```

**怎么验收**：输出目录有三张 SVG 和 `results.json`；点击文件可查看。若环境缺少 Python，应明确报告，不把计划当成已运行结果。示例计算本身离线运行；让 Astra 执行和解释任务仍会使用账号额度。

**想直接做作品**：新建一个空项目文件夹，发送：

```text
为 Paper Circuit Studio 制作一个本地工作坊报名页面。
包含介绍、人数选择和实时预算：固定成本 920 元，每人 52 元，总预算 2600 元。
显示剩余金额；不足预算 10% 时提示需要调整。
使用当前项目已有技术；空项目则采用易运行的简单方案。
交付源码、启动方法和实际预览，检查 24 人和 32 人两种情况及窄屏显示。
```

**想玩 Blender**：在同一个本地项目发送：

```text
按 docs/blender-playbook.md 的桌面机器人练习开始。
先检查本机 Blender 是否可用，以及现有脚本的输入输出。
有环境就运行并检查保存的 .blend；缺环境就说明安装步骤。
先验收七个独立部件和 144 帧时间轴，再安排灯光、镜头和渲染。
```

Blender 的 MCP 和 Computer Use 是根据任务选择的工具，不是使用 Astra 的通用前置条件。[桌面入口说明](https://learn.chatgpt.com/docs/quickstart) · [Blender 完整练习](blender-playbook.md)

<a id="codex-cli"></a>

## 3. 在 Codex CLI 中使用

### 安装并登录

未安装时，按 [官方 CLI 安装页](https://learn.chatgpt.com/docs/cli) 选择系统对应方式。macOS / Linux 官方独立安装命令为：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Windows 用户在同一官方页面选择 Windows 安装方式；装好后重新打开终端。CLI 不要求你先安装本仓库的 Python 或 JavaScript 示例依赖。

进入你要处理的项目文件夹，然后启动：

```bash
cd /path/to/your/project
codex -m gpt-6-astra
```

把 `/path/to/your/project` 换成自己的目录；Windows PowerShell 可使用 `cd 'C:\path\to\your\project'`。第一次启动按提示选择 **Sign in with ChatGPT**，在浏览器完成登录。无需为这条登录路线创建 API key。使用额度按账号与工作区规则计算。[官方 CLI 入门](https://learn.chatgpt.com/docs/cli)

### 确认模型并发出任务

进入 Codex 的交互界面后输入：

```text
/model
```

核对当前模型为 Astra，也可在此调整推理强度。输入 `/status` 查看会话配置；这些是 **Codex 内的命令**，不是直接输入到系统终端的命令。

然后像聊天一样发送：

```text
先阅读当前项目，说明启动方法和主要文件。
找一个可以独立验收的小改进，说明目标后完成修改。
运行相关检查，最后给出改动文件、运行结果和仍未验证的部分。
```

也可以在系统终端启动时附带任务：

```bash
codex -m gpt-6-astra "Read this project and explain how to run it."
```

在本仓库根目录，可附带一张原创报告图：

```bash
codex -m gpt-6-astra -i assets/screenshots/workshop-budget.png "Check this budget against examples/fixtures/studio-brief.json."
```

退出后想继续上一任务，在项目目录运行 `codex resume --last`，恢复后再用 `/model` 核对模型。上述 `-m`、`-i`、`resume --last` 已与本机 CLI 帮助核对；本次没有启动新的付费模型会话。

<a id="常见问题"></a>

## 常见问题

| 情况 | 具体处理 |
| --- | --- |
| 找不到 Astra | 先更新客户端，检查模型／Advanced 列表、登录账号和工作区开放情况；输入模型名不能绕过权限 |
| Power 显示别的模型 | 明确选择 Astra 选项，CLI 用 `/model` 核对；不要只靠模型自称判断 |
| CLI 提示 `codex` 不存在 | 完成官方安装后重开终端，检查安装页的路径提示 |
| CLI 登录没完成 | 回到登录提示，在浏览器完成授权；检查是否登录了预期账号 |
| 提示额度已用完 | 查看产品内用量及重置时间；更换入口不代表能绕过共享额度 |
| 只给了计划，没有成果 | 在同一任务追加“请继续执行并交付文件，报告实际检查结果” |
| 找不到本地项目文件 | 核对客户端选中的文件夹，或 CLI 启动时的目录 |
| 说做完了 Blender，但没有文件 | 要求明确 `.blend` 路径和实际打开检查；确认客户端具备本地软件工具 |

## API 放在什么时候学？

需要把 Astra 接入自己的产品或自动化程序时，再看 [API 进阶说明](api.md) 和 [Python / JavaScript 示例](../examples/README.md)。日常聊天、项目创作、终端协作可以先用上面的三条入口完成。

<a id="用-api-开始"></a>

旧版 API 入门链接已迁至 [API 进阶说明](api.md#用-api-开始)。

## 继续尝试：X 社区的新场景

[2026-09-22 新增八个练习](x-playbook.md)，包括字幕、调色、资产整理、Excel 像素画、仓库界面与史料核对。使用客户端直接提交任务即可；原帖、作者、验收标准和未验证范围均有记录。
