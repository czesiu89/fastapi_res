from fastapi import APIRouter

from cisco_ping.api.endpoints import health, info, ping

api_router = APIRouter()
api_router.include_router(health.router, tags=["HEALTH"])
api_router.include_router(info.router, tags=["INFO"])
api_router.include_router(ping.router, tags=["PING"])
