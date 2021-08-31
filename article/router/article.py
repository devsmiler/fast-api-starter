from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from repository import article
import schemas, database, oauth2

router = APIRouter(prefix="/article", tags=["Articles"])
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowArticle])
def all(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return article.all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(req: schemas.Article, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return article.create(req, db)


@router.get("/{id}")
def get_one(id: int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return article.get_one(id, db)


@router.put("/{id}", status_code=202)
def update(request: schemas.Article, id: int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return article.update(request, id, db)


@router.delete("/{id}", status_code=200)
def destory(id: int, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return article.destory(id, db)
