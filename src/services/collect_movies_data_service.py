from src.infrastructure.database import Database
from src.infrastructure.http_client import TmdbClient


class CollectMoviesDataService:
    def __init__(self, database: Database, tmdb_client: TmdbClient):
        self._database = database
        self._tmdb_client = tmdb_client

    def collect_and_store_movies_data(self):
        result = self._tmdb_client.get_popular_movies()
        with self._database.session_provider() as session:
            session.add()
            session.commit()
