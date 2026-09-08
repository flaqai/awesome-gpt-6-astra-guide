# GPT-6 Astra 實用指南

由 **[flaq.ai](https://flaq.ai/) 團隊整理的最新 GPT-6 Astra 指引**，涵蓋模型介紹、入門方法、程式範例、創作流程與真實截圖。

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · **繁體中文** · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

最後核對：2026-09-08。這是團隊獨立整理的指南，並非 OpenAI 官方文件。README 支援 12 種語言；深入教學與範例診斷訊息目前為簡體中文。

[入門教學](docs/quickstart.md) · [12 個案例](docs/cases.md) · [6 套工作流程](docs/workflows.md) · [程式範例](examples/README.md)

## Astra 是什麼？

Astra 是 OpenAI 用於複雜推理、程式開發、研究及多步驟工作的模型。它接受文字與圖片，輸出文字；瀏覽、執行軟體及製作影音需要應用環境提供相應工具。


[官方模型文件](https://developers.openai.com/api/docs/models/gpt-6-astra) · [參數與進階用法](https://developers.openai.com/api/docs/guides/latest-model)

## 不寫程式也能開始

在帳號可使用的產品中選擇 Astra，提供材料並指定一個小成果。例如：

```text
為咖啡店規劃兩天活動。預算人民幣 2000 元，兩位店員。交付活動規則、時間表、預算和三則文案。確認預算加總正確，並明確標示假設。
```

## 直接在客戶端使用

以 ChatGPT 帳號登入即可開始，無需先設定 API key；Astra 的可用性與額度依帳號及工作區而定。

### ChatGPT

登入 ChatGPT，製作完整成果時選 Work；在模型／Power 選單選 Astra，必要時開啟 Advanced。上傳預算圖，要求比較 24 人與 32 人的費用。

### Codex

登入 Codex 客戶端；統一桌面應用可切換至 Codex。開啟本機專案資料夾，新建任務並選 Astra，要求執行原創實驗並交付檔案與實際檢查結果。

### Codex CLI

[安裝 CLI](https://learn.chatgpt.com/docs/cli). 先依官方安裝頁安裝 CLI，在專案目錄啟動。首次選 Sign in with ChatGPT 完成登入；在互動介面用 /model 核對 Astra、/status 查看設定，再直接輸入任務。

```bash
codex -m gpt-6-astra
```

[詳細步驟（中文）](docs/quickstart.md) · [English](README.md) · [Models](https://learn.chatgpt.com/docs/models)

<details>
<summary>API 僅供自行開發應用時使用</summary>

[API](docs/api.md) · [Python / JavaScript](examples/README.md)

</details>

## 執行本專案原創實驗

三套獨立編寫的練習共用一份虛構工作室資料。圖片是本機程式生成 SVG 報告後取得的瀏覽器截圖，並非第三方作品或 Astra API 實測輸出。

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![工作坊預算：支出 2,168 元，預留 432 元。](assets/screenshots/workshop-budget.png)

工作坊預算：支出 2,168 元，預留 432 元。

![分鏡時間軸：20 秒、30 fps，共 600 個連續影格。](assets/screenshots/craft-storyboard.png)

分鏡時間軸：20 秒、30 fps，共 600 個連續影格。

![發布驗收：5 項虛構檢查通過 3 項，2 項待修正。](assets/screenshots/release-review.png)

發布驗收：5 項虛構檢查通過 3 項，2 項待修正。

[原始碼、重現步驟與練習](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## 實作流程

先做最小可用版本，再根據實際畫面、錯誤訊息和驗收結果逐項修改。要求可編輯檔案、啟動方式及真實截圖。

[6 套工作流程](docs/workflows.md)

## 驗證與貢獻

28 項離線測試已通過，尚未執行付費 API 呼叫。社群案例未全面實測。[驗證紀錄](docs/verification.md) · [資料來源](docs/sources.md) · [貢獻說明](CONTRIBUTING.md)。原創文字與程式使用 [MIT](LICENSE)；第三方素材保留各自權利。

## 趣味 3D：讓小機器人自行組裝

新增六種原創 Blender 練習：桌面機器人、零件組裝、閱讀角、紙電路短片、蘑菇吉祥物與場景檢查。中英文指引提供提示詞、工具設定、影格驗收和原創腳本。腳本僅通過語法檢查，尚未在 Blender 執行。

[開啟 Blender 趣味指引](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## 關於 flaq.ai

[flaq.ai](https://flaq.ai/) 為 AI Agent 與正式應用提供圖片、影片、音樂及語言模型的統一 API 存取。團隊透過這份指引分享可操作的 AI 實作方法。開源工作流程：[Backlink Skills](https://github.com/flaqai/backlink_skills)。

## 聯盟行銷與合作支援

歡迎創作者、開發者與教育者加入 [Flaq.ai 聯盟計畫](https://flaq.ai/affiliate-program/)，透過自己的推薦連結分享教學、評測與整合指南。

首筆有效付費訂單 **20%**；後續有效付費訂單 **10%**。有效訂單的歸因窗口為推薦使用者註冊後 **60 天**。

登入並完成聯盟資料後，可管理推薦連結、追蹤推薦及設定收款方式。分享時應揭露聯盟關係。資格、審核與結算以現行 [聯盟協議](https://flaq.ai/affiliate-agreement/) 為準，不保證收益。

## 引用來源與創作啟發

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

公眾號：数字生命卡兹克；作者：卡兹克、可达；2026-09-08。作為流程設計的啟發，不轉載文章圖片或長提示詞。
