import logging

from codemap import config
from neo4j import GraphDatabase

LOGGER = logging.getLogger(__name__)


if config.DB_HOST is None:
    LOGGER.warning("Database not configured! Set 'DB_HOST' env variable.")
    driver: GraphDatabase = None
else:
    db_url = f"neo4j://{config.DB_HOST}:{config.DB_PORT}"
    LOGGER.debug(f"DB URL: {db_url}")
    driver = GraphDatabase.driver(db_url, auth=(config.DB_USER, config.DB_PASSWORD))
