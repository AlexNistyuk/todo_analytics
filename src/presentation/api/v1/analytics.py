from fastapi import APIRouter, Depends
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from application.use_cases.analytics import AnalyticsUseCase
from domain.entities.analytics import AnalyticsRetrieve
from domain.permissions.users import IsAdminOrIsOwner
from domain.utils.action_types import ActionType
from domain.utils.period import Period

router = APIRouter()


@router.get(
    "/{user_id}",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
async def get_all_user_actions(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_all_actions(user_id, period)


@router.get(
    "/{user_id}/tasks",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
async def get_action_user_tasks(
    user_id: int,
    period: Period,
    action_type: ActionType = None,
    permission=Depends(IsAdminOrIsOwner()),
):
    await permission.check_object_permission(user_id)

    if action_type is None:
        return await AnalyticsUseCase().get_tasks(user_id, period)
    return await AnalyticsUseCase().get_action_tasks(user_id, action_type, period)


@router.get(
    "/{user_id}/sheets",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
async def get_all_user_sheets(
    user_id: int,
    period: Period,
    action_type: ActionType = None,
    permission=Depends(IsAdminOrIsOwner()),
):
    await permission.check_object_permission(user_id)

    if action_type is None:
        return await AnalyticsUseCase().get_sheets(user_id, period)
    return await AnalyticsUseCase().get_action_sheets(user_id, action_type, period)
