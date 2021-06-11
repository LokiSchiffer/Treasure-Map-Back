from pydantic import BaseModel

class GameIn(BaseModel):
    username : str
    rama : str

class GameOut(BaseModel):
    answer : str