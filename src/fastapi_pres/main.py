import uvicorn

from fastapi_pres.app import app
from fastapi_pres.core.config import config


if __name__ == "__main__":
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT, log_level=config.UVICORN_LOG_LEVEL)
