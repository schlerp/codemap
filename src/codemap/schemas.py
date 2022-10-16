from typing import Generic
from typing import List
from typing import Type
from typing import TypeVar

import pydantic

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class CodeAtom(pydantic.BaseModel, Generic[T]):
    value: T
    datatype: str  # Type[T] as str


class CodeBase(pydantic.BaseModel, Generic[K, V]):
    key: CodeAtom[K]
    value: CodeAtom[V]


class CodeDatabase(CodeBase):
    id: int


class CodeSetBase(pydantic.BaseModel):
    name: str
    codes: List[CodeBase | CodeDatabase]


class CodeSetDatabase(CodeSetBase):
    id: int
