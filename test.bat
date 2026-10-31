@echo off

REM ============================================================
REM test.bat — Run tests or open the interactive menu
REM ============================================================
REM
REM Usage:
REM   test.bat                  → opens the interactive menu
REM
REM The menu lets you pick:
REM   - Run a demo (16 available)
REM   - Run tests for a library (15 libraries)
REM   - Run the universal command on mycode.py
REM   - Run the identify command
REM
REM Other ways to run tests:
REM   pytest                                  → all tests, boxes failures
REM   pytest --no-mistake-box                → all tests, no boxes
REM   pytest tests/test_demo_math.py -v      → one library's tests
REM   python mistake_finder_universal.py --test         → all tests via universal
REM   python mistake_finder_universal.py --test pandas  → one library via universal
REM
REM Other ways to use the tool:
REM   mistake-box python mycode.py                          (run + box errors)
REM   mistake-box --file mycode.py                          (syntax check only)
REM   python mistake_finder_universal.py mycode.py         (universal — auto-detect)
REM   python mistake_finder_universal.py --identify mycode.py (identify library)
REM   python mistake_finder_universal.py --demo math       (run a demo)
REM   python mistake_finder_universal.py --pandas mycode.py (per-library)
REM   python menu.py                                        (interactive menu)
REM   python smart_run.py mycode.py                        (smart runner)
REM   python install_skill.py                               (install AI skill globally)
REM
REM ============================================================

.venv\Scripts\python.exe menu.py
