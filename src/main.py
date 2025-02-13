from contextlib import asynccontextmanager

from fastapi import FastAPI

from application.dependencies import Container
from infrastructure.managers.database import DatabaseManager
from infrastructure.middlewares.auth_middleware.init import init_auth_middleware
from presentation.routers import router as api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await DatabaseManager.connect()

    container = Container()
    container.wire(
        modules=[
            "presentation.api.v1.actions",
            "presentation.api.v1.analytics",
        ]
    )

    yield

    await DatabaseManager.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

init_auth_middleware(app)
