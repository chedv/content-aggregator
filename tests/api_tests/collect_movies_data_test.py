import json

import httpx
import pytest
from dependency_injector import providers

from src.containers import Container
from src.models.movie_models import TmdbPopularMovie


class TmdbClientMock:
    async def get_popular_movies(self, http_client: httpx.AsyncClient, page_number: int) -> list[TmdbPopularMovie]:
        with open("") as f:
            popular_movies_mock = json.load(f)
        return popular_movies_mock


@pytest.mark.anyio
async def test_collect_movies_data(fastapi_app, client, database):
    container: Container = fastapi_app.container
    container.tmdb_client.override(providers.Factory(TmdbClientMock, settings=container.settings))
    await client.post("/api/v1/collect_movies_data")
    result = await database.connection.fetch("select * from tmdb_popular_movies")
    pass
