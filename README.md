# Claude Skills

Claude Code で使用するカスタムスキルのコレクション。

## スキル一覧

| スキル | 概要 |
|--------|------|
| [ppt-creator](skills/ppt-creator/) | Marp でコンサルティング品質のスライド（PPTX/HTML/PDF）を生成する |

## セットアップ

```bash
uv sync
```

各スキルが必要とする外部ツール（Marp CLI など）は、スキルの SKILL.md に記載されています。

## ディレクトリ構成

```
claude-skills/
├── skills/           # スキル本体
│   └── <skill-name>/
│       ├── SKILL.md      # スキル定義（Claude Code が読み込む）
│       ├── scripts/      # 補助スクリプト
│       ├── references/   # 詳細リファレンス
│       └── ...
├── output/           # スキルの実行成果物（.gitignore）
└── pyproject.toml
```

## スキルの追加

`skills/<skill-name>/SKILL.md` を作成すれば、Claude Code のスキルとして認識されます。
