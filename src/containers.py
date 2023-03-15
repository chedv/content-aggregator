from dependency_injector import containers, providers

from src.api.settings import Settings
from src.infrastructure.database import Database, database_connection_pool_resource
from src.infrastructure.http_client import TmdbClient
from src.repositories.movies_repository import MoviesRepository
from src.services.collect_movies_data_service import CollectMoviesDataService


class Container(containers.DeclarativeContainer):
    settings = providers.Singleton(Settings)

    db_connection_pool_resource = providers.Resource(database_connection_pool_resource, settings=settings)
    database = providers.Singleton(Database, connection_pool=db_connection_pool_resource)

    movies_repository = providers.Factory(MoviesRepository)

    tmdb_client = providers.Factory(TmdbClient, settings=settings)

    collect_movies_data_service = providers.Factory(
        CollectMoviesDataService, database=database, movies_repo=movies_repository, tmdb_client=tmdb_client
    )
