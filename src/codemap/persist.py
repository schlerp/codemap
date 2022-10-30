import logging
from typing import List
from typing import Optional
from typing import Tuple
from typing import TypeVar

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

        def query_all_codesets(tx):
            query = (
                "MATCH (a:Code)-[:BELONGS_TO]->(b:CodeSet) RETURN a, b ORDER BY a.key"
            )
            data = tx.run(query)
            LOGGER.debug(list(data))
            return list(data)

        result = session.execute_read(query_all_codesets)


def get_codeset(name: str) -> Optional[schemas.CodeSet]:
    pass


def create_codeset(codeset: schemas.CodeSet) -> Optional[schemas.CodeSet]:
    pass


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
