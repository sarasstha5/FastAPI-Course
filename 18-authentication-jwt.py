# first install : pip install python-jose (JWT authentication we will use python-jose library.)
from fastapi import FastAPI, Depends, HTTPException, status,Header
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

#create token function to generate JWT token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp":expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

#login endpoint to generate token
@app.post("/login")
def login(username:str, password:str):
    #for simplicity we will use hardcoded username and password
    if username != "admin" and password != "1234":
        raise HTTPException(
            status_code = 401,
            detail = "Invalid username or password"
        )

    token = create_token(
        {
        "sub":username
        }
    )
    return {
        "access_token":token
    }

#verify token function
def verify(token:str= Header(None)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
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
