from codemap.adapaters import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import LargeBinary
from sqlalchemy import String
from sqlalchemy.orm import relationship


class CodeSet(Base):
    __tablename__ = "codeset"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    codes = relationship("Code", back_populates="codeset")


class Code(Base):
    __tablename__ = "code"
    id = Column(Integer, primary_key=True)
    code = Column(LargeBinary)
    value = Column(LargeBinary)
    code_type = Column(String)
    value_type = Column(String)
    codeset_id = Column(Integer, ForeignKey("CodeSet.id"))
    codeset = relationship("CodeSet", back_populates="codes")
