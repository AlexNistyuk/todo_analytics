import asyncio

from infrastructure.managers.database import DatabaseManager
from infrastructure.schemas.actions import create_actions_table


async def main():
    await DatabaseManager.connect()

    await create_actions_table(DatabaseManager.client)

    await DatabaseManager.close()


if __name__ == "__main__":
    asyncio.run(main())
