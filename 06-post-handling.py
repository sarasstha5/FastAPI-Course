from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


#@app.post("/users")
# def create_user(name: str , age: int):
#     return{
#         "user": name,
#         "age": age
#     }

#using dict: You can also use a dictionary to send data to the server. However, this approach does not provide validation or serialization of the data.
# @app.post("/users")
# def create_user(user: dict):
#     return{
#         "user": user
#     }

#pydantic model: Pydantic models are used to define the structure of the data that is expected in the request body. They provide validation and serialization of the data.
class User(BaseModel):
    name: str
    age: int
    
@app.post("/users")
def create_user(user: User):
    return{
        "user": user
    }