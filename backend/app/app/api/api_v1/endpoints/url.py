from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/{short_url}", response_model=schemas.Url)
def read_url(
    short_url: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve url.
    """
    url = crud.url.get_by_short_url(db, short_url=short_url)
    return url


@router.post("/", response_model=schemas.Url)
def create_url(
    *,
    db: Session = Depends(deps.get_db),
    url_in: schemas.UrlCreate,
) -> Any:
    """
    Create new url.
    """
    url = crud.url.get_by_short_url(db, short_url=url_in.short_url)
    if url:
        raise HTTPException(
            status_code=400,
            detail="short URL already exists in the system.",
        )
    url = crud.url.create(db, obj_in=url_in)
    return url
