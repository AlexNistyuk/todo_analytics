from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from infrastructure.managers.database import DatabaseManager
from infrastructure.middlewares.user import UserAuthMiddleware
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
app.add_middleware(UserAuthMiddleware)


# TODO delete in production

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
