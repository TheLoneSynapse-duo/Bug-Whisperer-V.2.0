"""TEST: sqlalchemy — NoSuchModuleError from invalid database URL."""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import NoSuchModuleError


def test_sqlalchemy_invalid_url():
    """An invalid database URL raises NoSuchModuleError."""
    with pytest.raises(NoSuchModuleError):
        create_engine("notavalidurl://")


def test_sqlalchemy_sqlite_url_works():
    """The correct version: use a valid URL like sqlite:///demo.db."""
    engine = create_engine("sqlite:///demo.db")
    assert engine is not None
