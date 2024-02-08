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

from application.use_cases.actions import ActionUseCase
from domain.entities.actions import ActionCreate, ActionRetrieve
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
async def get_all_actions(permission=Depends(IsAdmin())):
    return await ActionUseCase().get_all()


@router.post(
    "/",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
async def create_action(
    request: Request, new_action: ActionCreate, permission=Depends(IsAdmin())
):
    await ActionUseCase().create(new_action.model_dump(), request.state.user)


@router.get(
    "/{item_id}",
    response_model=ActionRetrieve,
    status_code=HTTP_200_OK,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
    },
)
async def get_action_by_id(item_id: str):
    return await ActionUseCase().get_by_id(item_id)


@router.put(
    "/{item_id}",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
async def update_action_by_id(
    item_id: str, updated_action: ActionCreate, permission=Depends(IsAdmin())
):
    await ActionUseCase().update_by_id(item_id, updated_action.model_dump())


@router.delete(
    "/{item_id}",
    status_code=HTTP_204_NO_CONTENT,
    responses={
        HTTP_400_BAD_REQUEST: {},
        HTTP_503_SERVICE_UNAVAILABLE: {},
        HTTP_403_FORBIDDEN: {},
    },
)
async def delete_action_by_id(item_id: str, permission=Depends(IsAdmin())):
    return await ActionUseCase().delete_by_id(item_id)
