from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Todos_list = []

class Todo(BaseModel):
    Id:int
    Title:str
    completion:bool

@app.post("/todos")
def creat_todo(todo:Todo):
    Todos_list.append(todo)
    return{
        "message":"todo created",
        "data": todo
    }

@app.get("/todos")
def get_todos():
    return{
        "data": Todos_list
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in Todos_list:
        if todo.Id == todo_id:
            return{
                "data":todo
            }
    return{
        "message":"todo not found"
    }