import datetime
import uuid

import botocore.exceptions

from application.use_cases.interfaces import IUseCase
from domain.exceptions.actions import (
    ActionCreateError,
    ActionDeleteError,
    ActionNotFoundError,
    ActionRetrieveError,
    ActionUpdateError,
)
from infrastructure.repositories.actions import ActionRepository


class ActionUseCase(IUseCase):
    repository = ActionRepository()

    async def create(self, data: dict, user=None) -> None:
        data["id"] = str(uuid.uuid4())

        if user is not None:
            data["user_id"] = user.get("id")

        data["created_at"] = int(datetime.datetime.utcnow().timestamp())
        data["action_at"] = data["action_at"].value
        data["action_type"] = data["action_type"].value

        try:
            await self.repository.create(data)
        except botocore.exceptions.ClientError:
            raise ActionCreateError

    async def get_all(self) -> list[dict]:
        try:
            result = await self.repository.get_all()

            return result["Items"]
        except botocore.exceptions.ClientError:
            raise ActionRetrieveError

    async def get_by_id(self, item_id: str) -> dict:
        try:
            result = await self.repository.get_by_id(item_id)
        except botocore.exceptions.ClientError:
            raise ActionNotFoundError

        if not result["Items"]:
            raise ActionNotFoundError
        return result["Items"][0]

    async def delete_by_id(self, item_id: str) -> None:
        try:
            await self.repository.delete_by_id(item_id)
        except botocore.exceptions.ClientError:
            raise ActionDeleteError

    async def update_by_id(self, item_id: str, data: dict) -> None:
        try:
            new_data = {key: {"Value": value} for key, value in data.items()}

            await self.repository.update_by_id(item_id, new_data)
        except botocore.exceptions.ClientError:
            raise ActionUpdateError
