# Make something playful with Astra + Blender

[English](../README.md) · [中文](../README_zh.md) · [中文完整指引](#中文动手指引)

Inspired by [《用GPT-6 Astra操控Blender玩3D，保姆级教程来了。》](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ), published by **数字生命卡兹克**, credited to **卡兹克、可达**, September 8, 2026. The article introduces desktop control, MCP, scripting, and combining generated assets with Blender. The exercises and code below were independently written for this guide; we do not reproduce the article's images, long prompts, or benchmark claims.

## Choose one small project

| Project | First deliverable | Check before expanding |
| --- | --- | --- |
| A mint-colored desk robot | Seven separately named geometric parts | Silhouette reads from front and side; feet meet the floor |
| A robot that assembles itself | Six seconds at 24 fps | 144 frames; inspect early, middle, and final poses for intersections |
| A tiny reading nook | Floor, two walls, a chair, a lamp | Human-scale proportions; camera sees the whole scene |
| A paper-circuit kit commercial | Three editable shots | Reuse our [20-second frame plan](original-lab.md); no gaps or unintended black frames |
| An original mushroom mascot | Imported or modeled static character | Consistent scale, complete textures, then a deformation check before animation |
| A miniature repair detective | A report of scene issues | Object names and evidence for each issue; no unsupported “all fixed” claims |

These are teaching tasks, not verified Astra-produced showcases. Start with the robot; keep the mascot for after you can inspect meshes and materials.

## Pick a control route

- **Computer Use:** useful when you want to inspect visible UI steps. Install/enable it through the app's plugin controls and review app access under computer-use settings. On macOS the official guide calls for screen-recording and accessibility permissions. See [OpenAI setup](https://learn.chatgpt.com/docs/computer-use).
- **Blender MCP:** useful for querying and editing a running scene through connected tools. The [Blender Lab page](https://www.blender.org/lab/mcp-server/) currently requires **Blender 5.1+**, its add-on, a compatible LLM client, and the MCP server. Installing the add-on alone does not complete the connection. Use the actual current setup instructions rather than an invented one-line installer. See also [Codex MCP documentation](https://learn.chatgpt.com/zh-Hans/docs/extend/mcp).
- **Python through Blender's command line:** useful for reproducible generation. Blender runs the `bpy` script; a normal Python interpreter is not a substitute. The original example below uses this route and does not need MCP or Computer Use.

The Blender Lab documentation notes that its MCP integration executes model-generated code without built-in data-protection guards; use a separate practice environment without sensitive files. This is a limitation of that integration, not a claim that a specific model will protect the scene.

## First prompt: an editable desk toy

```text
Create an original mint-and-amber desk robot in Blender.
Use seven separate geometric parts: body, head, two eyes, two feet, antenna.
Name them BOT_body, BOT_head, BOT_eye_L, BOT_eye_R,
BOT_foot_L, BOT_foot_R, and BOT_antenna.
First deliver only a blockout, front and side screenshots, and a saved .blend.
Check that feet touch the floor, eyes sit on the front face, and parts remain editable.
Describe the tools actually used and any checks you could not perform.
```

Follow up after inspecting the blockout:

```text
Keep the approved shape and materials. Make a six-second assembly animation at 24 fps.
Hold an exploded arrangement, move parts into place in staggered groups,
then hold the assembled robot. Use frames 1 through 144 inclusive.
Save a new .blend version. Inspect frames 1, 48, 96, and 144 before rendering video.
Report intersections or camera issues with the frame and object name.
```

## A small original script to inspect and adapt

[desk_robot.py](../examples/blender/desk_robot.py) creates the seven meshes and editable location keyframes, then saves `outputs/desk-robot/desk-robot.blend`. It creates **no camera, lighting, image, or video**; the next task is to add those after checking the model. The body stays in place while the other parts assemble.

Run from the repository root with Blender installed and available on your command path:

```bash
blender --background --factory-startup --python-exit-code 1 --python examples/blender/desk_robot.py
```

On macOS with the default application location:

```bash
/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python-exit-code 1 --python examples/blender/desk_robot.py
```

On Windows PowerShell, replace the installation path with your actual version:

```powershell
& 'C:\path\to\Blender\blender.exe' --background --factory-startup --python-exit-code 1 --python examples/blender/desk_robot.py
```

The script requires a background process, starts an empty scene there, and refuses to overwrite its existing `.blend` output. Move the previous output or use another working directory before rerunning. Its command-line options follow the [Blender manual](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html).

**Verification:** the source was checked for Python syntax only. Blender was not available in the current environment, so scene creation, playback, and screenshots have not been tested here. No paid Astra call or external 3D generation was performed. The earlier field-lab screenshots show offline reports and do not illustrate this Blender script's results.

## Keep the feedback concrete

Use “BOT_eye_L is hidden at frame 48; adjust its path while keeping the final pose,” rather than “make it better.” If a tool times out, first inspect the current scene and saved files; split the remaining work into modeling, materials, keyframes, preview frames, and export. Avoid blindly repeating a task that may already have created objects.

For a generated mascot, start from your own design and check the chosen service's export formats and asset terms. Import first, inspect textures and scale, test one bent-limb pose, then attempt a short gesture. A generated mesh is not automatically animation-ready. No external service is required for the geometric robot.

<a id="中文动手指引"></a>

## 中文动手指引

本指南借鉴文章中的工具协作思路，另写了六种玩法与桌面机器人脚本。文章里的建筑、摩托车和角色演示属于作者作品；本仓库不使用其截图，也不沿用其长提示词。作者报告的耗时与额度消耗不作为你的任务预算。

### 先把环境接通，再增加难度

1. 在你已有权限的客户端中选择 Astra，打开一个用于练习的本地项目，从 [Blender 官网](https://www.blender.org/download/) 安装软件。
2. 选一条路线即可开始。想观察操作过程可用 Computer Use；想读取正在编辑的场景可配置 MCP；想保留可重复执行的代码可用脚本。三条路线并非全部必装。
3. 若用官方 MCP，当前页面要求 Blender 5.1 及以上，并分别配置扩展、客户端和服务端。先让 Astra 列出场景中的对象验证连接，再让它建模。具体配置以 [Blender 官方入口](https://www.blender.org/lab/mcp-server/) 为准。
4. 若用界面操作，按 [OpenAI 官方说明](https://learn.chatgpt.com/docs/computer-use) 启用插件和所需系统权限。按钮名称可能随版本变化，不能仅凭旧截图判断已连接。
5. 第一次只交付粗模和保存文件。重新打开检查后，再加材质、灯光和动画。

### 玩法一：你的第一个桌面小机器人

```text
在 Blender 里制作一个原创的薄荷绿桌面小机器人，点缀琥珀色。
用身体、头、两只眼、两只脚、天线这七个独立几何体表达轮廓。
对象名分别使用 BOT_body、BOT_head、BOT_eye_L、BOT_eye_R、
BOT_foot_L、BOT_foot_R、BOT_antenna。
第一阶段只完成粗模，保存 .blend，并给出正面和侧面的实际截图。
检查脚底接地、眼睛朝前、各部件可独立编辑；说明实际使用了什么工具。
```

**验收**：打开对象列表找到七个名字；从侧面看眼睛没有藏进头部；保存后重新打开仍能编辑。上面的 [原创脚本](../examples/blender/desk_robot.py) 是可阅读的起点，目前只做过语法检查，未在 Blender 中实跑。

### 玩法二：让零件自己归位

```text
沿用刚才的小机器人，保留造型与材质。
制作 6 秒、24 fps 的组装动画，使用第 1 至 144 帧（含首尾）。
以身体为基准，其他零件先分开展示，再分组错峰归位，末尾保持完整姿态。
先检查第 1、48、96、144 帧，只输出预览；保存为新的 .blend 版本。
发现穿插时指出帧号和对象，调整运动路径，保留最终位置。
```

**验收**：帧数按 `144 - 1 + 1 = 144` 计算，时长为 `144 / 24 = 6` 秒。检查中间姿态，不只看终点。当前脚本只提供位置关键帧，灯光、镜头与视频编码需要后续完成。

### 玩法三：装进一间小小阅读角

```text
为小机器人布置原创阅读角：地面、两面墙、一把椅子、一盏落地灯。
先确定共同的尺寸单位，保证椅子和机器人比例协调。
使用简单材质，先固定一个能看到全部主体的镜头。
交付可编辑工程和一张低分辨率预览；检查脚底、椅脚与地面的接触。
```

**验收**：镜头不被墙遮挡，主体没有被裁切；尺寸与位置有记录。先确认构图，再讨论纹理与渲染精度。

### 玩法四：把纸电路分镜变成真实短片

```text
读取本仓库 outputs/field-lab/results.json 中的 film 数据。
先创建原创纸电路道具，再按准备、制作、分享三个镜头规划动画。
镜头时长保持 5、7、8 秒，30 fps，共 600 帧。
把数据的半开区间 [0,150)、[150,360)、[360,600)
映射到 Blender 的 1–150、151–360、361–600 帧（含首尾）。
先输出每个镜头的首、中、尾预览，再完成灯光和最终视频导出。
```

**验收**：先运行 [离线实验](original-lab.md) 得到 JSON。注意两套帧编号的差异，避免多一帧或少一帧。每个镜头起止都完整，再检查导出文件的实际时长。此项为拓展任务，仓库尚未生成对应视频。

### 玩法五：原创蘑菇小伙伴打招呼

```text
根据我提供的原创蘑菇吉祥物设定制作静态角色，记录不明确的背面结构。
若用外部 3D 生成服务，先核对导出格式与素材使用条款。
导入 Blender 后先检查比例、材质和贴图，再做一次手臂弯曲测试。
测试通过后制作一个三秒挥手动作；交付模型、贴图清单和可编辑工程。
```

**验收**：重新打开不丢贴图；抬手时肩部没有明显塌陷；不要把“成功导入”当成“骨骼动画已可用”。本仓库不默认调用或收费使用任何外部 3D 服务。

### 玩法六：让 Astra 当场景找茬助手

```text
只检查当前 Blender 场景，先不要修改。
列出没有材质的可见网格、名称重复而难以区分的对象、缺失外部文件，
以及镜头内可能遮住主角的物体。每项给出对象名和检查依据。
区分已经确认的问题与仅凭画面推测的问题，并列出修复顺序。
```

**验收**：任选两项回到 Blender 查证。需要修改时再指定对象与目标，并保存新版本。这是本指南设计的检查练习，不是已运行的诊断结果。

### 卡住时怎样继续

| 情况 | 下一步 |
| --- | --- |
| 安装了扩展但读不到场景 | 分别检查 Blender 扩展、MCP 服务端、客户端连接；从列对象开始 |
| 提示找不到 `bpy` | 用 Blender 执行脚本，不用系统 `python3` 运行建模代码 |
| `blender` 命令不存在 | 使用本机 Blender 可执行文件的完整路径 |
| MCP 操作超时 | 先确认当前场景和最近保存文件，再拆分剩余步骤，避免重复建模 |
| 静帧正常，动画穿插 | 指定出问题的帧号和对象，检查中间路径 |
| 渲染很慢 | 先用低分辨率少量预览帧确定构图，再扩大输出；记录本机耗时 |

## Sources and scope

- [微信原文：用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ) — 数字生命卡兹克；署名卡兹克、可达；2026-09-08。用途：工具协作与分阶段创作的选题启发。
- [Blender Lab MCP Server](https://www.blender.org/lab/mcp-server/) — 核对官方入口、版本要求与连接组件。
- [Blender command-line arguments](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html) — 核对后台执行与 Python 退出码参数。
- [OpenAI Computer Use](https://learn.chatgpt.com/docs/computer-use) · [MCP](https://learn.chatgpt.com/zh-Hans/docs/extend/mcp) — 核对客户端的工具连接方式。

以上页面于 2026-09-08 读取。本文为独立练习指引，未复现原作者作品或验证其效果、耗时与额度说法。没有复制文章素材，也没有新增未经实测的结果截图。
