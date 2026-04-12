---
name: slide-style-rector
description: レクタースライドスタイルガイドに基づいて Marp スライドを作成・整形する。Navy (#1B4565) + Teal (#3E9BA4) のカラースキームと39種のレイアウトパターンで、プロ品質のプレゼンスライドを生成する。ergon による画像生成、svg-creator による図解・アイコン生成にも対応。スライド、プレゼン、発表資料、デッキ、Marp、レクター、rector、ergon、SVG、図解 などのキーワードが含まれる場合は積極的に使用すること。
---

# slide-style-rector

レクタースタイルガイドに基づき、Marp で**そのまま配布できる品質**のスライドを作成する。

## 基本原則

- **独自レイアウトを作成しない。** `slides/example.md` に定義された39種のレイアウトパターンから最適なものを選んで適用する。パターンの組み合わせでデザインの一貫性を維持する
- **テーマは `rector` 固定。** 1920×1080、Navy + Teal + グレースケールのカラースキーム
- **1スライド1メッセージ。** 伝えたいことが2つあるなら2枚に分ける
- **理知的な文体。** コロン（：）をタイトルに使わない。感嘆符・疑問符・装飾的な絵文字を避ける
- **色による強調は控えめに。** 1スライドあたりアクセントカラーは1-2色まで

---

## 参照ファイル

| ファイル | 内容 | いつ読むか |
|---------|------|-----------|
| `slides/example.md` | 39種のレイアウトパターン実装 | **スライド作成時（必須）** |
| `docs/pattern-reference.md` | 各パターンの役割・活用シーン・デザイン解説 | **パターン選択時** |
| `docs/style-guide.md` | カラー、タイポグラフィ、クラス一覧、画像ガイドライン | デザインルール確認時 |
| `themes/rector.css` | Marp テーマ CSS | デッキ作成時にコピー |

---

## ワークフロー

### Step 1: 意図確認

スライド作成に着手する前に、以下を確認する：
- **対象読者**: 誰に見せるか
- **目的**: 何を伝えたいか、聴衆にどんな行動を促すか
- **枚数の目安**: 短い提案（5-7枚）か、詳細な報告（10-15枚）か
- **トーン**: 中立的か、説得的か

### Step 2: 構成を決める

プレゼンの全体構成を決める。代表的なパターン：

| シナリオ | 構成 | 枚数目安 |
|----------|------|----------|
| 提案資料 | 表紙 → 背景 → 課題 → 提案 → 効果 → 計画 → まとめ | 10-14 |
| 技術 LT | 表紙 → 背景 → アーキ → Before/After → まとめ | 8-12 |
| 進捗報告 | 表紙 → サマリ → 実績 → 課題 → 次アクション | 5-8 |
| 比較検討 | 表紙 → 評価軸 → 候補一覧 → 比較 → 推奨 | 8-12 |

### Step 3: パターン選択

`docs/pattern-reference.md` のパターン選択ガイドを参照し、各スライドに使うパターンを決める。アウトラインを提示して承認を得る：

```
 1. [Pattern 1: title]            表紙
 2. [Pattern 4: toc]              目次
 3. [Pattern 2: section]          背景
 4. [Pattern 7a: 2col text+img]   市場環境
 5. [Pattern 27: 統計]            現状 KPI
 6. [Pattern 2: section]          課題
 7. [Pattern 6: 2col比較]         期待 vs 現実
 8. [Pattern 17: icon list]       4つの課題
 9. [Pattern 2: section]          提案
10. [Pattern 38: 対比+結論]       従来 vs 提案 → 結論
11. [Pattern 16: timeline]        実行計画
12. [Pattern 36: まとめ]          3つのポイント
13. [Pattern 29: Q&A]             質疑応答
14. [Pattern 5: closing]          クロージング
```

### Step 4: Markdown 執筆

`slides/example.md` から該当パターンのマークダウンをコピーし、内容を書き換える。

**フロントマター:**

```yaml
---
marp: true
theme: rector
paginate: true
---
```

**rector.css の配置:** デッキと同じディレクトリに `rector.css` をコピーする。

**守るべきルール:**
- アクションタイトルで見出しを書く（トピックラベル「コスト分析」ではなく結論「ツールAは3年TCOで30%有利」）
- `<!-- _class: xxx -->` でスライドレベルのクラスを指定
- div 内のレイアウトはユーティリティクラスを使う（`grid grid-cols-2 gap-6` 等）
- 同じパターンを3回以上連続で使わない
- 出典は `<div class="source">出典: ...</div>` で記載

### Step 4.5: ビジュアル生成（ergon / svg-creator 連携）

スライドにビジュアルが必要な場合、内容に応じて適切なスキルを選択する:

| 必要なビジュアル | 使用スキル | 例 |
|----------------|-----------|-----|
| 写真・リアルなイラスト | `/ergon` | チーム写真、製品画像、背景写真 |
| 図解・ダイアグラム | `/svg-creator` | フロー図、アーキテクチャ図、プロセス図 |
| アイコン | `/svg-creator` | 機能アイコン、ステップ番号、カテゴリ記号 |
| 抽象的な装飾 | `/svg-creator` | 幾何学パターン、背景装飾 |

**SVG が効果的なパターン:**
- Pattern 17（アイコンリスト）— icon-circle 内のアイコンを SVG に置換
- Pattern 22（カード型）— card-image ヘッダーに概念図 SVG
- Pattern 8/9（3カラム）— 各カラムのヘッダー画像に SVG
- Pattern 12/13（グリッド）— グリッドセル内の小アイコン SVG
- Pattern 33（インライン画像）— アーキテクチャ図・フロー図 SVG
- Pattern 24（右配置背景）— 装飾的な SVG パターン

**ergon による画像生成:**

画像生成時は以下のスタイル指示をプロンプトに含め、スライド全体のトーンを統一する:

- `flat design style, color palette: navy blue #1B4565 and teal #3E9BA4`
- `clean white background, minimal shadows`
- `professional, modern, minimalist`

| 用途 | スタイル (`-t`) | アスペクト比 (`-a`) | プロンプト例 |
|------|----------------|-------------------|-------------|
| スライド背景 | `flat` | `16:9` | `abstract geometric pattern, navy #1B4565 and teal #3E9BA4 gradients, minimal` |
| コンセプト図 | `flat` | `16:9` | `[概念] concept illustration, flat design, navy and teal palette, white background` |
| アイコン的画像 | `minimal` | `1:1` | `[対象] icon, flat design, teal #3E9BA4, white background, centered` |
| 人物・チーム | `corporate` | `16:9` | `professional business team, flat illustration, navy and teal color scheme` |

環境変数: `GOOGLE_API_KEY=$GEMINI_API_KEY npx ergon image gen "プロンプト" -t flat -a 16:9 -o images/filename.png`

**ファイル配置:**
- ergon 画像: デッキと同じディレクトリの `images/` に保存
- SVG: デッキと同じディレクトリの `svg/` に保存
- Marp での参照: `![bg right:40%](images/filename.png)` or `<img src="svg/diagram.svg">`
- ビルド時 `--allow-local-files` フラグが必須

### Step 5: ビルド

```bash
# HTML 出力（プレビュー用）
npx @marp-team/marp-cli deck.md --theme-set rector.css --html --allow-local-files

# PPTX 出力（配布用）
npx @marp-team/marp-cli deck.md --theme-set rector.css --pptx --allow-local-files
```

`--allow-local-files` はローカル画像の読み込みに必須。

### Step 6: 目視確認

生成物を1枚ずつ確認し、以下をチェック：
- テキストがはみ出していないか
- 余白が極端に偏っていないか
- タイトルが結論になっているか（トピックラベルで止まっていないか）
- 1スライドに論点が2つ以上詰まっていないか

レイアウト崩れが見つかった場合は `/layout-fix` スキルで修正する。

---

## パターンカテゴリ一覧

| カテゴリ | パターン番号 | 概要 |
|---------|------------|------|
| **A. タイトル・セクション系** | 1-5 | 表紙、章扉、まとめ、目次、クロージング |
| **B. カラムレイアウト系** | 6-13 | 2-5カラム、グリッド |
| **C. 縦並びリスト系** | 14-17 | ステップ、タイムライン、アイコンリスト |
| **D. パネルデザイン系** | 18-22 | 基本、強調、ガラス、グラデーション、カード |
| **E. 背景・画像系** | 23-26 | 全画面、右配置、引用、分割背景 |
| **F. 強調・特殊系** | 27-29 | 統計、中央メッセージ、Q&A |
| **G. 応用パターン系** | 30-39 | QR、問いかけ、脚注、対比+結論、テーブル等 |

各パターンの詳細は `docs/pattern-reference.md` を参照。

---

## セクションクラス早見表

| クラス | 用途 |
|-------|------|
| `title` | 表紙（グラデーション背景、`_paginate: false`） |
| `section` | セクション扉（グラデーション背景） |
| `section-end` | セクションまとめ（gray-50 背景） |
| `toc` | 目次 |
| `closing` | クロージング（グラデーション背景） |
| `bg-full` | 全画面背景画像 |
| `quote` | 引用 |
| `center-message` | 中央メッセージ（64px） |
| `qanda` | Q&A（88px） |
| `question` | 問いかけ（グラデーション背景、白枠） |
| `compact` | 情報密度が高いスライド |

---

## 判断に迷ったら

- 迷ったら**スライドを分ける**
- 迷ったら **Pattern 6 (2カラム比較)** か **Pattern 8 (3カラム)**
- 表・グラフを入れたいなら **Pattern 39 (テーブル)** か **Pattern 27 (統計)**
- 装飾よりも明快さを優先する
- ユーザー指定の枚数は尊重する
