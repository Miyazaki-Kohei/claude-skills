from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from .common import DEFAULT_OUTPUT_DIR_NAME, TEMPLATES_DIR, THEMES_DIR, available_templates, available_themes


def copy_template(deck_name: str, template: str, theme: str, output_dir: Path) -> Path:
    deck_dir = output_dir / deck_name
    assets_dir = deck_dir / "assets"
    deck_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(exist_ok=True)

    # Copy template
    src = TEMPLATES_DIR / f"{template}.md"
    dst = deck_dir / "deck.md"
    title = deck_name.replace("-", " ").title()
    content = src.read_text(encoding="utf-8").replace("{{DECK_TITLE}}", title)

    # Inject theme into frontmatter
    content = re.sub(r"theme:\s*\S+", f"theme: {theme}", content)

    dst.write_text(content, encoding="utf-8")

    # Copy theme CSS to deck directory for marp --theme-set
    theme_src = THEMES_DIR / f"{theme}.css"
    if theme_src.exists():
        shutil.copy2(theme_src, deck_dir / f"{theme}.css")

    return dst


def main() -> None:
    templates = available_templates()
    themes = available_themes()

    parser = argparse.ArgumentParser(description="Create a new slide deck scaffold.")
    parser.add_argument("name", help="Deck name (used as directory name)")
    parser.add_argument(
        "--template",
        choices=templates,
        default="blank",
        help=f"Template to use (default: blank). Available: {', '.join(templates)}",
    )
    parser.add_argument(
        "--theme",
        choices=themes,
        default="consulting-light",
        help=f"Theme to use (default: consulting-light). Available: {', '.join(themes)}",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help=f"Output directory (e.g. /path/to/project/{DEFAULT_OUTPUT_DIR_NAME})",
    )
    args = parser.parse_args()

    created = copy_template(args.name, args.template, args.theme, args.output_dir)
    print(f"Created: {created}")
    print(f"Template: {args.template}")
    print(f"Theme: {args.theme}")
    print(f"Assets dir: {created.parent / 'assets'}")
    print(f"Dist dir: {created.parent / 'dist'}")


if __name__ == "__main__":
    main()
