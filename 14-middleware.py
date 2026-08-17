from fastapi import FastAPI, Depends, HTTPException, status, middleware,Request

app = FastAPI()
#middleware is a function that runs when client send request and request first goes to middle ware which is like checkpoint not actual endpoint which helps in verifying the request and goes to the actual endpoint function.
#It can be used to perform tasks such as logging, authentication, and modifying the request or response.

@app.middleware("http")
async def middleWare(request:Request,call_next):
    print("1. Request reached middleware from client")

    response = await call_next(request)  #this will call the next middleware or the actual endpoint function. It will return a response object.

    print("4. Response came back to middleware")

    return response

@app.get("/user")
def get_user():
    print("2. Request reached endpoint function")
    return{
        "message":"Hello user"
    }

