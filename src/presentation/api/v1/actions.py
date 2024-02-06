from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from application.use_cases.actions import ActionUseCase
from domain.entities.actions import ActionCreate, ActionRetrieve
from domain.permissions.users import IsAdmin

router = APIRouter()


@router.get("/", response_model=list[ActionRetrieve], status_code=HTTP_200_OK)
async def get_all_actions(permission=Depends(IsAdmin())):
    return await ActionUseCase().get_all()


@router.post("/", status_code=HTTP_204_NO_CONTENT)
async def create_action(
    request: Request, new_action: ActionCreate, permission=Depends(IsAdmin())
):
    return await ActionUseCase().create(new_action.model_dump(), request.state.user)


@router.get("/{item_id}", response_model=ActionRetrieve, status_code=HTTP_200_OK)
async def get_action_by_id(item_id: str):
    return await ActionUseCase().get_by_id(item_id)


@router.put("/{item_id}", status_code=HTTP_204_NO_CONTENT)
async def update_action_by_id(
    item_id: str, updated_action: ActionCreate, permission=Depends(IsAdmin())
):
    return await ActionUseCase().update_by_id(item_id, updated_action.model_dump())


@router.delete("/{item_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_action_by_id(item_id: str, permission=Depends(IsAdmin())):
    return await ActionUseCase().delete_by_id(item_id)
