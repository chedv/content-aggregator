from dataclasses import asdict

from sqlalchemy import insert

from src.infrastructure.database import SQLAlchemyConnection
from src.models.movie_models import TmdbPopularMovie
from src.repositories.models import TmdbPopularMoviesTable


class MoviesRepository:
    async def insert_tmdb_popular_movies(self, connection: SQLAlchemyConnection, movies: list[TmdbPopularMovie]):
        insert_stmt = insert(TmdbPopularMoviesTable).values([asdict(movie) for movie in movies])
        await connection.execute_sqlalchemy_query(insert_stmt)
