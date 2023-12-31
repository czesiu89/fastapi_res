import http

from fastapi import APIRouter, Body
from typing import Any

from fastapi_pres.schemas.ping import PingRequest
from fastapi_pres.services.ping import PingService


prefix = "/ping"
router = APIRouter(prefix=prefix)


@router.post("", description="Ping an endpoint and return it's content", status_code=http.HTTPStatus.OK)
async def ping(ping_request: PingRequest = Body(...)) -> Any:
    """
    POST - ping
    response: 200 OK
    """
    await PingService().ping_endpoint(ping_request.url)
    return ping_request
