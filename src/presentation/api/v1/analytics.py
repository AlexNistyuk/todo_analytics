from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from application.dependencies import Container
from domain.entities.analytics import AnalyticsRetrieve
from domain.enums.base import Period
from domain.enums.sheets import SheetActionType
from domain.enums.tasks import TaskActionType
from domain.permissions.users import IsAdminOrIsOwner

router = APIRouter()


@router.get(
    "/",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def get_all_user_actions(
    request: Request,
    period: Period,
    permission=Depends(IsAdminOrIsOwner()),
    analytics_use_case=Depends(Provide[Container.analytics_use_case]),
    user_id: int | None = None,
):
    if user_id is None:
        user_id = request.state.user.get("id")

    await permission.check_object_permission(user_id)

    return await analytics_use_case.get_all_actions(user_id, period)


@router.get(
    "/tasks/",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def get_action_user_tasks(
    request: Request,
    period: Period,
    action_type: TaskActionType = None,
    permission=Depends(IsAdminOrIsOwner()),
    analytics_use_case=Depends(Provide[Container.analytics_use_case]),
    user_id: int | None = None,
):
    if user_id is None:
        user_id = request.state.user.get("id")

    await permission.check_object_permission(user_id)

    if action_type is None:
        return await analytics_use_case.get_all_tasks(user_id, period)
    return await analytics_use_case.get_action_tasks(user_id, action_type, period)


@router.get(
    "/sheets/",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def get_all_user_sheets(
    request: Request,
    period: Period,
    action_type: SheetActionType = None,
    permission=Depends(IsAdminOrIsOwner()),
    analytics_use_case=Depends(Provide[Container.analytics_use_case]),
    user_id: int | None = None,
):
    if user_id is None:
        user_id = request.state.user.get("id")

    await permission.check_object_permission(user_id)

    if action_type is None:
        return await analytics_use_case.get_all_sheets(user_id, period)
    return await analytics_use_case.get_action_sheets(user_id, action_type, period)
