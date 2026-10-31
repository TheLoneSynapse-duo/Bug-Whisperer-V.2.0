#!/usr/bin/env python3
"""DEMO: Django mistake — using the ORM without a configured settings module.

Run with:
    .\run.bat demos\demo_django.py

NOTE: This demo requires Django installed.
If you see ModuleNotFoundError, run: pip install django
"""
import os

# WRONG (django.core.exceptions.ImproperlyConfigured):
# Django cannot start until DJANGO_SETTINGS_MODULE is set and
# django.setup() has been called.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

import django
django.setup()

print("Django configured OK")
