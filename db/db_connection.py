from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Ulquiorra91@yggdrassil-cloud.c74snuwjicxg.us-east-2.rds.amazonaws.com:5432/Treasure_map"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
Base.metadata.schema = "firstrun"
