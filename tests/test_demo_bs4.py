"""TEST: beautifulsoup4 — FeatureNotFound from unknown parser name."""

import pytest
from bs4 import BeautifulSoup
from bs4 import FeatureNotFound


def test_bs4_invalid_parser():
    """BeautifulSoup raises FeatureNotFound for an unknown parser name."""
    html = "<html><body><h1>Hello World</h1></body></html>"
    with pytest.raises(FeatureNotFound):
        BeautifulSoup(html, "notaparser")


def test_bs4_valid_parser():
    """The correct version: use a valid parser like 'html.parser'."""
    html = "<html><body><h1>Hello World</h1></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    assert soup.h1.text == "Hello World"
