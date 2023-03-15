from contextlib import asynccontextmanager
from typing import AsyncIterator

import asyncpg
from asyncpg import Pool, Connection
from sqlalchemy import ClauseElement
from sqlalchemy.dialects import postgresql

from src.api.settings import Settings


def compile_sqlalchemy_query(query: ClauseElement) -> str:
    return str(query.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))


class SQLAlchemyConnection(Connection):
    async def execute_sqlalchemy_query(self, query: ClauseElement):
        await self.execute(compile_sqlalchemy_query(query))


async def database_connection_pool_resource(settings: Settings):
    async with asyncpg.create_pool(
        settings.POSTGRES_DATABASE_URI, connection_class=SQLAlchemyConnection
    ) as connection_pool:
        yield connection_pool


class Database:
    def __init__(self, connection_pool: Pool):
        self._connection_pool = connection_pool

    @asynccontextmanager
    async def connection_provider(self) -> AsyncIterator[SQLAlchemyConnection]:
        async with self._connection_pool.acquire() as connection:
            yield connection  # type: ignore

    @asynccontextmanager
    async def transaction_provider(self) -> AsyncIterator[SQLAlchemyConnection]:
        async with self._connection_pool.acquire() as connection:
            transaction = connection.transaction()
            await transaction.start()
            try:
                yield connection  # type: ignore
            except Exception:
                await transaction.rollback()
                raise
            else:
                await transaction.commit()
