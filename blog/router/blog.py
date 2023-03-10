from fastapi import Depends, status, Response, APIRouter
from typing import List
import schemas, database, oauth2
from sqlalchemy.orm import Session
from repository import blogRepository
# from oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

# To get the authenticated user
def get_authenticated_user(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return current_user
logged_in_user = get_authenticated_user()

# Create Blog
@router.post('')
def create(request: schemas.Blog, db: Session = Depends(database.get_db), status_code=status.HTTP_201_CREATED, user: schemas.User = logged_in_user):
    return blogRepository.create(request, db)

# Get all blogs
# for python 3.6 and above -> List[Item]
# for python 3.9 and above -> list[Item]
@router.get('', response_model=List[schemas.ShowBlog])
def all_blog(db: Session = Depends(database.get_db), user: schemas.User = logged_in_user):
    return blogRepository.get_all(db)

## we can use like this too
# def all_blog(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blogRepository.get_all(db)

# Get blog, with specific ID
@router.get('/{id}', status_code=200)
def show_blog(id:int, response: Response, db: Session = Depends(database.get_db), user: schemas.User = logged_in_user):
    return blogRepository.show_blog_with_id(id, response, db)

# Delete Blog
@router.delete('/{id}')
def destroy(id:int, db: Session = Depends(database.get_db), user: schemas.User = logged_in_user):
    return blogRepository.destroy(id, db)

# Update Blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request_body: schemas.UpdateBlog, db: Session = Depends(database.get_db), user: schemas.User = logged_in_user):
    return blogRepository.update(id, request_body, db)
