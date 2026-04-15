---
name: slide-style-MIYAKOH
description: MIYAKOH スライドスタイルガイドに基づいて Marp スライドを作成・整形する。Navy (#1B4565) + Teal (#3E9BA4) のカラースキームと39種のレイアウトパターンで、プロ品質のプレゼンスライドを生成する。image-creator による画像生成、svg-creator による図解・アイコン生成にも対応。スライド、プレゼン、発表資料、デッキ、Marp、MIYAKOH、SVG、図解 などのキーワードが含まれる場合は積極的に使用すること。
---

# slide-style-MIYAKOH

Marp で配布品質のスライドを作成する。MIYAKOH テーマ（1920×1080、Navy + Teal）を使用。

## 基本原則

- `slides/example.md` の39種パターンから選んで適用する。独自レイアウトは作らない
- 1スライド1メッセージ
- 見出しはアクションタイトル（「コスト分析」ではなく「ツールAは3年TCOで30%有利」）
- コロン（：）、感嘆符、装飾的な絵文字を使わない
- アクセントカラーは1スライド1-2色まで
- `stat-box accent`（Teal背景）は並列要素の中で1つだけ強調したい場合のみ。全要素同列なら全部 `stat-box`（グレー）で統一

## 参照ファイル

| ファイル | 内容 | 参照タイミング |
|---------|------|-------------|
| `slides/example.md` | 39種パターンの実装コード | **スライド作成時（必須）** |
| `docs/pattern-reference.md` | パターンの役割・選択ガイド | パターン選択時 |
| `docs/style-guide.md` | カラー、クラス一覧、画像ガイドライン | デザインルール確認時 |
| `themes/MIYAKOH.css` | テーマCSS | デッキディレクトリにコピー |

## ワークフロー

### Step 1: 意図確認

着手前に確認する: 対象読者、目的（聴衆に促す行動）、枚数目安、トーン（中立 / 説得的）

### Step 2: 構成決定

| シナリオ | 構成例 | 枚数 |
|----------|--------|------|
| 提案資料 | 表紙→背景→課題→提案→効果→計画→まとめ | 10-14 |
| 技術LT | 表紙→背景→アーキ→Before/After→まとめ | 8-12 |
| 進捗報告 | 表紙→サマリ→実績→課題→次アクション | 5-8 |
| 比較検討 | 表紙→評価軸→候補一覧→比較→推奨 | 8-12 |

### Step 3: パターン選択

`docs/pattern-reference.md` の選択ガイドを参照し、各スライドのパターンを決める。アウトラインを提示して承認を得る。

### Step 4: Markdown 執筆

`slides/example.md` から該当パターンをコピーし、内容を書き換える。

フロントマター:
```yaml
---
marp: true
theme: MIYAKOH
paginate: true
---
```

`themes/MIYAKOH.css` をデッキと同じディレクトリにコピーする。

執筆ルール:
- `<!-- _class: xxx -->` でクラス指定
- div レイアウトはユーティリティクラス使用（`grid grid-cols-2 gap-6` 等）
- 同じパターンを3回以上連続で使わない
- 出典は `<div class="source">出典: ...</div>`

### Step 4.5: ビジュアル生成

| 必要なビジュアル | スキル |
|----------------|--------|
| 写真・リアルなイラスト | `/image-creator` |
| 図解・ダイアグラム・アイコン | `/svg-creator` |

画像スタイル統一: `flat design, navy #1B4565 and teal #3E9BA4, white background, minimal`
保存先: 画像 → `images/`、SVG → `svg/`

### Step 5: ビルド

```bash
npx @marp-team/marp-cli deck.md --theme-set MIYAKOH.css --html --allow-local-files
npx @marp-team/marp-cli deck.md --theme-set MIYAKOH.css --pptx --allow-local-files
```

### Step 6: レイアウト確認（必須）

ビルド後、`/layout-fix` でレイアウトを確認する。省略しない。

```bash
uv run --with playwright python skills/layout-fix/scripts/check_layout.py deck.md
```

確認項目: テキストはみ出し、余白の偏り、タイトルが結論か、論点の詰め込み。問題があれば修正→再確認を繰り返す。