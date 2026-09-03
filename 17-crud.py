from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import Boolean, create_engine, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker, declarative_base

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#create table in database named "todos"
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#create API
@app.post("/todos")
def create_todo(title:str, description:str, db:Session = Depends(get_db)):
    todo = Todo(
        title=title,
        description=description,
        completed=False
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message": "Todo created successfully",
        "todo": todo
    }
#read all data from database
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos

#read single data from database
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first() #filter() method is used to filter the results based on a condition. 
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    return {
        "message": "Todo retrieved successfully",
        "todo": todo
    }

#update data in database
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title:str,description:str, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(todo_id == Todo.id).first()
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found"
        )
    todo.title = title
    todo.description = description
    db.commit()
    db.refresh(todo)
    return{
        "message":"todo updated",
        "todo": todo
    }

#delete data from database
@app.delete("/todos/{todo_id}")
def todo_delete(todo_id:int, db:Session= Depends(get_db)):
    todo = db.query(Todo).filter(todo_id == Todo.id).first()
    if todo is None:
        raise HTTPException(
            status_code = 404,
            detail = "todo not found"
        )

    db.delete(todo)
    db.commit()
    return {
        "message": "todo deleted successfully",
        "todo": todo

    }