from fastapi import APIRouter

from .user_api import router as user_router

router = APIRouter()


router.include_router(prefix="/users", router=user_router, tags=['users'] )