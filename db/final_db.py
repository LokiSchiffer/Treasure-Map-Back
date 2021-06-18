'''from datetime import datetime'''
#from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, DateTime
from sqlalchemy import PrimaryKeyConstraint
import datetime

from db.db_connection import Base, engine

class FinalInDB(Base):
    __tablename__ = "podium"
    
    username = Column(Integer, ForeignKey("users.username"))
    place = Column(Integer, autoincrement=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    PrimaryKeyConstraint(username, place)

Base.metadata.create_all(bind=engine)
'''database_podium = []
generator = {"id" : 0}

def get_user_podium(username : str):
    for podium in database_podium:
        if username == podium.username:
            return podium
    return None

def save_place(final_in_db: FinalInDB):
    generator["id"] = generator["id"] + 1
    final_in_db.place = generator["id"]
    database_podium.append(final_in_db)
    return final_in_db'''