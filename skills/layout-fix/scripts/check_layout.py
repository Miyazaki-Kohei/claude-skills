#!/usr/bin/env python3
"""Playwright-based Marp slide layout checker.

Builds HTML from Marp markdown, opens in a headless Chromium browser,
and captures each slide as a screenshot. Replaces the manual
`marp-cli --images png` workflow with a single command.

Usage:
    uv run python skills/layout-fix/scripts/check_layout.py decks/my-deck/deck.md

Screenshots are saved to a temporary directory and paths are printed
for Claude to read. Use --cleanup to delete screenshots afterward.
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

VIEWPORT = {"width": 1920, "height": 1080}
THEME_CANDIDATES = ["MIYAKOH.css", "rector.css", "theme.css"]


def find_theme(deck_dir: Path) -> Path | None:
    """Auto-detect theme CSS in the deck directory."""
    for name in THEME_CANDIDATES:
        p = deck_dir / name
        if p.exists():
            return p
    return None


def build_html(deck: Path, theme: Path, html_out: Path) -> None:
    """Build Marp HTML from markdown."""
    cmd = [
        "npx", "@marp-team/marp-cli",
        str(deck),
        "--theme-set", str(theme),
        "--html",
        "--allow-local-files",
        "--output", str(html_out),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"marp-cli error:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)


def capture_slides(html_path: Path, out_dir: Path) -> list[Path]:
    """Open Marp HTML in Playwright and screenshot each slide."""
    out_dir.mkdir(parents=True, exist_ok=True)
    file_url = html_path.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport=VIEWPORT)

        page.goto(file_url)
        page.wait_for_load_state("networkidle")

        total = page.locator("section[id]").count()
        if total == 0:
            print("Error: No slides found in HTML", file=sys.stderr)
            browser.close()
            sys.exit(1)

        paths: list[Path] = []
        for i in range(1, total + 1):
            page.goto(f"{file_url}#{i}")
            page.wait_for_timeout(200)
            out = out_dir / f"slide-{i:03d}.png"
            page.screenshot(path=str(out))
            paths.append(out)

        browser.close()

    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description="Marp slide layout checker (Playwright)")
    parser.add_argument("deck", nargs="?", help="Path to deck.md")
    parser.add_argument("--theme", help="Path to theme CSS (auto-detected if omitted)")
    parser.add_argument("--cleanup", metavar="DIR", help="Delete screenshot directory and exit")
    args = parser.parse_args()

    # Cleanup mode
    if args.cleanup:
        target = Path(args.cleanup)
        if target.exists():
            shutil.rmtree(target)
            print(f"Cleaned up: {target}")
        return

    if not args.deck:
        parser.error("deck is required (unless using --cleanup)")

    deck = Path(args.deck).resolve()
    if not deck.exists():
        print(f"Error: {deck} not found", file=sys.stderr)
        sys.exit(1)

    # Resolve theme
    theme = Path(args.theme).resolve() if args.theme else find_theme(deck.parent)
    if theme is None or not theme.exists():
        print("Error: Theme CSS not found. Use --theme to specify.", file=sys.stderr)
        sys.exit(1)

    # Build HTML (reuse existing if already built)
    html_path = deck.with_suffix(".html")
    print(f"Building HTML...", file=sys.stderr)
    build_html(deck, theme, html_path)

    # Capture screenshots to temp dir
    tmp_dir = Path(tempfile.mkdtemp(prefix="marp-layout-"))
    print(f"Capturing slides with Playwright...", file=sys.stderr)
    paths = capture_slides(html_path, tmp_dir)

    # Output
    print(f"{len(paths)} slides captured", file=sys.stderr)
    print(f"SCREENSHOT_DIR={tmp_dir}")
    for p in paths:
        print(p)


if __name__ == "__main__":
    main()
