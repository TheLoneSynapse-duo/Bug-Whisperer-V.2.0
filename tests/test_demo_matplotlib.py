"""TEST: matplotlib — ValueError from invalid color name."""

import matplotlib
matplotlib.use("Agg")
import pytest
import matplotlib.pyplot as plt


def test_matplotlib_invalid_color():
    """ax.plot raises ValueError when given an invalid color name."""
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        ax.plot([1, 2, 3], [4, 5, 6], color="notacolor")
    plt.close(fig)


def test_matplotlib_valid_color():
    """The correct version: use a valid color name like 'blue'."""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6], color="blue")
    plt.close(fig)
