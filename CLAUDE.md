# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Marp スライド作成ワークフローの Claude Code スキルコレクション。スキルごとに責務を分離し、整形・画像生成・レイアウト検証を個別のスキルとして提供する。日本語ユーザー向け。

## Commands

```bash
# Setup
uv sync

# Build slides to HTML
npx @marp-team/marp-cli <deck.md> --theme <theme.css> --html true --allow-local-files -o output/deck.html

# Generate images (requires GEMINI_API_KEY in .env)
source .env && export GEMINI_API_KEY && npx @miyakoh/slimg "<prompt>" -t flat -a <ratio> -o <path>

# Layout check (screenshot each slide)
bash skills/layout-fix/scripts/check-layout.sh <deck.md>

# Run tests
uv run pytest
```

## Architecture

### Skill System

各スキルは `skills/<name>/SKILL.md`（YAML frontmatter + Markdown）で定義。Claude Code が自動的にスキルとして認識する。

| Skill | Role |
|-------|------|
| **slide-style-MIYAKOH** | 既存 Marp スライドに39種レイアウトパターンを適用して整形（コアスキル） |
| **slimg** | `@miyakoh/slimg` npm パッケージ経由で Google Imagen 4 による画像生成 |
| **svg-creator** | SVG ダイアグラム・アイコンを直接生成（API不要） |
| **layout-fix** | agent-browser でスクリーンショット撮影 → レイアウト崩れ検出・修正 |

### Workflow

```
Marp スライド（ユーザー作成）
  → /slide-style-MIYAKOH（パターン適用 + slimg/svg-creator で画像生成）
  → /layout-fix（スクリーンショット検証 → 崩れ修正）
  → output/ に HTML 出力
```

### slide-style-MIYAKOH の構造

このスキルがシステムの中核。参照ファイルの役割を把握すること:

- `slides/example.md` — 39種パターンの実装コード。**整形時に必ず参照**してここからコピーする
- `docs/pattern-reference.md` — パターンの役割・選択ガイド（どのパターンを使うか判断する時）
- `docs/style-guide.md` — カラー、クラス一覧（デザインルール確認時）
- `themes/MIYAKOH.css` — テーマCSS。デッキと同じディレクトリにコピーして使う

### Design System: MIYAKOH

- **Colors**: Navy `#1B4565` + Teal `#3E9BA4`、グラデーション: Navy → Teal
- **Slide size**: 1920×1080
- **Key CSS classes**: `.key-message`（タイトル下のサブテキスト）、`.source`（出典）、`.panel`、`.stat-box`、`.panel-glass`、`.panel-gradient`
- **Utility classes**: Tailwind-like（`grid grid-cols-2 gap-6`、`bg-gray-50`、`text-navy`、`rounded-xl` 等）

## Key Constraints

- パターンは `slides/example.md` の39種から選ぶ。独自レイアウトは作らない
- 見出しはアクションタイトルにする（「コスト分析」→「ツールAは3年TCOで30%有利」）
- コロン（：）、感嘆符、装飾的な絵文字を使わない
- アクセントカラーは1スライド1-2色まで
- `stat-box accent`（Teal背景）は並列要素で1つだけ強調する場合のみ
- 同じパターンを3回以上連続で使わない
- キーメッセージは `<div class="key-message">` タグで記述する（ベタ書き不可）
- Python パッケージ管理は `uv` を使う（pip 不可）
- スキルディレクトリ内にツール・スクリプト・UI をバンドルしない。独立した場所に置く
- output/ 内に成果物を出力する。スキルディレクトリ内に HTML を生成しない

## External Tools

- [slirev](https://github.com/Miyazaki-Kohei/slirev) — スライドレビューツール。プレビューとスライド単位のフィードバック管理
- `@miyakoh/slimg` — 画像生成 npm パッケージ。`GEMINI_API_KEY` 環境変数が必要
- `agent-browser` — ヘッドレスブラウザでスクリーンショット撮影（layout-fix で使用）
