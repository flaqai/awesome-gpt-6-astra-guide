# Astra field lab: from evidence to recommendations

[English](../README.md) · [中文](../README_zh.md) · [Code](../examples/field_lab.py) · [Authorship](originality.md)

This lab was written for the flaq.ai guide. One fictional project, **Paper Circuit Studio**, connects an event budget, a short-film storyboard, and a release review. The data, drawing code, illustrations, and report layouts were created for this repository. No external images, fonts, packages, or model calls are needed to generate the reports.

## 1. Generate the evidence offline

From the repository root, with Python 3.10+:

```bash
python3 examples/field_lab.py
```

Open the generated SVG files in a browser. The output directory contains:

| File in `outputs/field-lab/` | What to check |
| --- | --- |
| `workshop-budget.svg` | 920 fixed costs + 24 × 52 per guest = 2,168 CNY; 432 CNY remains, meeting a 10% reserve target |
| `craft-storyboard.svg` | 5 + 7 + 8 seconds at 30 fps = 600 frames; intervals [0,150), [150,360), [360,600) have no gaps |
| `release-review.svg` | Three of five fictional observations meet their targets; R02 and R03 block release |
| `results.json` | Machine-readable calculations and the original observations, explicitly marked `offline_fixture` |

These are deterministic teaching reports. The release values are fixture inputs, not measurements collected from a real website. The storyboard is a static planning report, not an exported video. The screenshots in the README show these reports in a browser, not results of paid Astra requests.

## 2. Change one constraint

```bash
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

Expected: spending rises to **2,584 CNY** and only **16 CNY** remains. The event is within the 2,600 CNY budget but fails the 10% reserve target. This distinction is deliberate: staying under budget is a different check from keeping enough reserve.

Edit a copy of [studio-brief.json](../examples/fixtures/studio-brief.json) to change costs, shot durations, or observed check values. Pass it with `--brief path/to/your-brief.json`. Money is represented as whole CNY for this exercise; no tax, currency conversion, or fractional-second timing is implemented. There must be exactly three shots and at most five cost lines and five release checks, matching the compact report layout. Use a new `--out` directory or explicitly pass `--overwrite` to regenerate existing files.

## 3. Discuss the evidence directly in ChatGPT or Codex

**ChatGPT / Work:** select Astra, attach the budget PNG and paste the relevant numbers from `results.json`. Ask it to compare the 24-guest and 32-guest scenarios and explain which constraints fail.

**Codex client:** open this repository as a local project, select Astra, and send:

```text
Read outputs/field-lab/results.json and outputs/field-lab-32/results.json.
Explain why the larger workshop fails its reserve target.
Propose two alternatives using the supplied numbers; state assumptions and tradeoffs.
Check the arithmetic against the local report, and give me the file paths you used.
```

**Codex CLI:** sign in with ChatGPT, start `codex -m gpt-6-astra` in the repository, then paste the same task. Codex can also run the lab for you when the required local tools are available. See the [client-first quickstart](quickstart.md).

The local calculations give you a reference to check the answer against. Suggestions do not automatically change the fixture or mark a real project as passing. Direct Astra use follows your account's usage rules; generating the reports alone is offline.

### Optional API integration

Only if you are connecting your own application, use [API setup](api.md) and [the examples](../examples/README.md). Python supports `--brief` for sending the JSON with a request. This is an additional integration route, not a requirement for completing the exercise.

## 中文快速说明

这是围绕同一个虚构工作室编写的原创练习，分为预算、分镜和验收三部分。先运行 `field_lab.py` 得到可复算的 JSON 与 SVG，再把数据交给 Astra 分析，最后用本地计算结果核对回答。新图片是本地报告的真实浏览器截图；不是第三方作品，也不是模型实测结果。

默认 24 人支出 2,168 元、预留 432 元；改为 32 人后支出 2,584 元、预留仅 16 元，虽未超预算但不满足 10% 预留目标。分镜共 600 帧；模拟验收 R02、R03 未通过。可以修改原创资料，观察结果变化，再要求 Astra 说明原因。完整练习见 [12 个原创案例](cases.md)。
