from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

from .common import run, which
from .generate_images import find_mermaid_blocks, process as render_mermaid

# Mermaid CDN loader. Injected into HTML output when `--with-mermaid` is set so
# ```mermaid code blocks render in the browser. PPTX/PDF exports cannot use
# this path — convert diagrams to images with generate_images.py instead.
MERMAID_SNIPPET = """<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
mermaid.initialize({ startOnLoad: false, theme: "default" });
document.querySelectorAll('pre code.language-mermaid, pre > code.language-mermaid').forEach((el, i) => {
  const container = document.createElement('div');
  container.className = 'mermaid';
  container.textContent = el.textContent;
  const pre = el.closest('pre');
  pre.parentNode.replaceChild(container, pre);
});
mermaid.run();
</script>"""


def find_theme_css(deck_path: Path) -> Path | None:
    """Find a custom theme CSS file in the deck directory."""
    css_files = list(deck_path.parent.glob("*.css"))
    return css_files[0] if css_files else None


def inject_mermaid(html_path: Path) -> None:
    """Insert the mermaid loader right before </body> in an HTML export."""
    text = html_path.read_text(encoding="utf-8")
    if "mermaid.esm.min.mjs" in text:
        return  # already injected
    if "</body>" in text:
        text = text.replace("</body>", f"{MERMAID_SNIPPET}\n</body>", 1)
    else:
        text += "\n" + MERMAID_SNIPPET
    html_path.write_text(text, encoding="utf-8")


# Formats that need to read local image files (e.g. bundled logo PNGs referenced
# from the theme CSS). Marp CLI blocks file:// access by default for PDF/PPTX/image
# exports as a security guard, so we opt-in via --allow-local-files for these.
# HTML output runs in the browser and doesn't need this flag.
LOCAL_FILE_FORMATS = {"pdf", "pptx", "png"}


def auto_render_mermaid_for_export(deck_path: Path, fmt: str, with_mermaid: bool) -> int:
    """Convert mermaid code blocks to PNG assets in-place so all export
    formats (html / pdf / pptx / png) show real diagrams consistently.

    Historically this only ran for binary exports (pdf/pptx/png) — HTML was
    expected to use the `--with-mermaid` CDN loader for browser-side
    rendering. That caused a jarring inconsistency where HTML and PPTX
    looked different for the same deck, and users had to remember the flag.
    Now we render to PNG for every format by default; `--with-mermaid` opts
    out and keeps the raw ```mermaid block so the HTML CDN loader can
    handle it instead.

    Returns 0 on success or no-op, non-zero when mermaid blocks exist and
    `mmdc` is missing (hard failure — user expects diagrams).
    """
    if with_mermaid and fmt == "html":
        return 0  # user explicitly opted into browser-side rendering
    text = deck_path.read_text(encoding="utf-8")
    if not find_mermaid_blocks(text):
        return 0
    if not shutil.which("mmdc"):
        print(
            f"ERROR: deck contains mermaid blocks but `mmdc` is not installed.\n"
            f"       {fmt.upper()} export cannot render mermaid as images without it.\n"
            f"       Install with: npm install -g @mermaid-js/mermaid-cli\n"
            f"       Or (HTML only) pass --with-mermaid for browser-side rendering."
        )
        return 3
    print(f"Auto-rendering mermaid blocks → PNG for {fmt} export...")
    return render_mermaid(deck_path, dry_run=False)


def marp_build_one(deck_path: Path, fmt: str, output: Path | None, with_mermaid: bool = False) -> int:
    # Resolve to absolute paths up front. We chdir into the deck directory when
    # invoking marp (so relative `assets/...` URLs in fj.css resolve), and
    # relative input/output args would otherwise dangle once cwd changes.
    deck_path = deck_path.resolve()
    code = auto_render_mermaid_for_export(deck_path, fmt, with_mermaid)
    if code != 0:
        return code

    marp = which("marp") or which("npx")
    if marp is None:
        print("marp or npx not found. Install @marp-team/marp-cli.")
        return 1

    out = (output or deck_path.parent / "dist" / f"{deck_path.stem}.{fmt}").resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    if Path(marp).name == "npx":
        cmd = [marp, "@marp-team/marp-cli", str(deck_path), f"--{fmt}", "-o", str(out)]
    else:
        cmd = [marp, str(deck_path), f"--{fmt}", "-o", str(out)]

    # Auto-detect custom theme CSS so we don't have to pass `--theme-set` every time.
    theme_css = find_theme_css(deck_path)
    if theme_css:
        cmd.extend(["--theme-set", str(theme_css.resolve())])

    # The bundled FJ theme references logo PNGs via url("assets/..."). Marp blocks
    # local file access by default for PDF/PPTX/image exports — opt in so the logos
    # actually appear in the output. HTML doesn't need this.
    if fmt in LOCAL_FILE_FORMATS:
        cmd.append("--allow-local-files")

    code = run(cmd, cwd=deck_path.parent)
    if code != 0:
        return code

    # HTML output references theme assets via relative URLs (e.g.
    # `url("assets/logo-slide.png")` from fj.css). The HTML lands in dist/, so the
    # browser resolves those URLs against dist/ — we have to mirror the deck's
    # assets/ dir into dist/assets/ for the logos to actually render. PPTX/PDF
    # embed images at conversion time so they don't need this.
    if fmt == "html":
        assets_src = deck_path.parent / "assets"
        if assets_src.is_dir():
            assets_dst = out.parent / "assets"
            shutil.copytree(assets_src, assets_dst, dirs_exist_ok=True)

    if with_mermaid:
        if fmt != "html":
            print(f"note: --with-mermaid only affects HTML output; ignoring for {fmt}")
        else:
            inject_mermaid(out)
            print(f"injected mermaid loader into {out}")

    return 0


def marp_build(deck_path: Path, formats: list[str], output: Path | None, with_mermaid: bool = False) -> int:
    """Build the deck into one or more formats by invoking marp once per format.

    Marp CLI itself cannot emit multiple formats in a single run, so we loop. The
    common case is `--format html pptx`: HTML for fast browser preview during
    iteration, PPTX for the deliverable. `--output` only applies when a single
    format is requested — multiple formats always go to the default `dist/` path.
    """
    if output is not None and len(formats) > 1:
        print("--output can only be used with a single --format. Drop --output to build multiple formats.")
        return 2

    for fmt in formats:
        code = marp_build_one(deck_path, fmt, output, with_mermaid=with_mermaid)
        if code != 0:
            return code
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Build a Marp deck into one or more formats. "
            "Pass multiple values to --format to emit them all in one invocation, "
            "e.g. `--format html pptx` builds both side by side."
        ),
    )
    parser.add_argument("deck", type=Path)
    parser.add_argument(
        "--format",
        nargs="+",
        choices=["html", "pdf", "pptx", "png"],
        default=["html"],
        help="One or more output formats. Default: html. Example: --format html pptx",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path. Only valid when a single --format is given.",
    )
    parser.add_argument(
        "--with-mermaid",
        action="store_true",
        help="Inject mermaid.js CDN loader into HTML output so ```mermaid blocks render in browser.",
    )
    args = parser.parse_args()

    code = marp_build(args.deck, args.format, args.output, with_mermaid=args.with_mermaid)
    sys.exit(code)


if __name__ == "__main__":
    main()
