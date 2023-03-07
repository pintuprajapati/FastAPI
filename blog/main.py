from fastapi import FastAPI
from database import engine
import models
from router import blog, user, authentication

app = FastAPI()

# It will create the table in database
models.Base.metadata.create_all(engine)

# for test case
@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)