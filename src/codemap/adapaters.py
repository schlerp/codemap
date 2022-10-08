import databases
from codemap import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# create database for async access
database = databases.Database(config.DATABASE_URL)

# create engine for nice handling of sqlalchemy DDL stuff
engine = create_engine(config.DATABASE_URL)

Base = declarative_base(bind=engine)
