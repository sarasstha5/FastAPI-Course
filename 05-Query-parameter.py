from fastapi import FastAPI
app = FastAPI()

#query parameter: A query parameter is a piece of data sent in the URL after a '?'
@app.get("/users")
def get_user(name: str):
    return{
        "user": name
    }

@app.get("/users")
def get_user(name: str="Guest"):
    return{
        "user": name
    }
       
         