#CROS(cross origin resource sharing) - Cros is inforce by the browser. cros will connect the frontend with the backend,
# without cros, frontend send the request but doesn't get the response due to different url or port of backend and frontend

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

#url = http://localhost:1532
origin = ["url of the frontend"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]  #  GET, POST, DELETE, PUT
)

@app.get("/")
def get():
    return{
        "message returned"
    }