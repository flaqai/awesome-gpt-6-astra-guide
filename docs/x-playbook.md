# From X demos to practical Astra tasks / 从 X 案例到动手练习

[English](../README.md) · [中文首页](../README_zh.md) · [客户端入门](quickstart.md) · [来源清单](research/x-sources-2026-09-22.json)

**Added September 22, 2026.** Seven X posts were read directly, yielding eight original exercises below. These are attributed community reports, not benchmarks or reproduced projects. No third-party images, videos, code, or long prompts are copied into this guide. Publication dates are the dates displayed by X; they are separate from our access date.

## Choose a task

| Exercise | What you can try | Entry point | Source / evidence |
| --- | --- | --- | --- |
| [01 · Subtitle cleanup](#x-01) | Turn your own timed transcript into an importable subtitle draft | ChatGPT Work; Codex for files | [JaydenCoach, Sep 11](https://x.com/JaydenCoach/status/2098136605135364534), creator demo |
| [02 · Color-grading brief](#x-02) | Specify a look, prepare a LUT candidate, compare frames | Codex + your editor | Same post; editor compatibility not tested |
| [03 · Engine migration](#x-03) | Port one scene slice before migrating a project | Codex + installed engines | [seftsaint, Sep 20](https://x.com/seftsaint/status/2101395711015497764), creator demo |
| [04 · Modular asset cleanup](#x-04) | Audit repeated meshes, optimize copies, preserve placement | Codex + Blender / engine tools | [insaneUEFN, Sep 16](https://x.com/insaneUEFN/status/2100237060573466631), workflow report |
| [05 · Spreadsheet pixel art](#x-05) | Make a small original cell-art flipbook | ChatGPT Work / Codex with spreadsheet tools | [higgsfield_ai, Sep 9](https://x.com/higgsfield_ai/status/2097465326133002488), vendor demo |
| [06 · Explore a warehouse](#x-06) | Turn a tiny inventory fixture into a navigable interface | Codex client or CLI | [sean_wallace_, Sep 17](https://x.com/sean_wallace_/status/2100596939511496848), promotional showcase |
| [07 · Historical evidence check](#x-07) | Separate transcription, interpretation, and corroboration | ChatGPT Work with supplied sources | [prinz, Sep 17](https://x.com/deredleritt3r/status/2100608983492862201), research claim |
| [08 · Define “done”](#x-08) | Turn a vague project into bounded, checkable work | Any supported Astra client | [shohei_botter, Sep 22](https://x.com/shohei_botter/status/2102318133226905766), personal experience |

For each exercise, select Astra in a client where your account has access. Attach source material in ChatGPT, or open a local project in Codex. CLI users can start from that project using `codex -m gpt-6-astra`. API integration is not required. Tool availability and usage limits still apply.

**English starter prompt:** “Use the selected exercise as a brief. Inspect my supplied materials, deliver the smallest useful artifact, and verify it against the listed acceptance checks. Write the result in English. Separate observed results, suggestions, and steps you could not run.” The detailed task prompts below are in Chinese and can be translated before use.

<a id="x-01"></a>

## 01 · 让字幕真正能交给剪辑师

**原帖说了什么**：[Jayden Douglass](https://x.com/JaydenCoach/status/2098136605135364534) 描述用 Astra 生成字幕和调色文件，再在 CapCut PC 中调整。本文已读取原帖，未验证其文件。原帖使用“animated .srt”表述；本练习将时间码字幕与编辑器里的动画效果分开验收，不承诺仅导入文本字幕就自动有动画。

**准备**：自己的一段短视频、已经核对的逐字稿及起止时间。没有听取音频或转写工具时，先提供时间码，不让模型猜。

```text
将我提供的带时间码逐字稿整理为字幕草稿。
保留原意和人名；修正断句；把疑似听错的词另列待确认。
输出 UTF-8 的 captions.srt，以及一份需人工核对的词语清单。
先检查每条开始时间小于结束时间、序号连续、没有意外重叠。
不要声称字幕有动画；另写一份在剪辑软件中设置样式与动画的建议。
```

**验收**：实际导入自己的编辑器，抽查第一条、中间一条和最后一条与画面对齐；发现偏移先统一时间基准，再逐条调整。导入失败就记录编辑器版本和报错，不能把文件已生成当成可用。

<a id="x-02"></a>

## 02 · 用三张对照帧沟通调色

**来源边界**：沿用 [JaydenCoach 的同一原帖](https://x.com/JaydenCoach/status/2098136605135364534)，这是从一条案例拆出的第二项练习，不计作第二位独立作者的验证。

**准备**：自己素材中的暗部、中间调和高光三张帧图，以及所用编辑器的导入要求。

```text
我希望这组素材更温暖，但保留白色物体和人物肤色的自然感。
先分析三张帧图，给出调整方向与需要确认的色彩空间。
若环境能生成并检查 .cube 文件，按编辑器要求交付一个候选版本；
否则先交付参数建议，不伪称已生成可用 LUT。
用同一组帧做处理前后对照，记录高光剪切、暗部细节和肤色变化。
```

**验收**：在原编辑器实际加载，检查三类帧；确认没有改变分辨率、时长或字幕。这个任务是可重复的视觉比较，不把“更电影感”当成唯一完成条件。

<a id="x-03"></a>

## 03 · 把场景迁移缩小到一个可走通的切片

**原帖说了什么**：[eta](https://x.com/seftsaint/status/2101395711015497764) 描述将已有 Godot 概念迁到 Unreal，修改树木和光照；[作者回复](https://x.com/seftsaint/status/2101553995420672417) 说明部分资产来自 Meshy。另有[用量较大的反馈](https://x.com/seftsaint/status/2101396401171337545)。这不能被简化成“一个提示词从零生成完整游戏”。

**准备**：你拥有使用权的现有场景、源引擎和目标引擎、一个可验收的功能范围。

```text
先检查当前源工程和目标工程的版本及可用工具。
只迁移一个包含地面、三棵树、灯光和相机的小场景，不迁移整个游戏。
保留源文件；建立单位、朝向、材质和对象名称的对照表。
完成后在目标引擎中走通场景，检查比例、碰撞、纹理和镜头。
交付新工程位置、资源来源、迁移差异和实际运行证据。
```

**验收**：目标工程能重新打开，三棵树位置符合对照，角色不穿地面；旧工程保持可用。没有源文件时，此任务只能生成迁移清单，不能完成真实迁移。

<a id="x-04"></a>

## 04 · 把一堆模型整理成可复用资产

**原帖说了什么**：[Jerome / InsaneUnreal](https://x.com/insaneUEFN/status/2100237060573466631) 描述连接 Atlas、Tripo、Blender 和 UEFN，优化资产后以独特资产和重复模块重建场景；作者也提到手动缩放。本指南未核验其数量、运行速度和最终工程。

**准备**：先用自己建模的一个窗户、一根梁和几份重复副本练习；不必购买或连接原帖的全部服务。

```text
检查练习场景，列出网格名称、面数、材质和重复对象候选。
先交付一份合并与实例复用方案，再在工程副本里处理。
保留不同位置与旋转，不把外观相似但材质不同的资产错误合并。
输出资源清单，记录修改前后数量、面数和可见差异。
最后重新打开工程，检查贴图路径和全部实例的位置。
```

**验收**：重复部件能追溯到源资产；处理后的副本位置正确，材质没有丢失。减面是否合适要看轮廓和用途，不照搬原帖的固定面数目标。

<a id="x-05"></a>

## 05 · 用 Excel 单元格做像素翻页书

**原帖说了什么**：[Higgsfield AI 品牌账号](https://x.com/higgsfield_ai/status/2097465326133002488) 展示让 Astra 将图像内容用于 Excel 单元格动画。帖子未提供本次可核验的工作簿或动画实现，因此不能确认其机制。

**本指南的原创小版本**：不用原帖图像，自己设计一个 16×16 的发光纸电路图案；先做四张工作表构成的翻页书，再决定是否做动画。

```text
制作一个原创纸电路像素翻页书，尺寸 16×16，调色板最多六色。
创建四张工作表分别表示熄灭、微亮、点亮、闪烁。
统一行高列宽和绘图区位置，另建说明页写清帧顺序和颜色含义。
交付 .xlsx；若当前没有表格工具，先输出网格数据和制作步骤。
不使用自动执行宏，不把手动切换工作表称为已完成连续动画。
```

**验收**：四页大小一致、颜色数符合约束、文件可打开编辑。要做连续播放时，应再明确具体软件与播放方式，单独测试。

<a id="x-06"></a>

## 06 · 把库存表变成可探索的小仓库

**原帖说了什么**：[Sean Wallace](https://x.com/sean_wallace_/status/2100596939511496848) 介绍 Enter Pro 与 Astra 的可探索仓库界面，附带产品推广链接。已读全文，但未验证实际库存、后端、代码或产品可靠性；这是一条推广展示。

**先用这份原创虚构数据**，无需接企业系统：

```csv
sku,rack,stock,reorder_level
PAPER-A,A1,24,10
LED-B,A2,4,8
TAPE-C,B1,12,5
CELL-D,B2,2,6
```

```text
根据这四条虚构库存数据制作本地仓库看板。
首版用可点击的二维货架图；点击货位显示 SKU、库存和补货线。
库存低于补货线时同时用文字与颜色提示，并保留表格视图。
货架视图与表格使用同一份数据，先不要接登录、支付或真实库存。
验收后再讨论是否需要 3D。
```

**验收**：只有 LED-B、CELL-D 提示补货；四个货位均可点击；修改库存后两种视图一致；键盘能选中货位。这里的数据和任务由本指南编写，并非原帖产品数据。

<a id="x-07"></a>

## 07 · 做历史资料的证据核对员

**原帖说了什么**：[prinz](https://x.com/deredleritt3r/status/2100608983492862201) 报告用 Astra 分析历史密文，并以舰船日志核对时间与事件。首次破解、解密结果和日志对应关系均未在本项目独立验证。

**更适合入门的版本**：给一张公开档案图片和两份已知参考资料，练习区分识读、解释与证据，不从“首次破解百年难题”开始。

```text
先逐行转录这份历史资料，无法辨认的字符用 [不确定] 标出。
把日期、地点、人物和事件整理成表，保留原文对应位置。
只用我提供的两份参考资料交叉核对，并为每个结论注明来源位置。
分成直接证据、推测、相互矛盾和仍待核对四类。
不要为了拼出合理故事补全缺字，也不要声称取得首次发现。
```

**验收**：至少抽查三项原图位置和引用；没有证据的推断不进入“已确认”栏。后续若研究历史谜题，也要保留算法、输入与可复算过程。

<a id="x-08"></a>

## 08 · 用完成条件约束过度工程化

**原帖说了什么**：[Shohei](https://x.com/shohei_botter/status/2102318133226905766) 分享个人经验：讨论 Astra 过度工程化时，意识到应定义完成条件。这是经验提示，不是降低耗时的对照实验证据。

```text
把当前任务的完成条件写进 DONE.md：只做库存看板的四个货位和表格。
验收条件：数据一致、两项补货提示、键盘操作、窄屏可读。
不要增加账号系统、支付、云数据库或与任务无关的重构。
逐项实现并检查；达到完成条件后交付，不继续添加功能。
遇到阻塞，报告缺失条件和当前可交付的部分。
```

**验收**：结束说明逐条对应 DONE.md，并给出实际检查证据。此练习可以套用到本仓库现有预算、分镜和 Blender 任务。

## How the sources were checked / 核对方法

2026-09-22 在 X 中检索 `GPT-6 Astra`，查看 Latest 与 Top；根据线索查询 `from:JaydenCoach Astra` 和 `"Astra" (Excel OR spreadsheet OR slides)`。打开所收录的七条原帖读取全文、署名及显示日期；引擎迁移条目另读取作者回复。研究类原帖最初通过新闻报道发现，再回到 X 核对正文及当前作者名。

没有完整观看所有视频，没有运行作者代码或外部服务，也没有验证耗时、花费、宣传效果或模型质量。未对账号发帖、点赞或发送消息。这里只保留简短归纳和链接，未保存第三方媒体。源记录见 [JSON 清单](research/x-sources-2026-09-22.json)。这些新练习尚未在本仓库实现，不计入既有离线测试的通过数量。
