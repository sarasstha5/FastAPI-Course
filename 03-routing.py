from fastapi import FastAPI

app = FastAPI()

#Home route       route is a URL path for any specific page. eg: /home, /about, /contact us . every route has one function.
@app.get("/")    #get let you fetch data from the backend.
def home():
    return{
        "message": "api route to home "
    }

#about page route
@app.get("/about")
def about():
    return{
        "message": "api route to about "
    }

@app.get("/contact-us")
def detail():
    return{
        "detail":[{"name":"saras"},{"name":"samir"}]
    }

