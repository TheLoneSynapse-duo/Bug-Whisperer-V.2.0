@echo off

REM ============================================================
REM check.bat — Syntax-check a Python file (no run)
REM ============================================================
REM
REM Usage:
REM   check.bat                  → checks mycode.py (default)
REM   check.bat mycode.py        → checks mycode.py
REM   check.bat myfile.py        → checks any Python file
REM
REM What it does:
REM   Parses the file for syntax errors WITHOUT running it.
REM   Useful when you want to check code that has side effects
REM   or that you don't want to execute.
REM
REM Other ways to check:
REM   mistake-box --file mycode.py              (if installed via pip)
REM   python -m py_compile mycode.py            (stdlib syntax check)
REM
REM ============================================================

if "%1"=="" (
    .venv\Scripts\mistake-box.exe --file mycode.py
) else (
    .venv\Scripts\mistake-box.exe --file %1
)
