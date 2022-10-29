from enum import Enum

from codemap import config
from neomodel import db
from neomodel import IntegerProperty
from neomodel import Relationship
from neomodel import RelationshipFrom
from neomodel import RelationshipTo
from neomodel import StringProperty
from neomodel import StructuredNode
from neomodel import UniqueIdProperty

db.set_connection(config.DATABASE_URL)


MEMBER_OF = "MEMBER_OF"
IS_ALIAS = "IS_ALIAS"


class CodeSet(StructuredNode):
    __tablename__ = "codeset"
    _id = UniqueIdProperty()
    name = StringProperty(required=True)
    codes = RelationshipFrom("Code", MEMBER_OF)


class Code(StructuredNode):
    __tablename__ = "code"
    _id = UniqueIdProperty()
    key = StringProperty(required=True)
    value = StringProperty(required=True)
    codesets = RelationshipTo("CodeSet", MEMBER_OF)
