from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str

class UpdateBlog(BaseModel):
    title: Optional[str]
    body: Optional[str]

