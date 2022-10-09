from typing import List
from typing import Optional
from typing import Tuple

from codemap import models
from codemap import schemas
from codemap.adapaters import database
from codemap.exceptions import PersistException
from sqlalchemy.sql.expression import insert
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.expression import update


async def get_all_codesets() -> List[schemas.CodeSet]:
    query = select(models.CodeSet)
    result: List[schemas.CodeSet] = await database.fetch_all(query)
    return result


async def get_codeset(name: str) -> Optional[schemas.CodeSet]:
    query = select(models.CodeSet).where(models.CodeSet.name == name)
    result: schemas.CodeSet = await database.fetch_one(query)
    return result


async def create_codeset(
    codeset: schemas.CodeSet,
) -> Tuple[Optional[schemas.CodeSet], PersistException]:
    query = insert(models.CodeSet).values(**codeset)
    result: List[schemas.CodeSet] = await database.execute(query)
    return await get_codeset(codeset.name)


async def update_codeset(
    codeset: schemas.CodeSet,
) -> Tuple[Optional[schemas.CodeSet], PersistException]:
    query = (
        update(models.CodeSet)
        .where(models.CodeSet.name == codeset.name)
        .values(**codeset)
    )
    result: List[schemas.CodeSet] = await database.execute(query)
    return await get_codeset(codeset.name)


def delete_codeset(name: str) -> Tuple[bool, PersistException]:
    query = delete(models.CodeSet).where(models.CodeSet.name == name)
    result: List[schemas.CodeSet] = await database.execute(query)
    return True


def add_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def update_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def delete_code(name: str, key: str) -> schemas.CodeSet:
    pass
