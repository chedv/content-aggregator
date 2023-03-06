import datetime

import httpx
import pytest
from dependency_injector import providers

from src.containers import Container
from src.models.movie_models import TmdbPopularMovie
from tests.utils import load_json


class TmdbClientMock:
    def __init__(self, collection_date: datetime.date):
        self.collection_date = collection_date

    async def get_popular_movies(self, http_client: httpx.AsyncClient, page_number: int) -> list[TmdbPopularMovie]:
        json_data = load_json("tmdb_popular_movies_mock.json")
        return [
            TmdbPopularMovie(
                movie_id=item["id"],
                popularity_index=item["popularity"],
                vote_average=item["vote_average"],
                vote_count=item["vote_count"],
                collection_date=self.collection_date
            ) for item in json_data["results"]
        ]


@pytest.mark.anyio
async def test_collect_movies_data(fastapi_app, client, database):
    container: Container = fastapi_app.container
    collection_date = datetime.date(2023, 1, 1)
    container.tmdb_client.override(providers.Factory(TmdbClientMock, collection_date=collection_date))
    await client.post("/api/v1/collect_movies_data")
    result = await database.connection.fetch("select * from tmdb_popular_movies")
    actual_result = [dict(row.items()) for row in result]
    expected_result = [
        {
            "movie_id": 631842,
            "popularity_index": 3886.366,
            "vote_average": 6.5,
            "vote_count": 709,
            "collection_date": collection_date
        },
        {
            "movie_id": 505642,
            "popularity_index": 2680.34,
            "vote_average": 7.4,
            "vote_count": 3734,
            "collection_date": collection_date
        },
        {
            "movie_id": 315162,
            "popularity_index": 2398.547,
            "vote_average": 8.4,
            "vote_count": 4202,
            "collection_date": collection_date
        },
        {
            "movie_id": 646389,
            "popularity_index": 1984.217,
            "vote_average": 6.9,
            "vote_count": 731,
            "collection_date": collection_date
        },
        {
            "movie_id": 1011679,
            "popularity_index": 1801.759,
            "vote_average": 4.2,
            "vote_count": 9,
            "collection_date": collection_date
        },
        {
            "movie_id": 1058949,
            "popularity_index": 1546.875,
            "vote_average": 6.4,
            "vote_count": 41,
            "collection_date": collection_date
        },
        {
            "movie_id": 772515,
            "popularity_index": 1341.204,
            "vote_average": 6.3,
            "vote_count": 47,
            "collection_date": collection_date
        },
        {
            "movie_id": 842942,
            "popularity_index": 1244.763,
            "vote_average": 6.6,
            "vote_count": 85,
            "collection_date": collection_date
        },
        {
            "movie_id": 76600,
            "popularity_index": 1177.986,
            "vote_average": 7.7,
            "vote_count": 5570,
            "collection_date": collection_date
        },
        {
            "movie_id": 823999,
            "popularity_index": 1173.24,
            "vote_average": 5.8,
            "vote_count": 46,
            "collection_date": collection_date
        },
        {
            "movie_id": 536554,
            "popularity_index": 1142.446,
            "vote_average": 7.5,
            "vote_count": 1852,
            "collection_date": collection_date
        },
        {
            "movie_id": 758009,
            "popularity_index": 1047.268,
            "vote_average": 6.4,
            "vote_count": 570,
            "collection_date": collection_date
        },
        {
            "movie_id": 640146,
            "popularity_index": 960.262,
            "vote_average": 6.5,
            "vote_count": 836,
            "collection_date": collection_date
        },
        {
            "movie_id": 965839,
            "popularity_index": 927.639,
            "vote_average": 7.2,
            "vote_count": 6,
            "collection_date": collection_date
        },
        {
            "movie_id": 267805,
            "popularity_index": 887.645,
            "vote_average": 5.6,
            "vote_count": 55,
            "collection_date": collection_date
        },
        {
            "movie_id": 677179,
            "popularity_index": 853.247,
            "vote_average": 7.3,
            "vote_count": 68,
            "collection_date": collection_date
        },
        {
            "movie_id": 436270,
            "popularity_index": 794.939,
            "vote_average": 7.2,
            "vote_count": 4321,
            "collection_date": collection_date
        },
        {
            "movie_id": 1058732,
            "popularity_index": 779.45,
            "vote_average": 5.4,
            "vote_count": 23,
            "collection_date": collection_date
        },
        {
            "movie_id": 1035806,
            "popularity_index": 773.001,
            "vote_average": 6.1,
            "vote_count": 73,
            "collection_date": collection_date
        },
        {
            "movie_id": 843794,
            "popularity_index": 752.001,
            "vote_average": 6.3,
            "vote_count": 353,
            "collection_date": collection_date
        }
    ]
    assert actual_result == expected_result
