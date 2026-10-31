"""TEST: pandas — KeyError from wrong column name (case-sensitive)."""

import pandas as pd
import pytest


def test_pandas_wrong_case_column():
    """Accessing a column with the wrong case raises KeyError."""
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
    with pytest.raises(KeyError):
        df["age"]


def test_pandas_correct_case_column():
    """The correct version: column names are case-sensitive — use 'Age' not 'age'."""
    df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
    assert df["Age"].tolist() == [25, 30]
