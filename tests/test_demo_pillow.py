"""TEST: Pillow (PIL) — FileNotFoundError from opening a missing image."""

import pytest
from PIL import Image
import os


def test_pillow_missing_file():
    """Image.open raises FileNotFoundError for a file that doesn't exist."""
    with pytest.raises(FileNotFoundError):
        Image.open("ghost.png")


def test_pillow_create_new_image():
    """The correct version: create a new image instead of opening a missing file."""
    img = Image.new("RGB", (100, 100), color="red")
    assert img.size == (100, 100)
