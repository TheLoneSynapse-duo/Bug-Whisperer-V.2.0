"""TEST: sqlite3 — ProgrammingError when placeholder count != parameter count."""
import pytest
import sqlite3


def test_sqlite3_parameter_count_match() -> None:
    """A parameterized query with matching placeholder and parameter counts works."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT, age INTEGER)")
    conn.execute("INSERT INTO users VALUES ('Alice', 30)")

    row = conn.execute(
        "SELECT * FROM users WHERE name = ? AND age = ?", ("Alice", 30)
    ).fetchone()
    assert row == ("Alice", 30)

    conn.close()


def test_sqlite3_parameter_count_mismatch() -> None:
    """A parameterized query whose placeholder count differs from parameters raises."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT, age INTEGER)")
    conn.execute("INSERT INTO users VALUES ('Alice', 30)")

    with pytest.raises(sqlite3.ProgrammingError):
        conn.execute("SELECT * FROM users WHERE name = ? AND age = ?", ("Alice",))

    conn.close()
