from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    return "Hello world"


@app.get("/article/")
def get_articles():
    return {"data": [1,2,3,4,5,6,7,8]}

@app.get("/article/{id}")
def get_article(id: int) -> dict:
    return {"data": id}

@app.get("/article/{id}/commen`ts")
def get_comments(id: int) -> dict:
    return {"data": [1,2,3,4,5]}

