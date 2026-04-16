---
name: slide-orchestrator
description: プレゼンテーション作成の全工程を自動化するオーケストレーター。構成設計→スライド作成→レイアウト修正→レビューの一連のフローを、各専門スキル（slide-planner, slide-style-MIYAKOH, svg-creator, slimg, layout-fix）とslirevを連携させて実行する。「プレゼンを一から作って」「スライドを全部作って」「資料作成を全部やって」「プレゼン作成の全工程をお願い」「スライド作成を自動化して」などのキーワードで積極的に使用すること。個別スキルの単独実行ではなく、全工程を通しで実行したい場合にこのスキルを使う。
---

# slide-orchestrator

プレゼンテーション作成の全工程をオーケストレーションする。

各ステップを SubAgent として実行し、ファイル経由で結果を受け渡す。こうすることで各ステップのコンテキストが独立し、品質を維持したまま一気通貫で資料を作成できる。

## 全体フロー

```
Step 1: 構成設計（slide-planner）
    ↓ output/outline.md
Step 2: Marp 変換 + スタイル適用（slide-style-MIYAKOH + slimg + svg-creator）
    ↓ output/deck.md, output/deck.html
Step 3: レイアウト修正（layout-fix）
    ↓ output/deck.md（修正済み）
Step 4: プレビュー＆レビュー（slirev）
    ↓ ユーザーフィードバック
Step 5: フィードバック反映（必要に応じてループ）
```

## ワークフロー

### Step 1: 構成設計

SubAgent に `/slide-planner` スキルを実行させる。ヒアリング（AskUserQuestion）でユーザーとの対話が発生するため、**フォアグラウンド**で実行する（バックグラウンド不可）。

**SubAgent への指示:**
```
スキル /slide-planner を使って、以下のユーザー要望に基づいて構成メモを作成してください。

ユーザー要望: [ユーザーの元の依頼内容をそのまま渡す]

出力先: output/outline.md
```

SubAgent がユーザーとのヒアリング（AskUserQuestion）、リサーチ、構成設計を実施し、構成メモを `output/outline.md` に保存する。

**SubAgent 完了後:**
- `output/outline.md` を読み、構成が妥当か簡易チェックする

**ユーザー確認（必須）:**

スライド構成と各スライドの内容をユーザーに提示し、フィードバックを求める。スタイル適用後の修正はコストが高いため、この段階で内容を固める。

提示する内容:
- 選択したナラティブパターン名
- スライド構成の一覧（番号、見出し、要点の概要）

ユーザーの回答に応じて対応する:
- **OKの場合** → Step 2 へ進む
- **修正がある場合** → outline.md を修正し、再度確認を取る

### Step 2: Marp 変換 + スタイル適用

構成メモを Marp スライドに変換し、MIYAKOH スタイルを適用する。

このステップは2つのフェーズに分かれる。

**Phase 2a: 構成メモ → Marp 変換**

SubAgent に構成メモを読ませ、基本的な Marp 形式に変換させる。

```
output/outline.md を読み、以下のルールで Marp 形式の .md ファイルに変換してください。

変換ルール:
- 冒頭に Marp フロントマターを追加: marp: true, theme: MIYAKOH, paginate: true
- 各 "## Slide N:" セクションを --- で区切ったスライドに変換
- **見出し:** の内容を # 見出しに変換
- **要点:** の箇条書きをそのまま箇条書きとして配置
- **ビジュアル:** の内容はHTMLコメントとして残す: <!-- ビジュアル: 〇〇 -->
- **出典:** があれば末尾に小さく配置
- メタデータヘッダーやアジェンダは適切なスライドとして変換

出力先: output/deck.md
```

**テーマ CSS の配置:**

Phase 2b の前に、MIYAKOH テーマ CSS を output ディレクトリにコピーする。

```bash
cp .claude/skills/slide-style-MIYAKOH/themes/MIYAKOH.css output/MIYAKOH.css
```

**Phase 2b: スタイル適用**

SubAgent に `/slide-style-MIYAKOH` スキルを実行させる。

```
スキル /slide-style-MIYAKOH を使って、output/deck.md にレイアウトパターンを適用してください。

対象ファイル: output/deck.md
```

slide-style-MIYAKOH が39種のパターンから最適なものを選び、slimg や svg-creator を必要に応じて呼び出して画像・図を生成する。

**SubAgent 完了後:**
- `output/deck.md` が更新されていることを確認する
- HTML をビルドする:
  ```bash
  npx @marp-team/marp-cli output/deck.md -o output/deck.html --html true --theme output/MIYAKOH.css
  ```

### Step 3: レイアウト修正

SubAgent に `/layout-fix` スキルを実行させ、レンダリング結果を確認・修正する。

```
スキル /layout-fix を使って、output/deck.md のレイアウトを確認・修正してください。

対象ファイル: output/deck.md
```

layout-fix が agent-browser でスクリーンショットを撮り、テキストのはみ出し・余白の偏り・カラム崩れなどを検出して自動修正する。

**SubAgent 完了後:**
- 修正が行われた場合、HTML を再ビルドする:
  ```bash
  npx @marp-team/marp-cli output/deck.md -o output/deck.html --html true --theme output/MIYAKOH.css
  ```

### Step 4: プレビュー＆レビュー

slirev を起動してユーザーにスライドをレビューしてもらう。

**事前準備:**
- `output/deck.html` が存在することを確認する
- なければ marp-cli でビルド:
  ```bash
  npx @marp-team/marp-cli output/deck.md -o output/deck.html --html true --theme output/MIYAKOH.css
  ```

**slirev 起動:**
```bash
cd output && npx @miyakoh/slirev
```

ユーザーに以下を伝える:
- ブラウザで slirev が開きます
- 各スライドを確認し、修正が必要な箇所にコメントを入力してください
- 確認が終わったら「Export Comments」でコメントを出力し、こちらに戻ってきてください

### Step 5: フィードバック反映

ユーザーが slirev から戻ったら、フィードバックを確認して対応する。

1. slirev のコメント JSON を読む（ユーザーにパスを確認）
2. コメント内容に応じて修正を実施:
   - テキスト修正 → `output/deck.md` を直接編集
   - レイアウト修正 → layout-fix を再実行
   - 画像差し替え → slimg / svg-creator を再実行
3. 修正後、HTML を再ビルド:
   ```bash
   npx @marp-team/marp-cli output/deck.md -o output/deck.html --html true --theme output/MIYAKOH.css
   ```
4. 必要に応じて Step 4 に戻る（slirev で再確認）

ユーザーが「OK」と言うまでこのループを繰り返す。

## 注意事項

- 各ステップは SubAgent で実行し、コンテキストの肥大化を防ぐ
- ステップ間のデータ受け渡しはすべてファイル経由（`output/` ディレクトリ）
- 各ステップ完了後に簡潔な進捗報告をユーザーに行う（何が完了し、次に何をするか）
- エラーが発生した場合は該当ステップのみリトライする。全体をやり直す必要はない
- ユーザーが途中で方針変更した場合は、該当ステップから再開できる
