"""DEMO: tqdm mistake — iterating over None instead of an iterable.

Run with:
    .\run.bat demos\demo_tqdm.py
"""

from tqdm import tqdm

# WRONG (TypeError: 'NoneType' object is not iterable)
for item in tqdm(None):
    print(item)

# CORRECT (pass an actual iterable like a list or range)
for item in tqdm(range(5), desc="Processing"):
    pass
print("Done!")

# NOTE: This demo requires tqdm installed.
# If you see ModuleNotFoundError, run: pip install tqdm
