"""TEST: fastapi — path parameter deserialization for int fields."""
import pytest

try:
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
except ImportError as exc:
    FastAPI = None
    TestClient = None
    _FASTAPI_IMPORT_ERROR = exc


def test_fastapi_int_path_param_valid() -> None:
    """A request with a valid integer path parameter is accepted."""
    if FastAPI is None:
        pytest.skip(f"fastapi not installed: {_FASTAPI_IMPORT_ERROR}")

    app = FastAPI()

    @app.get("/items/{item_id}")
    def read_item(item_id: int):
        return {"item_id": item_id}

    client = TestClient(app)
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42}


def test_fastapi_int_path_param_invalid() -> None:
    """A request with a non-integer path parameter returns 422."""
    if FastAPI is None:
        pytest.skip(f"fastapi not installed: {_FASTAPI_IMPORT_ERROR}")

    app = FastAPI()

    @app.get("/items/{item_id}")
    def read_item(item_id: int):
        return {"item_id": item_id}

    client = TestClient(app)
    response = client.get("/items/abc")
    assert response.status_code == 422
