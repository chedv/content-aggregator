from fastapi import FastAPI

from src.api import collect_movies
from src.containers import Container


def create_app():
    container = Container()
    container.wire(packages=[collect_movies])

    fastapi_app = FastAPI()
    fastapi_app.container = container
    fastapi_app.include_router(collect_movies.router, prefix="/api/v1")
    return fastapi_app


app = create_app()
