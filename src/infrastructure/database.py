from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from src.api.settings import Settings


class Database:
    def __init__(self, settings: Settings):
        self._engine = create_engine(settings.POSTGRES_DATABASE_URI)
        self._session_factory = scoped_session(sessionmaker(bind=self._engine, autoflush=False))

    @contextmanager
    def session_provider(self) -> Callable[..., AbstractContextManager[Session]]:
        session_obj = self._session_factory()
        try:
            yield session_obj
        except Exception:
            session_obj.rollback()
            raise
        finally:
            session_obj.close()
