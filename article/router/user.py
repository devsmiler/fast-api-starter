from sqlalchemy.sql.functions import user
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from repository import user

import schemas, database, models
from typing import List
from hashing import Hash

router = APIRouter(prefix="/user", tags=["Users"])

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_one(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)
