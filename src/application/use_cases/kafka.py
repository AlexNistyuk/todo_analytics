import json

from pydantic import ValidationError

from application.use_cases.interfaces import IUseCase
from domain.entities.kafka import Kafka
from infrastructure.managers.kafka import KafkaConsumerManager


class KafkaConsumerUseCase(KafkaConsumerManager):
    def __init__(self, action_use_case: IUseCase):
        self.action_use_case = action_use_case

    async def start(self):
        await self.consumer.start()

        async for msg in self.consumer:
            await self.__save_message(json.loads(msg.value))

    async def __save_message(self, message):
        try:
            data = Kafka(**message).model_dump()
        except ValidationError:
            return

        await self.action_use_case.create(data=data)
