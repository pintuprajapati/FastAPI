from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
import schemas
import models
from hashing import Hash
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
import database

router = APIRouter(
    prefix="/user",
    tags=['users'])

# Create User
@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get user, with specific ID
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    # if user doesn't exist
    if not user:
        content={'success': False, 'message': f"User with id {id} doesn't exist"}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)
    return user
