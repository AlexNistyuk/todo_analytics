import json
import logging

from pydantic import ValidationError

from application.use_cases.interfaces import IUseCase
from domain.entities.kafka import KafkaSheet, KafkaTask
from domain.enums.base import ActionAt
from infrastructure.managers.kafka import KafkaConsumerManager

logger = logging.Logger(__name__)


class KafkaConsumerUseCase(KafkaConsumerManager):
    validation_model_map = {
        ActionAt.sheet.value: KafkaSheet,
        ActionAt.task.value: KafkaTask,
    }

    def __init__(self, action_use_case: IUseCase):
        self.action_use_case = action_use_case

    async def start(self):
        await self.consumer.start()

        async for msg in self.consumer:
            await self.__save_message(json.loads(msg.value))

    async def __save_message(self, message: dict):
        action_at = message.get("action_at")

        model = self.validation_model_map.get(action_at)
        if not model:
            logger.warning(
                f"Validation model does not exist for action type. Message: {message}"
            )

            return

        try:
            data = model(**message).model_dump()
        except ValidationError as exc:
            logger.warning(
                f"Validation error. Validation model: {model}. Message: {message}. Error: {exc}"
            )

            return

        await self.action_use_case.create(data=data)
