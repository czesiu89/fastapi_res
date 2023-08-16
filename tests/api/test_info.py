import http

from fastapi.testclient import TestClient


def test_return_200_and_hardcoded_message(client: TestClient):
    response = client.get("/info")
    content = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert content == {"Receiver": "Cisco is the best"}
