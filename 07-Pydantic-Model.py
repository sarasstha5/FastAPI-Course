from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#creating schema
# class Schema(BaseModel):
#     name:str
#     age:int
#     email:str
# @app.post("/users")
# def users(user:Schema):
#     return user 

#Nested module
class Contact(BaseModel):
    phone_number:int
    email:str

class Detail(BaseModel):
    name:str
    age:int
    address:str
    contact:Contact

@app.post("/info")
def users(user:Detail):
    return user
