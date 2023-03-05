import pytest
from async_asgi_testclient import TestClient
from dependency_injector import providers

from src.api.app import app
from src.containers import Container
from tests.mocks import DatabaseMock


@pytest.fixture(scope="session")
def fastapi_app():
    return app


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def client(fastapi_app):
    async with TestClient(fastapi_app) as client:
        yield client


@pytest.fixture
async def database(fastapi_app):
    container: Container = fastapi_app.container
    connection_pool = container.db_connection_pool_resource
    container.database.override(providers.Singleton(DatabaseMock, connection_pool=connection_pool))
    database = await container.database()
    yield database
    await database.close()
