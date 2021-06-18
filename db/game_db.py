'''from typing import Dict'''
from pydantic import BaseModel
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String

class GameInDB(BaseModel):
    __tablename__ = "gameq"

    username = Column(Integer, ForeignKey("Users.username"), primary_key=True)
    manada = Column(String)
    tropa = Column(String)
    comunidad = Column(String)
    clan = Column(String)
    jefatura = Column(String)

Base.metadata.create_all(bind=engine)
'''database_game = Dict[str, GameInDB]

database_game = {
    "1018441322" : GameInDB(**{"username" : "1018441322",
                               "manada" : "Norberto Mosquera",
                               "tropa" : "Zulu",
                               "comunidad" : "False",
                               "clan" : "Yggdrasiil",
                               "jefatura" : "clan"}),

    "1010223143" : GameInDB(**{"username" : "1010223143",
                               "manada" : "María López",
                               "tropa" : "Caronte",
                               "comunidad" : "True",
                               "clan" : "Seattle",
                               "jefatura" : "manada"}),

    "1010223588" : GameInDB(**{"username" : "1010223588",
                               "manada" : "Paula Marulanda",
                               "tropa" : "Kiokun",
                               "comunidad" : "Maybe",
                               "clan" : "Windsor",
                               "jefatura" : "tropa"}),
}

def get_answer(username : str, rama : str):
    if username in database_game.keys():
        return database_game[username].dict()[rama]
    else:
        return None'''