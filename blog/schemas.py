from pydantic import BaseModel, EmailStr
from typing import Optional, List, Union

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True 

class UpdateBlog(BaseModel):
    title: Optional[str]
    body: Optional[str]
    
# For user registration
class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: List[Blog] = []

    class Config():
        orm_mode = True 

class ShowBlog(BaseModel):   
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

# JWT TOKEN Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Union[str, None] = None