from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_503_SERVICE_UNAVAILABLE,
)

from application.dependencies import Container
from domain.entities.actions import ActionCreateSheet, ActionCreateTask, ActionRetrieve
from domain.permissions.users import IsAdmin

router = APIRouter()


@router.get(
    "/",
    response_model=list[ActionRetrieve],
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def get_all_actions(
    permission=Depends(IsAdmin()),
    action_use_case=Depends(Provide[Container.action_use_case]),
):
    return await action_use_case.get_all()


@router.post(
    "/tasks/",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def create_task_action(
    request: Request,
    new_action: ActionCreateTask,
    permission=Depends(IsAdmin()),
    action_use_case=Depends(Provide[Container.action_use_case]),
):
    await action_use_case.create(new_action.model_dump(), request.state.user)


@router.post(
    "/sheets/",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def create_sheet_action(
    request: Request,
    new_action: ActionCreateSheet,
    permission=Depends(IsAdmin()),
    action_use_case=Depends(Provide[Container.action_use_case]),
):
    await action_use_case.create(new_action.model_dump(), request.state.user)


@router.get(
    "/{item_id}/",
    response_model=ActionRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
@inject
async def get_action_by_id(
    item_id: str, action_use_case=Depends(Provide[Container.action_use_case])
):
    return await action_use_case.get_by_id(item_id)


@router.put(
    "/tasks/{item_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def update_task_action_by_id(
    item_id: str,
    updated_action: ActionCreateTask,
    permission=Depends(IsAdmin()),
    action_use_case=Depends(Provide[Container.action_use_case]),
):
    await action_use_case.update_by_id(item_id, updated_action.model_dump())


@router.put(
    "/sheets/{item_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def update_sheet_action_by_id(
    item_id: str,
    updated_action: ActionCreateSheet,
    permission=Depends(IsAdmin()),
    action_use_case=Depends(Provide[Container.action_use_case]),
):
    await action_use_case.update_by_id(item_id, updated_action.model_dump())


@router.delete(
    "/{item_id}/",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
@inject
async def delete_action_by_id(
    item_id: str,
    permission=Depends(IsAdmin()),
    action_use_case=Depends(Provide[Container.action_use_case]),
):
    return await action_use_case.delete_by_id(item_id)
