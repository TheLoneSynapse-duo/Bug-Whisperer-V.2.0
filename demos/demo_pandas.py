"""DEMO: pandas mistake — using a wrong (misspelled) column name.

Run with:
    .run.bat demos/demo_pandas.py

NOTE: This demo requires pandas installed.
If you see ModuleNotFoundError, run: pip install pandas
"""

import pandas as pd

# WRONG (KeyError: 'names' is not a column; the real column is 'Names')
df = pd.DataFrame({"Names": ["Alice", "Bob"], "Age": [25, 30]})
print(df["names"])

# CORRECT (use the exact column name, case-sensitive)
print(df["Names"])
