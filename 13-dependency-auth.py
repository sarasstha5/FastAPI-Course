from fastapi import FastAPI, Depends, HTTPException, status,Header

app = FastAPI()

#dependency function
def user():
    return "saras"

@app.get("/users")
def get_user(user = Depends(user)):  #dependency injection using Depends
    return{
        "message":f"Hello {user}"
    }
#reusable dependency function
def get_current_user():
    return "saras"

@app.get("/")
def home(user = Depends(get_current_user)):
    return{
        "message":f"Hello {user}"
    }

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return{
        "message":f"Hello {user}"
    }

@app.get("/about")
def about(user = Depends(get_current_user)):
    return{
        "message":f"Hello {user}"
    }

#auth basic
def verify_token(token:str=Header(None)):
    if token!="saras":
        raise HTTPException(
            status_code = 401,
            detail = "invalid token"
        )
    return{
        "message":"valid token"
    }

@app.get("/auth")
def auth(token = Depends(verify_token)):
    return{
        "user":token
    }
