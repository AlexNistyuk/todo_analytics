from aiokafka import AIOKafkaConsumer

from infrastructure.config import get_settings
from infrastructure.managers.interfaces import IManager

settings = get_settings()


class KafkaConsumerManager(IManager):
    consumer: AIOKafkaConsumer

    @classmethod
    async def connect(cls):
        cls.consumer = AIOKafkaConsumer(
            settings.kafka_topic,
            group_id=settings.consumer_group,
            bootstrap_servers=settings.kafka_url,
        )

    @classmethod
    async def close(cls):
        await cls.consumer.stop()
