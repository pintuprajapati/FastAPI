from pydantic import BaseModel, EmailStr
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str

class UpdateBlog(BaseModel):
    title: Optional[str]
    body: Optional[str]

class ShowBlog(BaseModel):   
    title: str
    body: str
    class Config():
        orm_mode = True
    
# For user registration
class User(BaseModel):
    name: str
    email: EmailStr
    password: str
