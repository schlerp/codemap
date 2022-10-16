import logging
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

LOGGER = logging.getLogger(__name__)


async def get_all_codesets() -> List[schemas.CodeSetDatabase]:
    query = select(models.CodeSet)
    result: List[schemas.CodeSetDatabase] = await database.fetch_all(query)
    return result


async def get_codeset(name: str) -> Optional[schemas.CodeSetDatabase]:
    query = select(models.CodeSet).where(models.CodeSet.name == name)
    result: schemas.CodeSetDatabase = await database.fetch_one(query)
    return result


async def create_codeset(
    codeset: schemas.CodeSetBase,
) -> Tuple[Optional[schemas.CodeSetDatabase], Optional[PersistException]]:
    query = insert(models.CodeSet).values(
        [{"name": codeset.name, "codes": list(codeset.codes)}]
    )
    LOGGER.debug({"name": codeset.name, "codes": list(codeset.codes)})
    result: List[schemas.CodeSetDatabase] = await database.execute(query)
    return await get_codeset(codeset.name)


async def update_codeset(
    codeset: schemas.CodeSetBase,
) -> Tuple[Optional[schemas.CodeSetDatabase], Optional[PersistException]]:
    query = (
        update(models.CodeSet)
        .where(models.CodeSet.name == codeset.name)
        .values(**codeset)
    )
    result: List[schemas.CodeSetDatabase] = await database.execute(query)
    return await get_codeset(codeset.name)


async def delete_codeset(name: str) -> Tuple[bool, Optional[PersistException]]:
    query = delete(models.CodeSet).where(models.CodeSet.name == name)
    result: List[schemas.CodeSetDatabase] = await database.execute(query)
    return True


def add_code(name: str, code: schemas.CodeBase) -> schemas.CodeSetDatabase:
    pass


def update_code(name: str, code: schemas.CodeBase) -> schemas.CodeSetDatabase:
    pass


def delete_code(name: str, key: str) -> schemas.CodeSetDatabase:
    pass
