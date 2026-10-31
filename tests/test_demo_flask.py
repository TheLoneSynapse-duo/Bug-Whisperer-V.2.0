"""TEST: flask — RuntimeError when working outside the application context."""
import pytest


def test_flask_app_context() -> None:
    """Accessing Flask app internals is fine inside an app context."""
    import flask

    app = flask.Flask(__name__)
    assert app is not None
    with app.app_context():
        # This is the correct way to access app.name.
        assert app.name.endswith("demo_flask")


def test_flask_outside_app_context_raises() -> None:
    """Creating a Flask app then immediately using flask.current_app
    without a context raises RuntimeError."""
    import flask

    app = flask.Flask(__name__)
    with pytest.raises(RuntimeError, match="[Ww]orking outside of application context"):
        # flask.current_app requires an active application context.
        _ = flask.current_app.name
