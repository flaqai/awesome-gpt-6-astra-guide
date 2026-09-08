# GPT-6 Astra 実践ガイド

**[flaq.ai](https://flaq.ai/) チームがまとめた最新の GPT-6 Astra ガイド**です。モデルの概要、使い始め方、実行できるコード、制作ワークフロー、実際のスクリーンショットを紹介します。

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · **日本語** · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

最終確認：2026-09-08。OpenAI の公式ドキュメントではなく、チームによる独立したガイドです。README は12言語に対応しています。詳細なチュートリアルとサンプルの診断メッセージは現在、簡体字中国語です。

[入門](docs/quickstart.md) · [12の事例](docs/cases.md) · [6つのワークフロー](docs/workflows.md) · [コード例](examples/README.md)

## Astra とは

Astra は、複雑な推論、コーディング、調査、複数ステップの作業向けの OpenAI モデルです。テキストと画像を入力し、テキストを出力します。ブラウザー操作、ソフトウェアの実行、動画制作には、利用環境側のツールが必要です。


[公式モデル資料](https://developers.openai.com/api/docs/models/gpt-6-astra) · [設定と高度な使い方](https://developers.openai.com/api/docs/guides/latest-model)

## コードを書かずに始める

利用権限のある製品で Astra を選び、資料と小さな成果物を指定します。例えば次のように依頼します。

```text
カフェの2日間のイベントを計画してください。予算は2,000人民元、スタッフは2人です。ルール、時間割、予算表、宣伝文3本を作成し、合計額と仮定を確認してください。
```

## クライアントから直接使う

ChatGPTアカウントでログインして開始できます。APIキーの事前設定は不要です。Astraの利用可否と上限はアカウントやワークスペースにより異なります。

### ChatGPT

ChatGPTにログインし、成果物の制作にはWorkを選びます。モデル／PowerからAstraを選択し、必要ならAdvancedで確認。予算画像を添付し、24人と32人を比較するよう依頼します。

### Codex

Codexクライアントにログインします。統合デスクトップアプリではCodexに切り替え、ローカルフォルダーを開きます。新しいタスクでAstraを選び、独自実習の実行、ファイルと検証結果の提出を依頼します。

### Codex CLI

[CLIのインストール](https://learn.chatgpt.com/docs/cli). 公式ページからCLIをインストールし、プロジェクト内で起動します。初回はSign in with ChatGPTを選択。セッション内の/modelでAstra、/statusで設定を確認し、普通の言葉で依頼します。

```bash
codex -m gpt-6-astra
```

[詳しい手順（中国語）](docs/quickstart.md) · [English](README.md) · [Models](https://learn.chatgpt.com/docs/models)

<details>
<summary>APIは独自アプリへの組み込み時に</summary>

[API](docs/api.md) · [Python / JavaScript](examples/README.md)

</details>

## 独自の実習を動かす

独自に作成した3つの演習は、架空のスタジオ資料を共有します。画像はローカルで生成した SVG レポートの実際のブラウザー画面です。第三者の作品や Astra API の実測出力ではありません。

```bash
python3 examples/field_lab.py
# Alternative scenario / 独立输出目录
python3 examples/field_lab.py --guests 32 --out outputs/field-lab-32
```

![予算：支出 2,168 元、予備費 432 元。](assets/screenshots/workshop-budget.png)

予算：支出 2,168 元、予備費 432 元。

![絵コンテ：20秒、30 fps、連続する600フレーム。](assets/screenshots/craft-storyboard.png)

絵コンテ：20秒、30 fps、連続する600フレーム。

![公開前レビュー：架空の5項目中3項目が合格、2項目は要修正。](assets/screenshots/release-review.png)

公開前レビュー：架空の5項目中3項目が合格、2項目は要修正。

[ソースコード・再現手順・演習](docs/original-lab.md) · [SVG / PNG](assets/screenshots/README.md)

## 実践ワークフロー

最小限の動くものを作り、実際の表示やエラーに基づいて修正します。編集可能なファイル、起動手順、実際のスクリーンショットを成果物に含めましょう。

[6つのワークフロー](docs/workflows.md)

## 検証とコントリビューション

28件のオフラインテストに合格しています。有料 API 呼び出しや、全コミュニティ作品の再現検証は行っていません。[検証記録](docs/verification.md) · [出典](docs/sources.md) · [貢献方法](CONTRIBUTING.md)。独自の文章とコードは [MIT](LICENSE)、第三者の素材には各権利が適用されます。

## 楽しい3D：組み上がる小さなロボット

卓上ロボット、組立アニメーション、読書コーナー、紙回路の短編、キノコのキャラクター、シーン点検の6演習を追加しました。英語・中国語ガイドにプロンプト、設定、フレーム確認、独自スクリプトがあります。スクリプトは構文確認のみで、Blenderでの実行は未検証です。

[Blender実習ガイド](docs/blender-playbook.md) · [Python](examples/blender/desk_robot.py)

## flaq.ai について

[flaq.ai](https://flaq.ai/) は、AI エージェントや本番アプリケーション向けに、画像・動画・音楽・言語モデルへの統一 API を提供します。チームはこのガイドを通じて実践的な AI 活用方法を共有しています。公開ワークフロー：[Backlink Skills](https://github.com/flaqai/backlink_skills)。

## アフィリエイトとパートナー支援

クリエイター、開発者、教育者は [Flaq.ai アフィリエイトプログラム](https://flaq.ai/affiliate-program/)に参加し、自分の紹介リンクでチュートリアルやレビュー、導入ガイドを共有できます。

紹介ユーザーの最初の有効な有料注文は **20%**、以降の有効な有料注文は **10%**。対象期間は紹介ユーザーの登録後 **60日間**です。

ログインしてプロフィールを設定すると、紹介リンク、紹介実績、支払い設定を管理できます。紹介時にはアフィリエイト関係を明示してください。資格・審査・支払いは現行の[規約](https://flaq.ai/affiliate-agreement/)に従い、収益を保証するものではありません。

## 参考資料と着想

[用GPT-6 Astra操控Blender玩3D，保姆级教程来了。](https://mp.weixin.qq.com/s/yK65CvMwzhQqu5_E5EfVVQ)

発行：数字生命卡兹克。著者：卡兹克、可达。2026-09-08。制作手順の着想源です。記事の画像や長いプロンプトは転載していません。
