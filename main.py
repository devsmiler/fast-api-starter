from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    return "Hello world"


@app.get("/article/{id}")
def this_is_world(id=3):
    return {"data": id}
