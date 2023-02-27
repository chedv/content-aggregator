from starlette.testclient import TestClient

from src.api.app import app


def test_collect_movies_data():
    client = TestClient(app)
    client.post("/api/v1/collect_movies_data")
