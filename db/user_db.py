from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    name : str
    password: str
    participation: bool
    ceremony: bool

database_users = Dict[str, UserInDB]

database_users = {
    "1018441322" : UserInDB(**{"username" : "1018441322",
                               "name" : "Norberto Mosquera",
                               "password" : "Nomose",
                               "participation" : False,
                               "ceremony" : False}),

    "1010223143" : UserInDB(**{"username" : "1010223143",
                               "name" : "María López",
                               "password" : "Malomo",
                               "participation" : False,
                               "ceremony" : False}),

    "1010223588" : UserInDB(**{"username" : "1010223588",
                               "name" : "Paula Marulanda",
                               "password" : "Pamaal",
                               "Participation" : False,
                               "ceremony" : True}),
}

def get_user(username : str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db