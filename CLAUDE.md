# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Marp ベースのプレゼンテーション作成を自動化する Claude Code スキルコレクション。6つの専門スキルが責務分離された設計で連携する。

## コマンド

```bash
# セットアップ
uv sync

# Marp HTML ビルド
npx @marp-team/marp-cli output/deck.md --html true --theme output/MIYAKOH.css -o output/deck.html

# Marp PPTX エクスポート
npx @marp-team/marp-cli output/deck.md --pptx --theme-set output/MIYAKOH.css -o output/deck.pptx

# 画像生成（GEMINI_API_KEY 必要）
npx @miyakoh/slimg "<prompt>" -t <style> -a <ratio> -o images/<name>.png

# レイアウト検証（agent-browser でスクリーンショット撮影）
bash skills/layout-fix/scripts/check-layout.sh output/deck.md
bash skills/layout-fix/scripts/cleanup.sh /tmp/marp-layout-XXXXXX

# スライドレビュー（slirev）
cd output && npx @miyakoh/slirev

# テスト
uv run pytest
```

**Python パッケージ管理は `uv` を使う。pip は使わない。**

## アーキテクチャ

### スキル構成とパイプライン

```
slide-orchestrator（全工程オーケストレーション）
  ├→ SubAgent: slide-planner → output/outline.md
  ├→ SubAgent: slide-style-MIYAKOH → output/deck.md + deck.html
  │     ├→ /slimg（画像生成）
  │     └→ /svg-creator（SVG 生成）
  ├→ SubAgent: layout-fix → output/deck.md（修正済み）
  └→ slirev でユーザーレビュー → フィードバックループ
```

- **slide-planner**: 構成設計のみ（スタイリングしない）。8つのナラティブパターンから選択し `output/outline.md` を出力
- **slide-style-MIYAKOH**: スタイル整形のみ（コンテンツ変更しない）。39種のレイアウトパターンを適用
- **layout-fix**: agent-browser でスクリーンショット撮影し視覚的にレイアウト崩れを検出・修正
- **slimg**: Google Imagen 4 による画像生成。slide-style-MIYAKOH から呼ばれる
- **svg-creator**: Claude ネイティブの SVG 生成。外部 API 不要
- **slide-orchestrator**: 上記全スキルを SubAgent で順次実行

### ファイルベース連携

スキル間のデータ受け渡しはすべて `output/` ディレクトリのファイル経由。コンテキスト肥大化を防ぐため SubAgent 実行が基本。

### 重要な責務境界

- スキルファイル（`skills/` 配下）のデバッグ時のみスキルファイルを修正する。通常のデッキ生成では `output/deck.md` のみ修正し、スキルファイルには触れない
- ツール・スクリプト・UI をスキルディレクトリにバンドルしない。独立して管理する

### ディレクトリ構成

- `skills/` — スキルの正規ソース（各スキルに `SKILL.md`）
- `.claude/skills/` — Claude Code が読むスキルファイル（skills/ からコピー/シンボリックリンク）
- `output/` — ビルド成果物（gitignore）
- `decks/` — アーカイブ済みデッキ（gitignore）

### MIYAKOH デザインシステム

- **カラー**: Navy `#1B4565`、Teal `#3E9BA4`、9段階グレースケール
- **タイポグラフィ**: 56px〜18px の8段階、フォントは Helvetica Neue / Hiragino Kaku Gothic ProN
- **スライドサイズ**: 1920×1080
- **ユーティリティクラス**: Tailwind 風（grid-cols-N, gap-N, flex, text-xl 等）
- **テーマ CSS**: `skills/slide-style-MIYAKOH/themes/MIYAKOH.css`
- **パターンカタログ+使用例**: `skills/slide-style-MIYAKOH/slides/example.md`（39種、選択ガイド+説明コメント付き）

### スライドコンテンツルール

- 見出しはアクション型（「コスト分析」ではなく「ツールAは3年TCOで30%有利」）
- コロン・感嘆符・装飾絵文字は禁止
- 1スライド = 1メッセージ、箇条書きは3〜5項目
- アクセントカラーは1スライドにつき最大1〜2色

## スキルの追加

`skills/<skill-name>/SKILL.md` を作成すれば Claude Code のスキルとして認識される。
