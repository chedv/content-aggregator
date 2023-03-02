import httpx

from src.infrastructure.database import Database
from src.infrastructure.http_client import TmdbClient
from src.repositories.movies_repository import MoviesRepository


class CollectMoviesDataService:
    def __init__(self, database: Database, movies_repo: MoviesRepository, tmdb_client: TmdbClient):
        self._database = database
        self._movies_repo = movies_repo
        self._tmdb_client = tmdb_client

    async def collect_and_store_movies_data(self):
        async with httpx.AsyncClient() as http_client:
            tmdb_movies = await self._tmdb_client.get_popular_movies(http_client, page_number=1)
        async with self._database.transaction_provider() as connection:
            await self._movies_repo.insert_tmdb_popular_movies(connection, tmdb_movies)
