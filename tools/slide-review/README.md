# Slide Review - スライドフィードバックシステム

Marp スライドのレビュー・フィードバック収集を行う Web UI ツール。スライドをブラウザでプレビューしながら、スライドごとにコメントを残し、Claude Code に修正を依頼できる。

## 前提条件

- Python 3
- Marp CLI でビルド済みのデッキ HTML

```bash
# デッキ HTML がない場合は先にビルド
npx @marp-team/marp-cli deck.md --theme-set rector.css --html --allow-local-files
```

## 使い方

```bash
python3 tools/slide-review/generate_review.py <デッキHTMLパス>
```

```bash
# 例
python3 tools/slide-review/generate_review.py output/my-deck/deck.html
# → output/my-deck/deck-review.html が生成され、ブラウザで自動オープン
```

## ワークフロー

```
1. デッキをビルド（marp-cli → HTML）
2. python3 tools/slide-review/generate_review.py deck.html
3. ブラウザでスライドを確認しながらコメント入力
4. 「Submit All Reviews」→ feedback.json がダウンロードされる
5. Claude Code に「feedback.json を読んで修正して」と依頼
6. 修正後、再ビルド → 再レビュー（必要に応じて繰り返し）
```

## UI 操作

### ナビゲーション

| 操作 | 方法 |
|------|------|
| 次のスライド | `→` キー or `▶` ボタン |
| 前のスライド | `←` キー or `◀` ボタン |
| 任意のスライド | ヘッダーのドットをクリック |

### コメント入力

- 各スライドにテキストエリアでコメントを入力
- 入力内容は localStorage に自動保存（ブラウザを閉じても残る）
- コメント済みスライドはドットが色付きで表示される

### クイックアクションボタン

ボタンをクリックすると、コメント末尾にスキル呼び出しテキストが挿入される。

| ボタン | 挿入されるテキスト |
|--------|-------------------|
| スタイル整形 | `/slide-style-rector をつかってスタイルを整えて` |
| レイアウト修正 | `/layout-fix をつかってレイアウト崩れを修正して` |
| イラスト生成 | `/ergon をつかって説明イラストを作成して挿入して` |
| 図解生成 | `/svg-creator をつかって図解を作成して挿入して` |

### レイアウト選択

「レイアウト選択...」ボタンからモーダルを開き、39種のレイアウトパターンから選択できる。選択すると「このスライドを『パターン N: 名称』のレイアウトに変更して」がコメントに挿入される。

## 出力される feedback.json

```json
{
  "deck": "deck.html",
  "timestamp": "2026-04-13T10:30:00.000Z",
  "total_slides": 14,
  "reviews": [
    {"slide": 1, "comment": ""},
    {"slide": 3, "comment": "/layout-fix をつかってレイアウト崩れを修正して\nテキストが窮屈に見える"},
    {"slide": 8, "comment": "このスライドを「パターン8: 3カラム」のレイアウトに変更して"}
  ]
}
```

## ファイル構成

```
tools/slide-review/
├── README.md                 # このファイル
├── generate_review.py        # レビュー HTML 生成スクリプト
└── review-template.html      # レビュー UI テンプレート
```
