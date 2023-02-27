import httpx

from src.api.settings import Settings


class TmdbClient:
    def __init__(self, http_client: httpx.Client, settings: Settings):
        self._http_client = http_client
        self._tmdb_api_key_v3 = settings.TMDB_API_KEY_V3
        self._base_url_v3 = "https://api.themoviedb.org/3"

    def get_popular_movies(self):
        query_params = {"api_key": self._tmdb_api_key_v3, "language": "en-US", "page": 1}
        response = self._http_client.get(f"{self._base_url_v3}/movie/popular", params=query_params)
        return response.json()
