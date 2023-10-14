from fastapi import APIRouter
from src.api.v1.endpoints import translate

api_router = APIRouter()

api_router.include_router(translate.router, prefix="/translate", tags=["translate"])