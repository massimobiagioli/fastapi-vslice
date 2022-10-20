from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi_vslice.conf.settings import settings

SQLALCHEMY_DATABASE_URL = settings.db_url
SQLALCHEMY_DATABASE_TEST_URL = settings.db_test_url

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=settings.session_auto_commit,
    autoflush=settings.session_auto_flush,
    bind=engine
)

Base = declarative_base()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
