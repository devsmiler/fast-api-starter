from fastapi import FastAPI
from schemas import Article


app = FastAPI()


@app.post("/article")
def create(req: Article):
    return req
