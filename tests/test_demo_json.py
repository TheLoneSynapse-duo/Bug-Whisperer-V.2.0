"""TEST: json — JSONDecodeError from single quotes instead of double quotes."""

import json
import pytest


def test_json_single_quotes_fail():
    """json.loads rejects single-quoted keys — JSON requires double quotes."""
    with pytest.raises(json.JSONDecodeError):
        json.loads("{'name': 'Alice', 'age': 25}")


def test_json_double_quotes_work():
    """The correct version: use double quotes for JSON keys and string values."""
    data = json.loads('{"name": "Alice", "age": 25}')
    assert data["name"] == "Alice"
    assert data["age"] == 25
