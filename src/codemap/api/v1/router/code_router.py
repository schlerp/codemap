import logging
from typing import List

import fastapi
from codemap import persist
from codemap import schemas

LOGGER = logging.getLogger()

router = fastapi.APIRouter(
    prefix="/codesets",
    tags=["codesets"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[schemas.CodeSet])
async def get_all_codesets():
    """Get all codesets"""
    response = await persist.get_all_codesets()
    LOGGER.info(response)
    return response


@router.get("/{name}", response_model=schemas.CodeSet)
async def get_codeset(name: str):
    """Get a specific codeset by name"""
    response = persist.get_codeset(name)
    if response is None:
        raise fastapi.HTTPException(
            status_code=404, detail=f"codeset '{name}' not found!"
        )
    return response


@router.post("/", response_model=schemas.CodeSet)
async def create_codeset(codeset: schemas.CodeSet):
    """Create a new codeset"""
    response, error = persist.create_codeset(codeset)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return response


@router.put("/{name}", response_model=schemas.CodeSet)
async def update_codeset(name: str, codeset: schemas.CodeSet):
    """Update an existing codeset"""
    response, error = persist.update_codeset(codeset)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return response


@router.delete("/{name}")
async def delete_codeset(name: str):
    """Delete an existing codeset"""
    response, error = persist.delete_codeset(name)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return response


@router.post("/{name}/add", response_model=schemas.CodeSet)
async def add_code(name: str, code: schemas.Code):
    """Add a code to an existing codeset"""
    response, error = persist.add_code_to_codeset(name, code)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return response


@router.put("/{name}/{key}", response_model=schemas.CodeSet)
async def update_code(
    name: str,
    key: str,
    code: schemas.Code,
):
    """Update an existing code on an existing codeset"""
    response, error = persist.update_code_in_codeset(name, key, code)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return response


@router.delete("/{name}/{key}", response_model=schemas.CodeSet)
async def delete_code(name: str, key: str):
    """Delete an existing code from an existing codeset"""
    response, error = persist.remove_code_from_codeset(name, key)
    # TODO: better error handling for unique error cases (conflict etc)
    if error:
        raise fastapi.HTTPException(status_code=500, detail="an error occured")
    return response
