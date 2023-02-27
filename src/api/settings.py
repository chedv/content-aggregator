from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    POSTGRES_DATABASE_URI: PostgresDsn
    TMDB_API_KEY_V3: str
