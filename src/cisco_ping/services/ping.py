import http
import json
from typing import Any
import httpx

from loguru import logger

from cisco_ping.errors import RequestConnectionError, RequestDecodeError, RequestInvalidResponse


class PingService:
    
    async def ping_endpoint(self, url: str):
        try:
            async with httpx.AsyncClient() as client:
                url = url
                logger.info(f"Getting url={url}")
                response = await client.get(url)
                return self.handle_response(response=response, propagate_exc=False)
        except httpx.TransportError:
            raise RequestConnectionError(f"Failed to connect to requested url={url}")

    @staticmethod
    def handle_response(response: httpx.Response, propagate_exc: bool = False) -> Any:
        if response.status_code == http.HTTPStatus.OK:
            try:
                return response.json()
            except json.JSONDecodeError:
                logger.warning(f"Failed to decode response={response} content.")
                if propagate_exc:
                    raise RequestDecodeError(f"Failed to decode response={response} content.")
        else:
            logger.warning(f"Received non 200 status_code={response.status_code} from endpoint.")
            if propagate_exc:
                raise RequestInvalidResponse(f"Received non 200 status_code={response.status_code} from endpoint.")
