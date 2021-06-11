from db.user_db import UserInDB
from db.user_db import update_user, get_user

from db.game_db import GameInDB
from db.game_db import get_answer

from db.final_db import FinalInDB
from db.final_db import save_place

from models.user_models import UserIn, UserOut
from models.game_models import GameIn, GameOut
from models.final_models import FinalIn, FinalOut

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()


@api.post("/user/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=406, detail="Información incorrecta")

    return  {"Autenticado": True}

@api.get("/user/info/{username}")
async def get_user_info(username: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out
