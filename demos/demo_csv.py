#!/usr/bin/env python3
"""DEMO: csv mistake — reading a CSV with the wrong number of fields per row.

Run with:
    .\run.bat demos\demo_csv.py

This demo writes a small CSV, then reads it back with a DictReader that
assumes a header the file does not actually have, showing a common parsing
mistake.
"""
import csv
import io

# WRONG (reader misaligned with header): the data rows have 2 fields but
# the declared fieldnames list has 3 names, so values get mapped to the
# wrong keys and one column is always None.
data = "Alice,30\nBob,25\n"
reader = csv.DictReader(io.StringIO(data), fieldnames=["name", "age", "extra"])
rows = list(reader)
print(rows)
