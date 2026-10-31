#!/usr/bin/env python3
"""smart_run.py - Auto-detect which library a file uses and run analysis.

This module intelligently detects which Python library a source file uses
and runs the appropriate mistake-finder analysis on it.

Usage:
    python smart_run.py <file.py>      # Auto-detect and analyze
    python smart_run.py                 # Auto-detect from current directory
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# Project root - defined at module level
PROJECT_ROOT = Path(__file__).resolve().parent

# Path to the local mistake_box.py (before installation)
LOCAL_MISTAKE_BOX = PROJECT_ROOT / ".bob" / "skills" / "mistake-finder" / "mistake_box.py"

# Check if the package is installed
try:
    import mistake_finder  # type: ignore[no-redef]
    INSTALLED = True
except ImportError:
    INSTALLED = False

# Base environment with PYTHONIOENCODING set to UTF-8
_ENCODING_ENV = {**{"PYTHONIOENCODING": "utf-8"}, **os.environ}


def detect_library(filepath: Path) -> str | None:
    """Detect which Python library a file uses based on imports and content."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return None

    # Map file content to library names
    library_signatures = {
        "math": ["import math", "from math", "math.sqrt", "math.floor"],
        "json": ["import json", "json.loads", "json.dumps"],
        "numpy": ["import numpy", "from numpy", "np.", "array(", "np.array"],
        "pandas": ["import pandas", "from pandas", "pd.", "DataFrame"],
        "requests": ["import requests", "requests.get", "requests.post"],
        "bs4": ["import bs4", "from bs4", "BeautifulSoup", "bs4"],
        "pydantic": ["import pydantic", "from pydantic", "BaseModel", "ValidationError"],
        "matplotlib": ["import matplotlib", "pyplot", "plt.", "plt.imshow"],
        "sklearn": ["import sklearn", "from sklearn", "model.fit", "fit_predict"],
        "sqlalchemy": ["import sqlalchemy", "create_engine", "session"],
    }

    for lib, signatures in library_signatures.items():
        if any(sig in text for sig in signatures):
            return lib
    return None


def run_mistake_box(filepath: Path) -> int:
    """Run mistake-box on the given file.

    Uses the installed package if available, otherwise runs the local script.
    Sets PYTHONIOENCODING to UTF-8 to avoid encoding issues.
    """
    if INSTALLED:
        # Use the installed package module
        cmd = [sys.executable, "-m", "mistake_finder.mistake_box", "python", str(filepath)]
        result = subprocess.run(cmd, cwd=PROJECT_ROOT, env=_ENCODING_ENV)
    else:
        # Run the local mistake_box.py from its directory
        cmd = [sys.executable, str(LOCAL_MISTAKE_BOX), "python", str(filepath)]
        result = subprocess.run(cmd, cwd=LOCAL_MISTAKE_BOX.parent, env=_ENCODING_ENV)
    return result.returncode


def index_code_files(root: Path | None = None) -> list[Path]:
    """Index all Python code files in the project, skipping known dirs."""
    if root is None:
        root = PROJECT_ROOT

    skip_dirs = {
        ".venv", "venv", "__pycache__", ".git", ".pytest_cache",
        ".freebuff", ".bob", "build", "dist",
        ".mypy_cache", ".ruff_cache", "site-packages",
    }

    files: list[Path] = []
    for dirpath, dirnames, filenames in root.walk():
        # Skip directories
        dirnames[:] = [d for d in dirnames if d not in skip_dirs and not d.startswith(".")]
        for name in filenames:
            if name.endswith(".py"):
                full = Path(dirpath) / name
                try:
                    if full.is_file():
                        files.append(full)
                except OSError:
                    pass

    return sorted(files, key=lambda p: p.name.lower())


def analyze_file(filepath: Path) -> dict:
    """Analyze a Python file and return findings."""
    if INSTALLED:
        cmd = [sys.executable, "-m", "mistake_finder.mistake_box", "python", str(filepath)]
        result = subprocess.run(cmd, cwd=PROJECT_ROOT, env=_ENCODING_ENV)
    else:
        cmd = [sys.executable, str(LOCAL_MISTAKE_BOX), "python", str(filepath)]
        result = subprocess.run(cmd, cwd=LOCAL_MISTAKE_BOX.parent, env=_ENCODING_ENV)

    return {
        "file": str(filepath),
        "stderr": result.stderr or "",
        "stdout": result.stdout or "",
        "returncode": result.returncode,
    }


def smart_run(filepath: str | Path | None = None) -> int:
    """Run smart analysis on a file or auto-detect from current directory."""
    if filepath is None:
        # Auto-detect Python files in current directory
        files = index_code_files(PROJECT_ROOT)

        # Skip known non-analysis files
        skip_names = {
            "find_mistakes.py", "smart_run.py", "voice_agent.py",
            "install_skill.py", "menu.py", "mycode.py"
        }
        files = [f for f in files if f.name not in skip_names and f.parent.name not in {".venv", "venv"}]

        if not files:
            print("No Python files found for analysis.")
            return 1

        print(f"Found {len(files)} Python file(s) to analyze.")
        for f in files[:5]:  # Limit output
            print(f"  - {f.name}")
        if len(files) > 5:
            print(f"  ... and {len(files) - 5} more.")

        # Run analysis on each
        for f in files:
            result = analyze_file(f)
            if result["returncode"] != 0 or result["stderr"].strip():
                print(f"\n  --- {f.name} ---")
                print(f"  Return code: {result['returncode']}")
                if result["stderr"].strip():
                    lines = result["stderr"].splitlines()[:5]
                    for line in lines:
                        print(f"  {line}")

        return 0

    # Analyze specific file
    filepath = Path(filepath)
    if not filepath.is_file():
        print(f"File not found: {filepath}")
        return 1

    # Detect library
    lib = detect_library(filepath)
    if lib:
        print(f"  Detected library: {lib}")

    # Run analysis
    result = analyze_file(filepath)

    print(f"\n  --- {filepath.name} ---")
    print(f"  Library: {lib or 'unknown'}")
    print(f"  Return code: {result['returncode']}")

    if result["stderr"].strip():
        lines = result["stderr"].splitlines()[:10]
        for line in lines:
            print(f"  {line}")

    if result["stdout"].strip():
        print(f"\n  stdout output:")
        for line in result["stdout"].splitlines()[:5]:
            print(f"  {line}")

    return result["returncode"]


def main() -> None:
    """Entry point."""
    import sys
    raise SystemExit(smart_run() if len(sys.argv) <= 1 else smart_run(sys.argv[1]))


if __name__ == "__main__":
    main()