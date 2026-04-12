"""
Mermaid → image conversion for Marp decks.

Why this exists:
    Marp does not render Mermaid to images by itself. The HTML export can use
    a mermaid.js CDN loader (build.py --with-mermaid) to render in the
    browser, but PPTX/PDF exports have no such escape hatch — the diagram
    stays as a raw code block. When you need real pictures inside the PPTX,
    extract the Mermaid blocks and generate PNGs from them.

How it works:
    1. Scan the deck for ```mermaid ... ``` fenced blocks.
    2. For each block, derive a stable filename from a content hash.
    3. If `mmdc` (mermaid-cli) is on PATH, render assets/mermaid-<hash>.png.
    4. Rewrite the deck to replace each code block with an image reference
       (default width w:700px to match the FJ theme content region).

If `mmdc` is not available the script exits with WARNING (not ERROR). This
is a power-user path; the skill works fine on a machine that only has marp
installed.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

MERMAID_BLOCK = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL)

# Padding (px) to keep around the trimmed diagram so it doesn't sit
# flush against the edge of the PNG.
TRIM_PADDING = 16


def find_mermaid_blocks(text: str) -> list[tuple[int, int, str]]:
    """Return (start, end, source) tuples for each fenced mermaid block."""
    return [(m.start(), m.end(), m.group(1).strip()) for m in MERMAID_BLOCK.finditer(text)]


def asset_name(source: str) -> str:
    digest = hashlib.sha1(source.encode("utf-8")).hexdigest()[:10]
    return f"mermaid-{digest}.png"


def trim_whitespace(image_path: Path) -> None:
    """Crop surrounding whitespace from a PNG, keeping a small padding.

    Uses Pillow if available; silently skips if not installed — the image
    will just have the original mmdc whitespace which is functional, just
    not as tight.
    """
    try:
        from PIL import Image, ImageChops  # type: ignore[import-untyped]
    except ImportError:
        return  # Pillow not installed — skip trimming

    img = Image.open(image_path).convert("RGBA")
    # Create a reference image of the background color (white).
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox is None:
        return  # entirely white — nothing to trim

    # Expand bbox by TRIM_PADDING, clamped to image bounds.
    x0 = max(0, bbox[0] - TRIM_PADDING)
    y0 = max(0, bbox[1] - TRIM_PADDING)
    x1 = min(img.width, bbox[2] + TRIM_PADDING)
    y1 = min(img.height, bbox[3] + TRIM_PADDING)

    cropped = img.crop((x0, y0, x1, y1))
    cropped.save(image_path)


def render_with_mmdc(source: str, out_path: Path) -> bool:
    """Try to render using the Mermaid CLI (`mmdc`) if installed locally."""
    if not shutil.which("mmdc"):
        return False
    with out_path.with_suffix(".mmd").open("w", encoding="utf-8") as f:
        f.write(source)
    # Use a Puppeteer config to minimize whitespace around the diagram.
    # mmdc renders inside a Chromium viewport — by default it picks a large
    # viewport which adds generous padding around the SVG.  A JSON config
    # with ``fit`` + a tight viewport trims most of that dead space.
    import json as _json, tempfile as _tmp
    puppet_cfg = {"fit": True}
    cfg_file = _tmp.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, dir=str(out_path.parent)
    )
    _json.dump(puppet_cfg, cfg_file)
    cfg_file.close()
    cfg_path = cfg_file.name

    try:
        subprocess.run(
            [
                "mmdc",
                "-i", str(out_path.with_suffix(".mmd")),
                "-o", str(out_path),
                "-b", "white",
                "-s", "3",
                "-p", cfg_path,
            ],
            check=True,
            capture_output=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"  mmdc failed: {exc.stderr.decode(errors='replace')[:200]}")
        return False
    finally:
        out_path.with_suffix(".mmd").unlink(missing_ok=True)
        Path(cfg_path).unlink(missing_ok=True)
    return True


def process(deck_path: Path, dry_run: bool) -> int:
    text = deck_path.read_text(encoding="utf-8")
    blocks = find_mermaid_blocks(text)
    if not blocks:
        print("No mermaid blocks found — nothing to do.")
        return 0

    assets_dir = deck_path.parent / "assets"
    assets_dir.mkdir(exist_ok=True)

    print(f"Found {len(blocks)} mermaid block(s) in {deck_path.name}")

    if not shutil.which("mmdc"):
        print("WARNING: `mmdc` (mermaid-cli) not found on PATH. Leaving the deck untouched.")
        print("         Install with: npm install -g @mermaid-js/mermaid-cli")
        return 0

    # Build replacements from the end of the file backwards so byte offsets
    # computed from the original text remain valid as we splice.
    new_text = text
    for start, end, source in reversed(blocks):
        name = asset_name(source)
        out = assets_dir / name
        if not out.exists():
            if not render_with_mmdc(source, out):
                continue
            trim_whitespace(out)
            print(f"  rendered {name}")
        else:
            print(f"  reuse {name} (already exists)")
        # Intentionally emit no width directive. Sizing is handled by fj.css
        # based on where the image lands:
        #   - On content-image-right / -left: `max-width: 100%` inside the
        #     side panel so the image fits whatever 20–70% slot the author
        #     picked. A hardcoded width here would overflow narrow panels.
        #   - On a default-layout slide where the image is the only element
        #     in its paragraph: CSS enlarges it to `min(1100px, 95%)` so
        #     solo diagrams don't look like thumbnails.
        replacement = f"![mermaid diagram](assets/{name})"
        if dry_run:
            print(f"  (dry-run) would replace block at {start}-{end}")
        else:
            new_text = new_text[:start] + replacement + new_text[end:]

    if not dry_run and new_text != text:
        backup = deck_path.with_suffix(".md.bak")
        backup.write_text(text, encoding="utf-8")
        deck_path.write_text(new_text, encoding="utf-8")
        print(f"Updated {deck_path.name} (backup at {backup.name})")

    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Render Mermaid blocks in a Marp deck to PNGs.")
    parser.add_argument("deck", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen, don't modify files.")
    args = parser.parse_args()

    if not args.deck.exists():
        print(f"Deck not found: {args.deck}")
        sys.exit(1)

    sys.exit(process(args.deck, args.dry_run))


if __name__ == "__main__":
    main()
