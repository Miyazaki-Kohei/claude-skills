# Claude Skills

Claude Code で使用するスライド作成ワークフローのスキルコレクション。スキルごとに責務を分離した設計。

## スキル一覧

| スキル | 責務 | トリガー例 |
|--------|------|-----------|
| [slide-style-MIYAKOH](skills/slide-style-MIYAKOH/) | 既存 Marp スライドに39種のレイアウトパターンを適用して整形 | `スタイルを整えて` `パターンに合わせて` |
| [slimg](skills/slimg/) | Google Imagen 4 による画像生成（npm `@miyakoh/slimg`） | `画像を生成` `イラストを作成` |
| [svg-creator](skills/svg-creator/) | SVG ダイアグラム・アイコン・図解を直接生成 | `フロー図を作って` `アイコンを生成` |
| [layout-fix](skills/layout-fix/) | Playwright でレンダリングし、レイアウト崩れを検出・修正 | `レイアウト確認` `はみ出し修正` |

## スライドレビューツール

これらのスキル群は [slirev](https://github.com/Miyazaki-Kohei/slirev) と連携して使用することを推奨する。slirev はスライドのプレビューとスライド単位のフィードバック管理を提供し、各スキルへの修正指示をスムーズに行える。

## ワークフロー

```
1. Marp スライドを書く（ユーザー）
2. /slide-style-MIYAKOH でレイアウト整形（パターン適用 + slimg で画像生成）
3. /layout-fix でスクリーンショット撮影 → 崩れ修正
4. 完成（output/ に HTML 出力）
```

## セットアップ

```bash
uv sync
```

slimg を使う場合は `GEMINI_API_KEY` を `.env` に設定する。

## ディレクトリ構成

```
claude-skills/
├── skills/
│   ├── slide-style-MIYAKOH/  # スタイル整形（テーマ、パターン、リファレンス）
│   ├── slimg/                 # 画像生成
│   ├── svg-creator/           # SVG 生成
│   └── layout-fix/            # レイアウト検証・修正
├── output/                    # 実行成果物（.gitignore）
├── decks/                     # 作成済みデッキ（.gitignore）
└── pyproject.toml
```

## スキルの追加

`skills/<skill-name>/SKILL.md` を作成すれば、Claude Code のスキルとして認識される。
