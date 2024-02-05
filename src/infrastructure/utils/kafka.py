import asyncio

from aiokafka import AIOKafkaConsumer

from application.use_cases.actions import ActionUseCase
from domain.entities.actions import ActionAt, ActionType
from infrastructure.config import get_settings

settings = get_settings()


class Consumer:
    action_use_case = ActionUseCase()

    async def __aenter__(self):
        self.consumer = AIOKafkaConsumer(
            settings.kafka_topic,
            settings.consumer_group,
            bootstrap_servers=settings.kafka_url,
        )
        await self.consumer.start()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.consumer.stop()

    async def start(self):
        async for msg in self.consumer:
            await self.__save_message(msg.value)

    async def __save_message(self, data):
        if "user_id" not in data:
            return

        self.__set_action_at(data)
        self.__set_action_type(data)

        await self.action_use_case.create(data)

    @staticmethod
    def __set_action_at(data: dict):
        try:
            action_at = data.get("action_at")
            data["action_at"] = ActionAt(action_at)
        except ValueError:
            data.pop("action_at")

    @staticmethod
    def __set_action_type(data: dict):
        try:
            action_type = data.get("action_type")
            data["action_type"] = ActionType(action_type)
        except ValueError:
            data.pop("action_type")


async def consume():
    async with Consumer() as consumer:
        await consumer.start()


if __name__ == "__main__":
    asyncio.run(consume())
