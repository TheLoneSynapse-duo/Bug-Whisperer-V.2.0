#!/usr/bin/env python3
"""find_mistakes.py - Smart runner for mistake-finder.

Automatically detects which Python file to analyse and runs the appropriate
mistake-finder tool (mistake-box or pytest) on it.

Usage:
    python find_mistakes.py              # Auto-detect and run on recent/modified files
    python find_mistakes.py <file>      # Run on specific file
    python find_mistakes.py --menu      # Show interactive menu
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


DEMO_FILES = [
    ("demos/demo_math.py",         "math       - sqrt of negative"),
    ("demos/demo_json.py",         "json       - single quotes vs double quotes"),
    ("demos/demo_numpy.py",        "numpy      - shape mismatch in array ops"),
    ("demos/demo_pandas.py",       "pandas     - wrong column case"),
    ("demos/demo_requests.py",     "requests   - missing https:// scheme"),
    ("demos/demo_bs4.py",          "bs4        - bad parser name"),
    ("demos/demo_pydantic.py",     "pydantic   - wrong data type"),
    ("demos/demo_matplotlib.py",   "matplotlib - invalid color name"),
    ("demos/demo_sklearn.py",      "sklearn    - 1D array to fit()"),
    ("demos/demo_sqlalchemy.py",   "sqlalchemy - bad database URL"),
    ("demos/demo_tqdm.py",         "tqdm       - can't iterate over None"),
    ("demos/demo_scipy.py",        "scipy      - singular matrix inversion"),
    ("demos/demo_seaborn.py",      "seaborn    - passing None as data"),
    ("demos/demo_openpyxl.py",     "openpyxl   - invalid cell reference"),
    ("demos/demo_pillow.py",       "pillow     - can't open non-existent file"),
    ("demos/demo_numpy_dtype.py",  "numpy_dtype - dtype mismatch"),
]

TEST_FILE_MAP: dict[str, str] = {
    "math": "tests/test_demo_math.py",
    "json": "tests/test_demo_json.py",
    "pandas": "tests/test_demo_pandas.py",
    "numpy": "tests/test_demo_numpy.py",
    "requests": "tests/test_demo_requests.py",
    "bs4": "tests/test_demo_bs4.py",
    "pydantic": "tests/test_demo_pydantic.py",
    "matplotlib": "tests/test_demo_matplotlib.py",
    "sklearn": "tests/test_demo_sklearn.py",
    "sqlalchemy": "tests/test_demo_sqlalchemy.py",
    "scipy": "tests/test_demo_scipy.py",
    "seaborn": "tests/test_demo_seaborn.py",
    "pillow": "tests/test_demo_pillow.py",
    "openpyxl": "tests/test_demo_openpyxl.py",
    "tqdm": "tests/test_demo_tqdm.py",
}


def show_menu() -> None:
    """Show interactive menu of files to check."""
    files = index_code_files(PROJECT_ROOT)

    print("\n" + "=" * 65)
    print("   MISTAKE-FINDER — Pick a file to check")
    print("=" * 65)

    # Show demo files
    print("\n  Demo files (intentional mistakes):")
    for i, (path, desc) in enumerate(DEMO_FILES):
        full = PROJECT_ROOT / path
        if full.exists():
            print(f"  [{i + 1:2}]  {path:30} — {desc}")

    # Show test files
    print("\n  Test files:")
    # Collect test files that exist
    test_entries: list[tuple[str, str]] = []
    for lib, test_path in TEST_FILE_MAP.items():
        full = PROJECT_ROOT / test_path
        if full.exists():
            test_entries.append((lib, test_path))

    test_idx = len([f for f in DEMO_FILES if (PROJECT_ROOT / f[0]).exists()]) + 1
    for lib, test_path in test_entries:
        print(f"  [{test_idx:2}]  {test_path:30} — {lib}")
        test_idx += 1

    print(f"  [ 0]  Exit")
    print("=" * 65)


def main(argv: list[str] | None = None) -> int:
    """Main entry point for find_mistakes.py."""
    if argv is None:
        argv = sys.argv[1:]

    if not argv or "--menu" in argv:
        show_menu()
        try:
            choice = input("\n  Enter number: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n  Bye!")
            return 0
        if not choice.isdigit():
            print("  Invalid choice.")
            return 1
        choice = int(choice)
        if choice == 0:
            print("  Bye!")
            return 0

        # Build list of all selectable files
        all_files: list[tuple[int, Path, str]] = []

        # Add demo files that exist
        for i, path in enumerate(DEMO_FILES):
            full = PROJECT_ROOT / path
            if full.exists():
                all_files.append((i + 1, full, "demo"))

        # Add test files
        test_no = len(all_files) + 1
        for lib, test_path in TEST_FILE_MAP.items():
            full = PROJECT_ROOT / test_path
            if full.exists():
                all_files.append((test_no, full, "test"))
                test_no += 1

        if 1 <= choice <= len(all_files):
            _, filepath, ftype = all_files[choice - 1]
            print(f"\n  >> Running mistake-finder on: {filepath}")
            if ftype == "demo":
                subprocess.run(
                    [sys.executable, str(PROJECT_ROOT / "mistake_box.py"), "python", str(filepath)],
                    cwd=PROJECT_ROOT,
                    env=_ENCODING_ENV,
                )
            else:
                subprocess.run(
                    [sys.executable, "-m", "pytest", str(filepath), "--no-mistake-box"],
                    cwd=PROJECT_ROOT,
                )
            input("\n  Press Enter to go back...")
        else:
            print(f"  Invalid choice. Please enter 0 or 1-{len(all_files)}.")

        return 0

    elif len(argv) >= 1:
        # Run on specific file given as argument
        filepath = Path(argv[0])
        if not filepath.is_file():
            print(f"  File not found: {filepath}")
            return 1

        # Try to auto-detect library
        lib = detect_library(filepath)
        if lib:
            print(f"  Detected library: {lib}")

        print(f"  >> Running mistake-finder on: {filepath}")
        # Run using the appropriate method
        if INSTALLED:
            cmd = [sys.executable, "-m", "mistake_finder.mistake_box", "python", str(filepath)]
            result = subprocess.run(cmd, cwd=PROJECT_ROOT, env=_ENCODING_ENV)
        else:
            cmd = [sys.executable, str(LOCAL_MISTAKE_BOX), "python", str(filepath)]
            result = subprocess.run(cmd, cwd=LOCAL_MISTAKE_BOX.parent, env=_ENCODING_ENV)

        # Print output
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)

    else:
        # Auto-detect mode - run on recognized library files
        files = index_code_files(PROJECT_ROOT)
        ran_any = False
        for filepath in files:
            lib = detect_library(filepath)
            if lib:
                print(f"Detected {lib} file: {filepath.name}")
                ret = run_mistake_box(filepath)
                ran_any = True
                if ret != 0:
                    print(f"  Found mistakes in {filepath.name}")

        if not ran_any:
            print("No recognized library files found auto-detecting.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())