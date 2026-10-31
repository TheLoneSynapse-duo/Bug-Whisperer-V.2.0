"""TEST: math — ValueError from taking sqrt of a negative number."""

import math
import pytest


def test_sqrt_negative_raises_valueerror():
    """Taking sqrt of a negative number raises ValueError (math domain error)."""
    with pytest.raises(ValueError):
        math.sqrt(-9)


def test_sqrt_positive_works():
    """The correct version: sqrt of a positive number works fine."""
    assert math.sqrt(9) == 3.0
