from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """
    Hash the provided plain text password.
    Use bcrypt hashing algorithm for secure password storage.
    Return the hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    """
    Verify if the plain text password matches the hashed password.
    Use bcrypt to compare the passwords securely.
    Return True if they match, otherwise False.
    """
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict):
    """
    Create a JWT access token with an expiration time.
    Encode the provided data along with the expiration timestamp.
    Return the encoded JWT token as a string.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    """
    Decode the provided JWT token to extract the payload.
    Validate the token using the secret key and algorithm.
    Return the 'sub' field from the payload or None if invalid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None