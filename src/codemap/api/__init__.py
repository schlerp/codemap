import fastapi
from codemap import config


description = """# CodeMap

An application for managing code sets, and enabling easy access to them via a rest API.

"""


def create_api(api_version: int = 1):
    app = fastapi.FastAPI(
        title="CodeMap",
        description=description,
        version=config.VERSION,
    )
    if api_version == 1:
        import codemap.api.v1 as api
    else:
        raise NotImplementedError("Only api version 1 is available at the moment!")
    app.include_router(api.router)
