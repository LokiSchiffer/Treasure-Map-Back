from pydantic import BaseModel
from datetime import datetime

class FinalIn(BaseModel):
    username : str

class FinalOut(BaseModel):
    username : str
    place : int
    date : datetime

    class Config:
        orm_mode = True