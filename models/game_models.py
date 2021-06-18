from pydantic import BaseModel

class GameIn(BaseModel):
    username : int
    rama : str

class GameOut(BaseModel):
    answer : str