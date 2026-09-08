# GPT-6 Astra 実践ガイド

**[flaq.ai](https://flaq.ai/) チームがまとめた最新の GPT-6 Astra ガイド**です。モデルの概要、使い始め方、実行できるコード、制作ワークフロー、実際のスクリーンショットを紹介します。

<!-- languages:start -->
[English](README.md) · [简体中文](README_zh.md) · [繁體中文](README_tw.md) · **日本語** · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md) · [Русский](README_ru.md) · [Bahasa Indonesia](README_id.md) · [العربية](README_ar.md)
<!-- languages:end -->

最終確認：2026-09-08。OpenAI の公式ドキュメントではなく、チームによる独立したガイドです。README は12言語に対応しています。詳細なチュートリアルとサンプルの診断メッセージは現在、簡体字中国語です。

[入門](docs/quickstart.md) · [12の事例](docs/cases.md) · [6つのワークフロー](docs/workflows.md) · [コード例](examples/README.md)

## Astra とは

Astra は、複雑な推論、コーディング、調査、複数ステップの作業向けの OpenAI モデルです。テキストと画像を入力し、テキストを出力します。ブラウザー操作、ソフトウェアの実行、動画制作には、利用環境側のツールが必要です。

| モデル | `gpt-6-astra` |
| --- | --- |
| コンテキスト | 1,050,000 tokens |
| 最大出力 | 128,000 tokens |
| 推論レベル | `low` · `medium` · `high` · `xhigh` · `max` |

[公式モデル資料](https://developers.openai.com/api/docs/models/gpt-6-astra) · [設定と高度な使い方](https://developers.openai.com/api/docs/guides/latest-model)

## コードを書かずに始める

利用権限のある製品で Astra を選び、資料と小さな成果物を指定します。例えば次のように依頼します。

```text
カフェの2日間のイベントを計画してください。予算は2,000人民元、スタッフは2人です。ルール、時間割、予算表、宣伝文3本を作成し、合計額と仮定を確認してください。
```

## 最初のサンプルを実行する

Python 3.10+ または Node.js 20+ を使用し、リポジトリのルートで実行します。付属スクリプトは標準機能だけを使うため、パッケージのインストールは不要です。まずリクエストを無料で確認します。

```bash
python3 examples/astra.py text --dry-run
node examples/quickstart.mjs --dry-run
```

実際に呼び出す前に、Astra を利用できる OpenAI プロジェクトのキーを、現在のターミナルの `OPENAI_API_KEY` に設定します。[設定手順](docs/quickstart.md#用-api-开始)を参照してください。キーをコードや画像に含めないでください。`--dry-run` は通信せず、実際のリクエストは課金対象です。サンプルは OpenAI API を直接使います。Flaq.ai でのモデル提供状況は別途確認してください。

```bash
python3 examples/astra.py text --prompt 'カフェの2日間のイベントを計画してください。予算は2,000人民元、スタッフは2人です。ルール、時間割、予算表、宣伝文3本を作成し、合計額と仮定を確認してください。'
python3 examples/astra.py vision --image assets/screenshots/iphone-archive.png
python3 examples/astra.py research
python3 examples/astra.py extract
node examples/quickstart.mjs
```

[コード例](examples/README.md) · [Python](examples/astra.py) · [JavaScript](examples/quickstart.mjs)

## 作品と実際のスクリーンショット

以下はブラウザーで実際に取得した画像です。作品の権利は各作者に帰属し、制作プロジェクト全体を再現したものではありません。

![Tom Krcha の蒸気機関車：作者のプレビューを掲載したページ。](assets/screenshots/steam-train-reference.png)

Tom Krcha の蒸気機関車：作者のプレビューを掲載したページ。 [原投稿](https://x.com/tomkrcha/status/2095756085890310311)

![bluedev の iPhone Archive：実際に開いた公開サイト。](assets/screenshots/iphone-archive.png)

bluedev の iPhone Archive：実際に開いた公開サイト。 [原投稿](https://x.com/blueemi99/status/2096917792737911131) · [公開サイト](https://iphone-archive.vercel.app/)

![synabreu の Seoul 3D Atlas：City と Sunset の切り替えを確認。](assets/screenshots/seoul-atlas.png)

synabreu の Seoul 3D Atlas：City と Sunset の切り替えを確認。 [原投稿](https://x.com/synabreu/status/2096557555086725159) · [公開サイト](https://seoul-3d-atlas.synabreu.chatgpt.site/)

[画像の出典](assets/screenshots/README.md) · [12の事例](docs/cases.md)

## 実践ワークフロー

最小限の動くものを作り、実際の表示やエラーに基づいて修正します。編集可能なファイル、起動手順、実際のスクリーンショットを成果物に含めましょう。

[6つのワークフロー](docs/workflows.md)

## 検証とコントリビューション

17件のオフラインテストに合格しています。有料 API 呼び出しや、全コミュニティ作品の再現検証は行っていません。[検証記録](docs/verification.md) · [出典](docs/sources.md) · [貢献方法](CONTRIBUTING.md)。独自の文章とコードは [MIT](LICENSE)、第三者の素材には各権利が適用されます。

## flaq.ai について

[flaq.ai](https://flaq.ai/) は、AI エージェントや本番アプリケーション向けに、画像・動画・音楽・言語モデルへの統一 API を提供します。チームはこのガイドを通じて実践的な AI 活用方法を共有しています。公開ワークフロー：[Backlink Skills](https://github.com/flaqai/backlink_skills)。

## アフィリエイトとパートナー支援

クリエイター、開発者、教育者は [Flaq.ai アフィリエイトプログラム](https://flaq.ai/affiliate-program/)に参加し、自分の紹介リンクでチュートリアルやレビュー、導入ガイドを共有できます。

紹介ユーザーの最初の有効な有料注文は **20%**、以降の有効な有料注文は **10%**。対象期間は紹介ユーザーの登録後 **60日間**です。

ログインしてプロフィールを設定すると、紹介リンク、紹介実績、支払い設定を管理できます。紹介時にはアフィリエイト関係を明示してください。資格・審査・支払いは現行の[規約](https://flaq.ai/affiliate-agreement/)に従い、収益を保証するものではありません。
