import asyncio

from application.use_cases.kafka import KafkaConsumerUseCase
from infrastructure.managers.database import DatabaseManager
from infrastructure.managers.kafka import KafkaConsumerManager


async def consume():
    await DatabaseManager.connect()
    await KafkaConsumerManager.connect()

    await KafkaConsumerUseCase.start()

    await DatabaseManager.close()
    await KafkaConsumerManager.close()


if __name__ == "__main__":
    asyncio.run(consume())
