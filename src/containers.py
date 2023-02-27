import httpx
from dependency_injector import containers, providers

from src.api.settings import Settings
from src.infrastructure.database import Database
from src.infrastructure.http_client import TmdbClient
from src.services.collect_movies_data_service import CollectMoviesDataService


class Container(containers.DeclarativeContainer):
    settings = providers.Singleton(Settings)

    database = providers.Singleton(Database, settings=settings)

    http_client = providers.Factory(httpx.Client)
    tmdb_client = providers.Factory(TmdbClient, http_client=http_client, settings=settings)

    collect_movies_data_service = providers.Factory(CollectMoviesDataService,
                                                    database=database, tmdb_client=tmdb_client)
