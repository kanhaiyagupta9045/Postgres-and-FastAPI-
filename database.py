from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("URL_STRING")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
