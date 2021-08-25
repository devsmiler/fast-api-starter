from fastapi import FastAPI, Depends, status, Response, HTTPException
from schemas import Article
import schemas
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import uvicorn

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.post("/article", status_code=status.HTTP_201_CREATED)
def create(req: Article, db: Session = Depends(get_db)):
    new_article = models.Article(title=req.title, body=req.body)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


@app.get("/article")
def all(db: Session = Depends(get_db)):
    articles = db.query(models.Article).all()
    return articles


@app.get("/article/{id}")
def all(id: int, response: Response, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article id: {id} does not Exsist",
        )
    return article


@app.put("/article/{id}")
def update(id: int, req: schemas.Article, db: Session = Depends(get_db)):
    # article = db.query(models.Article).filter(models.Article.id == id).update({"title":req.title, "body":req.body})
    print(req)
    t = db.query(models.Article).filter(models.Article.id == id).first()

    # if not article.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"article id :{id} not found")
    # print(article)
    t.update(req)
    # db.commit()
    return "Updated"


@app.delete("/article/{id}", status_code=200)
def destory(id: int, response: Response, db: Session = Depends(get_db)):
    article = (
        db.query(models.Article)
        .filter(models.Article.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    return article

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)