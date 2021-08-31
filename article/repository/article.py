from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
import models, schemas


def all(db: Session):
    articles = db.query(models.Article).all()
    return articles


def get_one(id: int, db: Session):
    article = db.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article id: {id} does not Exsist",
        )
    return article


def create(req: schemas.Article, db: Session):
    new_article = models.Article(title=req.title, body=req.body, user_id=1)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def destory(id: int, db: Session):
    article = db.query(models.Article).filter(models.Article.id == id)

    if not article.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article id: {id} does not Exsist",
        )

    article.delete(synchronize_session=False)
    db.commit()
    return {"data": f"{id} has been deleted got it ?"}


def update(request: schemas.Article, id: int, db: Session):
    article = db.query(models.Article).filter(models.Article.id == id)

    if not article.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article {id} is not Available",
        )
    article.update(request)
    db.commit()
    return "updated"
