
from fastapi import FastAPI, APIRouter
import models
from database import engine
import uvicorn
from router import article, user

app = FastAPI()

models.Base.metadata.create_all(engine)
router = APIRouter()
app.include_router(article.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
