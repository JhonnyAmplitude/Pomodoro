from fastapi import APIRouter
from settings import Settings


router = APIRouter(prefix="/ping", tags=["ping"])


@router.get("/db")
async def ping():
    settings = Settings()
    return {"ping": settings.GOOGLE_TOKEN_ID}