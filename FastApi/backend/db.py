from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase
from sqlalchemy import Column, Integer, String

DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/FastApi"
engine = create_async_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass