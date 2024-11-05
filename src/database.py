from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,  async_sessionmaker
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, text,  MetaData, URL
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
    # pool_recycle=30,
    # pool_pre_ping=True,
    # pool_use_lifo=True
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,
    # pool_recycle=30,
    # pool_pre_ping=True,
    # pool_use_lifo=True
)

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT version()"))
#     print(f"result: {result=}")


async def get_async_session() -> AsyncSession:
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT version()"))
        print(f"result: {result=}")
