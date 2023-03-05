from contextlib import asynccontextmanager, AbstractAsyncContextManager
from typing import Callable

from asyncpg import Pool
from asyncpg.pool import PoolConnectionProxy


class DatabaseMock:
    def __init__(self, connection_pool: Pool):
        self.connection_pool = connection_pool
        self.connection = None
        self.transaction = None

    @asynccontextmanager
    async def connection_provider(self) -> Callable[..., AbstractAsyncContextManager[PoolConnectionProxy]]:
        if self.connection is None:
            self.connection = await self.connection_pool.acquire()
            self.transaction = self.connection.transaction()
            await self.transaction.start()
        yield self.connection

    @asynccontextmanager
    async def transaction_provider(self) -> Callable[..., AbstractAsyncContextManager[PoolConnectionProxy]]:
        if self.connection is None:
            self.connection = await self.connection_pool.acquire()
            self.transaction = self.connection.transaction()
            await self.transaction.start()
        yield self.connection

    async def close(self):
        if self.connection is not None:
            await self.transaction.rollback()
            await self.connection_pool.release(self.connection)
            self.connection = None
        await self.connection_pool.close()
