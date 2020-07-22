from fastapi import APIRouter

from app.api.api_v1.endpoints import url

api_router = APIRouter()
api_router.include_router(url.router, prefix="/url", tags=["url"])
