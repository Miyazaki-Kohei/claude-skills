from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES_DIR = ROOT / "themes"
TEMPLATES_DIR = ROOT / "templates"

# Default output directory name (created under the project root passed via CLI)
DEFAULT_OUTPUT_DIR_NAME = "output"


def run(cmd: list[str], cwd: Path | None = None) -> int:
    print("$", " ".join(cmd))
    completed = subprocess.run(cmd, cwd=str(cwd) if cwd else None)
    return completed.returncode


def which(binary: str) -> str | None:
    return shutil.which(binary)


def available_templates() -> list[str]:
    return sorted(p.stem for p in TEMPLATES_DIR.glob("*.md"))


def available_themes() -> list[str]:
    return sorted(p.stem for p in THEMES_DIR.glob("*.css"))
