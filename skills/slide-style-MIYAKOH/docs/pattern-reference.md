# MIYAKOH パターンリファレンス

39種のレイアウトパターンの役割と制約。実装コードは `slides/example.md` を参照。

## パターン選択ガイド

| 伝えたいこと | 推奨パターン |
|------------|------------|
| 章の始まり | 2 (section) |
| 章のまとめ | 3 (section-end) |
| 2つの比較 | 6 (2col比較) / 38 (対比+結論) |
| 3つの並列要素 | 8 (3col) / 9 (3col accent) |
| 4つのフェーズ | 10 (4col) |
| 段階・成熟度 | 11 (5col maturity) |
| ステップ・プロセス | 14 (v-step) / 15 (横型step) |
| 時系列 | 16 (timeline) |
| 機能・特徴一覧 | 17 (icon list) / 13 (2x3 grid) |
| 画像+テキスト | 7a/7b (2col text+img) |
| 製品紹介 | 22 (card) / 18 (panel+image) |
| KPI・数値 | 27 (統計) / 34 (統計比率) |
| 重要メッセージ | 28 (center-message) |
| 引用 | 25 (quote) |
| 問いかけ | 31 (question) |
| まとめ・結論 | 36 (ガラス風) / 38 (対比+結論) |
| データ表 | 39 (table+highlight) |
| QRコード | 30 (QR) |

---

## A. タイトル・セクション系 (1-5)

**Pattern 1: title** — 表紙。タイトル1-2行。`_paginate: false` 併用。

**Pattern 2: section** — 章扉。話題転換を示す。3-5枚に1回。`_paginate: false` 併用。

**Pattern 3: section-end** — セクションまとめ。箇条書き3-5項目で前スライドの要約。新情報は入れない。

**Pattern 4: toc** — 目次。タイトル直後に使用。項目名15字以内、7項目以内。

**Pattern 5: closing** — 最終スライド。テキスト3行以内。`_paginate: false` 併用。

---

## B. カラムレイアウト系 (6-13)

**Pattern 6: 2col比較** — 2概念を対比。各3-5項目。推奨側にTealボーダー。

**Pattern 7a: 2col（テキスト+画像）** — 左テキスト、右画像。50:50基本。

**Pattern 7b: 2col（画像+テキスト）** — 7aの左右反転。ビジュアル優先時。

**Pattern 8: 3col（画像+テキスト）** — 3要素並列。各3-4行。要素は同格。

**Pattern 9: 3col accent** — 3カテゴリをボーダーカラーで区分。Teal=推奨、Navy=重要、Gray=補助。

**Pattern 10: 4col** — 4フェーズ並列。各2-3行。

**Pattern 11: 5col maturity** — 段階的進化をグラデーション表現。各レベル1-2行。

**Pattern 12: 2x2 grid** — 4要素コンパクト紹介。各セル2-3行。左に小画像100px。

**Pattern 13: 2x3 grid** — 6要素整列。上段Teal/下段Navyでフェーズ区分。各2-3行。

---

## C. 縦並びリスト系 (14-17)

**Pattern 14: v-step** — 縦3ステップ。各2-3行。4以上はスライド分割。

**Pattern 15: 横型step** — 左→右のフロー。3ステップが上限。各1-2行。

**Pattern 16: timeline** — 時系列マイルストーン。3-4項目。日付は「2024 Q1」形式。

**Pattern 17: icon list** — Unicodeアイコン付きリスト。3-4項目。太字タイトル+説明文。

---

## D. パネルデザイン系 (18-22)

**Pattern 18: panel+image** — 画像ヘッダー+テキスト。2枚横並び。3枚ならPattern 22。

**Pattern 19: panel accent** — 左ボーダーで重要度表現。Teal=最重要、Navy=推奨、Gray=補足。各2-4行。

**Pattern 20: glass panel** — ガラスモーフィズム。`_backgroundColor` 設定で効果が出る。

**Pattern 21: gradient panel** — Navy→Tealグラデーション。1スライド1つまで。結論やCTAに。

**Pattern 22: card** — 3カード横並び。画像+テキスト。各2-3行。

---

## E. 背景・画像系 (23-26)

**Pattern 23: bg-full** — 全画面背景。テキスト2行以内。

**Pattern 24: bg right** — Marp `bg right:40%` で右に画像、左にテキスト。

**Pattern 25: quote** — 引用文1-3文。引用元必須。

**Pattern 26: split images** — 複数画像横並び。2-3分割。

---

## F. 強調・特殊系 (27-29)

**Pattern 27: 統計** — 数値3つを大きく表示。`.accent` は1つだけ強調したい場合のみ。

**Pattern 28: center-message** — 1メッセージを64pxで中央表示。1-2行。連続使用不可。

**Pattern 29: Q&A** — 質疑応答。`_paginate: false` 併用。

---

## G. 応用パターン系 (30-39)

**Pattern 30: QR** — QRコード+テキスト。左テキスト、右QRエリア220px。

**Pattern 31: question** — 問いかけ。質問は1つ。`_paginate: false` 併用。

**Pattern 32: footnote** — 出典付きデータ提示。`.source` で出典記載。パネル内3-4項目。

**Pattern 33: inline image** — テキスト+画像を同じ視線で。アーキテクチャ図解説に。

**Pattern 34: 統計比率** — 4つの比率並列。色で区分。

**Pattern 35: text+stats** — 左テキスト+右統計グリッド。`.accent` は1つまで。

**Pattern 36: まとめ（ガラス風）** — 番号付き3ポイント。プレゼン結論に。各1-2行。

**Pattern 37: list+supplement** — 手順リスト+補足パネル。左2:右1。

**Pattern 38: 対比+結論** — 2パネル比較+下部に結論帯。推奨側にTealボーダー。結論1-2行。

**Pattern 39: table+highlight** — 比較表。推奨列を太字。列4つ以内、行6-8以内。評価は◎/◯/△。
