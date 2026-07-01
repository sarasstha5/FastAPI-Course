from fastapi import FastAPI
app = FastAPI()


@app.post("/users")
# def create_user(name: str , age: int):
#     return{
#         "user": name,
#         "age": age
#     }

def create_user(user: dict):
    return{
        "user": user
    }