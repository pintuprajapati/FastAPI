from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import schemas, database, models, jwt_token
from hashing import Hash

router = APIRouter(
    tags=['authentication']
)

# login user and create JWT authentication token
@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    # if user doesn't match
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Check the username again")
    
    # if password doens't match
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    
    # generate a JWT TOKEN and return it
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
