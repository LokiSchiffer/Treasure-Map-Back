from pydantic import BaseModel
from datetime import datetime

class FinalIn(BaseModel):
    username : int

class FinalOut(BaseModel):
    username : int
    place : int
    date : datetime

    class Config:
        orm_mode = True