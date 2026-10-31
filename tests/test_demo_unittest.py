"""TEST: unittest — a unittest.TestCase with an intentional failure and a pass."""
import pytest
import sys
from pathlib import Path

DEMO_DIR = Path(__file__).resolve().parent.parent / "demos"
if str(DEMO_DIR) not in sys.path:
    sys.path.insert(0, str(DEMO_DIR))


def test_unittest_intentional_failure() -> None:
    """A unittest.TestCase that asserts something false reports a failure."""
    import types
    import unittest

    demo_module = types.SimpleNamespace()
    demo_module.TestCaseLocal = type(
        "TestCaseLocal", (unittest.TestCase,), {
            "test_fail": lambda self: self.assertEqual(1, 2),
        }
    )
    suite = unittest.TestLoader().loadTestsFromTestCase(demo_module.TestCaseLocal)
    import io
    result = unittest.TextTestRunner(verbosity=0, stream=io.StringIO()).run(suite)
    # unittest reports failure via wasSuccessful() == False, not by raising
    assert not result.wasSuccessful()
    assert result.failures  # should have at least one failure recorded


def test_unittest_correct_assertion_passes() -> None:
    """A unittest.TestCase that asserts something true passes."""
    import types
    import unittest

    demo_module = types.SimpleNamespace()
    demo_module.TestCaseLocal = type(
        "TestCaseLocal", (unittest.TestCase,), {
            "test_pass": lambda self: self.assertEqual(1, 1),
        }
    )
    suite = unittest.TestLoader().loadTestsFromTestCase(demo_module.TestCaseLocal)
    import io
    result = unittest.TextTestRunner(verbosity=0, stream=io.StringIO()).run(suite)
    assert result.wasSuccessful()
