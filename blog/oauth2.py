from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
import jwt_token

# this is the route from where fastapi will fetch the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    jwt_token.verify_token(token, credentials_exception)
    