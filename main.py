from db.user_db import UserInDB
from db.user_db import update_user, get_user

from db.game_db import GameInDB
from db.game_db import get_answer

from db.final_db import FinalInDB
from db.final_db import save_place, get_user_podium

from models.user_models import UserIn, UserOut
from models.game_models import GameIn, GameOut
from models.final_models import FinalIn, FinalOut

import datetime
from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()


origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "https://yggdrassil-app.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/game/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=406, detail="Información incorrecta")

    return  {"Autenticado": True}

@api.get("/game/info/{username}")
async def get_user_info(username: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out

@api.get("/game/play/{username}/{rama}")
async def play_answer(username: str, rama: str):

    answer = get_answer(username, rama)

    if answer == None:
        raise HTTPException(status_code=404, detail="Respuesta no existe")
    
    answer_out = GameOut(**{"answer": answer})
    
    return answer_out

@api.put("/game/final/")
async def end_game(final_in: FinalIn):

    podium = get_user_podium(final_in.username)

    if podium != None:
        raise HTTPException(status_code=403, detail="El usuario ya ha completado el juego")
    
    user_in_db = get_user(final_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    final_in_db = FinalInDB(**final_in.dict())
    final_in_db = save_place(final_in_db)

    final_out = FinalOut(**final_in_db.dict())

    return  final_out
