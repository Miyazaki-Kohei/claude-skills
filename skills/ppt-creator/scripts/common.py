from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES_DIR = ROOT / "themes"

# Fixed theme: ppt-creator bundles the FJ Marp theme and does not expose
# theme variants. The full layout reference is references/sample-slide.md.
THEME_NAME = "fj"
THEME_FILE = THEMES_DIR / f"{THEME_NAME}.css"

# Default output directory name (created under the project root passed via CLI)
DEFAULT_OUTPUT_DIR_NAME = "output"


def run(cmd: list[str], cwd: Path | None = None) -> int:
    print("$", " ".join(cmd))
    completed = subprocess.run(cmd, cwd=str(cwd) if cwd else None)
    return completed.returncode


def which(binary: str) -> str | None:
    return shutil.which(binary)


