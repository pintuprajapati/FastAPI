from fastapi import FastAPI
from database import engine
import models
from router import blog, user

app = FastAPI()

# It will create the table in database
models.Base.metadata.create_all(engine)

app.include_router(blog.router)

app.include_router(user.router)