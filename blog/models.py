# Here we are defining every field that should be in database table
from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    body = Column(String)

    # Added unique constraint to title field
    __table_args__ = (UniqueConstraint('title', name='uq_blog_title'),)