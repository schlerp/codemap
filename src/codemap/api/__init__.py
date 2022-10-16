import fastapi
from codemap import config
from codemap.adapaters import Base
from codemap.adapaters import database
from codemap.adapaters import engine
from codemap.api.v1.router import code_router

description = "An application for managing code sets, and enabling easy access to them via a rest API."

app = fastapi.FastAPI(
    title="CodeMap",
    description=description,
    version=config.VERSION,
)
app.include_router(code_router.router)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(engine)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
