from fastapi import FastAPI
from .routers import post, user, auth
from .database import Base, engine
from . import models
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
# models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
