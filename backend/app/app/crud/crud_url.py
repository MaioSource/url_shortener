from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.url import Url
from app.schemas.url import UrlCreate


class CRUDUrl(CRUDBase[Url, UrlCreate]):
    def get_by_short_url(self, db: Session, *, short_url: str) -> Optional[Url]:
        return db.query(Url).filter(Url.short_url == short_url).first()

    def create(self, db: Session, *, obj_in: UrlCreate) -> Url:
        db_obj = Url(
            url=obj_in.url,
            short_url=obj_in.short_url,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


url = CRUDUrl(Url)
