@echo off
chcp 65001 >nul

REM ============================================================
REM run.bat — Run a Python file and catch mistakes in a box
REM ============================================================
REM
REM Usage:
REM   run.bat                  → runs mycode.py (default)
REM   run.bat mycode.py        → runs mycode.py
REM   run.bat demos\demo_math.py → runs a demo
REM   run.bat myfile.py        → runs any Python file
REM
REM What it does:
REM   Runs the file through mistake-box. If the file errors,
REM   you get a friendly box instead of a raw traceback.
REM
REM Other ways to run:
REM   mistake-box python mycode.py              (if installed via pip)
REM   python mistake_finder_universal.py mycode.py  (universal command)
REM   python mistake_finder_universal.py --demo math  (run a demo)
REM   python mistake_finder_universal.py --identify mycode.py  (identify library)
REM   python menu.py                              (interactive menu)
REM   python smart_run.py mycode.py              (smart runner)
REM   pytest                                     (run tests, boxes failures)
REM   python mistake_finder_universal.py --test  (run all tests)
REM
REM ============================================================

if "%1"=="" (
    .venv\Scripts\python.exe smart_run.py mycode.py
) else (
    .venv\Scripts\python.exe smart_run.py %1
)
