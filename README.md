# GPT-6 Astra Guide

The latest practical GPT-6 Astra guide curated by the **[flaq.ai](https://flaq.ai/) team**: model essentials, first steps, runnable examples, creative workflows, and real screenshots.

<!-- languages:start -->
**English** · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

**Last reviewed: September 8, 2026.** An independent team-curated guide; not official OpenAI documentation. Dates identify the reviewed edition, and product details may change.

## Start here: choose your app

Use **GPT-6 Astra directly in ChatGPT, the Codex client, or Codex CLI**. Start by signing in with ChatGPT; this route does not require an API key. Model availability and usage depend on your account, workspace, and rollout. [Official model selection](https://learn.chatgpt.com/docs/models)

| Your goal | Start with | First action |
| --- | --- | --- |
| Analyze an image, plan an event, create a document | ChatGPT / Work | Select Astra and attach your material |
| Build a webpage, change local files, try Blender | Codex client | Open a local project folder and select Astra |
| Work from a terminal | Codex CLI | Run `codex -m gpt-6-astra` in your project |

Astra can reason through complex tasks and work with tools. The surrounding app supplies file, browser, and software access. Choosing Astra alone does not connect a web chat to local Blender.

## 1. ChatGPT: attach a file and ask

1. Sign in to ChatGPT on the web or in the app. Choose **Work** for research and finished deliverables.
2. Open the model / **Power** picker and choose an **Astra** option. If available, open **Advanced** to check the exact model. Labels can vary by version.
3. Attach [our budget screenshot](assets/screenshots/workshop-budget.png) and send:

```text
Read the workshop budget in this image. Recalculate each cost and the remaining money.
Compare 24 guests with 32 guests, keeping fixed costs unchanged.
Does each scenario keep at least 10% of the total budget in reserve?
Show the arithmetic and two practical suggestions. Flag unreadable numbers.
```

Check the answer: 24 guests cost CNY 2,168, leaving CNY 432. At 32 guests, CNY 2,584 leaves only CNY 16, below the reserve target. Continue in the same conversation with a focused change. [Official app quickstart](https://learn.chatgpt.com/docs/quickstart)

## 2. Codex client: open a folder and make something

1. Open your Codex client and sign in with ChatGPT. In the unified ChatGPT desktop app, select **Codex** from the product menu.
2. Create a project or open a local folder. For these exercises, select this repository's folder.
3. Start a task, select **Astra** in the model / Power picker, and send:

```text
Read this repository's instructions. Run examples/field_lab.py into a fresh output folder.
Open the three reports and explain the budget, frame timeline, and release checks.
Generate another report for 32 guests and compare the reserve.
Deliver clickable file paths and actual verification results; report missing tools.
```

To build something new, open an empty project and ask for a workshop signup page with a guest selector: fixed costs CNY 920, CNY 52 per guest, budget CNY 2,600. Ask it to check both 24 and 32 guests and the narrow-screen layout.

For 3D, ask Codex to follow [the Blender playbook](docs/blender-playbook.md), inspect whether Blender is installed, and check the editable model before adding lighting and rendering. MCP and Computer Use are task-specific tools, not prerequisites for every Astra task.

## 3. Codex CLI: sign in and start in your project

Install using the option for your system on the [official CLI page](https://learn.chatgpt.com/docs/cli). The macOS / Linux standalone installer is:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Open a terminal in your project folder, then run:

```bash
codex -m gpt-6-astra
```

On first launch choose **Sign in with ChatGPT** and finish the browser sign-in. In the Codex session, use `/model` to confirm Astra or adjust reasoning, and `/status` to inspect session configuration. Then type a normal task, such as “Read this project, explain how it runs, and fix one reproducible issue.”

You can also attach an image when starting from this repository:

```bash
codex -m gpt-6-astra -i assets/screenshots/workshop-budget.png "Check this budget against examples/fixtures/studio-brief.json."
```

Use `codex resume --last` from your project directory to continue the last session; check `/model` after resuming. These CLI flags were checked against local help; no new paid model session was run for this documentation update.

**Astra missing?** Update your client and check the model / Advanced list and your account or workspace access. Specifying a model name does not grant access. ChatGPT sign-in uses your applicable plan's usage rules, rather than making usage free.

[Detailed Chinese setup and troubleshooting](docs/quickstart.md) · [12 original exercises](docs/cases.md) · [Blender playbook: English / 中文](docs/blender-playbook.md)

## Run our original field lab

Three independently written exercises share one fictional studio brief. These are actual browser captures of locally generated SVG reports, not third-party artwork or Astra API output.

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![Workshop budget: CNY 2,168 spent; CNY 432 reserved.](assets/screenshots/workshop-budget.png)

Workshop budget: CNY 2,168 spent; CNY 432 reserved.

![Storyboard: 20 seconds at 30 fps, with 600 contiguous frames.](assets/screenshots/craft-storyboard.png)

Storyboard: 20 seconds at 30 fps, with 600 contiguous frames.

![Release review: 3 of 5 fictional checks pass; two need work.](assets/screenshots/release-review.png)

Release review: 3 of 5 fictional checks pass; two need work.

[Source code, reproduction steps, and exercises](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## A workflow that is easy to repeat

1. Supply useful material: a reference, existing files, audience, and constraints.
2. Build the smallest working version first.
3. Request editable deliverables and clear launch instructions.
4. Check actual behavior, calculations, or file contents.
5. Revise using a screenshot or a reproducible error.

Start with the client’s default reasoning setting. If the task needs deeper work, adjust the model / Power controls or use `/model` in Codex CLI. [Official model controls](https://learn.chatgpt.com/docs/models)

## Optional: integrate the API

Building your own application? Keep the [API setup](docs/api.md) and [Python / JavaScript examples](examples/README.md) for that stage. Direct use through ChatGPT sign-in does not require these steps.

## Verification and contributions

The examples passed **28 offline tests**. Screenshots are real browser captures. No paid API calls or end-to-end reproductions of the community projects were performed. See [verification](docs/verification.md), [sources](docs/sources.md), and [contributing](CONTRIBUTING.md).

Original guide content and code use the [MIT License](LICENSE). External works and trademarks retain their respective rights. See the [authorship record](docs/originality.md).

## Play with 3D: a robot that assembles itself

Try six original Blender exercises: a desk robot, assembly animation, reading nook, paper-circuit short film, mushroom mascot, and scene inspection. The English/Chinese guide includes prompts, tool setup, frame checks, and an original script. The Blender script has only been checked for Python syntax; no Blender run or new result screenshot is claimed.

[Open the Blender playbook](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## About flaq.ai

[flaq.ai](https://flaq.ai/) provides unified API access to image, video, music, and language models for AI agents and production applications. Our team curates this guide to make current AI capabilities easier to understand, try, and evaluate through practical examples.

Explore our open-source workflows: [Backlink Skills](https://github.com/flaqai/backlink_skills).

## Affiliate marketing and partner support

Create tutorials, reviews, or integration guides? Join the **[Flaq.ai Affiliate Program](https://flaq.ai/affiliate-program/)** and use your own referral link when recommending Flaq.ai.

- **20%** on a referred user's first eligible paid order.
- **10%** on subsequent eligible paid orders.
- Eligible orders fall within **60 days after the referred user registers**.

Sign in, complete your affiliate profile, and create a referral link in the affiliate workspace. It supports link management, referral tracking, and payout setup. Clearly disclose affiliate links when sharing them. Eligibility, reviews, and payouts follow the current [Affiliate Agreement](https://flaq.ai/affiliate-agreement/); commissions are not guaranteed.

**[Visit flaq.ai](https://flaq.ai/) · [Join the affiliate program](https://flaq.ai/affiliate-program/)**

## References and inspiration

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

Published by 数字生命卡兹克; authors: 卡兹克、可达; September 8, 2026. Used as inspiration for the workflow guide; article images and long prompts are not reproduced.
