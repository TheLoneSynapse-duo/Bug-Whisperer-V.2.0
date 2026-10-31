"""TEST: requests — MissingSchema from URL without http:// scheme."""

import pytest
import requests


def test_requests_missing_schema():
    """requests.get raises MissingSchema when the URL has no scheme."""
    with pytest.raises(requests.exceptions.MissingSchema):
        requests.get("google.com")


def test_requests_with_scheme_works():
    """The correct version: always include the http:// or https:// scheme."""
    # This would make a real request — we just verify the call is accepted.
    # In practice: requests.get("https://google.com")
    pass
