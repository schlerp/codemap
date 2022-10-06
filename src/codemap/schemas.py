from typing import Generic
from typing import List
from typing import TypeVar

import pydantic

K = TypeVar("K")
V = TypeVar("V")


class Code(pydantic.BaseModel, Generic[K, V]):
    key: K
    value: V


class CodeSet(pydantic.BaseModel):
    name: str
    codes: List[Code]
