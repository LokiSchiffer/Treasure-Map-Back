from pydantic import BaseModel

class UserIn(BaseModel):
    username : int
    password : str

class UserOut(BaseModel):
    username : int
    name : str
    ceremony : bool

    class Config:
        orm_mode = True