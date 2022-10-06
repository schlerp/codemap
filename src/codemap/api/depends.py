from codemap.adapaters import SessionLocal


async def db_session():
    return SessionLocal
