from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

def _build_database_url() -> str:
    if url := os.getenv("DATABASE_URL"):
        return url
    host = os.getenv("PG_HOST", "localhost")
    port = os.getenv("PG_PORT", "5432")
    db   = os.getenv("PG_DATABASE", "postgres")
    user = os.getenv("PG_USER", "postgres")
    pw   = os.getenv("PG_PASSWORD", "")
    return f"postgresql://{user}:{pw}@{host}:{port}/{db}"

DATABASE_URL = _build_database_url()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
