from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#creating schema
class Schema(BaseModel):
    name:str
    age:int
    email:str
@app.post("/users")
def users(user:Schema):
    return user 