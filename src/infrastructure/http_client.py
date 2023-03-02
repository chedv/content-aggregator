import datetime

import httpx

from src.api.settings import Settings
from src.models.movie_models import TmdbPopularMovie


class TmdbClient:
    def __init__(self, settings: Settings):
        self._tmdb_api_key_v3 = settings.TMDB_API_KEY_V3
        self._base_url_v3 = "https://api.themoviedb.org/3"

    async def get_popular_movies(self, http_client: httpx.AsyncClient, page_number: int) -> list[TmdbPopularMovie]:
        query_params = {"api_key": self._tmdb_api_key_v3, "language": "en-US", "page": page_number}
        response = await http_client.get(f"{self._base_url_v3}/movie/popular", params=query_params)
        response_data = response.json()
        collection_date = datetime.datetime.now().date()
        return [
            TmdbPopularMovie(
                movie_id=item["id"],
                popularity_index=item["popularity"],
                vote_average=item["vote_average"],
                vote_count=item["vote_count"],
                collection_date=collection_date
            ) for item in response_data["results"]
        ]
