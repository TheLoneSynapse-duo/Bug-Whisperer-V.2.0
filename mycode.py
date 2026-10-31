"""mycode.py — your scratch file for checking code.

HOW TO USE THIS FILE
--------------------
1.  Paste YOUR code over everything below (keep it one .py file).
2.  In the terminal (project root, .venv interpreter), run ONE of:

        mistake-box python mycode.py                          # run it -> box any error
        mistake-box --file mycode.py                          # syntax check only, no run
        python mistake_finder_universal.py mycode.py          # universal — auto-detect library
        python mistake_finder_universal.py --identify mycode.py  # identify the library
        python mistake_finder_universal.py --pandas mycode.py     # per-library (25 libs)
        python menu.py                                        # interactive menu
        python smart_run.py mycode.py                        # smart runner
        pytest                                               # run tests, boxes failures
        python mistake_finder_universal.py --test            # run all 30 tests

    On Windows you can also use the batch launchers:

        run.bat mycode.py     → runs mycode.py and catches mistakes
        check.bat mycode.py   → syntax-check only (no run)
        test.bat              → opens the interactive menu

3.  Read the box: WHERE (file:line + your line + caret),
    WHAT WENT WRONG (exception + message), SUGGESTIONS (concrete fixes).
4.  Want the demo back? Restore the code below from git, or just re-paste it.


ALL THE WAYS TO USE THE TOOL (reference)
-----------------------------------------

1.  mistake-box CLI (installed via pip install .):
        mistake-box python mycode.py              # run + box errors
        mistake-box --file mycode.py              # syntax check only
        mistake-box --log ci.log                  # parse a log file
        mistake-box --ascii python mycode.py     # plain ASCII box
        mistake-box --raw python mycode.py       # show raw error too
        set MISTAKE_BOX=0                        # turn off globally (Windows)

2.  pytest plugin (installed via pip install .):
        pytest                                          # all tests, boxes failures
        pytest --no-mistake-box                         # no boxes
        pytest tests/test_demo_math.py -v               # one library
        pytest tests/test_demo_pandas.py -v             # one library

3.  Universal command (mistake_finder_universal.py) — 5 modes:
        python mistake_finder_universal.py mycode.py         # universal — auto-detect
        python mistake_finder_universal.py --identify mycode.py  # identify library
        python mistake_finder_universal.py --demo math       # run a demo (16 available)
        python mistake_finder_universal.py --test            # run all tests
        python mistake_finder_universal.py --test pandas     # run one library's tests

4.  Per-library commands (25 libraries — see --help for full list):
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

5.  Demo mode (16 demos — see --help for full list):
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

6.  AI-agent skill:
        python install_skill.py              # install globally
        python install_skill.py --check      # verify install
        python install_skill.py --remove     # uninstall


DEMO BUG (below): df["age"] uses the wrong case — pandas columns are
case-sensitive, so it raises KeyError: 'age' before the correct line runs.
"""


import pandas as pd

df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})

# WRONG (Causes KeyError because 'age' is lowercase)
print(df["age"])

# CORRECT (Column names are case-sensitive)
print(df["Age"])