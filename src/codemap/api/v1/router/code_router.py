from typing import List

import fastapi
from codemap import persist
from codemap import schemas
from codemap.api import depends

router = fastapi.APIRouter(
    prefix="/codesets",
    tags=["codesets"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.CodeSet])
async def get_all_codesets(db_session=fastapi.Depends(depends.db_session)):
    codesets = persist.get_all_codesets(db_session)
    return codesets


@router.get("/{name}", response_model=schemas.CodeSet)
async def get_codeset(name: str, db_session=fastapi.Depends(depends.db_session)):
    codeset = persist.get_codeset(db_session)
    if codeset is None:
        raise fastapi.HTTPException(
            status_code=404, detail=f"codeset '{name}' not found!"
        )
    return codeset


@router.post("/", response_model=schemas.CodeSet)
async def create_codeset(
    codeset: CodeSet, db_session=fastapi.Depends(depends.db_session)
):
    codeset, error = persist.create_codeset(codeset, db_session=db_session)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return codeset


@router.put("/{name}", response_model=schemas.CodeSet)
async def update_codeset(
    name: str, codeset: schemas.CodeSet, db_session=fastapi.Depends(depends.db_session)
):
    codeset, error = persist.update_codeset(codeset, db_session=db_session)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return codeset


@router.delete("/{name}")
async def delete_codeset(name: str, db_session=fastapi.Depends(depends.db_session)):
    codeset, error = persist.delete_codeset(name, db_session=db_session)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return codeset


@router.post("/{name}/add", response_model=schemas.CodeSet)
async def add_code(
    name: str, code: schemas.Code, db_session=fastapi.Depends(depends.db_session)
):
    codeset, error = persist.add_code_to_codeset(name, code, db_session=db_session)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return codeset


@router.put("/{name}/{key}", response_model=schemas.CodeSet)
async def update_code(
    name: str,
    key: str,
    code: schemas.Code,
    db_session=fastapi.Depends(depends.db_session),
):
    codeset, error = persist.update_code_in_codeset(
        name, key, code, db_session=db_session
    )
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return codeset


@router.delete("/{name}/{key}", response_model=schemas.CodeSet)
async def delete_code(
    name: str, key: str, db_session=fastapi.Depends(depends.db_session)
):
    codeset, error = persist.remove_code_from_codeset(name, key, db_session=db_session)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return codeset
