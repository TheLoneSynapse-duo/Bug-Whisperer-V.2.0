"""TEST: pydantic — ValidationError from string passed as integer field."""

from pydantic import BaseModel, ValidationError
import pytest


class User(BaseModel):
    name: str
    age: int


def test_pydantic_wrong_type():
    """Passing a string where an int is expected raises ValidationError."""
    with pytest.raises(ValidationError):
        User(name="Alice", age="not-a-number")


def test_pydantic_correct_type():
    """The correct version: pass an integer for the age field."""
    user = User(name="Alice", age=25)
    assert user.age == 25
