from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from application.use_cases.analytics import AnalyticsUseCase
from domain.entities.analytics import AnalyticsRetrieve
from domain.permissions.users import IsAdminOrIsOwner
from domain.utils.period import Period

router = APIRouter()


@router.get("/{user_id}", response_model=AnalyticsRetrieve, status_code=HTTP_200_OK)
async def get_all_user_actions(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_all_actions(user_id, period)


@router.get(
    "/{user_id}/tasks", response_model=AnalyticsRetrieve, status_code=HTTP_200_OK
)
async def get_all_user_tasks(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_tasks(user_id, period)


@router.get(
    "/{user_id}/tasks/done", response_model=AnalyticsRetrieve, status_code=HTTP_200_OK
)
async def get_done_tasks(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_done_tasks(user_id, period)


@router.get(
    "/{user_id}/tasks/created",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
)
async def get_created_tasks(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_created_tasks(user_id, period)


@router.get(
    "/{user_id}/tasks/retrieved",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
)
async def get_retrieved_tasks(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_retrieved_tasks(user_id, period)


@router.get(
    "/{user_id}/sheets", response_model=AnalyticsRetrieve, status_code=HTTP_200_OK
)
async def get_all_user_sheets(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_sheets(user_id, period)


@router.get(
    "/{user_id}/sheets/created",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
)
async def get_created_sheets(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_created_sheets(user_id, period)


@router.get(
    "/{user_id}/sheets/retrieved",
    response_model=AnalyticsRetrieve,
    status_code=HTTP_200_OK,
)
async def get_retrieved_sheets(
    user_id: int, period: Period, permission=Depends(IsAdminOrIsOwner())
):
    await permission.check_object_permission(user_id)

    return await AnalyticsUseCase().get_retrieved_tasks(user_id, period)
