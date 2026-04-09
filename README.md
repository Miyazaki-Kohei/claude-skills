# Claude Code Slides Skill (Python + uv)

Claude Code の Skills でスライド作成を安定運用するための雛形です。

- 標準レンダラ: **Marp**
- 例外ルート: **Slidev**（インタラクティブ、コードデモ、ライブ発表向け）
- 補助実装: **Python + uv**
- Node ツールはレンダリング用途に限定

## なぜこの構成か

- Claude Code の skill は `SKILL.md` ベースで動作するため、Markdown 中心のワークフローと相性が良い。
- Marp CLI は Markdown から HTML / PDF / PPTX に変換でき、業務スライドの自動生成・差分管理・修正運用に向く。 citeturn846913search0turn846913search1turn846913search9
- Slidev は PDF / PPTX 出力も可能だが、Playwright 前提でデモ・インタラクティブ用途向き。 citeturn846913search2turn846913search10turn846913search18
- `uv` は Python プロジェクトと単体スクリプトの運用に向く。 citeturn846913search3turn846913search7turn846913search11turn846913search19

## セットアップ

### 1. Python 環境

```bash
uv sync
```

### 2. Node レンダラ

Marp を使う場合:

```bash
npm install -D @marp-team/marp-cli
```

Slidev を使う場合:

```bash
npm install -D @slidev/cli playwright-chromium
```

## 使い方

新規 Marp デッキ作成:

```bash
uv run python -m scripts.new_deck my-deck --engine marp
```

ビルド:

```bash
uv run python -m scripts.build decks/my-deck/deck.md --format html
uv run python -m scripts.build decks/my-deck/deck.md --format pdf
uv run python -m scripts.build decks/my-deck/deck.md --format pptx
```

Lint:

```bash
uv run python -m scripts.lint_deck decks/my-deck/deck.md
```

環境確認:

```bash
uv run python -m scripts.doctor
```

## 推奨運用

1. Claude に先にストーリーラインを作らせる
2. 1 枚 1 メッセージで Markdown 化させる
3. Python lint で文字量と構成をチェックする
4. Marp で HTML/PDF を出して視覚確認する
5. 必要時のみ Slidev に切り替える

