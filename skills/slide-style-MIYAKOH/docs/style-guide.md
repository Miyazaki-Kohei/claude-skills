# MIYAKOH スタイルガイド

## カラーパレット

### アクセントカラー

| カラー名 | HEX | 用途 |
|---------|-----|------|
| Navy | `#1B4565` | タイトル、見出し、重要ラベル |
| Teal | `#3E9BA4` | アクセント、ボーダー、強調要素 |
| Navy Light | `#2A5F8F` | 背景、補助色 |
| Teal Light | `#5BB8C0` | 補助アクセント |

プライマリグラデーション: `linear-gradient(to right, #1B4565, #3E9BA4)`
用途: タイトル、セクション扉、クロージングの背景。

### グレースケール

| トークン | HEX | 用途 |
|---------|-----|------|
| `gray-50` | `#F9FAFB` | パネル背景（淡い） |
| `gray-100` | `#F3F4F6` | パネル背景（やや濃い）、画像エリア |
| `gray-200` | `#E5E7EB` | ボーダー、区切り線 |
| `gray-300` | `#D1D5DB` | 矢印、薄いアクセント |
| `gray-400` | `#9CA3AF` | ミュートテキスト |
| `gray-500` | `#6B7280` | サブテキスト、ラベル |
| `gray-600` | `#4B5563` | セカンダリテキスト |
| `gray-700` | `#374151` | 見出しテキスト |
| `gray-800` | `#1F2937` | メインテキスト |

### 色使いルール

- 1スライドあたりアクセントカラーは1-2色まで
- 強調は `gray-600` / `gray-700` のトーン差で表現
- `red-600` / `green-600` などの色付け強調は使わない

---

## タイポグラフィ

### フォントサイズ（1920×1080）

| CSS変数 | サイズ | 用途 |
|---------|-------|------|
| `--font-size-4xl` | 56px | タイトル見出し |
| `--font-size-3xl` | 48px | h1 |
| `--font-size-2xl` | 40px | h2 |
| `--font-size-xl` | 34px | h3、パネルタイトル |
| `--font-size-lg` | 30px | 本文 |
| `--font-size-base` | 26px | リスト項目 |
| `--font-size-sm` | 22px | 小テキスト |
| `--font-size-xs` | 18px | 注釈、出典 |

### em サイズクラス

| クラス | 倍率 | 用途 |
|-------|------|------|
| `text-em-3xl` | 2.4em | 数値強調 |
| `text-em-2xl` | 1.8em | パネル見出し |
| `text-em-xl` | 1.4em | サブ見出し |
| `text-em-lg` | 1.2em | 本文 |

### 文体ルール

- コロン（：）不可 → `原則1 自律性の最大化`
- 感嘆符・疑問符不可 → `AIで開発が10倍速に`
- 装飾的な絵文字不可

---

## セクションクラス（`_class` ディレクティブ）

| クラス | 用途 | 背景 |
|-------|------|------|
| `title` | 表紙（`_paginate: false` 併用） | グラデーション、白文字 |
| `section` | セクション扉（`_paginate: false` 併用） | グラデーション、白文字 |
| `section-end` | セクションまとめ | gray-50、Navy文字 |
| `toc` | 目次 | 白 |
| `closing` | クロージング（`_paginate: false` 併用） | グラデーション、白文字 |
| `bg-full` | 全画面背景画像 | カスタム |
| `quote` | 引用 | 白、大引用符 |
| `center-message` | 中央メッセージ（64px） | 白 |
| `qanda` | Q&A（88px） | gray-50 |
| `question` | 問いかけ（`_paginate: false` 併用） | グラデーション、白枠 |
| `compact` | 高密度スライド | フォント縮小 |

---

## ユーティリティクラス

### レイアウト

| クラス | 効果 |
|-------|------|
| `grid` | CSS Grid |
| `grid-cols-2` 〜 `grid-cols-5` | 列数指定 |
| `gap-2` 〜 `gap-10` | Gap（8px〜40px） |
| `flex` / `flex-col` / `flex-row` | Flexbox |
| `items-center` / `items-start` | 交差軸配置 |
| `justify-center` / `justify-between` | 主軸配置 |

### スペーシング

| クラス | 効果 |
|-------|------|
| `mt-2` 〜 `mt-10` | margin-top |
| `mb-2` 〜 `mb-8` | margin-bottom |
| `p-2` 〜 `p-10` | padding |
| `px-4` 〜 `px-8` | 左右padding |
| `py-2` 〜 `py-8` | 上下padding |

### タイポグラフィ

| クラス | 効果 |
|-------|------|
| `text-xs` 〜 `text-4xl` | フォントサイズ |
| `font-bold` / `font-semibold` | 太さ |
| `text-center` / `text-left` / `text-right` | 配置 |
| `text-navy` / `text-teal` / `text-white` | 色 |
| `text-gray-400` 〜 `text-gray-900` | グレー |

### 背景・ボーダー

| クラス | 効果 |
|-------|------|
| `bg-white` / `bg-gray-50` / `bg-gray-100` | 背景色 |
| `bg-navy` / `bg-teal` / `bg-gradient` | アクセント背景 |
| `rounded-lg` / `rounded-xl` / `rounded-2xl` | 角丸 |
| `shadow` / `shadow-md` / `shadow-lg` | シャドウ |
| `border-l-4` / `border-t-4` | ボーダー |
| `border-navy` / `border-teal` / `border-gray-200` | ボーダー色 |

---

## コンポーネントクラス

### パネル系

| クラス | デザイン |
|-------|---------|
| `panel` | gray-50背景、角丸、パディング |
| `panel-accent` | gray-50 + 左Tealボーダー |
| `panel-glass` | 半透明白、細い境界線、シャドウ |
| `panel-gradient` | Navy→Tealグラデーション、白文字 |

### 統計系

| クラス | デザイン |
|-------|---------|
| `stat-box` | テキスト中央、gray-50背景 |
| `stat-box.accent` | グラデーション背景、白文字 |
| `stat-value` | 56px、weight 800 |
| `stat-label` | 26px、gray-500 |

`accent` は並列数値の中で1つだけ強調する場合のみ使用。全要素同列なら `stat-box` のみ。

### ステップ・プロセス系

| クラス | デザイン |
|-------|---------|
| `v-step` + `data-step="N"` | 縦型ステップ（番号丸） |
| `step` + `step-number` + `step-content` | 横型ステップ |
| `step-arrow` | ステップ間矢印 |

### タイムライン系

| クラス | デザイン |
|-------|---------|
| `timeline-item` | Flexレイアウト |
| `timeline-date` | 右寄せ、Teal、太字 |
| `timeline-dot` | 16px丸、Teal + 縦線 |
| `timeline-content` | flex: 1 |

### その他

| クラス | デザイン |
|-------|---------|
| `icon-item` + `icon-circle` | アイコン付きリスト |
| `maturity-bar` + `maturity-level` | 5段階成熟度バー |
| `card` + `card-image` | カード型レイアウト |
| `source` | 出典（右下固定、18px、gray-400） |
| `badge` | インラインバッジ |
| `vs-divider` | VS区切り |
| `divider` | 水平線 |
| `attribution` | 引用帰属表示 |

---

## Marp ディレクティブ

| ディレクティブ | 用途 |
|--------------|------|
| `<!-- _class: xxx -->` | セクションクラス指定 |
| `<!-- _paginate: false -->` | ページ番号非表示 |
| `<!-- _backgroundColor: #hex -->` | 背景色上書き |
| `<!-- _backgroundImage: "..." -->` | 背景画像/グラデーション |
| `<!-- _color: white -->` | テキスト色上書き |
| `![bg right:40%](path)` | Marp背景画像（右40%） |

---

## ビジュアル生成ガイドライン

### image-creator 連携

- スタイル: フラットデザイン (`-t flat`) 基本
- カラー: Navy + Teal をプロンプトに明示
- 背景: 白またはライトグレー基調
- 保存先: `images/`

推奨アスペクト比:

| 用途 | 比率 | 対応パターン |
|------|------|-------------|
| スライド全面背景 | 16:9 | Pattern 23 |
| 右配置背景 | 3:4 | Pattern 24 |
| カード画像 | 4:3 | Pattern 22 |
| アイコン | 1:1 | Pattern 17 |
| 2カラム画像 | 4:3 | Pattern 7a/7b |

### svg-creator 連携

- 色は MIYAKOH パレットのみ（Navy, Teal, グレースケール, 白）
- ストローク幅 1.5-2px、角丸 `rx="8"`
- viewBox 必須、width/height 指定なし
- 保存先: `svg/`
