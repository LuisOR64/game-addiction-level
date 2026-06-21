from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    config("SQL_CONNECT")
)

#if not database_exists(DATABASE_URL):
#    create_database(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()