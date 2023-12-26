import asyncio
from typing import AsyncGenerator
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession

from alembic.versions.main import app
from config import settings
from core.models.base import BaseORM
from sqlalchemy.orm import sessionmaker

from core.database import db


sync_engine = create_engine(
    url=settings.url_sync,
    echo=False,
)

sync_session_factory = sessionmaker(sync_engine)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.get_scoped_session() as session:
        yield session


@pytest.fixture(autouse=True, scope="session")
def prepare_database():
    BaseORM.metadata.drop_all(sync_engine)
    BaseORM.metadata.create_all(sync_engine)
    # yield
    # Base.metadata.drop_all(sync_engine)


@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
