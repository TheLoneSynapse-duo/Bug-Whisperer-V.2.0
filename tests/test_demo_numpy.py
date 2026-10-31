"""TEST: numpy — ValueError from shape mismatch when adding two arrays."""

import numpy as np
import pytest


def test_numpy_shape_mismatch():
    """Adding arrays of different shapes raises ValueError."""
    a = np.array([1, 2, 3])
    b = np.array([1, 2])
    with pytest.raises(ValueError):
        a + b


def test_numpy_same_shape_works():
    """The correct version: arrays must have the same shape to add."""
    a = np.array([1, 2, 3])
    b = np.array([1, 2, 3])
    result = a + b
    assert np.array_equal(result, np.array([2, 4, 6]))
