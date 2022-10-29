import fastapi
from codemap import config
from codemap.api.v1.router import code_router

description = "An application for managing code sets, and enabling easy access to them via a rest API."

app = fastapi.FastAPI(
    title="CodeMap",
    description=description,
    version=config.VERSION,
)
app.include_router(code_router.router)
