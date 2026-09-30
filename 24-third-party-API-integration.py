from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/posts")
def get_all():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

@app.get("/posts/{user_id}")
def get_all(user_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"
    response = requests.get(url)
    return response.json()