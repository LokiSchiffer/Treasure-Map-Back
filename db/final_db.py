from datetime import datetime
from pydantic import BaseModel

class FinalInDB(BaseModel):
    username : str
    place : int
    date : datetime = datetime.now()

database_podium = []
generator = {"id" : 0}

def save_place(final_in_db: FinalInDB):
    generator["id"] = generator["id"] + 1
    final_in_db.place = generator["id"]
    database_podium.append(final_in_db)
    return final_in_db