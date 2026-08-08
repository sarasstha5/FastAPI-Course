from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:str

# response model is a feature in FastAPI that allows you to define the structure of the-
# -response data that your API endpoints will return. By using a response model,-
# -you can control which fields are included in the response, ensuring that sensitive information (like passwords) is not exposed to clients.
@app.get("/users", response_model=UserResponse)
def get_users():
    return{
        "name": "John Doe",
        "age": "30",
        "password": "secret"  # This field will not be included in the response because of the response_model
    }