import schemas, models
from sqlalchemy.orm import Session
from hashing import Hash
from fastapi.responses import JSONResponse
from fastapi import status

# create User
def create(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get user, with specific ID
def show_user(id:int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    # if user doesn't exist
    if not user:
        content={'success': False, 'message': f"User with id {id} doesn't exist"}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=content)
    return user