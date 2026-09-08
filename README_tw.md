# GPT-6 Astra 實用指南

由 **[flaq.ai](https://flaq.ai/) 團隊整理的最新 GPT-6 Astra 指引**，涵蓋模型介紹、入門方法、程式範例、創作流程與真實截圖。

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · **繁體中文** · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

最後核對：2026-09-08。這是團隊獨立整理的指南，並非 OpenAI 官方文件。README 支援 12 種語言；深入教學與範例診斷訊息目前為簡體中文。

[入門教學](docs/quickstart.md) · [12 個案例](docs/cases.md) · [6 套工作流程](docs/workflows.md) · [程式範例](examples/README.md)

## Astra 是什麼？

Astra 是 OpenAI 用於複雜推理、程式開發、研究及多步驟工作的模型。它接受文字與圖片，輸出文字；瀏覽、執行軟體及製作影音需要應用環境提供相應工具。

| 模型 | `gpt-6-astra` |
| --- | --- |
| 上下文 | 1,050,000 tokens |
| 最大輸出 | 128,000 tokens |
| 推理強度 | `low` · `medium` · `high` · `xhigh` · `max` |

[官方模型文件](https://developers.openai.com/api/docs/models/gpt-6-astra) · [參數與進階用法](https://developers.openai.com/api/docs/guides/latest-model)

## 不寫程式也能開始

在帳號可使用的產品中選擇 Astra，提供材料並指定一個小成果。例如：

```text
為咖啡店規劃兩天活動。預算人民幣 2000 元，兩位店員。交付活動規則、時間表、預算和三則文案。確認預算加總正確，並明確標示假設。
```

## 執行第一個範例

使用 Python 3.10+ 或 Node.js 20+，在儲存庫根目錄執行。完整腳本使用內建函式庫，不需要安裝套件。先免費預覽請求：

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

真實呼叫前，請在目前終端設定有 Astra 權限的 OpenAI 專案密鑰 `OPENAI_API_KEY`。請依照 [設定教學](docs/quickstart.md#用-api-开始) 操作，不要將密鑰放進程式碼或截圖。`--dry-run` 不連線；真實請求會產生費用。範例直接呼叫 OpenAI API，Flaq.ai 的模型供應情況需另行確認。

```bash
python3 examples/astra.py text --prompt '為咖啡店規劃兩天活動。預算人民幣 2000 元，兩位店員。交付活動規則、時間表、預算和三則文案。確認預算加總正確，並明確標示假設。'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[程式範例](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## 作品與真實截圖

以下圖片為實際瀏覽器截圖。社群作品保留原作者權利；未完整重現其工程。

![Tom Krcha 的蒸汽火車：作者預覽的頁面截圖。](assets/screenshots/steam-train-reference.png)

Tom Krcha 的蒸汽火車：作者預覽的頁面截圖。 [原帖](https://x.com/tomkrcha/status/2095756085890310311)

![bluedev 的 iPhone Archive：實際開啟的線上頁面。](assets/screenshots/iphone-archive.png)

bluedev 的 iPhone Archive：實際開啟的線上頁面。 [原帖](https://x.com/blueemi99/status/2096917792737911131) · [線上作品](https://iphone-archive.vercel.app/)

![synabreu 的首爾 3D 地圖：已檢查 City 與 Sunset 切換。](assets/screenshots/seoul-atlas.png)

synabreu 的首爾 3D 地圖：已檢查 City 與 Sunset 切換。 [原帖](https://x.com/synabreu/status/2096557555086725159) · [線上作品](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[截圖來源](assets/screenshots/README.md) · [12 個案例](docs/cases.md)

## 實作流程

先做最小可用版本，再根據實際畫面、錯誤訊息和驗收結果逐項修改。要求可編輯檔案、啟動方式及真實截圖。

[6 套工作流程](docs/workflows.md)

## 驗證與貢獻

17 項離線測試已通過，尚未執行付費 API 呼叫。社群案例未全面實測。[驗證紀錄](docs/verification.md) · [資料來源](docs/sources.md) · [貢獻說明](CONTRIBUTING.md)。原創文字與程式使用 [MIT](LICENSE)；第三方素材保留各自權利。

## 關於 flaq.ai

[flaq.ai](https://flaq.ai/) 為 AI Agent 與正式應用提供圖片、影片、音樂及語言模型的統一 API 存取。團隊透過這份指引分享可操作的 AI 實作方法。開源工作流程：[Backlink Skills](https://github.com/flaqai/backlink_skills)。

## 聯盟行銷與合作支援

歡迎創作者、開發者與教育者加入 [Flaq.ai 聯盟計畫](https://flaq.ai/affiliate-program/)，透過自己的推薦連結分享教學、評測與整合指南。

首筆有效付費訂單 **20%**；後續有效付費訂單 **10%**。有效訂單的歸因窗口為推薦使用者註冊後 **60 天**。

登入並完成聯盟資料後，可管理推薦連結、追蹤推薦及設定收款方式。分享時應揭露聯盟關係。資格、審核與結算以現行 [聯盟協議](https://flaq.ai/affiliate-agreement/) 為準，不保證收益。
