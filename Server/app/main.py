from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.utils.logger import logger
from app.api.v1.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("AHUMonitor Enterprise Started")

    yield

    logger.info("AHUMonitor Enterprise Stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise Employee Monitoring Platform",
    lifespan=lifespan,
)

app.include_router(api_router)


@app.get("/")
def root():

    return {

        "application": settings.APP_NAME,

        "version": settings.APP_VERSION,

        "status": "Running"

    }