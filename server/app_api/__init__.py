from fastapi import APIRouter

from .user_api import router as user_router
from .q_api import router as q_router

router = APIRouter()


router.include_router(prefix="/users", router=user_router, tags=['users'] )
router.include_router(prefix="/q", router=q_router, tags=['q'])