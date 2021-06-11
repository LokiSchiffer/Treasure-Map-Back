from pydantic import BaseModel
from datetime import date, datetime

class FinalIn(BaseModel):
    username : str

class FinalOut(BaseModel):
    username : str
    place : int
    date : datetime