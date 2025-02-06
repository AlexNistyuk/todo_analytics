import asyncio

from dependency_injector.wiring import Provide

from application.dependencies import Container
from infrastructure.managers.database import DatabaseManager
from infrastructure.managers.kafka import KafkaConsumerManager


async def consume(kafka_consumer_use_case=Provide[Container.kafka_consumer_use_case]):
    await DatabaseManager.connect()
    await KafkaConsumerManager.connect()

    await kafka_consumer_use_case.start()

    await DatabaseManager.close()
    await KafkaConsumerManager.close()


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    asyncio.run(consume())
