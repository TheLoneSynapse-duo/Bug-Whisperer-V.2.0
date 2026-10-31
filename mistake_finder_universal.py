#!/usr/bin/env python3
"""
mistake-finder universal - one command for any Python file.

Three modes:

  1. UNIVERSAL  (default) - point at any .py file, it auto-detects the library
     and runs mistake-box on it. No need to know which library you're using.

       python mistake_finder_universal.py mycode.py

  2. IDENTIFY  - tell it a file and it tells you what library it uses, plus
     the exact command to run to find mistakes in it.

       python mistake_finder_universal.py --identify mycode.py

  3. PER-LIBRARY  - if you already know the library, use the short form:

       python mistake_finder_universal.py --math mycode.py
       python mistake_finder_universal.py --pandas mycode.py
       python mistake_finder_universal.py --numpy mycode.py
       ... (see --help for the full list)

  4. DEMO  - run any of the built-in demo files to see the tool in action:

       python mistake_finder_universal.py --demo math
       python mistake_finder_universal.py --demo json
       ... (see --help for the full list)

It works with ANY Python code - not just the libraries it recognizes.
If it can't identify the library, it still runs mistake-box and catches errors.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Library detection signatures
# ---------------------------------------------------------------------------

LIBRARY_SIGNATURES: dict[str, list[str]] = {
    "math":        ["import math", "from math", "math.sqrt", "math.floor", "math.ceil", "math.pi", "math.e"],
    "json":        ["import json", "json.loads", "json.dumps", "json.load", "json.dump"],
    "numpy":       ["import numpy", "from numpy", "np.", "numpy.array", "numpy.zeros", "numpy.arange"],
    "pandas":      ["import pandas", "from pandas", "pd.", "pd.DataFrame", "pd.read_csv", "pd.Series"],
    "requests":    ["import requests", "requests.get", "requests.post", "requests.put", "requests.delete", "requests.head"],
    "bs4":         ["from bs4 import", "import bs4", "BeautifulSoup", "bs4.BeautifulSoup"],
    "pydantic":    ["from pydantic import", "import pydantic", "BaseModel", "Field(", " ValidationError"],
    "matplotlib":  ["import matplotlib", "matplotlib.pyplot", "plt.", "plt.plot", "plt.imshow", "plt.subplots", "import matplotlib.pyplot"],
    "seaborn":     ["import seaborn", "sns.", "sns.plot", "sns.histplot", "sns.scatterplot", "import seaborn as sns"],
    "sklearn":     ["import sklearn", "from sklearn", "sklearn.linear_model", "model.fit", "fit_predict", "train_test_split"],
    "sqlalchemy":  ["import sqlalchemy", "from sqlalchemy", "create_engine", "session.query", "Column(", "declarative_base"],
    "scipy":       ["import scipy", "from scipy", "scipy.linalg", "scipy.stats", "scipy.optimize", "scipy.signal"],
    "openpyxl":    ["from openpyxl import", "import openpyxl", "Workbook(", "openpyxl.Workbook"],
    "pillow":      ["from PIL import", "import PIL", "Image.open", "Image.new", "PIL.Image"],
    "tqdm":        ["from tqdm import", "import tqdm", "tqdm(", "tqdm(range"],
    "flask":       ["import flask", "from flask import", "Flask(", "@app.route", "flask.Flask"],
    "fastapi":     ["import fastapi", "from fastapi", "FastAPI(", "@app.get", "fastapi.FastAPI"],
    "django":      ["import django", "from django", "django.db", "models.Model", "@transaction.atomic"],
    "torch":       ["import torch", "from torch", "torch.tensor", "torch.nn", "torch.optim"],
    "tensorflow":  ["import tensorflow", "from tensorflow", "tf.", "tf.keras", "tf.constant"],
    "csv":         ["import csv", "csv.reader", "csv.writer", "csv.DictReader"],
    "sqlite3":     ["import sqlite3", "sqlite3.connect", "conn.cursor"],
    "pytest":      ["import pytest", "from pytest", "pytest.mark", "@pytest", "pytest.raises"],
    "unittest":    ["import unittest", "from unittest", "unittest.TestCase", "self.assert"],
    "numpy_dtype":  ["demos/demo_numpy_dtype.py"],
}

# Demo files bundled with the project
DEMOS: dict[str, str] = {
    "math":         "demos/demo_math.py",
    "json":         "demos/demo_json.py",
    "requests":     "demos/demo_requests.py",
    "numpy":        "demos/demo_numpy.py",
    "pandas":       "demos/demo_pandas.py",
    "pydantic":     "demos/demo_pydantic.py",
    "sklearn":      "demos/demo_sklearn.py",
    "sqlalchemy":   "demos/demo_sqlalchemy.py",
    "bs4":          "demos/demo_bs4.py",
    "openpyxl":     "demos/demo_openpyxl.py",
    "pillow":       "demos/demo_pillow.py",
    "scipy":        "demos/demo_scipy.py",
    "seaborn":      "demos/demo_seaborn.py",
    "matplotlib":   "demos/demo_matplotlib.py",
    "tqdm":         "demos/demo_tqdm.py",
    "numpy_dtype":  "demos/demo_numpy_dtype.py",
    "flask":        "demos/demo_flask.py",
    "fastapi":      "demos/demo_fastapi.py",
    "django":       "demos/demo_django.py",
    "torch":        "demos/demo_torch.py",
    "tensorflow":   "demos/demo_tensorflow.py",
    "csv":          "demos/demo_csv.py",
    "sqlite3":      "demos/demo_sqlite3.py",
}

# Test files (the working pytest versions)
TESTS: dict[str, str] = {
    "math":         "tests/test_demo_math.py",
    "json":         "tests/test_demo_json.py",
    "requests":     "tests/test_demo_requests.py",
    "numpy":        "tests/test_demo_numpy.py",
    "pandas":       "tests/test_demo_pandas.py",
    "pydantic":     "tests/test_demo_pydantic.py",
    "sklearn":      "tests/test_demo_sklearn.py",
    "sqlalchemy":   "tests/test_demo_sqlalchemy.py",
    "bs4":          "tests/test_demo_bs4.py",
    "openpyxl":     "tests/test_demo_openpyxl.py",
    "pillow":       "tests/test_demo_pillow.py",
    "scipy":        "tests/test_demo_scipy.py",
    "seaborn":      "tests/test_demo_seaborn.py",
    "matplotlib":   "tests/test_demo_matplotlib.py",
    "tqdm":         "tests/test_demo_tqdm.py",
    "numpy_dtype":  "tests/test_demo_numpy_dtype.py",
    "flask":        "tests/test_demo_flask.py",
    "fastapi":      "tests/test_demo_fastapi.py",
    "django":       "tests/test_demo_django.py",
    "torch":        "tests/test_demo_torch.py",
    "tensorflow":   "tests/test_demo_tensorflow.py",
    "csv":          "tests/test_demo_csv.py",
    "sqlite3":      "tests/test_demo_sqlite3.py",
}

# Per-library one-liner description
LIB_HELP: dict[str, str] = {
    "math":         "math - sqrt of negative, math domain errors",
    "json":         "json - single vs double quotes, JSONDecodeError",
    "requests":     "requests - missing https:// scheme, MissingSchema",
    "numpy":        "numpy - shape mismatch, array operations",
    "pandas":       "pandas - wrong column case, KeyError",
    "pydantic":     "pydantic - wrong data type, ValidationError",
    "sklearn":      "sklearn - 1D array to fit(), ValueError",
    "sqlalchemy":   "sqlalchemy - invalid DB URL, NoSuchModuleError",
    "bs4":          "bs4 - invalid parser name, FeatureNotFound",
    "openpyxl":     "openpyxl - invalid cell reference, ValueError",
    "pillow":       "pillow - opening missing file, FileNotFoundError",
    "scipy":        "scipy - inverting singular matrix, LinAlgError",
    "seaborn":      "seaborn - passing None data, ValueError",
    "matplotlib":   "matplotlib - invalid color name, ValueError",
    "tqdm":         "tqdm - iterating over None, TypeError",
    "numpy_dtype":  "numpy - dtype mismatches",
    "flask":        "flask - app context / routing mistakes",
    "fastapi":      "fastapi - path param validation errors",
    "django":       "django - settings / ORM setup errors",
    "torch":        "torch - device mismatch errors",
    "tensorflow":   "tensorflow - graph/shape errors",
    "csv":          "csv - parsing/format errors",
    "sqlite3":      "sqlite3 - SQL/connection errors",
}


def detect_library(filepath: Path) -> str | None:
    """Detect which library a Python file uses by scanning its imports."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return None

    best_lib: str | None = None
    best_score = 0

    for lib, sigs in LIBRARY_SIGNATURES.items():
        score = sum(1 for s in sigs if s.lower() in text)
        if score > best_score:
            best_score = score
            best_lib = lib

    return best_lib if best_score > 0 else None


def run_mistake_box(filepath: Path) -> int:
    """Run mistake-box on a file. Uses installed package or local script."""
    installed = True
    try:
        import mistake_finder  # noqa: F401
    except ImportError:
        installed = False

    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}

    if installed:
        cmd = [sys.executable, "-m", "mistake_finder.mistake_box", "python", str(filepath)]
        result = subprocess.run(cmd, env=env)
    else:
        local_box = Path(__file__).resolve().parent / ".bob" / "skills" / "mistake-finder" / "mistake_box.py"
        cmd = [sys.executable, str(local_box), "python", str(filepath)]
        result = subprocess.run(cmd, cwd=local_box.parent, env=env)
    return result.returncode


def run_pytest(test_file: Path) -> int:
    """Run pytest on a test file, letting the mistake-finder plugin box failures."""
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=short"],
        cwd=Path(__file__).resolve().parent,
        env=env,
    )
    return result.returncode


def cmd_universal(filepath: Path) -> int:
    """Universal mode: detect library, run mistake-box, report what was found."""
    lib = detect_library(filepath)
    if lib:
        print(f"  Detected library: {lib}")
    else:
        print("  No recognized library detected - running generic analysis anyway.")

    print(f"  File: {filepath}")
    print()
    return run_mistake_box(filepath)


def cmd_identify(filepath: Path) -> int:
    """Identify mode: tell the user what library the file uses and the command to run."""
    lib = detect_library(filepath)
    print()
    print("=")
    print("  CODE IDENTIFICATION")
    print("=" * 60)
    print(f"  File:    {filepath}")
    print()

    if lib:
        desc = LIB_HELP.get(lib, "")
        print(f"  Library: {lib}")
        if desc:
            print(f"  What:    {desc}")
        print()
        print("  Recommended command to find mistakes:")
        print()
        print(f"    python mistake_finder_universal.py --{lib} {filepath}")
        print()
        print("  Or use the universal command (auto-detects for you):")
        print()
        print(f"    python mistake_finder_universal.py {filepath}")
        print()
        if lib in TESTS:
            test_path = Path(TESTS[lib])
            if test_path.exists():
                print("  Matching test file (run with pytest):")
                print()
                print(f"    pytest {test_path} -v")
                print()
    else:
        print("  Could not identify a specific library.")
        print("  The file may use only standard library modules or an unrecognized library.")
        print()
        print("  You can still run the universal command - it catches all Python errors:")
        print()
        print(f"    python mistake_finder_universal.py {filepath}")
        print()

    print("=" * 60)
    return 0


def cmd_per_library(lib: str, filepath: Path) -> int:
    """Per-library mode: run mistake-box on a file for a specific library."""
    detected = detect_library(filepath)
    if detected and detected != lib:
        print(f"  Warning: detected '{detected}' but you specified '--{lib}'.")
        print(f"  Using '{lib}' as requested.")
    elif not detected:
        print(f"  No library detected - running --{lib} analysis anyway.")

    print(f"  Library: {lib}")
    print(f"  File:    {filepath}")
    print()
    return run_mistake_box(filepath)


def cmd_demo(lib: str) -> int:
    """Demo mode: run a bundled demo file."""
    demo_path = DEMOS.get(lib)
    if not demo_path:
        print(f"  Unknown demo: {lib}")
        print(f"  Available demos: {', '.join(sorted(DEMOS.keys()))}")
        return 1

    filepath = Path(__file__).resolve().parent / demo_path
    if not filepath.exists():
        print(f"  Demo file not found: {filepath}")
        return 1

    print(f"  Running demo: {lib}")
    print(f"  File: {filepath}")
    print()
    return run_mistake_box(filepath)


def cmd_run_tests(lib: str | None = None) -> int:
    """Run the pytest test suite for one or all libraries."""
    project_root = Path(__file__).resolve().parent

    if lib:
        test_path = project_root / TESTS.get(lib, "")
        if not test_path.exists():
            print(f"  No test file for '{lib}'.")
            print(f"  Available test libraries: {', '.join(sorted(TESTS.keys()))}")
            return 1
        print(f"  Running tests for: {lib}")
        print(f"  File: {test_path}")
        print()
        return run_pytest(test_path)
    else:
        print("  Running all tests...")
        print()
        return run_pytest(project_root / "tests")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mistake-finder",
        description="Universal mistake-finder - auto-detects your Python library and finds mistakes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  # Universal - auto-detects the library and runs analysis
  python mistake_finder_universal.py mycode.py

  # Identify - tell me what library this file uses
  python mistake_finder_universal.py --identify mycode.py

  # Per-library - you know the library already
  python mistake_finder_universal.py --pandas mycode.py
  python mistake_finder_universal.py --numpy mycode.py
  python mistake_finder_universal.py --requests mycode.py
  python mistake_finder_universal.py --pydantic mycode.py

  # Run a built-in demo to see the tool in action
  python mistake_finder_universal.py --demo math
  python mistake_finder_universal.py --demo json
  python mistake_finder_universal.py --demo pandas
  python mistake_finder_universal.py --demo flask
  python mistake_finder_universal.py --demo fastapi
  python mistake_finder_universal.py --demo django
  python mistake_finder_universal.py --demo torch
  python mistake_finder_universal.py --demo tensorflow
  python mistake_finder_universal.py --demo csv
  python mistake_finder_universal.py --demo sqlite3
  python mistake_finder_universal.py --demo pytest
  python mistake_finder_universal.py --demo unittest

  # Run tests for a specific library
  python mistake_finder_universal.py --test math
  python mistake_finder_universal.py --test pandas
  python mistake_finder_universal.py --test flask
  python mistake_finder_universal.py --test csv

  # Run all tests
  python mistake_finder_universal.py --test
""",
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="Python file to analyze (default: universal mode)",
    )

    parser.add_argument(
        "--identify",
        action="store_true",
        help="Identify the library in a file and show the right command to run",
    )

    parser.add_argument(
        "--demo",
        metavar="LIB",
        help="Run a built-in demo file (e.g. --demo math, --demo json)",
    )

    parser.add_argument(
        "--test",
        nargs="?",
        const="",
        metavar="LIB",
        help="Run pytest tests for a library, or all tests if no library given",
    )

    # Per-library flags
    for lib in sorted(LIBRARY_SIGNATURES.keys()):
        parser.add_argument(
            f"--{lib.replace('.', '_')}",
            nargs="?",
            metavar="FILE",
            help=f"Analyze a {lib} file (e.g. --{lib} mycode.py)",
        )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # --identify mode
    if args.identify:
        filepath = Path(args.file) if args.file else Path("mycode.py")
        if not filepath.is_file():
            print(f"  File not found: {filepath}")
            print("  Create a Python file and try again.")
            return 1
        return cmd_identify(filepath)

    # --demo mode
    if args.demo:
        return cmd_demo(args.demo)

    # --test mode
    if args.test is not None:
        lib = args.test if args.test else None
        return cmd_run_tests(lib)

    # Per-library flags: check which one was passed
    for lib in sorted(LIBRARY_SIGNATURES.keys()):
        flag_name = lib.replace(".", "_")
        val = getattr(args, flag_name, None)
        if val is not None:
            filepath = Path(val) if val else (Path(args.file) if args.file else Path("mycode.py"))
            if not filepath.is_file():
                print(f"  File not found: {filepath}")
                print(f"  Try: python mistake_finder_universal.py --{lib} <your-file.py>")
                return 1
            return cmd_per_library(lib, filepath)

    # Default: universal mode
    if not args.file:
        print()
        print("  Usage:")
        print()
        print("    python mistake_finder_universal.py <your-file.py>   # auto-detect + analyze")
        print("    python mistake_finder_universal.py --identify <file>  # identify the library")
        print("    python mistake_finder_universal.py --demo math       # run a demo")
        print("    python mistake_finder_universal.py --help            # see all options")
        print()
        print("  Or specify a library directly:")
        print()
        per_lib = [f"  --{lib} <file>" for lib in sorted(LIBRARY_SIGNATURES.keys())]
        for line in ["    " + ", ".join(per_lib[i:i+4]) for i in range(0, len(per_lib), 5)]:
            print(line)
        print()
        return 0

    filepath = Path(args.file)
    if not filepath.is_file():
        print(f"  File not found: {filepath}")
        return 1
    return cmd_universal(filepath)


if __name__ == "__main__":
    raise SystemExit(main())
