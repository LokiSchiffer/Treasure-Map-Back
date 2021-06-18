from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.user_db import UserInDB
from db.game_db import GameInDB

from models.game_models import GameIn, GameOut

router = APIRouter()

@router.get("/game/play/{username}/{rama}")
async def get_user_info(username: str, rama: str, db: Session = Depends(get_db)):
    
    user_in_db = db.query(UserInDB).get(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="La respuesta no existe")
    
    answer_out = GameOut(**{"answer": user_in_db[rama]})
    
    return answer_out