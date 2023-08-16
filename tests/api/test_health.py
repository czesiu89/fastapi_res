import http

from fastapi.testclient import TestClient


def test_return_200(client: TestClient):
    response = client.get("/health")

    assert response.status_code == http.HTTPStatus.OK
