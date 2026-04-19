---
marp: true
theme: MIYAKOH
paginate: true
header: ''
---

<!--
パターン選択ガイド:
  章の始まり → 2 (section)
  章のまとめ → 3 (section-end)
  自己紹介 → 4 (self-intro)
  2つの比較 → 6 (2col比較) / 38 (対比+結論)
  3つの並列要素 → 8 (3col) / 9 (3col accent)
  4つの並列要素 → 10 (4col)
  段階・成熟度 → 11 (5col maturity)
  ステップ・プロセス → 14 (v-step) / 15 (横型step)
  時系列 → 16 (timeline)
  機能・特徴一覧 → 17 (icon list) / 13 (2x3 grid)
  画像+テキスト → 7a/7b (2col text+img)
  製品紹介 → 22 (card) / 18 (panel+image)
  KPI・数値 → 27 (統計) / 34 (統計比率)
  重要メッセージ → 28 (center-message)
  引用 → 25 (quote)
  問いかけ → 31 (question)
  まとめ・結論 → 36 (ガラス風) / 38 (対比+結論)
  データ表 → 39 (table+highlight)
  QRコード → 30 (QR)
-->

<!-- _class: title -->
<!-- _paginate: false -->

# レイアウトパターン スタイルガイド
## 39種類のMarpレイアウトテンプレート

MIYAKOH (@miyakoh)

---

<!-- toc — 目次。タイトル直後に使用。項目名15字以内、7項目以内。 -->
<!-- _class: toc -->
<!-- _header: '' -->

# 目次

1. タイトルスライド
2. セクション開始スライド
3. セクション終了・まとめ
4. 目次スライド
5. クロージングスライド
6. 2カラム比較（Before/After）
7. 2カラム（テキスト＋画像）

---

<!-- A. タイトル・セクション系 ============================= -->

<!-- _class: section -->
<!-- _paginate: false -->

# A. タイトル・セクション系
5つの基本パターン

---

<!-- Pattern 1: title — 表紙。タイトル1-2行。_paginate: false 併用。 -->
<!-- _class: title -->
<!-- _paginate: false -->

# プレゼンテーションのタイトル
## サブタイトルが入ります

発表者名 (@handle)

---

<!-- Pattern 4: self-intro — 自己紹介。左にテキスト（氏名・役割等）、右にプロフィール画像。項目4-5行。 -->

# 自己紹介

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; flex: 1; margin-top: -112px;">
<div>
<p style="font-size: 40px; line-height: 3.4; margin: 0;">
<strong>氏名</strong>　　MIYAKOH（宮﨑　昂平）<br>
<strong>業界</strong>　　不動産デベロッパー<br>
<strong>役割</strong>　　データ分析、データマネジメント<br>
<strong>趣味</strong>　　キャンプ、筋トレ
</p>
</div>
<div class="flex justify-center">
<div class="rounded-2xl overflow-hidden" style="width: 560px; height: 560px;">
<img src="images/profile.jpg" class="img-cover">
</div>
</div>
</div>

---

<!-- Pattern 2: section — 章扉。話題転換を示す。3-5枚に1回。_paginate: false 併用。 -->
<!-- _class: section -->
<!-- _paginate: false -->

# セクションタイトル
セクションの概要テキストが入ります

---

<!-- Pattern 3: section-end — セクションまとめ。箇条書き3-5項目で前スライドの要約。新情報は入れない。 -->
<!-- _class: section-end -->

# セクションのまとめ

- まとめの要点が入ります
- 前のスライド群の要約を3-5項目で記載する
- 新しい情報は入れず振り返りに使う

---

<!-- Pattern 5: closing — 最終スライド。テキスト3行以内。_paginate: false 併用。 -->
<!-- _class: closing -->
<!-- _paginate: false -->

# Thank You
クロージングメッセージが入ります

## email@example.com

---

<!-- B. カラムレイアウト系 ============================= -->

<!-- _class: section -->
<!-- _paginate: false -->

# B. カラムレイアウト系
8つのカラムパターン

---

<!-- Pattern 6: 2col比較 — 2概念を対比。各3-5項目。強調側にTealボーダー（中立比較ならボーダーなし可）。 -->
<!-- header: 'B. カラムレイアウト系' -->

# 6. 2カラム比較（Before/After）

<div class="key-message">2つの視点を左右に並べて対比する</div>

<div class="grid grid-cols-2 gap-8 mt-6" style="min-height: 420px;">
<div class="bg-gray-50 rounded-xl shadow-lg p-10 border-l-4 border-gray-400">

<h3 class="text-xl font-bold mb-4 text-gray-800">期待</h3>

- AIエージェントで10倍以上の生産性
- 開発チームは少人数で十分
- すべてが自動化される

</div>
<div class="bg-gray-50 rounded-xl shadow-lg p-10 border-l-4 border-teal">

<h3 class="text-xl font-bold mb-4 text-gray-800">現実</h3>

- 多くの企業では2-3倍程度
- 人間の判断は依然として重要
- 本質的複雑性は残る

</div>
</div>

---

<!-- Pattern 7a: 2col（テキスト+画像） — 左テキスト、右画像。50:50基本。 -->

# 7a. 2カラム（テキスト＋画像）

<div class="key-message">テキストと図を並列に配置して直感的に伝える</div>

<div class="grid grid-cols-2 gap-8 mt-6">
<div>

### プロジェクト概要

テキストと画像を横並びに配置するレイアウト。説明文を左側に、関連する図やスクリーンショットを右側に配置する。

- テキスト側: 60%〜50%
- 画像側: 40%〜50%
- 画像は中央揃え

</div>
<div class="rounded-xl overflow-hidden" style="min-height:300px;">

<img src="images/col-project.png" class="img-cover">

</div>
</div>

---

<!-- Pattern 7b: 2col（画像+テキスト） — 7aの左右反転。ビジュアル優先時。 -->

# 7b. 2カラム（画像＋テキスト）

<div class="key-message">ビジュアルを先に見せてから説明へ誘導する</div>

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="rounded-xl overflow-hidden" style="min-height:300px;">

<img src="images/col-analysis.png" class="img-cover">

</div>
<div>

### 分析結果

画像を左側、テキストを右側に配置する逆パターン。ビジュアルを先に見せてから説明を読ませたい場合に有効。

- データの可視化結果
- スクリーンショット
- アーキテクチャ図

</div>
</div>

---

<!-- Pattern 8: 3col（画像+テキスト） — 3要素並列。各3-4行。要素は同格。 -->

# 8. 3カラム（画像＋テキスト）

<div class="key-message">3つの要素を画像付きカードで並列に紹介する</div>

<div class="grid grid-cols-3 gap-6 mt-6 text-base">
<div class="bg-gray-50 rounded-xl shadow-md p-5">
<div class="rounded-lg mb-4 overflow-hidden" style="height:140px;">
<img src="images/phase-planning.png" class="img-cover">
</div>

**フェーズ1: 計画**

要件定義とスコープの明確化を行い、プロジェクト全体の方向性を決定する

</div>
<div class="bg-gray-50 rounded-xl shadow-md p-5">
<div class="rounded-lg mb-4 overflow-hidden" style="height:140px;">
<img src="images/phase-development.png" class="img-cover">
</div>

**フェーズ2: 実装**

設計に基づいた開発を進め、イテレーティブに機能を構築する

</div>
<div class="bg-gray-50 rounded-xl shadow-md p-5">
<div class="rounded-lg mb-4 overflow-hidden" style="height:140px;">
<img src="images/phase-testing.png" class="img-cover">
</div>

**フェーズ3: 検証**

テストと品質保証を通じて、リリース可能な状態に仕上げる

</div>
</div>

---

<!-- Pattern 9: 3col accent — 3カテゴリをボーダーカラーで区分。色でカテゴリの違いを表現。 -->

# 9. 3カラム（アクセントカラー付き）

<div class="key-message">色分けボーダーで3つのカテゴリを視覚的に区別する</div>

<div class="grid grid-cols-3 gap-8 mt-6" style="min-height: 420px;">
<div class="bg-gray-50 rounded-xl p-8 border-t-4 border-teal">

<h3 class="text-teal font-bold">セキュリティ</h3>

各セクションの意味を色で強調するパターン。上部のボーダーカラーで区分を示す

- 認証・認可
- 暗号化
- 監査ログ

</div>
<div class="bg-gray-50 rounded-xl p-8 border-t-4 border-navy">

<h3 class="text-navy font-bold">パフォーマンス</h3>

ボーダーカラーをNavyに変更して、異なるカテゴリであることを視覚的に表現

- レスポンスタイム
- スループット
- リソース効率

</div>
<div class="bg-gray-50 rounded-xl p-8 border-t-4" style="border-top-color:#6B7280;">

<h3 class="text-gray-600 font-bold">運用性</h3>

グレーのボーダーで補助的なカテゴリを表現

- モニタリング
- デプロイ自動化
- ドキュメント

</div>
</div>

---

<!-- Pattern 10: 4col — 4要素並列。各2-3行。 -->

# 10. 4カラムレイアウト

<div class="key-message">4つのフェーズや要素を均等に並べて俯瞰する</div>

<div class="grid grid-cols-4 gap-6 mt-6 text-base" style="min-height: 360px;">
<div class="bg-gray-50 rounded-lg shadow-md p-6">

<h4 class="text-navy font-bold mb-2">Phase 1</h4>

**企画**

ビジネス要件の整理とフィージビリティの検討

</div>
<div class="bg-gray-50 rounded-lg shadow-md p-6">

<h4 class="text-navy font-bold mb-2">Phase 2</h4>

**設計**

アーキテクチャ設計とUI/UXデザイン

</div>
<div class="bg-gray-50 rounded-lg shadow-md p-6">

<h4 class="text-navy font-bold mb-2">Phase 3</h4>

**開発**

スプリントベースの反復開発とCI/CD整備

</div>
<div class="bg-gray-50 rounded-lg shadow-md p-6">

<h4 class="text-navy font-bold mb-2">Phase 4</h4>

**運用**

本番デプロイとモニタリング体制の構築

</div>
</div>

---

<!-- Pattern 11: 5col maturity — 段階的進化をグラデーション表現。各レベル1-2行。 -->

# 11. 5カラム（成熟度レベル）

<div class="key-message">段階的な進化をグラデーションで表現する</div>

<div class="maturity-bar mt-6" style="min-height: 420px;">
<div class="maturity-level">

<h4>Level 1</h4>

レベル名

<span class="sub">副題文
ここに入る</span>

</div>
<div class="maturity-level">

<h4>Level 2</h4>

レベル名

<span class="sub">副題文
ここに入る</span>

</div>
<div class="maturity-level">

<h4>Level 3</h4>

レベル名

<span class="sub">副題文
ここに入る</span>

</div>
<div class="maturity-level">

<h4>Level 4</h4>

レベル名

<span class="sub">副題文
ここに入る</span>

</div>
<div class="maturity-level">

<h4>Level 5</h4>

レベル名

<span class="sub">副題文
ここに入る</span>

</div>
</div>

---

<!-- Pattern 12: 2x2 grid — 4要素コンパクト紹介。各セル2-3行。左に小画像120px。 -->

# 12. 2x2グリッド（画像＋テキスト）

<div class="key-message">画像付きカード4枚で機能や要素を一覧する</div>

<div class="grid grid-cols-2 gap-8 mt-4 text-lg" style="min-height: 520px;">
<div class="bg-gray-50 rounded-xl shadow-md p-8 flex gap-8 items-center">
<div class="rounded-lg overflow-hidden" style="min-width:120px;height:120px;">
<img src="images/feat-analytics.svg" class="img-contain">
</div>
<div>

**機能A: データ分析**
大量データから有意義なインサイトを自動抽出

</div>
</div>
<div class="bg-gray-50 rounded-xl shadow-md p-8 flex gap-8 items-center">
<div class="rounded-lg overflow-hidden" style="min-width:120px;height:120px;">
<img src="images/feat-report.svg" class="img-contain">
</div>
<div>

**機能B: レポート生成**
分析結果を自動でレポートとして出力

</div>
</div>
<div class="bg-gray-50 rounded-xl shadow-md p-8 flex gap-8 items-center">
<div class="rounded-lg overflow-hidden" style="min-width:120px;height:120px;">
<img src="images/feat-alert.svg" class="img-contain">
</div>
<div>

**機能C: アラート通知**
異常値を検知して即座に通知を送信

</div>
</div>
<div class="bg-gray-50 rounded-xl shadow-md p-8 flex gap-8 items-center">
<div class="rounded-lg overflow-hidden" style="min-width:120px;height:120px;">
<img src="images/feat-dashboard.svg" class="img-contain">
</div>
<div>

**機能D: ダッシュボード**
リアルタイムでKPIをモニタリング

</div>
</div>
</div>

---

<!-- Pattern 13: 2x3 grid — 6要素整列。上段Teal/下段Navyでフェーズ区分。各2-3行。 -->

# 13. 2x3グリッドレイアウト

<div class="key-message">6つの要素を3列2行のグリッドで整理する</div>

<div class="grid grid-cols-3 gap-8 mt-4 text-lg" style="min-height: 520px;">
<div class="bg-gray-50 rounded-lg p-10 border-l-4 border-teal">

**要件定義**

ステークホルダーとの合意形成

</div>
<div class="bg-gray-50 rounded-lg p-10 border-l-4 border-teal">

**基本設計**

システムアーキテクチャの策定

</div>
<div class="bg-gray-50 rounded-lg p-10 border-l-4 border-teal">

**詳細設計**

コンポーネント仕様の決定

</div>
<div class="bg-gray-50 rounded-lg p-10 border-l-4 border-navy">

**実装**

コーディングとユニットテスト

</div>
<div class="bg-gray-50 rounded-lg p-10 border-l-4 border-navy">

**結合テスト**

システム間連携の検証

</div>
<div class="bg-gray-50 rounded-lg p-10 border-l-4 border-navy">

**リリース**

本番デプロイと運用開始

</div>
</div>

---

<!-- C. 縦並びリスト系 ============================= -->

<!-- _class: section -->
<!-- _paginate: false -->

# C. 縦並びリスト系
4つの縦型パターン

---

<!-- Pattern 14: v-step — 縦3ステップ。各2-3行。4以上はスライド分割。 -->
<!-- header: 'C. 縦並びリスト系' -->

# 14. 縦3つステップ

<div class="key-message">縦に並べたステップで手順や流れを示す</div>

<div class="mt-4">
<div class="v-step" data-step="1">
<div>

**ステップ1: 現状把握**

現在のワークフローを可視化し、ボトルネックを特定する。チームメンバーへのヒアリングと定量データの収集を並行して行う

</div>
</div>
<div class="v-step" data-step="2">
<div>

**ステップ2: 改善策の立案**

特定された課題に対して、コスト・効果・実現性の3軸で優先順位を付けて改善策を策定する

</div>
</div>
<div class="v-step" data-step="3">
<div>

**ステップ3: 実行と検証**

パイロット導入で効果を検証し、結果に基づいて全社展開の計画を立てる

</div>
</div>
</div>

---

<!-- Pattern 15: 横型step — 左→右のフロー。3-4ステップ。各1-2行。 -->

# 15. 番号付きステップ（横型）

<div class="key-message">矢印でプロセスの流れを示す</div>

<div class="grid items-center text-lg" style="grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr; min-height: 300px;">
<div class="step">
<div class="step-number gray">1</div>
<div class="step-content">

**ステップ1**
説明文が
ここに入る

</div>
</div>
<div class="step-arrow">→</div>
<div class="step">
<div class="step-number gray">2</div>
<div class="step-content">

**ステップ2**
説明文が
ここに入る

</div>
</div>
<div class="step-arrow">→</div>
<div class="step">
<div class="step-number gray">3</div>
<div class="step-content">

**ステップ3**
説明文が
ここに入る

</div>
</div>
<div class="step-arrow">→</div>
<div class="step">
<div class="step-number gray">4</div>
<div class="step-content">

**ステップ4**
説明文が
ここに入る

</div>
</div>
</div>

---

<!-- Pattern 16: timeline — 時系列マイルストーン。3-4項目。 -->

# 16. タイムラインレイアウト

<div class="key-message">時系列に沿ってマイルストーンを整理する</div>

<div class="mt-4">
<div class="timeline-item">
<div class="timeline-date">2024 Q1</div>
<div class="timeline-dot"></div>
<div class="timeline-content">

**概念実証（PoC）の完了**
3つのユースケースでAI統合の実現可能性を確認

</div>
</div>
<div class="timeline-item">
<div class="timeline-date">2024 Q2</div>
<div class="timeline-dot"></div>
<div class="timeline-content">

**パイロット導入**
選定された2チームで本番環境への限定展開を実施

</div>
</div>
<div class="timeline-item">
<div class="timeline-date">2024 Q3</div>
<div class="timeline-dot"></div>
<div class="timeline-content">

**全社展開**
成功事例をもとに全部門への段階的ロールアウト

</div>
</div>
</div>

---

<!-- Pattern 17: icon list — Unicodeアイコン付きリスト。3-4項目。太字タイトル+説明文。 -->

# 17. アイコン付きリスト

<div class="key-message">アイコン付きリストで特徴や強みを訴求する</div>

<div class="mt-4">
<div class="icon-item">
<div class="icon-circle">✓</div>
<div>

**高い拡張性** — マイクロサービスアーキテクチャにより、個別のサービスを独立してスケーリング可能

</div>
</div>
<div class="icon-item">
<div class="icon-circle">⚡</div>
<div>

**高速レスポンス** — エッジキャッシュとCDNの活用により、グローバルで50ms以下のレスポンスを実現

</div>
</div>
<div class="icon-item">
<div class="icon-circle">🔒</div>
<div>

**セキュリティ** — ゼロトラストアーキテクチャを採用し、全通信を暗号化・認証

</div>
</div>
<div class="icon-item">
<div class="icon-circle">📊</div>
<div>

**可観測性** — OpenTelemetryによる統合的なログ・メトリクス・トレースの収集

</div>
</div>
</div>

---

<!-- D. パネルデザイン系 ============================= -->

<!-- _class: section -->
<!-- _paginate: false -->

# D. パネルデザイン系
5つのパネルバリエーション

---

<!-- Pattern 18: panel+image — 画像ヘッダー+テキスト。2枚横並び。3枚ならPattern 22。 -->
<!-- header: 'D. パネルデザイン系' -->

# 18. 基本パネル（画像ヘッダー付き）

<div class="key-message">画像とテキストを組み合わせたカード型で紹介する</div>

<div class="grid grid-cols-2 gap-6 mt-6 text-base">
<div class="bg-white rounded-xl shadow-lg overflow-hidden">
<div class="overflow-hidden" style="height:160px;">
<img src="images/panel-product-a.png" class="img-cover">
</div>
<div class="p-6">

**パネルタイトルA**

画像をパネル上部に配置し、下部にテキストコンテンツを配置するカードデザイン

</div>
</div>
<div class="bg-white rounded-xl shadow-lg overflow-hidden">
<div class="overflow-hidden" style="height:160px;">
<img src="images/panel-product-b.png" class="img-cover">
</div>
<div class="p-6">

**パネルタイトルB**

画像とテキストを組み合わせた読みやすいレイアウト。製品紹介やサービス説明に最適

</div>
</div>
</div>

---

<!-- Pattern 19: panel accent — 左ボーダーで重要度表現。各2-4行。 -->

# 19. 強調パネル（左ボーダー付き）

<div class="key-message">重要度に応じて3段階で情報を整理する</div>

<div class="mt-6">
<div class="panel-accent mb-6">

### 重要な発見

左側のラインで重要度を示すパネル。注意を引きたい情報や結論の強調に使用する。ボーダーカラーでカテゴリを区別できる

</div>

<div class="bg-gray-50 rounded-lg p-6 mb-6" class="border-l-4 border-navy">

### 推奨事項

NavyカラーのボーダーでTealとは異なるカテゴリを表現。アクションアイテムや次のステップの提示に使う

</div>

<div class="bg-gray-50 rounded-lg p-6" class="border-l-4 border-gray-400">

### 補足情報

グレーのボーダーで補足的な情報を表現。参考データや注意書きに使用

</div>
</div>

---

<!-- Pattern 20: glass panel — ガラスモーフィズム。_backgroundColor 設定で効果が出る。 -->
<!-- _backgroundColor: #E8EDF2 -->

# 20. ガラス風パネル

<div class="key-message">モダンなガラスモーフィズムで洗練された印象を与える</div>

<div class="grid grid-cols-2 gap-6 mt-6 text-base">
<div class="panel-glass">

<h3 class="text-navy font-bold">ガラス風パネルタイトル</h3>

背景を透過して見せるガラスモーフィズムデザイン。モダンでクリーンな印象を与える

- 半透明の背景色
- 細い境界線で輪郭を表現
- 影で浮遊感を演出

</div>
<div class="panel-glass">

<h3 class="text-teal font-bold">セカンダリパネル</h3>

背景色やグラデーションの上に重ねて使用することで、ガラスの透過感を強調できる

- コントラスト確保
- 読みやすさ重視
- 内側ハイライトで立体感

</div>
</div>

---

<!-- Pattern 21: gradient panel — Navy→Tealグラデーション。1スライド1つまで。結論やCTAに。 -->

# 21. グラデーションパネル

<div class="key-message">主要メッセージの優先度を視覚的に明確にする</div>

<div class="grid grid-cols-2 gap-6 mt-6 text-base">
<div class="panel-gradient">

<h3 class="font-bold">主要メッセージ</h3>

グラデーション背景のパネルで、特に重要なメッセージを目立たせる。白文字で読みやすさを確保

- 結論のハイライト
- CTAの強調
- KPIの提示

</div>
<div class="panel">

<h3 class="font-bold">サブメッセージ</h3>

通常のパネルと組み合わせて、情報の優先度を視覚的に表現する

- 補足情報
- 詳細データ
- 参考資料

</div>
</div>

---

<!-- Pattern 22: card — 3カード横並び。画像+テキスト。各2-3行。 -->

# 22. カード型レイアウト（画像付き）

<div class="key-message">画像付きカードで複数のアイテムを比較紹介する</div>

<div class="grid grid-cols-3 gap-5 mt-6 text-sm">
<div class="bg-white rounded-xl shadow-lg overflow-hidden">
<div class="overflow-hidden" style="height:130px;">
<img src="images/card-service-a.png" class="img-cover">
</div>
<div class="p-5">

**サービスA**

製品やサービスを紹介するカードデザイン。画像と説明文を組み合わせて視覚的に訴求する

</div>
</div>
<div class="bg-white rounded-xl shadow-lg overflow-hidden">
<div class="overflow-hidden" style="height:130px;">
<img src="images/card-service-b.png" class="img-cover">
</div>
<div class="p-5">

**サービスB**

統一されたカードフォーマットで、複数のアイテムを比較しやすく表示する

</div>
</div>
<div class="bg-white rounded-xl shadow-lg overflow-hidden">
<div class="overflow-hidden" style="height:130px;">
<img src="images/card-service-c.png" class="img-cover">
</div>
<div class="p-5">

**サービスC**

カード間の余白と影で視覚的な区切りを作り、情報の独立性を担保する

</div>
</div>
</div>

---

<!-- E. 背景・画像系 ============================= -->

<!-- _class: section -->
<!-- _paginate: false -->

# E. 背景・画像系
3つの画像パターン

---

<!-- Pattern 23: bg-full — 全画面背景。テキスト2行以内。 -->
<!-- header: 'E. 背景・画像系' -->
<!-- _class: bg-full -->
<!-- _backgroundImage: linear-gradient(rgba(27,69,101,0.7), rgba(62,155,164,0.7)), url("images/bg-full-digital.png") -->
<!-- _backgroundSize: cover -->

# 全画面背景のタイトル
サブテキストが入ります

---

<!-- Pattern 25: quote — 引用文1-3文。引用元必須。 -->
<!-- _class: quote -->

> 引用テキストが入ります。印象的な一文を大きく表示して聴衆の注意を引くパターンです

<div class="attribution">— 発言者名、肩書き</div>

---

<!-- Pattern 26: split images — 複数画像横並び。2-3分割。 -->

# 26. 複数画像・分割背景

<div class="key-message">複数の画像を横並びで見せる</div>

<div style="display: flex; gap: 24px; margin-top: 24px; flex: 1;">
  <div style="flex: 1; border-radius: 16px; overflow: hidden; min-height: 0;">
    <img src="images/split-a.png" class="img-cover">
  </div>
  <div style="flex: 1; border-radius: 16px; overflow: hidden; min-height: 0;">
    <img src="images/split-b.png" class="img-cover">
  </div>
</div>

---

<!-- F. 強調・特殊系 ============================= -->

<!-- _class: section -->
<!-- _paginate: false -->

# F. 強調・特殊系
3つの特殊パターン

---

<!-- Pattern 27: 統計 — 数値を大きく表示。2-4項目。.accent は1つだけ強調したい場合のみ。 -->
<!-- header: 'F. 強調・特殊系' -->

# 27. 統計強調スライド

<div class="key-message">大きな数字で主要KPIをインパクトある形で示す</div>

<div class="grid grid-cols-3 gap-6 mt-8">
<div class="stat-box">
<div class="stat-value text-navy">35万文字</div>
<div class="stat-label">総文字数</div>
<p class="text-xs text-gray-400 mt-2">4部16章60節</p>
</div>
<div class="stat-box accent">
<div class="stat-value">774件</div>
<div class="stat-label">GitHub Issue</div>
</div>
<div class="stat-box">
<div class="stat-value text-navy">1ヶ月</div>
<div class="stat-label">執筆期間</div>
</div>
</div>

---

<!-- Pattern 28: center-message — 1メッセージを64pxで中央表示。1-2行。 -->
<!-- _class: center-message -->

# 強調したい
# メッセージ

補足テキストが入ります

---

<!-- Pattern 29: Q&A — 質疑応答。_paginate: false 併用。 -->
<!-- _class: qanda -->
<!-- _paginate: false -->

# Q&A
質問を促すテキストが入ります

---

<!-- G. 応用パターン系 ============================= -->

<!-- _class: section -->
<!-- _paginate: false -->

# G. 応用パターン系
12の応用パターン

---

<!-- Pattern 30: QR — QRコード+テキスト。左テキスト、右QRエリア220px。 -->
<!-- header: 'G. 応用パターン系' -->

# 30. QRコード付き紹介

<div class="key-message">書籍やサイトへ誘導する</div>

<div class="flex flex-col items-center" style="flex:1; justify-content:center;">
<div class="bg-gray-100 rounded-xl flex items-center justify-center" style="width:300px;height:300px;border:2px solid #E5E7EB;">
<span class="text-gray-400 text-2xl">QR Code</span>
</div>
<p class="mt-4 text-lg text-gray-600">タイトルがここに入ります</p>
<p class="text-teal font-bold">https://example.com</p>
</div>

---

<!-- Pattern 31: question — 問いかけ。質問は1つ。_paginate: false 併用。 -->
<!-- _class: question -->
<!-- _paginate: false -->

# 聴衆への問いかけが入ります

---

<!-- Pattern 32: footnote — 出典付きデータ提示。.source で出典記載。パネル内3-4項目。 -->

# 32. 脚注引用スライド

<div class="key-message">データに基づく主張を出典付きで裏付ける</div>

<div class="grid grid-cols-2 gap-8 mt-4" style="min-height: 380px;">
<div class="panel">

**定量効果**
- 作業時間: **60%削減**
- エラー率: **85%低減**
- コスト: **年間40%削減**

</div>
<div class="panel">

**定性効果**
- 従業員満足度の向上
- クリエイティブ業務への時間創出
- 意思決定スピードの改善

</div>
</div>

<div class="source">出典: AI導入効果調査レポート 2025, 総務省</div>

---

<!-- Pattern 33: inline image — テキスト+画像を同じ視線で。アーキテクチャ図解説に。 -->

# 33. インライン画像スライド

<div class="key-message">テキストと図を横並びにして視覚的に補足する</div>

<div class="grid grid-cols-2 gap-8 mt-6 items-center">
<div class="text-base">

### システムアーキテクチャ

画像をコンテンツの中に自然に配置するパターン。テキストと画像を同じ視線の流れで読めるようにする

主なコンポーネント:
- APIゲートウェイ
- マイクロサービス群
- データレイク

</div>
<div class="rounded-xl overflow-hidden" style="min-height:320px;">

<img src="images/architecture.png" class="img-cover">

</div>
</div>

---

<!-- Pattern 34: 統計比率 — 4つの比率並列。色で区分。 -->

# 34. 統計比率スライド

<div class="key-message">比率や割合を大きな数字で視覚的に伝える</div>

<div class="grid grid-cols-4 gap-6 mt-8 text-base" style="min-height: 280px;">
<div class="stat-box">
<div class="stat-value text-teal">42%</div>
<div class="stat-label">導入済み</div>
</div>
<div class="stat-box">
<div class="stat-value text-navy">28%</div>
<div class="stat-label">検討中</div>
</div>
<div class="stat-box">
<div class="stat-value text-gray-600">18%</div>
<div class="stat-label">計画段階</div>
</div>
<div class="stat-box">
<div class="stat-value text-gray-400">12%</div>
<div class="stat-label">未検討</div>
</div>
</div>

<div class="mt-6 text-base text-center">

AI活用の導入ステージ別企業割合（n=500）

</div>

---

<!-- Pattern 35: text+stats — 左テキスト+右統計グリッド。.accent は1つまで。 -->

# 35. テキスト＋統計パネル混合

<div class="key-message">テキストの説明と統計パネルを組み合わせる</div>

<div class="grid grid-cols-2 gap-8 mt-6 text-base">
<div>

### 主要な成果

第1四半期の目標を全て達成。特に顧客満足度とリードタイムの改善が顕著

- 新規顧客獲得数が前年比150%
- 解約率は過去最低の0.8%を記録
- NPSスコアが+15pt改善

</div>
<div class="grid grid-cols-2 gap-4">
<div class="stat-box">
<div class="stat-value text-teal" class="text-2xl">150%</div>
<div class="stat-label">新規顧客</div>
</div>
<div class="stat-box">
<div class="stat-value text-navy" class="text-2xl">0.8%</div>
<div class="stat-label">解約率</div>
</div>
<div class="stat-box accent">
<div class="stat-value" class="text-2xl">+15</div>
<div class="stat-label">NPS</div>
</div>
<div class="stat-box">
<div class="stat-value text-teal" class="text-2xl">30%</div>
<div class="stat-label">コスト削減</div>
</div>
</div>
</div>

---

<!-- Pattern 36: まとめ（ガラス風） — 番号付き3ポイント。プレゼン結論に。各1-2行。 -->

# 36. まとめスライド（ガラス風縦並び）

<div class="key-message">番号付きのガラス風パネルでまとめを提示する</div>

<div class="grid gap-8 mt-4 text-base">
<div class="panel-glass flex gap-4 items-center">
<div class="bg-teal rounded-full flex items-center justify-center text-white font-bold" style="min-width:48px;height:48px;">1</div>
<div>

**スタイルガイドの整備** — AIの出力品質を制約で担保するために、デザインルールを体系化する

</div>
</div>
<div class="panel-glass flex gap-4 items-center">
<div class="bg-teal rounded-full flex items-center justify-center text-white font-bold" style="min-width:48px;height:48px;">2</div>
<div>

**パターンカタログの構築** — 39種類のレイアウトから最適なものを選択可能にする

</div>
</div>
<div class="panel-glass flex gap-4 items-center">
<div class="bg-teal rounded-full flex items-center justify-center text-white font-bold" style="min-width:48px;height:48px;">3</div>
<div>

**自動検証ループの実装** — スクリーンショット→AI検出→修正の品質保証サイクルを確立する

</div>
</div>
</div>

---

<!-- Pattern 37: list+supplement — 箇条書きリスト+下部に補足パネル。 -->

# 37. シンプルリスト＋補足パネル

<div class="key-message">箇条書きに補足情報を添える</div>

- リスト項目1がここに入ります。山路を登りながら。
- リスト項目2がここに入ります。智に働けば角が立つ。
- リスト項目3がここに入ります。情に棹させば流される。
- **強調したいリスト項目がここに入ります**

<div class="panel mt-6">

補足説明文がここに入ります。
次のアクションへの導入など。

</div>

---

<!-- Pattern 38: 対比+結論 — 2パネル比較+下部に結論帯。強調側にTealボーダー（中立比較ならボーダーなし可）。結論1-2行。 -->

# 38. 対比＋結論スライド

<div class="key-message">2つの選択肢を対比し結論を導く</div>

<div class="grid grid-cols-2 gap-6 mt-4 text-base">
<div class="bg-gray-50 rounded-xl p-6">

<h3 class="text-gray-600 font-bold">従来のアプローチ</h3>

- 手動でのコードレビュー
- 週次のデプロイサイクル
- リアクティブな障害対応
- 属人化したナレッジ

</div>
<div class="bg-gray-50 rounded-xl p-6 border-2 border-teal">

<h3 class="text-teal font-bold">提案するアプローチ</h3>

- AI支援のコードレビュー
- 継続的デリバリー（CD）
- プロアクティブな監視
- ナレッジの体系化

</div>
</div>

<div class="panel-gradient text-center" style="margin-top: 56px; font-size: 24px;">

<strong style="font-size: 28px;">結論: AI支援の開発プロセスへ移行することで、品質と速度の両立が可能になる</strong>

</div>

---

<!-- Pattern 39: table+highlight — 比較表。推奨列を太字。列4つ以内、行6-8以内。 -->

# 39. テーブル＋ハイライト

<div class="key-message">テーブルとハイライトで比較データを提示する</div>

| 評価項目 | ツールA | ツールB | **ツールC（推奨）** |
|:---------|:-------:|:-------:|:-------------------:|
| 導入コスト | ◯ | △ | **◎** |
| 学習コスト | △ | ◯ | **◎** |
| 拡張性 | ◯ | ◯ | **◎** |
| サポート | △ | ◎ | **◯** |
| セキュリティ | ◯ | △ | **◎** |
| **総合評価** | **B** | **B** | **A** |


