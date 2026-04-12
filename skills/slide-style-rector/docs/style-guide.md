# レクタースライドスタイルガイド

## デザイン哲学

- **美麗でシンプル**: 情報過多を避け、視覚的にクリーンなスライドを作る
- **色数制限**: グレースケール基調に限定的なアクセントカラーのみ使用
- **可読性重視**: フォントサイズと余白を適切に確保する
- **一貫性**: パターンの繰り返しで理解しやすいデッキを構成する

---

## カラーパレット

### アクセントカラー

| カラー名 | HEX | 用途 |
|---------|-----|------|
| Navy | `#1B4565` | タイトル、重要ラベル、見出し |
| Teal | `#3E9BA4` | アクセント、ボーダー、強調要素 |
| Navy Light | `#2A5F8F` | 背景画像、補助色 |
| Teal Light | `#5BB8C0` | 補助アクセント |

### プライマリグラデーション

```css
background: linear-gradient(to right, #1B4565, #3E9BA4);
```

タイトルスライド、セクション扉、クロージングの背景に使用。

### グレースケール

| トークン | HEX | 用途 |
|---------|-----|------|
| `gray-50` | `#F9FAFB` | パネル背景（淡い） |
| `gray-100` | `#F3F4F6` | パネル背景（やや濃い）、カード画像エリア |
| `gray-200` | `#E5E7EB` | ボーダー、区切り線 |
| `gray-300` | `#D1D5DB` | 矢印、薄いアクセント |
| `gray-400` | `#9CA3AF` | プレースホルダテキスト、ミュートテキスト |
| `gray-500` | `#6B7280` | サブテキスト、ラベル |
| `gray-600` | `#4B5563` | セカンダリテキスト |
| `gray-700` | `#374151` | 見出しテキスト |
| `gray-800` | `#1F2937` | メインテキスト |
| `gray-900` | `#111827` | 最も濃いテキスト |

### 色使いのルール

- **1スライドあたりアクセントカラーは1-2色まで**
- 強調は `gray-600` / `gray-700` のトーン差で表現し、派手な色は避ける
- `red-600` / `green-600` などの色付け強調は使わない

---

## タイポグラフィ

### フォントサイズ階層（1920×1080）

| CSS変数 | サイズ | 用途 |
|---------|-------|------|
| `--font-size-4xl` | 56px | タイトルスライドの見出し |
| `--font-size-3xl` | 48px | h1 見出し |
| `--font-size-2xl` | 40px | h2 見出し |
| `--font-size-xl` | 34px | h3 見出し、パネルタイトル |
| `--font-size-lg` | 30px | 本文、p タグ |
| `--font-size-base` | 26px | リスト項目、補助テキスト |
| `--font-size-sm` | 22px | 小さなテキスト |
| `--font-size-xs` | 18px | 注釈、出典 |

### Tailwind 風 em サイズクラス

| クラス | 倍率 | 用途 |
|-------|------|------|
| `text-em-3xl` | 2.4em | 数値強調、インパクトキーワード |
| `text-em-2xl` | 1.8em | パネル見出し、セクションタイトル |
| `text-em-xl` | 1.4em | サブ見出し |
| `text-em-lg` | 1.2em | 本文、リスト項目 |

### 文体ルール

- **コロン（：）を使用しない**
  - NG: `原則❶：自律性の最大化`
  - OK: `原則❶ 自律性の最大化`
- **感嘆符（!）や疑問符（?）を避ける**
  - NG: `AIで開発が10倍速に!`
  - OK: `AIで開発が10倍速に`
- **装飾的な絵文字を避ける**
  - NG: `🧩 問題領域の複雑さ`
  - OK: `問題領域の複雑さ`

---

## セクションクラス（`_class` ディレクティブ）

スライド全体のレイアウトを制御する。`<!-- _class: xxx -->` で指定。

| クラス名 | 用途 | 背景 |
|---------|------|------|
| `title` | 表紙スライド（`_paginate: false` と併用） | Navy→Teal グラデーション、白文字 |
| `section` | セクション扉（`_paginate: false` と併用） | Navy→Teal グラデーション、白文字 |
| `section-end` | セクションまとめ | gray-50、Navy 文字 |
| `toc` | 目次スライド | 白、番号付きリスト |
| `closing` | クロージングスライド（`_paginate: false` と併用） | Navy→Teal グラデーション、白文字 |
| `bg-full` | 全画面背景画像 | カスタム背景 |
| `quote` | 引用スライド | 白、大きな引用符 |
| `center-message` | 中央配置メッセージ | 白、64px 見出し |
| `qanda` | Q&A スライド | gray-50、88px 見出し |
| `question` | 問いかけスライド | Navy→Teal グラデーション、白枠 |
| `compact` | 情報密度が高いスライド | フォント縮小 |

---

## ユーティリティクラス

### レイアウト

| クラス | 効果 |
|-------|------|
| `grid` | CSS Grid |
| `grid-cols-2` 〜 `grid-cols-5` | 列数指定 |
| `gap-2` 〜 `gap-10` | Gap（8px 〜 40px） |
| `flex` | Flexbox |
| `flex-col` / `flex-row` | 方向 |
| `items-center` / `items-start` | 交差軸配置 |
| `justify-center` / `justify-between` | 主軸配置 |

### スペーシング

| クラス | 効果 |
|-------|------|
| `mt-2` 〜 `mt-10` | margin-top（8px 〜 40px） |
| `mb-2` 〜 `mb-8` | margin-bottom |
| `p-2` 〜 `p-10` | padding |
| `px-4` 〜 `px-8` | 左右 padding |
| `py-2` 〜 `py-8` | 上下 padding |

### タイポグラフィ

| クラス | 効果 |
|-------|------|
| `text-xs` 〜 `text-4xl` | フォントサイズ |
| `font-bold` / `font-semibold` | 太さ |
| `text-center` / `text-left` / `text-right` | テキスト配置 |
| `text-navy` / `text-teal` / `text-white` | テキスト色 |
| `text-gray-400` 〜 `text-gray-900` | グレー文字 |

### 背景・ボーダー

| クラス | 効果 |
|-------|------|
| `bg-white` / `bg-gray-50` / `bg-gray-100` | 背景色 |
| `bg-navy` / `bg-teal` / `bg-gradient` | アクセント背景 |
| `rounded-lg` / `rounded-xl` / `rounded-2xl` | 角丸 |
| `shadow` / `shadow-md` / `shadow-lg` | ドロップシャドウ |
| `border-l-4` / `border-t-4` | ボーダー（左/上） |
| `border-navy` / `border-teal` / `border-gray-200` | ボーダー色 |

---

## コンポーネントクラス

### パネル系

| クラス | デザイン |
|-------|---------|
| `panel` | gray-50 背景、角丸、パディング |
| `panel-accent` | gray-50 + 左 Teal ボーダー |
| `panel-glass` | 半透明白背景、細い境界線、シャドウ（ガラスモーフィズム） |
| `panel-gradient` | Navy→Teal グラデーション背景、白文字 |

### 統計系

| クラス | デザイン |
|-------|---------|
| `stat-box` | テキスト中央、gray-50 背景、角丸 |
| `stat-box.accent` | グラデーション背景、白文字 |
| `stat-value` | 56px、font-weight 800 |
| `stat-label` | 26px、gray-500 |

### ステップ・プロセス系

| クラス | デザイン |
|-------|---------|
| `v-step` + `data-step="N"` | 縦型ステップ（番号付き丸） |
| `step` + `step-number` + `step-content` | 横型ステップ |
| `step-arrow` | ステップ間の矢印（→） |

### タイムライン系

| クラス | デザイン |
|-------|---------|
| `timeline-item` | Flex レイアウト |
| `timeline-date` | 右寄せ、Teal、太字 |
| `timeline-dot` | 16px 丸、Teal + 縦線コネクタ |
| `timeline-content` | flex: 1 |

### その他

| クラス | デザイン |
|-------|---------|
| `icon-item` + `icon-circle` | アイコン付きリスト |
| `maturity-bar` + `maturity-level` | 5段階成熟度バー |
| `card` + `card-image` | カード型レイアウト |
| `source` | 出典表示（右下固定、18px、gray-400） |
| `badge` | インラインバッジ（角丸、小さな文字） |
| `vs-divider` | VS 区切り |
| `divider` | 水平線 |
| `attribution` | 引用の帰属表示 |

---

## Marp フロントマター

```yaml
---
marp: true
theme: rector
paginate: true
---
```

### ディレクティブ

| ディレクティブ | 用途 |
|--------------|------|
| `<!-- _class: xxx -->` | セクションクラス指定 |
| `<!-- _paginate: false -->` | ページ番号非表示 |
| `<!-- _backgroundColor: #hex -->` | 背景色上書き |
| `<!-- _backgroundImage: "..." -->` | 背景画像/グラデーション |
| `<!-- _color: white -->` | テキスト色上書き |
| `![bg right:40%](path)` | Marp 背景画像（右40%） |

---

## ビルドコマンド

```bash
# HTML 出力（プレビュー用）
npx @marp-team/marp-cli deck.md --theme-set rector.css --html --allow-local-files

# HTML ファイル指定出力
npx @marp-team/marp-cli deck.md --theme-set rector.css --html --output deck.html --allow-local-files

# PPTX 出力
npx @marp-team/marp-cli deck.md --theme-set rector.css --pptx --allow-local-files

# PDF 出力
npx @marp-team/marp-cli deck.md --theme-set rector.css --pdf --allow-local-files
```

`--allow-local-files` はローカル画像の読み込みに必須。
