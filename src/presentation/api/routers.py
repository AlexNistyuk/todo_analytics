from fastapi import APIRouter

from presentation.api.v1.actions import router as action_router
from presentation.api.v1.analytics import router as analytics_router

router = APIRouter(prefix="/v1", tags=["V1"])
router.include_router(action_router, prefix="/actions", tags=["Actions"])
router.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])
