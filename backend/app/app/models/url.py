from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Url(Base):
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    short_url = Column(String, unique=True)
