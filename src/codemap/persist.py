import logging
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar

from codemap import models
from codemap import schemas
from codemap.exceptions import ExistsException
from codemap.exceptions import PersistException
from neomodel import RelationshipManager
from neomodel import StructuredNode
from pydantic import BaseModel

LOGGER = logging.getLogger(__name__)


S = TypeVar("S", bound=BaseModel)


def model_to_schema(model: StructuredNode, Schema: Type[S]) -> S:
    init_dict = {}
    for key in Schema.__fields__:
        value = model.__dict__[key]
        if isinstance(value, RelationshipManager):
            value = value.all()
        init_dict[key] = value
    print(model.__dict__)
    return Schema(**init_dict)


def get_all_codesets() -> List[schemas.CodeSet]:
    return [model_to_schema(x, schemas.CodeSet) for x in models.CodeSet.nodes.all()]


def get_codeset(name: str) -> Optional[schemas.CodeSet]:
    codeset = models.CodeSet.nodes.get_or_none(name=name)
    if codeset is not None:
        codeset = model_to_schema(codeset, schemas.CodeSet)
    return codeset


def create_codeset(codeset: schemas.CodeSet) -> Optional[schemas.CodeSet]:
    if get_codeset(name=codeset.name) is not None:
        msg = f"Codeset {codeset.name} already exists!"
        LOGGER.error(msg)
        raise ExistsException(msg)

    codeset_model = models.CodeSet(name=codeset.name)
    codeset_model.save()
    for code in codeset.codes:
        code_model = models.Code(
            key=code.key,
            value=code.value,
        )
        code_model.save()
        code_model.codesets.connect(codeset_model)
    codeset_model.refresh()
    LOGGER.debug(f"created new model: {codeset_model}")
    return_schema = model_to_schema(codeset_model, schemas.CodeSet)
    return_schema.codes = [
        model_to_schema(c, schemas.Code) for c in codeset_model.codes.all()
    ]
    LOGGER.debug(return_schema)
    return return_schema


def update_codeset(
    codeset: schemas.CodeSet,
) -> Tuple[Optional[schemas.CodeSet], Optional[PersistException]]:
    return get_codeset(codeset.name)


def delete_codeset(name: str) -> Tuple[bool, Optional[PersistException]]:
    return True


def add_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def update_code(name: str, code: schemas.Code) -> schemas.CodeSet:
    pass


def delete_code(name: str, key: str) -> schemas.CodeSet:
    pass
