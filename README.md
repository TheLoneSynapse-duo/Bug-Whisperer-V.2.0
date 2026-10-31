# 🐛 Bug Whisperer — Find Mistakes in Your Python Code

> **One tool. Two ways to use it. Zero dependencies. Works on any Python code.**

**Bug Whisperer** helps you find, understand, and fix mistakes in your Python code. It works in two ways:

1. **As a command-line tool and pytest plugin** — install with `pip install .` and get friendly boxed error reports instead of raw tracebacks, in any terminal or IDE, with zero configuration.
2. **As an AI-agent skill** — give it to any AI coding agent (Claude Code, Cursor, Codex, ChatGPT Codex, Devin, or any agent that can read files, run commands, and edit files). The skill tells the agent exactly how to investigate failing tests and review code, step by step, with evidence for every claim.

It is **IDE- and platform-agnostic**. It does not depend on any specific editor, AI provider, or cloud service. The core engine has **zero third-party dependencies**.

---

## 📖 Table of Contents

1. [What is this?](#-what-is-this)
2. [What does it do?](#-what-does-it-do)
3. [The 5 ways to use the tool](#-the-5-ways-to-use-the-tool)
4. [For Python learners](#-for-python-learners)
5. [Every command and what it does](#-every-command-and-what-it-does)
6. [Every library the tool knows about](#-every-library-the-tool-knows-about)
7. [Every demo file and what mistake it shows](#-every-demo-file-and-what-mistake-it-shows)
8. [Every test file and what it tests](#-every-test-file-and-what-it-tests)
9. [What do I need before I start?](#-what-do-i-need-before-i-start)
10. [Step 1 — Install the tool](#-step-1--install-the-tool)
11. [Step 2 — Use it in your Terminal (all modes)](#-step-2--use-it-in-your-terminal-all-modes)
12. [Step 3 — Use it with pytest](#-step-3--use-it-with-pytest)
13. [Step 4 — Use the universal command](#-step-4--use-the-universal-command-mistake_finder_universalpy)
14. [Step 5 — Add the skill to your AI agent](#-step-5--add-the-skill-to-your-ai-agent)
15. [Batch launchers — Windows quick buttons](#-batch-launchers--windows-quick-buttons)
16. [How the AI agent skill works](#how-the-ai-agent-skill-works)
17. [Example: What the output looks like](#-example-what-the-output-looks-like)
18. [Troubleshooting](#-troubleshooting)
19. [Project File Map](#-project-file-map)
20. [Is it safe to use on my real code?](#is-it-safe-to-use-on-my-real-code)
21. [About this project](#about-this-project)

---

## 🤔 What is this?

**Bug Whisperer** is a tool that reads your Python code and tells you exactly **what went wrong**, **where it went wrong**, and **how to fix it** — in simple, friendly language.

Think of it like a helpful teacher looking over your shoulder while you code. When something breaks, instead of seeing a scary red error message, you see a neat box that says:

- 📍 **WHERE** the mistake is (exact file and line number)
- ❌ **WHAT WENT WRONG** (explained in plain English)
- 💡 **SUGGESTIONS** (step-by-step tips to fix it)

---

## ✨ What does it do?

### Mode 1 — Triage Failing Tests 🔴→🟢

When your tests are failing (showing red errors), Bug Whisperer helps an agent:

1. Look at every failing test at the same time (in parallel)
2. Figure out the root cause of each failure, with file:line evidence
3. Propose the smallest possible fix for each one
4. Apply one fix at a time and verify it — rolling back anything that fails, and stopping for human review when it cannot auto-repair

### Mode 2 — Review Your Code 🔍

When you just wrote some code and want a second opinion, Bug Whisperer:

1. Checks for logic errors and edge cases
2. Checks for security issues
3. Checks for missing error handling
4. Gives you a ranked list of findings with evidence

### Mode 3 — Run Your Code and Catch Errors 💻

Drop any Python file on the tool and it runs it, catches any error, and shows it in a friendly box:

```bash
mistake-box python mycode.py
```

### Mode 4 — Identify What Library Your Code Uses 🕵️

Point the universal command at any `.py` file and it tells you which library it uses, plus the exact command to run to find mistakes in it:

```bash
python mistake_finder_universal.py --identify mycode.py
```

### Mode 5 — Run Built-in Demos 🎓

See the tool in action on any of the 16 built-in demo files, each with one intentional mistake:

```bash
python mistake_finder_universal.py --demo math
python mistake_finder_universal.py --demo pandas
```

---

## 🎓 The 5 ways to use the tool

| # | Way | When to use it | Command |
|---|-----|----------------|---------|
| 1 | **mistake-box CLI** | You have a Python file and want to run it, catching errors in a box | `mistake-box python mycode.py` |
| 2 | **pytest plugin** | You run tests and want failing ones boxed automatically | `pytest` (after `pip install .`) |
| 3 | **universal command** | You have any `.py` file — it auto-detects the library and runs analysis | `python mistake_finder_universal.py mycode.py` |
| 4 | **identify mode** | You want to know what library a file uses before running it | `python mistake_finder_universal.py --identify mycode.py` |
| 5 | **per-library command** | You already know the library — skip detection | `python mistake_finder_universal.py --pandas mycode.py` |
| 6 | **demo mode** | You want to see the tool work on a built-in example | `python mistake_finder_universal.py --demo math` |
| 7 | **test mode** | You want to run the pytest test suite for one or all libraries | `python mistake_finder_universal.py --test` |
| 8 | **interactive menu** | You want a menu to pick what to run | `python menu.py` |
| 9 | **smart runner** | You want auto-detection from the current directory | `python smart_run.py` or `python smart_run.py mycode.py` |
| 10 | **global skill install** | You want the AI-agent skill available in every project | `python install_skill.py` |

---

## 📋 Every command and what it does

### 1. `mistake-box` — the main CLI command

Installed by `pip install .`. Runs any Python command and catches errors.

```bash
# Run a Python file and box any error
mistake-box python mycode.py

# Syntax-check a file without running it
mistake-box --file mycode.py

# Parse an existing log/error file
mistake-box --log ci.log

# Use plain ASCII box (no Unicode box-drawing characters)
mistake-box --ascii python mycode.py

# Show the original raw error too
mistake-box --raw python mycode.py

# Turn off the box globally
set MISTAKE_BOX=0      # Windows
export MISTAKE_BOX=0   # Mac/Linux
```

### 2. `pytest` — the pytest plugin

Installed by `pip install .` as a `pytest11` entry point. Boxes every failing test automatically.

```bash
# Run all tests — failing ones get boxed
pytest

# Run without the boxes
pytest --no-mistake-box

# Run a specific test file
pytest tests/test_demo_math.py -v

# Run one library's tests
pytest tests/test_demo_pandas.py -v
```

### 3. `mistake_finder_universal.py` — the universal command

One command for any Python file. **5 modes:**

| Mode | Command | What it does |
|------|---------|-------------|
| **Universal** (default) | `python mistake_finder_universal.py mycode.py` | Auto-detects the library, runs mistake-box, catches errors |
| **Identify** | `python mistake_finder_universal.py --identify mycode.py` | Tells you what library the file uses + the exact command to run + matching test file |
| **Per-library** | `python mistake_finder_universal.py --pandas mycode.py` | You know the library, skip detection — 25 libraries supported |
| **Demo** | `python mistake_finder_universal.py --demo math` | Runs a built-in demo file so you can see the tool in action |
| **Test** | `python mistake_finder_universal.py --test` or `--test pandas` | Runs pytest for one or all libraries |

Run `python mistake_finder_universal.py --help` for the full list of per-library flags.

### 4. `--identify` mode — code identification

When you give it a file, it:

1. Reads the file's imports and content
2. Matches them against 25 known library signatures
3. Prints: **Library detected**, **What mistake patterns to watch for**, **The exact command to run**, and **The matching test file** (if one exists)

```bash
$ python mistake_finder_universal.py --identify mycode.py

============================================================
  CODE IDENTIFICATION
============================================================
  File:    mycode.py

  Library: pandas
  What:    pandas - wrong column case, KeyError

  Recommended command to find mistakes:

    python mistake_finder_universal.py --pandas mycode.py

  Or use the universal command (auto-detects for you):

    python mistake_finder_universal.py mycode.py

  Matching test file (run with pytest):

    pytest tests/test_demo_pandas.py -v
============================================================
```

### 5. Per-library commands — 25 libraries

If you already know which library your code uses, use the per-library flag to skip detection:

```bash
python mistake_finder_universal.py --math mycode.py
python mistake_finder_universal.py --json mycode.py
python mistake_finder_universal.py --numpy mycode.py
python mistake_finder_universal.py --pandas mycode.py
python mistake_finder_universal.py --requests mycode.py
python mistake_finder_universal.py --bs4 mycode.py
python mistake_finder_universal.py --pydantic mycode.py
python mistake_finder_universal.py --matplotlib mycode.py
python mistake_finder_universal.py --seaborn mycode.py
python mistake_finder_universal.py --sklearn mycode.py
python mistake_finder_universal.py --sqlalchemy mycode.py
python mistake_finder_universal.py --scipy mycode.py
python mistake_finder_universal.py --openpyxl mycode.py
python mistake_finder_universal.py --pillow mycode.py
python mistake_finder_universal.py --tqdm mycode.py
python mistake_finder_universal.py --numpy_dtype mycode.py
python mistake_finder_universal.py --tensorflow mycode.py
python mistake_finder_universal.py --torch mycode.py
python mistake_finder_universal.py --django mycode.py
python mistake_finder_universal.py --flask mycode.py
python mistake_finder_universal.py --fastapi mycode.py
python mistake_finder_universal.py --pytest mycode.py
python mistake_finder_universal.py --unittest mycode.py
python mistake_finder_universal.py --csv mycode.py
python mistake_finder_universal.py --sqlite3 mycode.py
```

Even if detection fails, the per-library command still runs mistake-box and catches errors.

### 6. `--demo` mode — 16 built-in demos

```bash
python mistake_finder_universal.py --demo math
python mistake_finder_universal.py --demo json
python mistake_finder_universal.py --demo requests
python mistake_finder_universal.py --demo numpy
python mistake_finder_universal.py --demo pandas
python mistake_finder_universal.py --demo pydantic
python mistake_finder_universal.py --demo sklearn
python mistake_finder_universal.py --demo sqlalchemy
python mistake_finder_universal.py --demo bs4
python mistake_finder_universal.py --demo openpyxl
python mistake_finder_universal.py --demo pillow
python mistake_finder_universal.py --demo scipy
python mistake_finder_universal.py --demo seaborn
python mistake_finder_universal.py --demo matplotlib
python mistake_finder_universal.py --demo tqdm
python mistake_finder_universal.py --demo numpy_dtype
```

Each demo runs a file with one intentional mistake and shows the boxed error.

### 7. `--test` mode — run the test suite

```bash
# Run all tests (30 tests across 15 libraries)
python mistake_finder_universal.py --test

# Run tests for one library
python mistake_finder_universal.py --test math
python mistake_finder_universal.py --test pandas
python mistake_finder_universal.py --test requests
```

### 8. `menu.py` — interactive menu

```bash
python menu.py
```

Shows a menu where you can pick: run a demo, run tests for a library, run the universal command on mycode.py, or run the identify command.

### 9. `smart_run.py` — smart runner

```bash
# Auto-detect Python files in the current directory and analyze each
python smart_run.py

# Analyze a specific file (detects library automatically)
python smart_run.py mycode.py
```

### 10. `install_skill.py` — global skill installer

```bash
# Install the skill globally (~/.bob/skills/mistake-finder/)
python install_skill.py

# Check install status
python install_skill.py --check

# Remove the global install
python install_skill.py --remove
```

---

## 📚 Every library the tool knows about

The universal command (`mistake_finder_universal.py`) detects **25 libraries** by scanning file imports and content:

| Library | What it detects | Common mistake it catches |
|---------|----------------|---------------------------|
| `math` | `import math`, `math.sqrt`, `math.floor` | sqrt of negative → ValueError (math domain error) |
| `json` | `import json`, `json.loads`, `json.dumps` | Single quotes in JSON → JSONDecodeError |
| `numpy` | `import numpy`, `np.`, `numpy.array` | Shape mismatch when adding arrays → ValueError |
| `pandas` | `import pandas`, `pd.`, `pd.DataFrame` | Wrong column case → KeyError |
| `requests` | `import requests`, `requests.get` | Missing `https://` scheme → MissingSchema |
| `bs4` | `from bs4 import`, `BeautifulSoup` | Invalid parser name → FeatureNotFound |
| `pydantic` | `from pydantic import`, `BaseModel` | Wrong data type → ValidationError |
| `matplotlib` | `import matplotlib`, `plt.`, `plt.plot` | Invalid color name → ValueError |
| `seaborn` | `import seaborn`, `sns.` | Passing None data → ValueError |
| `sklearn` | `import sklearn`, `model.fit` | 1D array to fit() → ValueError |
| `sqlalchemy` | `import sqlalchemy`, `create_engine` | Invalid DB URL → NoSuchModuleError |
| `scipy` | `import scipy`, `scipy.linalg` | Inverting singular matrix → LinAlgError |
| `openpyxl` | `from openpyxl import`, `Workbook(` | Invalid cell reference → ValueError |
| `pillow` | `from PIL import`, `Image.open` | Opening missing file → FileNotFoundError |
| `tqdm` | `from tqdm import`, `tqdm(` | Iterating over None → TypeError |
| `numpy_dtype` | `np.dtype` | dtype mismatches with Python lists |
| `tensorflow` | `import tensorflow`, `tf.` | Graph/shape errors |
| `torch` | `import torch`, `torch.tensor` | Tensor shape/device errors |
| `django` | `import django`, `models.Model` | ORM/validation errors |
| `flask` | `import flask`, `Flask(` | Routing/context errors |
| `fastapi` | `import fastapi`, `FastAPI(` | Endpoint/validation errors |
| `pytest` | `import pytest`, `pytest.raises` | Assertion/test errors |
| `unittest` | `import unittest`, `TestCase` | Assertion errors |
| `csv` | `import csv`, `csv.reader` | Parsing/format errors |
| `sqlite3` | `import sqlite3`, `sqlite3.connect` | SQL/connection errors |

**If the tool can't identify the library**, it still runs mistake-box and catches all Python errors — it just won't have a library-specific description.

---

## 📂 Every demo file and what mistake it shows

The `demos/` folder has **16 demo files**, each with **one intentional mistake** and the correct version commented out:

| Demo file | Library | The mistake | What you learn |
|-----------|---------|-------------|----------------|
| `demos/demo_math.py` | `math` | `math.sqrt(-9)` — square root of a negative number | Why you can't take sqrt of a negative number (ValueError: math domain error) |
| `demos/demo_json.py` | `json` | `json.loads("{'name': 'Alice'}")` — single quotes | Why JSON requires double quotes, not single quotes (JSONDecodeError) |
| `demos/demo_requests.py` | `requests` | `requests.get("google.com")` — no https:// | Why URLs need an `https://` scheme (MissingSchema) |
| `demos/demo_numpy.py` | `numpy` | `np.array([1,2,3]) + np.array([1,2])` — shape mismatch | Why arrays must have the same shape to add them (ValueError) |
| `demos/demo_pandas.py` | `pandas` | `df["names"]` when column is `"Names"` — wrong case | Why column names are case-sensitive (KeyError) |
| `demos/demo_pydantic.py` | `pydantic` | `User(age="not-a-number")` — string where int expected | Why Pydantic rejects the wrong data type (ValidationError) |
| `demos/demo_sklearn.py` | `sklearn` | `model.fit(np.array([1,2,3]), ...)` — 1D array | Why scikit-learn needs 2D arrays, not 1D (ValueError) |
| `demos/demo_sqlalchemy.py` | `sqlalchemy` | `create_engine("notavalidurl://")` — bad URL | Why database URLs must follow a specific format (NoSuchModuleError) |
| `demos/demo_bs4.py` | `bs4` | `BeautifulSoup(html, "notaparser")` — fake parser | Why BeautifulSoup needs a real parser name (FeatureNotFound) |
| `demos/demo_openpyxl.py` | `openpyxl` | `ws["ZZZZ99999"] = "Hello"` — invalid cell | Why Excel cell references must be valid (ValueError) |
| `demos/demo_pillow.py` | `pillow` | `Image.open("ghost.png")` — file doesn't exist | Why you can't open a file that doesn't exist (FileNotFoundError) |
| `demos/demo_scipy.py` | `scipy` | `inv([[1,2],[2,4]])` — singular matrix | Why some matrices can't be inverted (LinAlgError) |
| `demos/demo_seaborn.py` | `seaborn` | `sns.histplot(data=None, x="col")` — None data | Why seaborn can't plot None data (ValueError) |
| `demos/demo_matplotlib.py` | `matplotlib` | `ax.plot(..., color="notacolor")` — bad color | Why matplotlib rejects invalid color names (ValueError) |
| `demos/demo_tqdm.py` | `tqdm` | `for item in tqdm(None)` — None is not iterable | Why you can't iterate over None (TypeError) |
| `demos/demo_numpy_dtype.py` | `numpy_dtype` | `np.dtype([('f8', float), ('i4', int)])` — dtype with list | Why dtype mismatches happen with Python lists vs numpy arrays |

**How to run a demo:**

```bash
# Using mistake-box directly
mistake-box python demos/demo_math.py

# Using the universal command
python mistake_finder_universal.py demos/demo_math.py

# Using the demo mode
python mistake_finder_universal.py --demo math

# Using the batch launcher
run.bat demos/demo_math.py
```

Each demo shows you:
1. The **wrong code** (with a comment explaining what's wrong)
2. The **error** (parsed and explained in a box)
3. The **correct code** (with a comment showing the fix)

Read the wrong code, predict what error you'll get, then run it and check your answer against the box.

---

## 🧪 Every test file and what it tests

The `tests/` folder has **15 pytest test files** (properly named `test_demo_*.py` to avoid conflicts with stdlib module names). Each has **2 tests**: one that demonstrates the mistake (using `pytest.raises`) and one that shows the correct version passing.

| Test file | Library | Test 1 (mistake) | Test 2 (correct) |
|-----------|---------|------------------|-------------------|
| `tests/test_demo_math.py` | `math` | `test_sqrt_negative_raises_valueerror` — `math.sqrt(-9)` raises ValueError | `test_sqrt_positive_works` — `math.sqrt(9) == 3.0` |
| `tests/test_demo_json.py` | `json` | `test_json_single_quotes_fail` — `json.loads("{'name': 'Alice'}")` raises JSONDecodeError | `test_json_double_quotes_work` — double-quoted JSON parses correctly |
| `tests/test_demo_requests.py` | `requests` | `test_requests_missing_schema` — `requests.get("google.com")` raises MissingSchema | `test_requests_with_scheme_works` — correct URL is accepted |
| `tests/test_demo_numpy.py` | `numpy` | `test_numpy_shape_mismatch` — arrays of different shape raise ValueError | `test_numpy_same_shape_works` — same-shape arrays add correctly |
| `tests/test_demo_pandas.py` | `pandas` | `test_pandas_wrong_case_column` — `df["age"]` raises KeyError | `test_pandas_correct_case_column` — `df["Age"]` works |
| `tests/test_demo_pydantic.py` | `pydantic` | `test_pydantic_wrong_type_raises` — `age="not-a-number"` raises ValidationError | `test_pydantic_correct_type_works` — `age=25` works |
| `tests/test_demo_sklearn.py` | `sklearn` | `test_sklearn_1d_array_fails` — 1D array to fit() raises ValueError | `test_sklearn_2d_array_works` — reshaped 2D array works |
| `tests/test_demo_sqlalchemy.py` | `sqlalchemy` | `test_sqlalchemy_bad_url_raises` — invalid URL raises NoSuchModuleError | `test_sqlalchemy_good_url_works` — `sqlite:///` URL works |
| `tests/test_demo_bs4.py` | `bs4` | `test_bs4_bad_parser_raises` — `"notaparser"` raises FeatureNotFound | `test_bs4_good_parser_works` — `"html.parser"` works |
| `tests/test_demo_openpyxl.py` | `openpyxl` | `test_openpyxl_bad_cell_raises` — `"ZZZZ99999"` raises ValueError | `test_openpyxl_good_cell_works` — `"A1"` works |
| `tests/test_demo_pillow.py` | `pillow` | `test_pillow_missing_file_raises` — `Image.open("ghost.png")` raises FileNotFoundError | `test_pillow_create_image_works` — `Image.new()` works |
| `tests/test_demo_scipy.py` | `scipy` | `test_scipy_singular_matrix_raises` — singular matrix raises LinAlgError | `test_scipy_non_singular_works` — non-singular matrix inverts |
| `tests/test_demo_seaborn.py` | `seaborn` | `test_seaborn_none_data_raises` — `data=None` raises ValueError | `test_seaborn_real_data_works` — real DataFrame works |
| `tests/test_demo_matplotlib.py` | `matplotlib` | `test_matplotlib_bad_color_raises` — `"notacolor"` raises ValueError | `test_matplotlib_good_color_works` — `"blue"` works |
| `tests/test_demo_tqdm.py` | `tqdm` | `test_tqdm_none_iterable_raises` — `tqdm(None)` raises TypeError | `test_tqdm_real_iterable_works` — `tqdm(range(5))` works |

**Run the tests:**

```bash
# Run all tests (30 tests, 2 per library)
pytest

# Run one library's tests
pytest tests/test_demo_math.py -v

# Run with the mistake-box plugin (default — boxes failures)
pytest

# Run without the boxes
pytest --no-mistake-box
```

---

## 🎓 For Python learners

Learning Python? Bug Whisperer is built for you. Here's how to use it to learn faster:

### The demo files are learning exercises

The `demos/` folder has 16 Python demo files, each with **one intentional mistake**. Run them and read the box — you'll learn what different errors look like.

### How to practice

```bash
# Run a demo and see the mistake explained
mistake-box python demos/demo_math.py

# Or check a file for syntax errors without running it
mistake-box --file demos/demo_json.py

# Run all the demos through the interactive menu
python menu.py

# Use the universal command
python mistake_finder_universal.py demos/demo_pandas.py

# Use the per-library command
python mistake_finder_universal.py --pandas demos/demo_pandas.py
```

Each demo shows you:
1. The **wrong code** (with a comment explaining what's wrong)
2. The **error** (parsed and explained in a box)
3. The **correct code** (with a comment showing the fix)

Read the wrong code, predict what error you'll get, then run it and check your answer against the box.

---

## 📋 What do I need before I start?

You need **2 things** installed on your computer:

| Thing | What it is | Where to get it |
|-------|-----------|-----------------|
| **Python 3.8 or newer** | The programming language this tool uses | [python.org/downloads](https://python.org/downloads) |
| **Git** (optional) | A tool to download code from GitHub | [git-scm.com](https://git-scm.com/downloads) |

> 💡 **Not sure if you have Python?** Open a terminal (Command Prompt on Windows) and type:
> ```
> python --version
> ```
> If you see something like `Python 3.11.0` — you're good! If you see an error, install Python from [python.org/downloads](https://python.org/downloads).

> 💡 **Not sure if you have pip?** Try `python -m pip --version`. If that fails, reinstall Python and make sure to check **"Add Python to PATH"** during installation.

---

## 📦 Step 1 — Install the tool

### Option A — Install from GitHub (recommended)

Open your terminal and run:

```bash
git clone https://github.com/your-username/Bug-Whisperer.git
cd Bug-Whisperer
pip install .
```

> **Note:** Replace `your-username` with your actual GitHub username before running this command.

### Option B — Install from a local copy

If you've already downloaded the project folder, open a terminal in that folder and run:

```bash
pip install .
```

> This command reads the project and installs everything automatically. It takes about 10–30 seconds.

**What this does:**
- Installs a command called `mistake-box` that you can use anywhere
- Installs a pytest plugin that automatically shows errors in a friendly box every time you run tests

> ✅ If you see `Successfully installed mistake-finder-1.0.0`, installation was successful!

---

## 💻 Step 2 — Use it in your Terminal (all modes)

You don't need any special IDE to use this tool. Open any terminal and try it.

### Mode A — Run your code and see errors in a friendly box (mistake-box CLI)

```bash
mistake-box python mycode.py
```

Instead of a raw Python traceback, you'll see a neat box like this:

```
╔══════════════════════════════════════════════════════════════╗\n║ MISTAKE FOUND - SyntaxError                                  ║\n╠══════════════════════════════════════════════════════════════╣\n║ WHERE                                                        ║\n║   mycode.py:12                                               ║\n║ >>  12 |     if x = 5:                                       ║\n║               ^                                              ║\n╠══════════════════════════════════════════════════════════════╣\n║ WHAT WENT WRONG                                              ║\n║   SyntaxError: invalid syntax. Maybe you meant '==' or ':='? ║\n╠══════════════════════════════════════════════════════════════╣\n║ SUGGESTIONS                                                  ║\n║   1. A single `=` assigns; use `==` to compare.              ║\n╚══════════════════════════════════════════════════════════════╝
```

### Mode B — Check a file for syntax errors without running it

```bash
mistake-box --file mycode.py
```

### Mode C — Parse an existing log/error file

```bash
mistake-box --log ci.log
```

### Mode D — Use plain ASCII box (no Unicode)

```bash
mistake-box --ascii python mycode.py
```

Or set it as the default:

```bash
set MISTAKE_BOX_ASCII=1      # Windows
export MISTAKE_BOX_ASCII=1   # Mac/Linux
```

### Mode E — Show the original raw error too

```bash
mistake-box --raw python mycode.py
```

### Mode F — Turn off the box globally (advanced)

```bash
set MISTAKE_BOX=0      # Windows
export MISTAKE_BOX=0   # Mac/Linux
```

### Mode G — The universal command (auto-detect + analyze)

```bash
python mistake_finder_universal.py mycode.py
```

This auto-detects which library your file uses, then runs mistake-box on it. No need to know which library you're using.

### Mode H — Identify what library a file uses

```bash
python mistake_finder_universal.py --identify mycode.py
```

This tells you:
- What library the file uses
- What mistake patterns to watch for
- The exact command to run to find mistakes
- The matching test file (if one exists)

### Mode I — Per-library command (you know the library)

```bash
python mistake_finder_universal.py --pandas mycode.py
python mistake_finder_universal.py --numpy mycode.py
python mistake_finder_universal.py --requests mycode.py
# ... 25 libraries supported, see --help for the full list
```

### Mode J — Run a built-in demo

```bash
python mistake_finder_universal.py --demo math
python mistake_finder_universal.py --demo pandas
# ... 16 demos available
```

### Mode K — Run the test suite

```bash
python mistake_finder_universal.py --test          # all tests
python mistake_finder_universal.py --test pandas   # one library
```

### Mode L — Interactive menu

```bash
python menu.py
```

Pick from: run a demo, run tests for a library, run universal on mycode.py, or run identify.

### Mode M — Smart runner

```bash
python smart_run.py              # auto-detect files in current directory
python smart_run.py mycode.py   # analyze a specific file
```

---

## 🧪 Step 3 — Use it with pytest

Once installed, the pytest plugin works automatically. Every time you run `pytest`, any failing tests are shown as friendly boxes.

```bash
# Run your tests — failing ones get boxed automatically
pytest

# Run tests without the boxes
pytest --no-mistake-box

# Run a specific test file
pytest tests/test_demo_math.py -v

# Run one library's tests
pytest tests/test_demo_pandas.py -v
```

The `tests/` folder has 15 pytest test files, one per popular Python library. Each has an intentional mistake — run them to see how the pytest plugin works.

```bash
# Run all tests and see every mistake in a box
pytest

# Run just one library's test
pytest tests/test_demo_json.py -v
```

---

## 🤖 Step 4 — Use the universal command (`mistake_finder_universal.py`)

This is the **one-command-does-everything** tool. Drop any `.py` file on it and it figures out the rest.

### Universal mode (default)

```bash
python mistake_finder_universal.py mycode.py
```

It:
1. Reads your file
2. Detects which library it uses (from 25 known libraries)
3. Runs mistake-box on it
4. Catches and boxes any error

If it can't identify the library, it still runs mistake-box and catches all Python errors.

### Identify mode

```bash
python mistake_finder_universal.py --identify mycode.py
```

It tells you:
- What library the file uses
- What mistake patterns to watch for
- The exact command to run to find mistakes
- The matching test file (if one exists)

### Per-library mode

```bash
python mistake_finder_universal.py --pandas mycode.py
```

25 libraries supported. Use `python mistake_finder_universal.py --help` to see them all.

### Demo mode

```bash
python mistake_finder_universal.py --demo math
```

16 demos available. See `--help` for the list.

### Test mode

```bash
python mistake_finder_universal.py --test          # all 30 tests
python mistake_finder_universal.py --test pandas   # one library
```

---

## 🤖 Step 5 — Add the skill to your AI agent

Bug Whisperer includes an **AI-agent skill** — a set of instructions that tell any AI coding agent exactly how to find and fix mistakes in your code.

### What is an AI agent skill?

An AI agent skill is a file (usually `SKILL.md`) that you give to your AI coding agent. When you ask the agent to "fix my failing tests" or "review my code", the agent reads the skill file and follows its instructions. The skill tells the agent:

- How to investigate failing tests systematically
- How to trace errors back to their root cause
- How to propose minimal fixes and verify them
- How to review code for common mistake patterns
- What rules to follow (never weaken tests, always provide evidence, etc.)

### How to add the skill to your agent

The skill lives in `.bob/skills/mistake-finder/`. The folder name comes from the original design, but the skill itself is **IDE-agnostic** — you can use it with any AI agent.

**Option A — Project-scoped (recommended for learning)**

Keep the skill in your project's `.bob/skills/mistake-finder/` folder. When you ask your AI agent to work on this project, tell it:

> "Use the mistake-finder skill in `.bob/skills/mistake-finder/SKILL.md` to help with this task."

The agent reads the skill and follows it.

**Option B — Global install (works in every project)**

```bash
python install_skill.py
```

This copies the skill to `~/.bob/skills/mistake-finder/` so it's available in every project you work on.

To check if it worked:

```bash
python install_skill.py --check
```

To remove it later:

```bash
python install_skill.py --remove
```

### What to ask your AI agent

Once the skill is available, talk to your agent naturally:

**If your tests are failing:**

```
Run mistake-finder on the failing tests.
```

**If you just wrote some code and want it reviewed:**

```
Check my code for mistakes.
```

**To review a specific file:**

```
Check src/myfile.py for mistakes.
```

**If you have a log file from a CI/CD pipeline:**

```
Run mistake-finder on artifacts/ci.log.
```

---

## 🧠 How the AI agent skill works

The skill (`SKILL.md`) defines a four-phase workflow that any AI agent can follow. Here's what happens behind the scenes:

### Phase 0 — Understand the situation

The agent figures out:
- What language and test runner the project uses
- Which tests are failing (from actual test output, not memory)
- Or, for code review, which files to inspect

### Phase 1 — Fan out investigation

The agent splits the work into parallel investigations:

- **For failing tests**: one investigation per failing test (or per group of related failures). Each investigation traces from the failing assertion back to the line of code that caused it.
- **For code review**: one investigation per mistake class (logic errors, error handling, security issues, performance problems, etc.). Each investigation checks the code for that specific kind of mistake.

### Phase 2 — Aggregate findings

The agent combines all investigations into one ranked report:
- Most severe findings first (correctness and security issues before style)
- Every finding has a `file:line` pointer to the evidence
- Conflicting findings are surfaced, not silently resolved

### Phase 3 — Fix loop (for failing tests, with rollback)

The agent works through the ranked list, one fix at a time, and **never edits test files, never weakens assertions, and never skips a failing test**:
1. Apply one minimal fix to source code only
2. Re-run the affected test
3. If it passes → move on
4. If it fails → revert the fix and flag the row for human review
5. Stop when everything is resolved or two attempts on the same row have failed

### Phase 4 — Verify and report

The agent runs the full test suite one more time and produces a final summary:
- What was found
- What was fixed
- What was rolled back (needs human review)
- Recall rate (fixed / total failures)

---

## 🖼️ Example: What the output looks like

Here's a real example. Imagine your test file has this failing test:

```python
def test_add():
    assert add(2, 3) == 5   # but add() returns -1 by mistake
```

Running `pytest` will now show:

```
╔════════════════════════════════════════════════════════════════╗\n║ MISTAKE FOUND - AssertionError                                 ║\n╠════════════════════════════════════════════════════════════════╣\n║ TEST                                                           ║\n║   tests/test_calc.py::test_add                                 ║\n╠════════════════════════════════════════════════════════════════╣\n║ WHERE                                                          ║\n║   tests/test_calc.py:5                                         ║\n║      4 | def test_add():                                       ║\n║ >>   5 |     assert add(2, 3) == 5                             ║\n╠════════════════════════════════════════════════════════════════╣\n║ WHAT WENT WRONG                                                ║\n║   AssertionError: assert -1 == 5  (where -1 = add(2, 3))      ║\n╠════════════════════════════════════════════════════════════════╣\n║ SUGGESTIONS                                                    ║\n║   1. Read the assertion: what value did the code actually      ║\n║      produce, and what did the test expect?                    ║\n║   2. The function returned -1 but 5 was expected. Check        ║\n║      the logic inside add().                                   ║\n╚════════════════════════════════════════════════════════════════╝
```

Much friendlier than a raw Python traceback!

---

## 🆘 Troubleshooting

### ❓ "python is not recognized as a command"

**Fix:** Python is not installed or not added to PATH.
- Reinstall Python from [python.org](https://python.org/downloads) and make sure to check **"Add Python to PATH"** during installation.
- Restart your terminal after installing.

---

### ❓ "pip is not recognized as a command"

**Fix:** Try using `pip3` instead of `pip`:

```bash
pip3 install .
```

Or try:

```bash
python -m pip install .
```

---

### ❓ "mistake-box is not recognized as a command"

**Fix:** Run `pip install .` again from inside the `Bug-Whisperer` folder. Make sure you see `Successfully installed mistake-finder-...` at the end.

If you're using a virtual environment, make sure it's activated when you install and when you run `mistake-box`.

---

### ❓ Tests are not showing the friendly box

**Fix:** Make sure you installed the tool first with `pip install .` in the `Bug-Whisperer` folder. Also check that you're using the same Python/pip that runs your tests.

To verify the plugin is installed:

```bash
pytest --help | grep mistake
```

You should see `--mistake-box` and `--no-mistake-box` options.

---

### ❓ The box shows weird characters instead of box-drawing lines

**Fix:** Your terminal doesn't support Unicode box-drawing characters. Use the ASCII box instead:

```bash
mistake-box --ascii python mycode.py
```

Or set it as the default:

```bash
set MISTAKE_BOX_ASCII=1      # Windows
export MISTAKE_BOX_ASCII=1   # Mac/Linux
```

---

### ❓ "git is not recognized as a command"

**Fix:** Git is not installed. Download and install from [git-scm.com](https://git-scm.com/downloads), then restart your terminal.

> **Note:** Git is only needed to clone the project from GitHub. You don't need Git to use the tool after it's installed.

---

### ❓ The AI agent doesn't follow the skill

**Fix:** Make sure the agent knows the skill exists. Try:

> "Read the file `.bob/skills/mistake-finder/SKILL.md` and follow its instructions for this task."

Different agents load skills differently. Check your agent's documentation for how to add custom skills or instructions.

---

### ❓ "ModuleNotFoundError" when running a demo or test

**Fix:** Some demos and tests use third-party libraries that aren't installed by default. Install what you need:

```bash
pip install numpy pandas requests beautifulsoup4 matplotlib openpyxl pillow scipy seaborn scikit-learn sqlalchemy pydantic tqdm
```

The core tool itself has **zero dependencies** — only the demos and tests that use those libraries need them installed.

---

### ❓ "No module named mistake_finder" when running `mistake_finder_universal.py`

**Fix:** The universal command can work in two ways:
1. If `mistake-finder` is installed (`pip install .`), it uses the installed package
2. If not installed, it falls back to the local `.bob/skills/mistake-finder/mistake_box.py`

If both fail, install the package:

```bash
pip install .
```

---

## 🗂️ Project File Map

Here's what every file and folder in this project does:

```
Bug-Whisperer/
│
├── .bob/skills/mistake-finder/   ← The AI-agent skill (works with any agent)
│   ├── SKILL.md                   ← The skill instructions (the "brain")
│   ├── review-checklist.md        ← Mistake classes for code review mode
│   ├── report-template.md         ← How reports are formatted
│   ├── box.py                     ← Core engine: parses errors and draws the box
│   ├── mistake_box.py             ← The `mistake-box` command for terminals
│   ├── pytest_plugin.py           ← Auto-shows boxes when pytest tests fail
│   └── __init__.py                ← Makes the folder work as a Python package
│
├── demos/                         ← 16 demo files with intentional mistakes
│   ├── demo_math.py               ← math.sqrt(-9) → ValueError
│   ├── demo_json.py               ← json.loads('{...}') → JSONDecodeError
│   ├── demo_requests.py           ← requests.get("google.com") → MissingSchema
│   ├── demo_numpy.py              ← arrays of different shape → ValueError
│   ├── demo_pandas.py             ← df["names"] wrong case → KeyError
│   ├── demo_pydantic.py           ← age="not-a-number" → ValidationError
│   ├── demo_sklearn.py            ← 1D array to fit() → ValueError
│   ├── demo_sqlalchemy.py         ← invalid URL → NoSuchModuleError
│   ├── demo_bs4.py                ← "notaparser" → FeatureNotFound
│   ├── demo_openpyxl.py           ← "ZZZZ99999" → ValueError
│   ├── demo_pillow.py             ← Image.open("ghost.png") → FileNotFoundError
│   ├── demo_scipy.py              ← singular matrix → LinAlgError
│   ├── demo_seaborn.py            ← data=None → ValueError
│   ├── demo_matplotlib.py         ← color="notacolor" → ValueError
│   ├── demo_tqdm.py               ← tqdm(None) → TypeError
│   └── demo_numpy_dtype.py        ← np.dtype with list → TypeError
│
├── tests/                         ← 15 pytest test files, 30 tests total
│   ├── test_demo_math.py           ← 2 tests: sqrt(-9) fails, sqrt(9) passes
│   ├── test_demo_json.py           ← 2 tests: single quotes fail, double quotes pass
│   ├── test_demo_requests.py       ← 2 tests: MissingSchema caught, scheme works
│   ├── test_demo_numpy.py          ← 2 tests: shape mismatch fails, same shape works
│   ├── test_demo_pandas.py         ← 2 tests: wrong case KeyError, correct case passes
│   ├── test_demo_pydantic.py       ← 2 tests: wrong type ValidationError, correct type passes
│   ├── test_demo_sklearn.py        ← 2 tests: 1D array fails, 2D array works
│   ├── test_demo_sqlalchemy.py     ← 2 tests: bad URL fails, good URL works
│   ├── test_demo_bs4.py            ← 2 tests: bad parser fails, good parser works
│   ├── test_demo_openpyxl.py       ← 2 tests: bad cell fails, good cell works
│   ├── test_demo_pillow.py         ← 2 tests: missing file fails, create image works
│   ├── test_demo_scipy.py          ← 2 tests: singular matrix fails, non-singular works
│   ├── test_demo_seaborn.py        ← 2 tests: None data fails, real data works
│   ├── test_demo_matplotlib.py     ← 2 tests: bad color fails, good color works
│   └── test_demo_tqdm.py           ← 2 tests: None iterable fails, real iterable works
│
├── mycode.py                      ← Template: paste your own code here to check it
│
├── mistake_finder_universal.py    ← The universal command — 5 modes, 25 libraries
├── smart_run.py                   ← Auto-detects which library a file uses
├── menu.py                        ← Interactive menu to pick what to run
├── find_mistakes.py               ← Smart runner — detects which file to analyse
├── install_skill.py               ← Installs the skill globally (~/.bob/skills/)
│
├── pyproject.toml                 ← Package config (used by pip install)
│   └─ Registers: mistake-box CLI command + pytest11 plugin
├── README.md                      ← This file!
├── LICENSE                        ← MIT license
├── index.html                     ← Project landing page
│
├── .env                           ← Your local configuration (never committed)
├── .env.example                   ← Template for configuration (if needed)
│
├── run.bat                        ← Run mycode.py and catch mistakes (Windows)
├── check.bat                      ← Syntax-check a file (no run) (Windows)
├── test.bat                       ← Open the interactive menu (Windows)
├── run.ps1, check.ps1, test.ps1  ← Same launchers for PowerShell
│
├── .gitignore                     ← Files that Git should ignore
└── .venv/                         ← Python virtual environment (if used)
```

---

## 🛡️ Is it safe to use on my real code?

For the **core tool** (CLI + pytest plugin), yes — it runs entirely on your computer, has no API keys, makes no network calls, and never touches your files except to read them.

For the **AI-agent skill**, safety depends on how you use it. The skill (`SKILL.md`) is written so a well-behaved agent:

- **Investigates read-only** — it reads your files to find mistakes; it does not edit them while investigating.
- **Never weakens tests** — it does not skip, delete, or soften failing tests.
- **Asks before changing code** — the fix loop proposes one minimal source-code fix at a time, verifies it, and rolls back anything that fails; the agent should stop for human review when it cannot auto-repair.
- **Every claim has evidence** — a finding without a `file:line` pointer is not reported.

Those are guardrails written into the skill instructions. They work when the agent follows them. They are **not** a guarantee the agent will obey them — any AI agent can ignore instructions. Treat the skill the same way you would treat any AI coding assistant that can edit files: use it on copies or version-controlled code first, review every change it proposes, and do not let it run unattended on code you cannot afford to lose.

**Voice mode is an exception** — if you use `voice_agent.py`, your voice is sent to IBM Watson for transcription and a network call is made. If you do not use voice mode, the tool makes no network calls.

---

## 📋 About this project

**Bug Whisperer** is a Python package that makes debugging easier and more approachable — especially for people learning Python.

### What makes it different

- **No dependencies** — the core engine is pure Python, no third-party packages
- **Works everywhere** — any IDE, any terminal, any OS, any AI agent
- **Two tools in one** — a CLI/pytest plugin for instant feedback, plus an AI-agent skill for deeper analysis
- **Learner-friendly** — the demo files are ready-made exercises for practicing error-reading
- **Open source** — use it, study it, modify it, share it

### Package info

| Field | Value |
|-------|-------|
| Package name | `mistake-finder` |
| CLI command | `mistake-box` |
| Version | 1.0.0 |
| Python requirement | 3.8+ |
| Third-party dependencies | None (core engine) |
| License | MIT |

### Built for learning and productivity

Whether you're learning Python for the first time, teaching others, or building real projects, Bug Whisperer helps you understand your mistakes faster so you can fix them and move on.

### Quick reference — all commands at a glance

```bash
# Install (one time)
pip install .

# Run a file and box errors
mistake-box python mycode.py

# Syntax check only
mistake-box --file mycode.py

# Run tests (boxes failures automatically)
pytest

# Universal command — auto-detect + analyze
python mistake_finder_universal.py mycode.py

# Identify what library a file uses
python mistake_finder_universal.py --identify mycode.py

# Per-library (25 supported)
python mistake_finder_universal.py --pandas mycode.py
python mistake_finder_universal.py --numpy mycode.py

# Run a demo (16 available)
python mistake_finder_universal.py --demo math

# Run tests via universal command
python mistake_finder_universal.py --test

# Interactive menu
python menu.py

# Smart runner
python smart_run.py mycode.py

# Install AI-agent skill globally
python install_skill.py
```

---

*Happy coding — and may your bugs be few! 🐞*
