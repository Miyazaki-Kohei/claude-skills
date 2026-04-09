---
name: ppt-creator
description: Marp でコンサルティング品質のスライドを生成・編集する。提案資料、役員報告、ツール比較、進捗報告などのビジネススライドを作成する際に使用する。McKinsey/BCG スタイルのアクションタイトル、SCQA・ピラミッド原則・MECE のフレームワーク、プロフェッショナルな CSS テーマを適用する。スライド、プレゼン、発表資料、デッキ、提案書、パワポ、pptx などのキーワードが含まれる場合は積極的に使用すること。
---

# Consulting Slides Skill

Marp + Python でコンサルティング品質のスライドを生成する。
スクリプトはプロジェクトルートから `PYTHONPATH=skills/ppt-creator` を付けて実行し、成果物はプロジェクトの `output/` に出力する。

## Philosophy

- **Marp 専用**。Slidev は使わない。
- **アクションタイトル必須**: 見出しにはトピックラベル (「コスト分析」) ではなく結論 (「ツール A は 3 年 TCO で 30% 有利」) を書く。聴衆が見出しだけ読んでもストーリーが伝わる状態を目指す。
- **1 スライド 1 メッセージ**: 伝えたいことが 2 つあるなら 2 枚に分ける。
- **フレームワーク駆動**: まず構造 (SCQA / Pyramid / MECE) を決め、次にコンテンツ、最後にレイアウト。構造が決まれば中身はぶれない。
- **品質はスクリプトで担保**: `lint_deck.py` で機械的にチェックし、人の目視は最小限にする。

---

## Workflow

### Step 1: 意図確認（必ず実施）

スライド作成に着手する前に、以下の項目をユーザーに確認する。
ユーザーのリクエストから推測できる場合でも、推測内容をテーブル形式で提示して承認を得ること。
確認なしにいきなりスライドを作り始めない — ヒアリングが品質の出発点になる。

| 項目 | 例 | 補足 |
|------|-----|------|
| **audience** | 情シス部門と経営層 | 誰が見るかでトーンとテーマが変わる |
| **purpose** | ETL ツール選定の意思決定支援 | 目的によりフレームワークが決まる |
| **takeaway** | 運用安定性を優先しツール A を採用すべき | 聴衆が持ち帰るべき結論 |
| **tone** | 簡潔、事実ベース、断定的 | 断定的 / 中立 / 説得的 etc. |
| **pages** | 10 | ±2 枚で調整する |
| **theme** | consulting-light | light / dark / minimal から選択 |

### Step 2: テンプレート & テーマ選択

| シナリオ | テンプレート | フレームワーク | 枚数目安 |
|----------|-------------|---------------|----------|
| 提案資料 | `proposal` | SCQA | 10 |
| 役員報告 | `executive-summary` | Pyramid | 5 |
| ツール / 手法比較 | `comparison` | MECE | 8 |
| 進捗報告 | `status-report` | — | 6 |
| その他 / 自由構成 | `blank` | SCQA (default) | 自由 |

迷ったら `consulting-light` テーマ + SCQA フレームワーク。

```bash
# プロジェクトルートで実行する
PYTHONPATH=skills/ppt-creator uv run python -m scripts.new_deck my-deck \
  --template proposal \
  --theme consulting-light \
  --output-dir /absolute/path/to/project/output
```

### Step 3: アウトライン作成

テンプレートの `{{...}}` プレースホルダをアクションタイトルに置き換える。
レイアウトクラスも決める。以下のようなアウトラインをユーザーに提示して承認を得る:

```
1. [center] タイトル + 日付
2. [center] 結論: 運用安定性を優先しツール A を採用すべき
3. [split] 現在 3 つの ETL ツールが市場で主流となっている
4. [split] 手動運用はデータ量増加に耐えられない
5. [quote] どのツールを採用すべきか？
6. [center] ツール A が安定性・コストの両面で最適
7. [grid-2] ツール A は導入実績と保守性で他を上回る
8. [vs] コスト比較ではツール A が 3 年 TCO で 30% 有利
9. [kpi] 導入効果: 工数 50% 削減、エラー率 80% 低減
10. [split] 来週 PoC 開始、4 週間で評価完了
```

### Step 4: Markdown 執筆

`deck.md` を開き、`{{...}}` プレースホルダを **すべて** 実際のコンテンツに置き換える。
`{{` が 1 つでも残っていたら未完成。完成後にファイル内に `{{` が含まれないことを確認する。

守るべきルール:
- アクションタイトルで見出しを書く (トピックラベル禁止)
- 1 スライド 1 メッセージ
- `<!-- _class: xxx -->` でレイアウトを指定
- Content Limits を守る (後述)
- 図が必要な箇所は `![placeholder](assets/xxx.png)` を置く
- テンプレートのスライド構成は目安。内容に応じてスライドの追加・削除・順序変更をしてよい
- **参照リンク**: 調査やデータに基づくスライドでは、最終スライドまたは各スライドのフッターに出典URLを記載する。聴衆が後から原典をたどれるようにするため

### Step 5: Lint

```bash
PYTHONPATH=skills/ppt-creator uv run python -m scripts.lint_deck /absolute/path/to/project/output/my-deck/deck.md
```

ERROR → 必ず修正。WARNING → できる限り対処。
品質の目安は `references/quality-checklist.md` を参照。

### Step 6: Build

```bash
PYTHONPATH=skills/ppt-creator uv run python -m scripts.build /absolute/path/to/project/output/my-deck/deck.md --format html
PYTHONPATH=skills/ppt-creator uv run python -m scripts.build /absolute/path/to/project/output/my-deck/deck.md --format pptx
```

`marp` が未インストールの場合、`npx @marp-team/marp-cli` を自動的にフォールバックする。
それも使えない場合は `PYTHONPATH=skills/ppt-creator uv run python -m scripts.doctor` で環境を確認し、インストール手順を案内する。

### Step 7: 品質評価 & フィードバックループ

Build 完了後、成果物を自己評価して品質を担保する。**90 点以上になるまでこのループを繰り返す。**

1. **HTML を確認**: 生成された HTML をブラウザで開き、レイアウト・色・フォントが意図通りか目視確認する。
2. **品質チェックリストで採点**: `references/quality-checklist.md` の 100 点満点ルブリックに沿って、Content (40 点)・Design (30 点)・Code (15 点)・Accessibility (15 点) の各項目をスコアリングする。
3. **改善点を特定**: 減点された項目を洗い出し、原因を分析する。典型的な減点要因:
   - アクションタイトルがトピックラベルになっている → 結論を述べる形に書き直す
   - 同一レイアウトの連続 → レイアウトクラスを変更
   - コンテンツ過多 → スライドを分割するか文言を削る
   - **情報不足** → 具体的な数値・比較データ・根拠を追加する。スライドが簡潔でも中身が薄ければ減点
   - ユーザーの要求事項の未カバー → 要求されたトピックがすべて含まれているか確認
   - 視覚要素が少ない → KPI ボックス、比較表、図のプレースホルダを追加
   - スライド数が指定と大幅にずれている → 指定枚数 ±2 枚以内に調整
4. **deck.md を修正**: 改善点に基づいてスライドを編集する。
5. **再 Lint → 再 Build**: Step 5 → Step 6 を再実行する。
6. **再採点**: 90 点以上であれば完了。未達なら 3 に戻る。

```
┌─────────┐    ┌──────┐    ┌───────┐    ┌──────────┐
│ Build   │───▶│ 確認 │───▶│ 採点  │───▶│ 90点以上?│
└─────────┘    └──────┘    └───────┘    └────┬─────┘
                                             │
                                    No ◀─────┘─────▶ Yes → 完了
                                     │
                              ┌──────▼──────┐
                              │ 修正 → Lint │
                              │   → Build   │
                              └─────────────┘
```

このループにより、スキルが自律的に品質を高める。ユーザーの介入は最終承認のみ。

---

## Consulting Frameworks

### アクションタイトル

全スライドの見出しに適用する。

| NG (トピックラベル) | OK (アクションタイトル) |
|---------------------|------------------------|
| 市場分析 | 国内 SaaS 市場は年率 15% で拡大している |
| コスト比較 | ツール A は B より初期費用が 40% 低い |
| 課題 | 現行システムの保守コストが利益を圧迫している |
| 提案 | 段階的移行により年間 2000 万円の削減が可能 |
| スケジュール | 3 フェーズ 16 週間で本番稼働を目指す |

### SCQA (Situation → Complication → Question → Answer)

提案資料・問題解決型に使う。テンプレート: `proposal.md`。
聴衆は論理的なストーリーに沿って理解する: 現状 → 課題 → 問い → 提案 → 根拠 → 次アクション。

### Pyramid Principle (結論 → 根拠)

役員報告・意思決定支援に使う。テンプレート: `executive-summary.md`。
結論を最初に示し、3 つの根拠で支える。

### MECE (Mutually Exclusive, Collectively Exhaustive)

比較・評価に使う。テンプレート: `comparison.md`。
評価軸を定義し、各選択肢を漏れなくダブりなく分析する。

フレームワーク詳細・具体例 → `references/consulting-frameworks.md`

---

## Layout Patterns

`<!-- _class: classname -->` でスライドごとに適用する。

| Class | 用途 | いつ使うか |
|-------|------|-----------|
| `center` | タイトル、セクション区切り | 最初と最後のスライド、章の区切り |
| `split` | 50/50 左右分割 | テキスト + データ、現状 + 目標 |
| `split-right` | 40/60 分割 | 左にラベル、右に詳細 |
| `grid-2` | 2 カラムカード | A vs B 比較、メリット vs デメリット |
| `grid-3` | 3 カラム | 3 つのフェーズ、3 択比較 |
| `vs` | VS 比較 | 二者択一の対比を強調 |
| `quote` | キーメッセージ | 問いかけ、結論の強調 |
| `kpi` | KPI 指標ボックス | 2-4 個の定量メトリクス |

**レイアウト多様性**: 同じクラスを 3 回以上連続で使わない (lint で検出)。

レイアウトの Markdown 記法例 → `references/layouts.md`

---

## Color System

60-30-10 ルール: 60% ベース色、30% セカンダリ、10% アクセント。

| テーマ | ベース | アクセント | 用途 |
|--------|--------|-----------|------|
| `consulting-light` | 白 | 青 (#0984e3) | 提案、業務報告、汎用 |
| `consulting-dark` | 紺 (#1a1a2e) | 赤 (#e94560) | 戦略、経営層、M&A |
| `minimal` | 白灰 | ティール (#00b894) | 技術、データ分析 |

アクセント色カスタマイズ → フロントマターの `style:` で `--color-accent` を上書き。
詳細 → `references/color-system.md`

---

## Content Limits

| 要素 | 上限 |
|------|------|
| アクションタイトル | 40 文字 (JA) / 50 文字 (EN) |
| 箇条書き数 | 7 個 / スライド (split 内は各カラム 7 個) |
| 箇条書き 1 行 | 80 文字 (visual width) |
| 本文行数 | 14 行 / スライド |
| 総コンテンツ量 | 500 文字 / スライド |
| 同一レイアウト連続 | 2 回まで |

すべて `lint_deck.py` で自動検査される。

**重要: 簡潔さと情報量のバランス**
上限を守りつつも、聴衆が意思決定できるだけの具体的な数値・根拠・比較データをスライドに含めること。
「スライドが簡潔でも中身が薄い」は品質が低い。上限に余裕があるなら、具体的なデータや補足を追加する。

---

## Never Rules

- テキストだけのスライドを作らない — 必ずレイアウトクラスか視覚要素を入れる
- トピックラベル見出しを使わない — アクションタイトルにする
- 7 個を超える箇条書きを 1 スライドに入れない
- 同じレイアウトを 3 回以上連続で使わない
- 情報を削りすぎてスカスカのスライドにしない — 数値・根拠・比較を十分に含める
- Lint を通さずにビルドしない
- 1 枚に複数の論点を詰め込まない — 2 枚に分ける
- 過度に細かい表は使わない — 4 列 × 6 行が目安上限
- フロントマターなしのデッキを作らない

---

## Concrete Example

完成したスライド 1 枚の例 (proposal テンプレートの Slide 7 相当):

```markdown
<!-- _class: grid-2 -->

# ツール A は導入実績と保守性で他を上回る

<div>

### ツール A
- 国内導入 500 社以上
- 日本語ドキュメント完備
- 24/7 サポート対応
- SLA 99.9%

</div>
<div>

### ツール B
- 国内導入 80 社
- 英語ドキュメントのみ
- 営業時間内サポート
- SLA 99.5%

</div>
```

---

## Commands

すべてプロジェクトルートから `PYTHONPATH=skills/ppt-creator` を付けて実行する。
出力先には `output/` ディレクトリを絶対パスで指定する。

```bash
# 新規デッキ作成
PYTHONPATH=skills/ppt-creator uv run python -m scripts.new_deck <name> \
  --template <template> --theme <theme> \
  --output-dir /path/to/project/output

# Lint (ビルド前に必ず実行)
PYTHONPATH=skills/ppt-creator uv run python -m scripts.lint_deck /path/to/project/output/<name>/deck.md

# Build (HTML / PDF / PPTX / PNG)
PYTHONPATH=skills/ppt-creator uv run python -m scripts.build /path/to/project/output/<name>/deck.md --format pptx

# 環境チェック
PYTHONPATH=skills/ppt-creator uv run python -m scripts.doctor
```

---

## Directory Layout

スキル (読み取り専用):
```
skills/ppt-creator/
├── SKILL.md
├── references/     # 詳細リファレンス (必要時に参照)
├── themes/         # CSS テーマ (3 種)
├── templates/      # デッキテンプレート (5 種)
└── scripts/        # Python ツール
```

出力 (プロジェクト内に生成):
```
<project>/output/
└── <deck-name>/
    ├── deck.md     # スライド Markdown
    ├── *.css       # テーマ CSS
    ├── assets/     # 画像・データ
    └── dist/       # ビルド成果物 (HTML / PDF / PPTX)
```

---

## References

| ファイル | 内容 | いつ読むか |
|---------|------|-----------|
| `references/consulting-frameworks.md` | SCQA / Pyramid / MECE の詳細と具体例 | アウトライン作成時 |
| `references/layouts.md` | 8 つのレイアウトパターンの Markdown 記法 | スライド執筆時 |
| `references/color-system.md` | テーマのカラーパレットとカスタマイズ方法 | テーマ選択・変更時 |
| `references/quality-checklist.md` | 100 点満点の品質スコアリングと Before/After 例 | Lint 後の品質確認時 |
| `references/marp-advanced.md` | ディレクティブ、画像記法、スコープ付き CSS | 高度なレイアウト調整時 |

---

## Decision Rules

- 迷ったらスライドを分けて情報を整理する（ただし削りすぎない）
- 迷ったら `consulting-light`
- 迷ったら SCQA
- 装飾よりも明快さを優先する
- ユーザーが指定した枚数は尊重する。10枚と言われたら8-12枚の範囲で作る
