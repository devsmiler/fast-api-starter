from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    return "Hello world"


@app.get("/article/")
def get_articles():
    return {"data": [1,2,3,4,5,6,7,8]}

@app.get("/article/{id}")
def get_article(id=3):
    return {"data": id}

@app.get("/article/{id}/comments")
def get_comments(id):
    return {"data": [1,2,3,4,5]}

