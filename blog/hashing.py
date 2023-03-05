from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    # Encrypt Password
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    # Decrypt Password
    def verify_password(plain_password, hashed_password):
        return pwd_cxt.verify(plain_password, hashed_password)
