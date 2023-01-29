import logging
from typing import List
from typing import Optional
from typing import Tuple
from typing import TypeVar

from codemap import cyphers
from codemap import schemas
from codemap.adapters import driver
from codemap.exceptions import ExistsException
from codemap.exceptions import NoDatabaseConfiguredException
from codemap.exceptions import PersistException
from pydantic import BaseModel

LOGGER = logging.getLogger(__name__)


S = TypeVar("S", bound=BaseModel)


def get_all_codesets() -> List[schemas.CodeSet]:
    if driver is None:
        raise NoDatabaseConfiguredException
    with driver.session(database="neo4j") as session:

        result = session.execute_read(query_all_codesets)
    return result


def get_codeset(name: str) -> Optional[schemas.CodeSet]:
    if driver is None:
        raise NoDatabaseConfiguredException
    with driver.session(database="neo4j") as session:

        result = session.execute_read(cyphers.handle_get_codeset_by_name, name)
    return result


def create_codeset(codeset: schemas.CodeSet) -> Optional[schemas.CodeSet]:
    if not get_codeset(codeset.name):
        with driver.session(database="neo4j") as session:
            result = session.execute_write(cyphers.handle_create_codeset, codeset)
        LOGGER.debug(f"Created codeset: {codeset.name}\n{result}")

    for code in codeset.codes:
        existing_code = None


def update_codeset(codeset: schemas.CodeSet) -> Optional[schemas.CodeSet]:
    pass


def delete_codeset(name: str) -> bool:
    pass


def add_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def update_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def delete_code(name: str, key: str) -> schemas.CodeSet:
    pass
