from telnetlib import Telnet
import pytest

from typing import Generator
from fastapi.testclient import TestClient

from cisco_ping.app import app


@pytest.fixture(scope="session")
def client() -> Generator:
    with TestClient(app) as app_client:
        yield app_client
