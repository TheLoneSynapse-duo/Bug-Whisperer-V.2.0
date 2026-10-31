"""TEST: scikit-learn — ValueError from passing 1D array to fit()."""

import numpy as np
import pytest
from sklearn.linear_model import LinearRegression


def test_sklearn_1d_array_fails():
    """LinearRegression.fit raises ValueError when given a 1D array."""
    model = LinearRegression()
    with pytest.raises(ValueError):
        model.fit(np.array([1, 2, 3]), np.array([1, 2, 3]))


def test_sklearn_2d_array_works():
    """The correct version: reshape to 2D with .reshape(-1, 1)."""
    model = LinearRegression()
    model.fit(np.array([1, 2, 3]).reshape(-1, 1), np.array([1, 2, 3]))
    assert model.coef_ is not None
