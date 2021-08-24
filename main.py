from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Article(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get("/")
def health_check():
    return "Hello world"


@app.get("/article/")
def get_articles(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    return {"data": f"{limit} articles from DB"}


@app.post("/article/")
def create_article(article: Article):
    return {"data": f"Article is created with title as {article.title}"}


@app.get("/article/{id}")
def get_article(id: int):
    return {"data": id}


@app.get("/article/{id}/comments")
def get_comments(id: int = 10):
    return {"data": f"comments: {id}"}
