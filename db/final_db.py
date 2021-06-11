from datetime import datetime
from pydantic import BaseModel

class FinalInDB(BaseModel):
    username : str
    place : int = 0
    date : datetime = datetime.now()

database_podium = []
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
    return final_in_db