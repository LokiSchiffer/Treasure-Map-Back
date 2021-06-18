'''from typing import Dict'''
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean

from db.db_connection import Base, engine

class UserInDB(BaseModel):
    __tablename__ = "users"
    
    username = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    password = Column(String)
    ceremony = Column(Boolean)

Base.metadata.create_all(bind=engine)
'''database_users = Dict[str, UserInDB]

database_users = {
    "1018441322" : UserInDB(**{"username" : "1018441322",
                               "name" : "Norberto Mosquera",
                               "password" : "Nomose",
                               "ceremony" : False}),

    "1010223143" : UserInDB(**{"username" : "1010223143",
                               "name" : "María López",
                               "password" : "Malomo",
                               "ceremony" : False}),

    "1010223588" : UserInDB(**{"username" : "1010223588",
                               "name" : "Paula Marulanda",
                               "password" : "Pamaal",
                               "ceremony" : True}),
}

def get_user(username : str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db'''