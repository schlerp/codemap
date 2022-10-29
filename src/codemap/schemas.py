from typing import List
from typing import Union

from pydantic import BaseModel
from pydantic import Field


class Code(BaseModel):
    key: str
    value: str


class CodeSet(BaseModel):
    name: str
    codes: List[Code] = Field(default_factory=list)
