"""DEMO: pydantic mistake — passing a string where an integer is expected.

Run with:
    .\run.bat demos\demo_pydantic.py
"""

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# WRONG (ValidationError: age must be an integer, not a string)
user = User(name="Alice", age="not-a-number")

# CORRECT (pass an actual integer)
user = User(name="Alice", age=25)
print("User:", user)

# NOTE: This demo requires pydantic installed.
# If you see ModuleNotFoundError, run: pip install pydantic
