# GPT-6 Astra Guide

The latest practical GPT-6 Astra guide curated by the **[flaq.ai](https://flaq.ai/) team**: model essentials, first steps, runnable examples, creative workflows, and real screenshots.

<!-- languages:start -->
**English** · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

**Last reviewed: September 8, 2026.** An independent team-curated guide; not official OpenAI documentation. Dates identify the reviewed edition, and product details may change.

## Start here

| Your goal | Read / run | What you get |
| --- | --- | --- |
| Try Astra without coding | [Beginner guide](docs/quickstart.md#不用写代码) | A small task with clear acceptance criteria |
| Make your first API call | [API setup](docs/quickstart.md#用-api-开始) | Python and JavaScript entry points |
| Explore what people build | [12 selected cases](docs/cases.md) | Creator links, smaller practice tasks, and checks |
| Build something yourself | [6 practical workflows](docs/workflows.md) | Websites, games, 3D, video, research, and code review |
| Analyze images or extract JSON | [Examples](examples/README.md) | Four Python modes and a JavaScript example |
| Troubleshoot a request | [Errors and cost](docs/quickstart.md#常见问题) | Authentication, limits, incomplete output, and cost basics |

The READMEs are available in 12 languages. The detailed `docs/` tutorials and example diagnostics are currently in Simplified Chinese; the quickstart below works on its own.

## What is GPT-6 Astra?

Astra is an OpenAI model for complex reasoning, coding, research, and work involving multiple steps and tools. It accepts text and images and produces text. Browsing, running software, and creating media require suitable tools in the surrounding application.

| Item | Documented value |
| --- | --- |
| API model | `gpt-6-astra` |
| Context window | 1,050,000 tokens |
| Maximum output | 128,000 tokens |
| Knowledge cutoff | April 30, 2026 |
| Reasoning effort | `low`, `medium`, `high`, `xhigh`, `max` |
| Standard text pricing, per 1M tokens | Input $10 · cached input $1 · output $50 |

Source: [OpenAI model documentation](https://developers.openai.com/api/docs/models/gpt-6-astra). Tool charges and long-context rates can differ. Confirm model access and billing for your account. Creating a video typically means coordinating editing, rendering, or generation tools; it does not mean the Astra endpoint natively outputs video.

## Your first task — no code needed

Choose Astra in a product where your account has access, provide your materials, and start with a small deliverable:

```text
Plan a two-day event for a local coffee shop.
Goal: encourage first-time visitors to return.
Constraints: budget of CNY 2,000; two staff members; use the existing shop and social account.
Deliver: event rules, a schedule, an itemized budget, and three promotional messages.
Check: the budget adds up, each action has a time and responsible role,
and any assumptions are explicit. Do not invent customer data.
```

Inspect the result, then ask for a focused revision. For coding or design work, request source files, launch instructions, and screenshots of the actual result.

## Run your first API example

Use **Python 3.10+** or **Node.js 20+**. Run commands from the repository root. The included scripts use built-in libraries and require no package installation.

```bash
# Offline: inspect a request without an API key, network access, or charges
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

To make a real request, set `OPENAI_API_KEY` for an OpenAI API project with Astra access. In Bash, read the key without saving it in command history:

```bash
bash
read -r -s -p 'OpenAI API key: ' OPENAI_API_KEY
export OPENAI_API_KEY

python3 examples/astra.py text \
  --prompt 'Explain three checks for an AI-generated website in English.'
```

Windows PowerShell:

```powershell
$astraSecureKey = Read-Host 'OpenAI API key' -AsSecureString
$env:OPENAI_API_KEY = [System.Net.NetworkCredential]::new('', $astraSecureKey).Password
python examples/astra.py text --prompt 'Explain three checks for an AI-generated website in English.'
```

Expect a text answer and token usage. Real requests incur API charges. Keep keys out of source files and screenshots. The scripts do not load `.env` files automatically.

### Four Python modes and JavaScript

```bash
python3 examples/astra.py text --prompt 'Write a checklist for reviewing a landing page.'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png \
  --prompt 'Describe the visible layout and components in English. Separate observations from guesses.'
python3 examples/astra.py research \
  --prompt 'Research Astra setup in official OpenAI documentation. Answer in English with source links.'
python3 examples/astra.py extract \
  --prompt 'Extract action items: Alex will review the screenshots by Friday. Sam will check mobile layout. Use null for missing details.'
node examples/quickstart.mjs
```

`vision` sends the selected image to the API. `research` filters searches to OpenAI documentation domains and prints returned citations. `extract` uses a strict JSON schema. `--output outputs/result.json` saves the full response; `--dry-run` previews any Python mode without sending it. JavaScript uses the prompt defined in [quickstart.mjs](examples/quickstart.mjs).

These examples call the **OpenAI API directly** and use an OpenAI key. They are not a Flaq.ai endpoint configuration. Model availability on Flaq.ai should be checked separately.

## See what creators have built

### Reference image → editable Blender model

![Tom Krcha's steam train, captured from a community showcase page](assets/screenshots/steam-train-reference.png)

By **Tom Krcha**. This is a screenshot of the creator's preview, not a Blender project reproduced in this repository. [Original post](https://x.com/tomkrcha/status/2095756085890310311) · [Practice task](docs/cases.md#case-04)

### Interactive iPhone history

![The iPhone Archive, captured from the live site](assets/screenshots/iphone-archive.png)

By **bluedev**. The live page was opened and captured; the complete app collection was not tested. [Live project](https://iphone-archive.vercel.app/) · [Original post](https://x.com/blueemi99/status/2096917792737911131)

### Seoul in 3D

![Seoul 3D Atlas in City and Sunset mode](assets/screenshots/seoul-atlas.png)

By **synabreu**. City and Sunset controls were checked; geographic accuracy was not audited. [Live project](https://seoul-3d-atlas.synabreu.chatgpt.site/) · [Original post](https://x.com/synabreu/status/2096557555086725159)

Explore all [12 cases](docs/cases.md), including physics toys, games, holographic cards, CAD assembly, video editing, pixel art, and scientific visualization. Practice prompts are written by the flaq.ai team for this guide; they are not the creators' original prompts. [Screenshot provenance](assets/screenshots/README.md)

## A workflow that is easy to repeat

1. Supply useful material: a reference, existing files, audience, and constraints.
2. Build the smallest working version first.
3. Request editable deliverables and clear launch instructions.
4. Check actual behavior, calculations, or file contents.
5. Revise using a screenshot or a reproducible error.

[OpenAI's model guide](https://developers.openai.com/api/docs/guides/latest-model) covers reasoning settings and advanced features. The API examples default to `low`; increase effort only when the task benefits from it. Use the documented settings rather than copying incompatible parameters from older examples.

## Verification and contributions

The examples passed **17 offline tests**. Screenshots are real browser captures. No paid API calls or end-to-end reproductions of the community projects were performed. See [verification](docs/verification.md), [sources](docs/sources.md), and [contributing](CONTRIBUTING.md).

Original guide content and code use the [MIT License](LICENSE). Third-party artwork, screenshots, trademarks, and linked code retain their respective rights.

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
