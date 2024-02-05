from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from infrastructure.managers.database import DatabaseManager
from migrations.actions import create_actions_table
from presentation.routers import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager = await DatabaseManager.connect()
    await create_actions_table(db_manager.client)

    yield

    await db_manager.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
