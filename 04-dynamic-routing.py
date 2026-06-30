from fastapi import FastAPI 
app = FastAPI()

#dynamic routing
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return{
        "user":user_id
    }