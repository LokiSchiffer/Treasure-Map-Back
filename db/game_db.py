from typing import Dict
from pydantic import BaseModel

class GameInDB(BaseModel):
    username: str
    manada : str
    tropa : str
    comunidad : str
    clan : str
    jefatura : str

database_game = Dict[str, GameInDB]

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
        return database_game[username][rama]
    else:
        return None