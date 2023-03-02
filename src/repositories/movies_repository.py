from dataclasses import asdict

from asyncpg.pool import PoolConnectionProxy
from sqlalchemy import insert

from src.models.movie_models import TmdbPopularMovie
from src.repositories.models import TmdbPopularMoviesTable


class MoviesRepository:
    async def insert_tmdb_popular_movies(self, connection: PoolConnectionProxy, movies: list[TmdbPopularMovie]):
        insert_stmt = insert(TmdbPopularMoviesTable).values([asdict(movie) for movie in movies])
        await connection.execute_sqlalchemy_query(insert_stmt)
