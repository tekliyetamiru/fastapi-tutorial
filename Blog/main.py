from fastapi import Depends, FastAPI, HTTPException,status
from sqlalchemy.orm import Session
from Blog.database import get_db, engine
from Blog import models, schemas
from Blog.hashing import Hash
from Blog.routers import blog, user


app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)


