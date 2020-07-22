from typing import Optional

from pydantic import BaseModel


# Shared properties
class UrlBase(BaseModel):
    url: Optional[str] = None
    short_url: Optional[str] = None


# Properties to receive via API on creation
class UrlCreate(UrlBase):
    url: str
    short_url: str


class UrlInDBBase(UrlBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Url(UrlInDBBase):
    pass
