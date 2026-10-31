"""TEST: seaborn — ValueError from passing None as data."""

import matplotlib
matplotlib.use("Agg")
import pytest
import seaborn as sns


def test_seaborn_none_data():
    """sns.histplot raises ValueError when data is None."""
    with pytest.raises(ValueError):
        sns.histplot(data=None, x="col")


def test_seaborn_with_real_data():
    """The correct version: pass a real DataFrame with data."""
    import pandas as pd
    df = pd.DataFrame({"col": [1, 2, 3, 4, 5]})
    ax = sns.histplot(data=df, x="col")
    assert ax is not None
