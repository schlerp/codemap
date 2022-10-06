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
        LOGGER.warn(f"ENV variable '{key}' is unset, falling back to: '{default}'")
    LOGGER.debug(f"ENV variable '{key}' is '{default}'")
    return value


VERSION = get_env("CODEMAP_VERSION", default="v0.0.1-local_dev")

IS_TEST = get_env_flag("IS_TEST")

if IS_TEST:
    DATABASE_URL = "sqlite:///./test.db"
else:
    DATABASE_URL = get_env("DATABASE_URL", is_required=True)
