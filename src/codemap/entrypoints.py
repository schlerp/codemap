import importlib
import logging.config
from pathlib import Path
from typing import List

import uvicorn

LOGGING_CONFIG = Path(__file__).parent / "logging.conf"
logging.config.fileConfig(LOGGING_CONFIG, disable_existing_loggers=False)


def run_api():
    """runs the api on the configured port"""
    from codemap import config
    from codemap.api import app

    uvicorn.run(app, host=config.API_HOST, port=config.API_PORT)


def _try_import_for_ptpython(name: str):
    from prompt_toolkit import print_formatted_text
    from prompt_toolkit.formatted_text import HTML

    try:
        importlib.import_module(name)
        print_formatted_text(HTML(f"<green>import {name}</green>"))
    except Exception as e:
        print_formatted_text(
            HTML(f"<yellow>{name}</yellow> failed to import.\n<grey>{e}</grey>\n")
        )


def _configure_prompt(*args):
    modules = [
        "codemap",
        "codemap.config",
        "codemap.exceptions",
        "codemap.bootstrap",
        "codemap.entrypoints",
        "codemap.models",
        "codemap.persist",
        "codemap.schemas",
    ]

    for module in modules:
        _try_import_for_ptpython(module)


def run_prompt():
    from ptpython.repl import embed

    embed(globals(), locals(), configure=_configure_prompt)
