from fastapi import Depends, APIRouter
import schemas, database
from sqlalchemy.orm import Session
from repository import userRepository

router = APIRouter(
    prefix="/user",
    tags=['users'])

# create User
@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return userRepository.create(request, db)

# get user, with specific ID
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(database.get_db)):
    return userRepository.show_user(id, db)
