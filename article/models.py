from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    writer = relationship("User", back_populates="articles",)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    articles = relationship("Article", back_populates="writer",)
