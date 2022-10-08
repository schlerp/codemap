from typing import List
from typing import Optional
from typing import Tuple

from codemap import models
from codemap import schemas
from codemap.adapaters import database
from codemap.exceptions import PersistException
from sqlalchemy.orm import Query


async def get_all_codesets() -> List[schemas.CodeSet]:
    query = Query(models.CodeSet)
    return await database.fetch_all(query)


def get_codeset(name: str) -> Optional[schemas.CodeSet]:
    pass


def create_codeset(
    codeset: schemas.CodeSet,
) -> Tuple[Optional[schemas.CodeSet], PersistException]:
    pass


def update_codeset(
    codeset: schemas.CodeSet,
) -> Tuple[Optional[schemas.CodeSet], PersistException]:
    pass


def delete_codeset(name: str) -> Tuple[Optional[schemas.CodeSet], PersistException]:
    pass


def add_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def update_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def delete_code(name: str, key: str) -> schemas.CodeSet:
    pass
