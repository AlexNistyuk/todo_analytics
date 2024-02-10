from boto3.dynamodb.conditions import Key

from infrastructure.managers.database import DatabaseManager
from infrastructure.repositories.interfaces import IRepository


class ActionRepository(DatabaseManager, IRepository):
    table = "actions"

    async def create(self, data: dict) -> None:
        table = await self.client.Table(self.table)
        await table.put_item(Item=data)

    async def get_all(self):
        table = await self.client.Table(self.table)

        return await table.scan()

    async def get_by_id(self, item_id: str):
        table = await self.client.Table(self.table)
        query = Key("id").eq(item_id)

        return await table.query(KeyConditionExpression=query)

    async def get_by_filters(self, filters):
        table = await self.client.Table(self.table)

        return await table.scan(FilterExpression=filters)

    async def delete_by_id(self, item_id: str) -> None:
        table = await self.client.Table(self.table)
        await table.delete_item(Key={"id": item_id})

    async def update_by_id(self, item_id, data: dict) -> None:
        table = await self.client.Table(self.table)

        await table.update_item(
            Key={"id": item_id},
            AttributeUpdates=data,
        )
