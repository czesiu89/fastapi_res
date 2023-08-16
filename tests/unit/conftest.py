import pytest

from unittest.mock import MagicMock


@pytest.fixture
def response_mock() -> MagicMock:
    response_mock: MagicMock = MagicMock()
    response_mock.json = MagicMock()
    response_mock.status_code = 200
    return response_mock
