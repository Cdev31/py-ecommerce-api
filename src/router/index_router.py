from fastapi import APIRouter, FastAPI
from ..modules import user_router

def api_router( app: FastAPI ):
    router = APIRouter(prefix="/api/v1")
    router.include_router(prefix="/users", router=user_router )
    app.include_router( router )