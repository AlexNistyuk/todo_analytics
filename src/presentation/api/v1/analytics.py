from fastapi import APIRouter
from starlette.status import HTTP_200_OK

from application.use_cases.analytics import AnalyticsUseCase
from domain.entities.actions import ActionRetrieve

router = APIRouter()


@router.get("/", response_model=list[ActionRetrieve], status_code=HTTP_200_OK)
async def get_week_actions():
    return await AnalyticsUseCase().get_week_actions()
