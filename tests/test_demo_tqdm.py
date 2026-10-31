"""TEST: tqdm — TypeError from iterating over None."""

import pytest
from tqdm import tqdm


def test_tqdm_none_iterable():
    """Passing None to tqdm raises TypeError because None is not iterable."""
    with pytest.raises(TypeError):
        for item in tqdm(None):
            print(item)


def test_tqdm_valid_iterable():
    """The correct version: pass a valid iterable like range(5)."""
    items = []
    for item in tqdm(range(5), desc="Processing"):
        items.append(item)
    assert items == [0, 1, 2, 3, 4]
