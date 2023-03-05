# Here we are defining every field that should be in database table
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from database import Base
from sqlalchemy.orm import relationship



class Blog(Base):
    __tablename__ = 'blogs'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Added unique constraint to title field
    __table_args__ = (UniqueConstraint('title', name='uq_blog_title'),)

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
