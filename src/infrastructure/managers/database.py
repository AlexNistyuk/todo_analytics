from logging import Logger

import aioboto3

from infrastructure.config import get_settings
from infrastructure.managers.interfaces import IManager

settings = get_settings()
logger = Logger(__name__)


class DatabaseManager(IManager):
    session = aioboto3.Session()
    client = None

    @classmethod
    async def connect(cls):
        try:
            cls.client = await cls.session.resource(
                "dynamodb",
                region_name=settings.aws_region,
                endpoint_url=settings.db_url,
                aws_access_key_id=settings.aws_access_key_id,
                aws_secret_access_key=settings.aws_secret_access_key,
            ).__aenter__()

            return cls
        except Exception as exc:
            logger.error(f"Error while connecting to dynamodb: {exc}")

    @classmethod
    async def close(cls):
        await cls.client.__aexit__(None, None, None)
