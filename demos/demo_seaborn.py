"""DEMO: seaborn mistake — passing None as data with a column name.

Run with:
    .\run.bat demos\demo_seaborn.py
"""

import seaborn as sns
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

# WRONG (TypeError/ValueError: data is None but x='col' was specified)
try:
    sns.histplot(data=None, x="col")
except Exception as e:
    print("Expected error:", type(e).__name__, str(e)[:120])

# CORRECT (pass actual DataFrame data)
df = pd.DataFrame({"col": [1, 2, 3, 4, 5, 3, 2, 1]})
sns.histplot(data=df, x="col")
plt.savefig("seaborn_output.png")
print("Plot saved as seaborn_output.png")

# NOTE: This demo requires seaborn and matplotlib installed.
# If you see ModuleNotFoundError, run: pip install seaborn matplotlib
