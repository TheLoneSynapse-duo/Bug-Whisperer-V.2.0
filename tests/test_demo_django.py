"""TEST: django — ImproperlyConfigured when settings are not configured."""
import os
import sys

DEMO_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "demos")
)
if DEMO_DIR not in sys.path:
    sys.path.insert(0, DEMO_DIR)

import pytest

try:
    import django
    from django.core.exceptions import ImproperlyConfigured
except ImportError as exc:
    django = None
    ImproperlyConfigured = None
    _DJANGO_IMPORT_ERROR = exc


def test_django_app_configured_ok() -> None:
    """A Django project configured with a minimal settings module starts."""
    if django is None:
        pytest.skip(f"django not installed: {_DJANGO_IMPORT_ERROR}")

    import types

    settings_module = types.SimpleNamespace()
    settings_module.DEBUG = True
    settings_module.SECRET_KEY = "test-secret-key-for-demo"
    settings_module.INSTALLED_APPS = []

    os.environ["DJANGO_SETTINGS_MODULE"] = "demo_settings"
    sys.modules["demo_settings"] = settings_module

    try:
        # Reset Django so it re-reads DJANGO_SETTINGS_MODULE below.
        if hasattr(django, "conf"):
            try:
                django.conf.INSTALLED_APPS = None  # force re-setup next time
            except Exception:
                pass
        django.setup()
    finally:
        sys.modules.pop("demo_settings", None)
        os.environ.pop("DJANGO_SETTINGS_MODULE", None)


def test_django_without_setup_raises() -> None:
    """Using Django's ORM / settings before django.setup() raises."""
    if ImproperlyConfigured is None:
        pytest.skip(f"django not installed: {_DJANGO_IMPORT_ERROR}")

    if "DJANGO_SETTINGS_MODULE" in os.environ:
        del os.environ["DJANGO_SETTINGS_MODULE"]

    with pytest.raises(ImproperlyConfigured):
        from django.conf import settings  # noqa: F401
