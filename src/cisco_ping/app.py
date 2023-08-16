from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from cisco_ping.api.api import api_router
from cisco_ping.core.config import config
from cisco_ping.errors import CustomException
from cisco_ping.utils.logger import setup_logger


setup_logger()


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def init_routers(app: FastAPI) -> None:
    app.include_router(api_router)


def init_listeners(app: FastAPI) -> None:
    # Exception handler
    @app.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


def create_app() -> FastAPI:
    app = FastAPI(
        title="CISCO PING",
        version="0.1.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
    )
    init_routers(app=app)
    init_cors(app=app)
    init_listeners(app=app)
    return app


app = create_app()
