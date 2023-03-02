from sqlalchemy import Table, Column, Integer, Float, Date
from sqlalchemy.orm import declarative_base

BaseModel = declarative_base()

TmdbPopularMoviesTable = Table(
    "tmdb_popular_movies",
    BaseModel.metadata,
    Column("movie_id", Integer, primary_key=True),
    Column("popularity_index", Float, nullable=False),
    Column("vote_average", Float, nullable=False),
    Column("vote_count", Integer, nullable=False),
    Column("collection_date", Date, nullable=False),
)
