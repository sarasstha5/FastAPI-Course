from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Todos_list = []

class Todo(BaseModel):
    Id:int
    Title:str
    completion:bool

#create todo
@app.post("/todos")
def creat_todo(todo:Todo):
    Todos_list.append(todo)
    return{
        "message":"todo created",
        "data": todo
    }

#get all list of todos
@app.get("/todos")
def get_todos():
    return{
        "data": Todos_list
    }

#get sepecific todo using query parameter
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

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,t in enumerate(Todos_list):
        if t.Id == todo_id:
            Todos_list[index] = updated_todo
            return{
                "message":"todo updated",
                "data": updated_todo
            }
    return{
        "message":"todo not found"
    }