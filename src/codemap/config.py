import logging
import os
import sys
from typing import Any

LOGGER = logging.getLogger(__name__)


def get_env_flag(key: str) -> bool:
    value = os.getenv(key, "").lower() in ("true", "t", "1", "yes", "y")
    LOGGER.debug(f"ENV variable '{key}' is '{value}'")
    return value


def get_env(key: str, default: Any = None, is_required: bool = False) -> Any:
    value = os.getenv(key)
    if value is None:
        if is_required:
            LOGGER.error(f"ENV variable '{key}' must be set!")
            sys.exit(1)
        value = default
        LOGGER.warning(f"ENV variable '{key}' is unset, falling back to: '{default}'")
    LOGGER.debug(f"ENV variable '{key}' is '{value}'")
    return value


VERSION = get_env("CODEMAP_VERSION", default="v0.0.1-local_dev")

DB_USER = get_env("DB_USER", default="neo4j")
DB_PASSWORD = get_env("DB_PASSWORD", default="neo4j")
DB_HOST = get_env("DB_HOST", default="neo4j")
DB_PORT = get_env("DB_PORT", default="7687")

DATABASE_URL = f"bolt://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"

API_HOST = get_env("API_HOST", default="0.0.0.0")
API_PORT = get_env("API_PORT", default=8123)
