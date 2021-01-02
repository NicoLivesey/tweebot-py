from fastapi.testclient import TestClient

from tweebot_py.app import app


client = TestClient(app)


def test_health():
    response = client.get("/health").json()
    assert response["status_code"] == 200
    assert response["response"] == "ok"


def test_predict():
    response = client.get("/tweet")
    assert response.status_code == 200
