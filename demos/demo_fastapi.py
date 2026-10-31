#!/usr/bin/env python3
"""DEMO: FastAPI mistake — using a path parameter type that doesn't match the path.

Run with:
    .\run.bat demos\demo_fastapi.py

NOTE: This demo requires FastAPI and uvicorn installed.
If you see ModuleNotFoundError, run: pip install fastapi
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # WRONG at runtime when called with a non-integer path, e.g. /items/abc.
    # FastAPI will return a 422 validation error because item_id is declared int
    # but the path value cannot be coerced.
    return {"item_id": item_id}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
