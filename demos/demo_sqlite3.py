#!/usr/bin/env python3
"""DEMO: sqlite3 mistake — executing a query with a placeholder count mismatch.

Run with:
    .\run.bat demos\demo_sqlite3.py

This demo creates an in-memory SQLite database and runs a parameterized
query where the number of ? placeholders does not match the parameters
passed, showing a common SQL mistake.
"""
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (name TEXT, age INTEGER)")
conn.execute("INSERT INTO users VALUES ('Alice', 30)")

# WRONG (sqlite3.ProgrammingError: bind parameter count mismatch):
# The query has 2 placeholders but only 1 parameter is supplied.
row = conn.execute("SELECT * FROM users WHERE name = ? AND age = ?", ("Alice",))
print(row.fetchone())
conn.close()
