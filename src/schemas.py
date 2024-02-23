import asyncio
import logging

import botocore

from infrastructure.managers.database import DatabaseManager
from infrastructure.schemas.actions import create_actions_table

logger = logging.Logger(__name__)


async def main():
    try:
        await DatabaseManager.connect()

        await create_actions_table(DatabaseManager.client)
    except botocore.errorfactory.ClientError as exc:
        logger.warning(f"Handled exception message: {exc}")
    finally:
        await DatabaseManager.close()


if __name__ == "__main__":
    asyncio.run(main())
