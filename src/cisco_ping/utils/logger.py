import json
from re import sub
import sys

from datetime import timezone
from loguru import logger
from pprint import pprint
from typing import Any, Dict

from cisco_ping.core.config import config


logger_set_up: bool = False


def setup_logger() -> None:
    global logger_set_up
    if not logger_set_up:
        handlers = _get_handlers()
        logger.configure(handlers=handlers)
        logger_set_up = True


def _get_handlers() -> Dict[Any, Any]:
    if config.SERIALIZE_LOG:
        return [dict(sink=_sink, level=config.LOG_LEVEL)]
    else:
        time_formatter = "<green>{time:YYYY:MM:DDTHH:mm:ss!UTC}</green>"
        level_formatter = "<level>{level:<8}</level>"
        line_formatter = "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
        line_formatter = f"{line_formatter: <30}"
        message_formatter = "<level>{message}</level>"
        formatter = f"{time_formatter} | {level_formatter} | {line_formatter} - {message_formatter}"
        return [dict(sink=sys.stdout, format=formatter, level=config.LOG_LEVEL)]


def _sink(message):
    serialized = _serialize(message.record)
    pprint(serialized)


def _serialize(record) -> str:
    subset = {
        "timestamp": record["time"].now(tz=timezone.utc),
        "level": record["level"].name,
        "path": f"{record['name']::record{'function'}:{record['line']}}",
        "message": record["message"],
        "extra": record["extra"]
    }
    return json.dumps(subset, default=str)
