from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .common import run, which


def find_theme_css(deck_path: Path) -> Path | None:
    """Find a custom theme CSS file in the deck directory."""
    css_files = list(deck_path.parent.glob("*.css"))
    return css_files[0] if css_files else None


def marp_build(deck_path: Path, fmt: str, output: Path | None) -> int:
    marp = which("marp") or which("npx")
    if marp is None:
        print("marp or npx not found. Install @marp-team/marp-cli.")
        return 1

    out = output or deck_path.parent / "dist" / f"{deck_path.stem}.{fmt}"
    out.parent.mkdir(parents=True, exist_ok=True)

    if Path(marp).name == "npx":
        cmd = [marp, "@marp-team/marp-cli", str(deck_path), f"--{fmt}", "-o", str(out)]
    else:
        cmd = [marp, str(deck_path), f"--{fmt}", "-o", str(out)]

    # Auto-detect custom theme CSS
    theme_css = find_theme_css(deck_path)
    if theme_css:
        cmd.extend(["--theme-set", str(theme_css)])

    return run(cmd, cwd=deck_path.parent)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a Marp deck.")
    parser.add_argument("deck", type=Path)
    parser.add_argument("--format", choices=["html", "pdf", "pptx", "png"], default="html")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    code = marp_build(args.deck, args.format, args.output)
    sys.exit(code)


if __name__ == "__main__":
    main()
