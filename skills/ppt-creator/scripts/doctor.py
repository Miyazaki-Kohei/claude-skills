from __future__ import annotations

import platform
import shutil
import subprocess

from .common import available_templates, available_themes

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
    print(f"  marp (via npx): run `npx @marp-team/marp-cli --version`")
    print()

    print(f"Themes: {', '.join(available_themes())}")
    print(f"Templates: {', '.join(available_templates())}")


if __name__ == "__main__":
    main()
