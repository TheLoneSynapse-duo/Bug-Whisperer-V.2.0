"""TEST: tensorflow — InvalidArgumentError / ValueError from shape mismatch."""
import pytest

try:
    import tensorflow as tf
except ImportError as exc:
    tf = None
    _TF_IMPORT_ERROR = exc


def test_tensorflow_same_shape_add() -> None:
    """Two TF constants with the same shape can be added."""
    if tf is None:
        pytest.skip(f"tensorflow not installed: {_TF_IMPORT_ERROR}")

    a = tf.constant([[1, 2], [3, 4]])
    b = tf.constant([[1, 1], [1, 1]])
    result = a + b
    expected = tf.constant([[2, 3], [4, 5]])
    tf.debugging.assert_equal(result, expected)


def test_tensorflow_incompatible_shape_raises() -> None:
    """Two TF constants with incompatible shapes raise at execution."""
    if tf is None:
        pytest.skip(f"tensorflow not installed: {_TF_IMPORT_ERROR}")

    a = tf.constant([[1, 2], [3, 4]])
    b = tf.constant([1, 2, 3])
    with pytest.raises((ValueError, tf.errors.InvalidArgumentError)):
        # Eager mode raises ValueError for shape mismatch in some versions;
        # graph mode can raise InvalidArgumentError. Both are acceptable here.
        _ = a + b
