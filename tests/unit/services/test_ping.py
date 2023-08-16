import httpx
import json
import pytest

from cisco_ping.errors import RequestConnectionError, RequestDecodeError, RequestInvalidResponse
from cisco_ping.services.ping import PingService


@pytest.mark.asyncio
class TestPingService:

    @staticmethod
    async def test_ping_endpoint_do_nothin_when_url_responds_with_200(httpx_mock):
        # given
        test_url = "http://test.url"
        httpx_mock.add_response(
            method="GET",
            status_code=200,
        )
        # when
        await PingService().ping_endpoint(test_url)
        # then
        httpx_requests = httpx_mock.get_requests()
        assert len(httpx_requests) == 1
        assert httpx_requests[0].method == "GET"
        assert httpx_requests[0].url == test_url

    @staticmethod
    async def test_ping_endpoint_raise_request_connection_error_on_transport_exception(httpx_mock):
        # given
        httpx_mock.add_exception(httpx.TransportError("Test exc"))
        test_url = "http://test.url"
        # when/then
        with pytest.raises(RequestConnectionError):
            await PingService().ping_endpoint(test_url)

    @staticmethod
    async def test_handle_response_raise_request_invalid_response_on_non_200_from_url(httpx_mock):
        # given
        test_url = "http://test.url"
        httpx_mock.add_response(
            method="GET",
            status_code=404,
        )
        # when/then
        with pytest.raises(RequestInvalidResponse):
            await PingService().ping_endpoint(test_url)
    

    @staticmethod
    async def test_handle_response_raise_request_invalid_response_on_non_200_from_url(response_mock):
        # given
        response_mock.status_code = 404
        # when/then
        with pytest.raises(RequestInvalidResponse):
            await PingService().handle_response(response_mock, propagate_exc=True)
    

    @staticmethod
    async def test_handle_response_raise_request_decode_error_on_non_json_seriazible_content(response_mock):
        # given
        response_mock.json.side_effect = [json.JSONDecodeError("failed to decode", "doc", 1)]
        # when/then
        with pytest.raises(RequestDecodeError):
            await PingService().handle_response(response_mock, propagate_exc=True)
