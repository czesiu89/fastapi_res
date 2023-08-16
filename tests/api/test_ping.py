import http

from fastapi.testclient import TestClient


def test_return_200_and_requested_content(client: TestClient):
    response = client.post("/ping", json={"url": "http://0.0.0.0:9000/health"})
    content = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert content == {"url": "http://0.0.0.0:9000/health"}
