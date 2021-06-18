from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.game_db import GameInDB

from models.game_models import GameIn, GameOut

router = APIRouter()

@router.get("/game/play/{username}/{rama}")
async def get_user_info(username: str, rama: str, db: Session = Depends(get_db)):
    
    user_in_db = db.query(GameInDB).get(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="La respuesta no existe")
    
    if rama == "manada":
        answer_out = GameOut(**{"answer": user_in_db.manada})
    elif rama == "tropa":
        answer_out = GameOut(**{"answer": user_in_db.tropa})
    elif rama == "comunidad":
        answer_out = GameOut(**{"answer": user_in_db.comunidad})
    elif rama == "clan":
        answer_out = GameOut(**{"answer": user_in_db.clan})
    elif rama == "jefatura":
        answer_out = GameOut(**{"answer": user_in_db.jefatura})
    
    return answer_out