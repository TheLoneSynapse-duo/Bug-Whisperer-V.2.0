"""TEST: scipy — LinAlgError from inverting a singular matrix."""

import numpy as np
import pytest
from scipy.linalg import inv, LinAlgError


def test_scipy_singular_matrix():
    """inv raises LinAlgError when the matrix is singular (rows are multiples)."""
    with pytest.raises(LinAlgError):
        inv(np.array([[1, 2], [2, 4]]))


def test_scipy_invertible_matrix():
    """The correct version: use a non-singular matrix."""
    result = inv(np.array([[1, 2], [3, 4]]))
    assert result.shape == (2, 2)
