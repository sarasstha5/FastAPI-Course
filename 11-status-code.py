from fastapi import FastAPI, status, HTTPException

app = FastAPI()

#HTTP status codes
@app.get("/status", status_code = status.HTTP_200_OK)
def get_status():
    return {"message": "Request was successful!"}

@app.post("/status", status_code = status.HTTP_201_CREATED)
def create_status():
    return {"message": "Resource created successfully!"}

#Basic Error handling with status codes
#raise immediately stops the function and tells FastAPI: Something went wrong. Send this HTTP error response to the client.
@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(               
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )
    return{
        "user_id": user_id
    }

#custom response
@app.get("/custom_response", status_code = status.HTTP_202_ACCEPTED)
def custom_response():
    return{
        "message": "This is a custom response with a 202 Accepted status code.",
        "status":"202 Accepted",
        "user_id": 1
    }