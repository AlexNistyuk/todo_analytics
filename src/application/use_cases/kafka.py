import json

from pydantic import ValidationError

from application.use_cases.actions import ActionUseCase
from domain.entities.kafka import Kafka
from infrastructure.managers.kafka import KafkaConsumerManager


class KafkaConsumerUseCase(KafkaConsumerManager):
    action_use_case = ActionUseCase()

    @classmethod
    async def start(cls):
        await cls.consumer.start()

        async for msg in cls.consumer:
            await cls.__save_message(json.loads(msg.value))

    @classmethod
    async def __save_message(cls, message):
        try:
            data = Kafka(**message).model_dump()
        except ValidationError:
            return

        await cls.action_use_case.create(data=data)
