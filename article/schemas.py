from pydantic import BaseModel
from typing import List

class ArticleBase(BaseModel):
    title: str
    body: str

class Article(ArticleBase):
    class Config:
        orm_mode = True
class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    articles: List[Article]
    class Config:
        orm_mode = True


class ShowArticle(Article):
    title: str
    body: str
    writer: ShowUser
    class Config:
        orm_mode = True
