from fastapi import FastAPI,Depends,HTTPException,status
from jose import jwt
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext 

app = FastAPI()

SECRET_KEY= "mysecretkey"
ALGORITHM = "HS256"

#password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"])

#OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#lets setup a simple user database with hashed passwords for demonstration purposes
#admin is used in key also in its value for fast lookup, but in real world in sql alchemy we don't have to do so.
fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("1234")
    }
}

#config jwt
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp":expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

#login API [OAUTH2 with password flow]
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    #here the .get() method will check with the key "admin" rather than the value for fast lookup,if matched all the key value pair is placed in user variable.
    user = fake_users_db.get(form_data.username) 
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code = 401,
            detail = "Invalid username or password"
        )

    token = create_token(
        {
        "sub": user["username"] 
        }
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }

#verify token
def verify(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid token"
        )

#secure endpoint that requires authentication
@app.get("/secure")
def secure(user = Depends(verify)):
    return{
        "message":"This is a secure endpoint",
        "user":user
    }

