"""TEST: csv — DictReader fieldnames count must match the data columns."""
import csv
import io
import pytest


def test_csv_dictreader_fieldnames_match() -> None:
    """When fieldnames match the row column count, values map correctly."""
    data = "Alice,30\nBob,25\n"
    reader = csv.DictReader(io.StringIO(data), fieldnames=["name", "age"])
    rows = list(reader)
    assert rows[0]["name"] == "Alice"
    assert rows[0]["age"] == "30"


def test_csv_dictreader_fieldnames_mismatch() -> None:
    """When fieldnames count differs from columns, data maps to wrong keys."""
    data = "Alice,30\nBob,25\n"
    reader = csv.DictReader(io.StringIO(data), fieldnames=["name", "age", "extra"])
    rows = list(reader)
    # When fieldnames exceed columns, the extra fieldnames get None.
    # With 2 data columns and 3 fieldnames, the 3rd fieldname gets None.
    assert rows[0]["name"] == "Alice"
    assert rows[0]["age"] == "30"
    assert rows[0]["extra"] is None
