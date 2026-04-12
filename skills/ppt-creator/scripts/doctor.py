from __future__ import annotations

import platform
import shutil
import subprocess

from .common import THEME_FILE, THEME_NAME

TOOLS = [
    "python",
    "uv",
    "node",
    "npm",
    "marp",
]


def version(binary: str) -> str:
    path = shutil.which(binary)
    if not path:
        return "not found"
    try:
        out = subprocess.check_output(
            [binary, "--version"], text=True, stderr=subprocess.STDOUT
        ).strip()
        return out or path
    except Exception:
        return path


def main() -> None:
    print(f"Platform: {platform.platform()}")
    print()

    print("Tools:")
    for tool in TOOLS:
        print(f"  {tool}: {version(tool)}")
    print("  marp (via npx): run `npx @marp-team/marp-cli --version`")
    print()

    theme_status = "present" if THEME_FILE.exists() else "MISSING"
    print(f"Theme: {THEME_NAME} ({theme_status}) — {THEME_FILE}")
    print("Scaffold: embedded in scripts/new_deck.py")
    print()

    print("Optional:")
    mmdc = shutil.which("mmdc")
    print(f"  mmdc (mermaid-cli): {mmdc or 'not found — install for PPTX Mermaid rendering'}")


if __name__ == "__main__":
    main()
