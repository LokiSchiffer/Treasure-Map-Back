from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.user_db import UserInDB
from db.final_db import FinalInDB

from models.final_models import FinalIn, FinalOut

router = APIRouter()

@router.put("/game/final/", response_model=FinalOut)
async def end_game(final_in: FinalIn, db: Session = Depends(get_db)):

    podium = db.query(FinalInDB).get(final_in.username)

    if podium != None:
        raise HTTPException(status_code=403, detail="El usuario ya ha completado el juego")
    
    user_in_db = db.query(UserInDB).get(final_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    final_in_db = FinalInDB(**final_in.dict())
    
    db.add(final_in_db)
    db.commit()
    db.refresh(final_in_db)

    return  final_in_db