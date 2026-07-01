from fastapi import FastAPI
app = FastAPI()

#query parameter: A query parameter is a piece of data sent in the URL after a '?'
@app.get("/users")
def get_user(name: str):
    return{
        "user": name
    }

#default value: You can set a default value for a query parameter by assigning it in the function definition. If the client does not provide a value, the default will be used.
# @app.get("/users")
# def get_user(name: str="Guest"):
#     return{
#         "user": name
#     }

