from sqlalchemy.ext.asyncio import create_async_engine
from models.contact import Base
import asyncio

DATABASE_URL = "sqlite+aiosqlite:///fastapi-app.db"
engine = create_async_engine(DATABASE_URL, echo=True)

async def reset_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(reset_database())