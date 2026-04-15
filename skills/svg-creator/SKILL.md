---
name: svg-creator
description: SVG ダイアグラム・アイコン・図解を直接生成するスキル。MIYAKOHスタイル（Navy #1B4565 + Teal #3E9BA4）に準拠したベクターグラフィックスを作成する。SVG、図解、ダイアグラム、アイコン、フローチャート、アーキテクチャ図、概念図、プロセス図などのキーワードが含まれる場合は積極的に使用すること。
---

# svg-creator

Claude が直接 SVG コードを生成し、スライドや資料に使えるベクターグラフィックスを作成する。外部 API 不要。

---

## デザインルール

### カラーパレット（MIYAKOH準拠）

SVG 内で使用する色はMIYAKOHパレットに限定する:

| 色 | HEX | 用途 |
|----|-----|------|
| Navy | `#1B4565` | 主要図形、タイトル、重要ラベル |
| Teal | `#3E9BA4` | アクセント、ハイライト、接続線 |
| Navy Light | `#2A5F8F` | 補助的な図形、グラデーション |
| Teal Light | `#5BB8C0` | 補助アクセント |
| gray-50 | `#F9FAFB` | パネル背景、ノード内部 |
| gray-100 | `#F3F4F6` | 薄い背景 |
| gray-200 | `#E5E7EB` | ボーダー、区切り線 |
| gray-500 | `#6B7280` | サブテキスト、ラベル |
| gray-800 | `#1F2937` | メインテキスト |
| 白 | `#FFFFFF` | 背景、パネル内部 |

### スタイル原則

- **フラットデザイン**: 影・テクスチャ・3D 効果は使わない
- **ストローク幅**: 1.5-2px で統一
- **角丸**: `rx="8"` を標準とする
- **テキスト**: `font-family="system-ui, sans-serif"`
- **アクセントカラーは1つの SVG に1-2色まで**

---

## SVG 種別とサイズガイド

| 種別 | 用途 | viewBox | 例 |
|------|------|---------|-----|
| アイコン | icon-circle, リスト装飾 | `0 0 48 48` 〜 `0 0 96 96` | チェックマーク、盾、グラフ、歯車 |
| 小イラスト | カード画像、カラムヘッダー | `0 0 400 160` 〜 `0 0 400 300` | サービス概念図、機能イメージ |
| ダイアグラム | インライン図解 | `0 0 800 400` 〜 `0 0 800 600` | フロー図、アーキテクチャ図、比較図 |
| 背景装飾 | bg-right, 分割背景 | `0 0 400 600` 〜 `0 0 768 1080` | 抽象パターン、幾何学模様 |

---

## 出力ルール

- **保存先**: デッキと同じディレクトリの `svg/` フォルダ
- **ファイル名**: 英語3-4語、ケバブケース（例: `data-flow-diagram.svg`, `security-shield-icon.svg`）
- **viewBox 必須**、width/height 属性は指定しない（レスポンシブ対応）
- **`<title>`** と **`<desc>`** タグで内容を説明する
- **xmlns 必須**: `xmlns="http://www.w3.org/2000/svg"`

---

## テンプレート

### アイコン（48×48）

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
  <title>セキュリティ</title>
  <desc>盾のアイコン</desc>
  <circle cx="24" cy="24" r="22" fill="#F9FAFB" stroke="#3E9BA4" stroke-width="2"/>
  <path d="M24 10 L34 16 V26 C34 32 24 38 24 38 S14 32 14 26 V16 Z" 
        fill="none" stroke="#1B4565" stroke-width="2" stroke-linejoin="round"/>
</svg>
```

### フローダイアグラム（800×300）

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 300">
  <title>データ処理フロー</title>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#3E9BA4"/>
    </marker>
  </defs>
  <!-- ノード1 -->
  <rect x="20" y="110" width="160" height="80" rx="8" fill="#F9FAFB" stroke="#1B4565" stroke-width="2"/>
  <text x="100" y="155" text-anchor="middle" fill="#1F2937" font-family="system-ui, sans-serif" font-size="16">入力データ</text>
  <!-- 矢印 -->
  <line x1="180" y1="150" x2="280" y2="150" stroke="#3E9BA4" stroke-width="2" marker-end="url(#arrow)"/>
  <!-- ノード2 -->
  <rect x="280" y="110" width="160" height="80" rx="8" fill="#F9FAFB" stroke="#1B4565" stroke-width="2"/>
  <text x="360" y="155" text-anchor="middle" fill="#1F2937" font-family="system-ui, sans-serif" font-size="16">処理エンジン</text>
  <!-- 矢印 -->
  <line x1="440" y1="150" x2="540" y2="150" stroke="#3E9BA4" stroke-width="2" marker-end="url(#arrow)"/>
  <!-- ノード3 -->
  <rect x="540" y="110" width="160" height="80" rx="8" fill="#F9FAFB" stroke="#3E9BA4" stroke-width="2"/>
  <text x="620" y="155" text-anchor="middle" fill="#1F2937" font-family="system-ui, sans-serif" font-size="16">出力結果</text>
</svg>
```

### 抽象パターン（背景装飾用）

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600">
  <title>抽象装飾パターン</title>
  <rect width="400" height="600" fill="#FFFFFF"/>
  <circle cx="200" cy="150" r="80" fill="none" stroke="#E5E7EB" stroke-width="1.5"/>
  <circle cx="200" cy="150" r="50" fill="none" stroke="#3E9BA4" stroke-width="1.5" opacity="0.6"/>
  <circle cx="200" cy="350" r="100" fill="none" stroke="#E5E7EB" stroke-width="1.5"/>
  <circle cx="200" cy="350" r="60" fill="none" stroke="#1B4565" stroke-width="1.5" opacity="0.4"/>
  <line x1="200" y1="230" x2="200" y2="250" stroke="#E5E7EB" stroke-width="1.5"/>
</svg>
```

---

## Marp での参照方法

```markdown
<!-- icon-circle 内のアイコン -->
<div class="icon-circle"><img src="svg/security-icon.svg" width="32" height="32"></div>

<!-- インライン図解 -->
<div class="mt-4"><img src="svg/data-flow-diagram.svg" style="width:100%"></div>

<!-- カード画像 -->
<div class="card-image"><img src="svg/service-concept.svg"></div>

<!-- Marp 背景画像 -->
![bg right:40%](svg/abstract-pattern.svg)
```

---

## 生成のコツ

- **シンプルに保つ**: 1つの SVG に要素を詰め込みすぎない。情報量が多い場合は複数の SVG に分割する
- **テキストは最小限に**: SVG 内のテキストは短いラベルに留める。長文はスライド側で記載する
- **整列を意識する**: ノードの位置は等間隔に配置し、矢印は水平・垂直に揃える
- **defs でマーカーを定義**: 矢印は `<marker>` で定義し、`marker-end` で参照する
- **日本語テキスト**: `font-family="system-ui, sans-serif"` で OS のデフォルトフォントを使用
