from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from configurations import FASTApiApp
from routes import api_router
from utils import database
from scheduler.scheduler_manager import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await database.connect()
        scheduler.start()
    except Exception as e:
        print(str(e))
    yield
    await database.disconnect()

app = FastAPI(
    title=FASTApiApp.APP_NAME,
    debug=FASTApiApp.DEBUG,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=FASTApiApp.ORIGINS,
    allow_methods=FASTApiApp.METHODS,
    allow_headers=FASTApiApp.HEADERS,
)

app.include_router(api_router)