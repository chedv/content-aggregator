import datetime
from dataclasses import dataclass


@dataclass
class TmdbPopularMovie:
    movie_id: int
    popularity_index: float
    vote_average: float
    vote_count: int
    collection_date: datetime.date
