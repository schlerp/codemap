from codemap import models
from codemap import schemas
from codemap.persist import model_to_schema


def test_code():
    test_model = models.Code(key="test_key", value="test_value")
    test_schema = model_to_schema(test_model, schemas.Code)
    assert isinstance(test_schema, schemas.Code)
    assert test_schema.key == test_model.key
    assert test_schema.value == test_model.value


def test_codeset():
    test_model = models.CodeSet(name="test_name")
    test_schema = model_to_schema(test_model, schemas.CodeSet)
    assert isinstance(test_schema, schemas.CodeSet)
    assert test_schema.name == test_model.name
