import uvicorn

from cisco_ping.app import app
from cisco_ping.core.config import config


if __name__ == "__main__":
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT, log_level=config.UVICORN_LOG_LEVEL)
