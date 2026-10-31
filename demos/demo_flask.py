#!/usr/bin/env python3
"""DEMO: Flask mistake — using flask.current_app outside an application context.

Run with:
    .\run.bat demos\demo_flask.py

NOTE: This demo requires Flask installed.
If you see ModuleNotFoundError, run: pip install flask
"""
import flask

app = flask.Flask(__name__)

# CORRECT: access app.name inside an app context
with app.app_context():
    print("Flask app name:", app.name)

# WRONG (RuntimeError: Working outside of application context):
# flask.current_app can only be used inside an active application context.
# The line below raises RuntimeError when executed directly.
try:
    print(flask.current_app.name)
except RuntimeError as e:
    print("RuntimeError:", str(e))
