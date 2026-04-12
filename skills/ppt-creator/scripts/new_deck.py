from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path

from .common import DEFAULT_OUTPUT_DIR_NAME, THEME_FILE, THEME_NAME, THEMES_DIR

THEME_ASSETS_DIR = THEMES_DIR / "assets"

SCAFFOLD = """---
marp: true
theme: {theme}
paginate: true
title: {title}
description: {title}
footer: "{title}"
---

<!-- _class: title -->
<!-- _paginate: false -->

# {title}

{today}

発表者名

---

# 最初のメッセージを**アクションタイトル**で書く

- トピックラベル (例: 「現状分析」) ではなく、結論 (例: 「A案が3つの指標で優位」) を見出しにする
- 1スライド1メッセージを守る
- 必要に応じて `content-image-right`, `column-layout`, `small-text` などの FJ クラスを使い分ける
- 見出し内強調は「**強調語**」のように **約物の内側** に `**` を置く (`**「強調語」**` だと CommonMark の right-flanking 違反で bold が効かない)

---

<!-- _class: align-center all-text-center -->

# まとめ

# **最も伝えたい1文**をここに置く

次アクション: YYYY/MM/DD までに◯◯を完了
"""


def create_deck(deck_name: str, output_dir: Path) -> Path:
    deck_dir = output_dir / deck_name
    assets_dir = deck_dir / "assets"
    deck_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(exist_ok=True)

    title = deck_name.replace("-", " ").title()
    today = f"{date.today().year}年{date.today().month}月{date.today().day}日"
    deck_path = deck_dir / "deck.md"
    deck_path.write_text(
        SCAFFOLD.format(theme=THEME_NAME, title=title, today=today), encoding="utf-8"
    )

    # Copy the theme CSS next to the deck so `marp --theme-set` can pick it up.
    if THEME_FILE.exists():
        shutil.copy2(THEME_FILE, deck_dir / THEME_FILE.name)

    # Copy bundled brand assets (logos referenced from fj.css) into the deck's
    # assets/ dir. The CSS uses url("assets/logo-*.png") relative to fj.css,
    # which after copy lives at <deck>/fj.css, so the logos must sit at
    # <deck>/assets/logo-*.png.
    if THEME_ASSETS_DIR.exists():
        for asset in THEME_ASSETS_DIR.iterdir():
            if asset.is_file():
                shutil.copy2(asset, assets_dir / asset.name)

    return deck_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Create a new slide deck scaffold using the bundled FJ theme. "
            "Writes a minimal 3-slide scaffold (title → body → closing). "
            "Compose structure and content using references/layouts.md, "
            "references/sample-slide.md, and references/consulting-frameworks.md."
        ),
    )
    parser.add_argument("name", help="Deck name (used as directory name)")
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help=f"Output directory (e.g. /path/to/project/{DEFAULT_OUTPUT_DIR_NAME})",
    )
    args = parser.parse_args()

    created = create_deck(args.name, args.output_dir)
    print(f"Created: {created}")
    print(f"Theme: {THEME_NAME} (fixed)")
    print(f"Assets dir: {created.parent / 'assets'}")
    print(f"Dist dir: {created.parent / 'dist'}")


if __name__ == "__main__":
    main()
