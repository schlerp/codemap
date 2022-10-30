class PersistException(Exception):
    pass


class ExistsException(PersistException):
    pass


class NoDatabaseConfiguredException(PersistException):
    pass
