from fastapi import FastAPI,Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

#Limiter setup
limiter = Limiter(key_func = get_remote_address)
app.state.limiter = limiter

#Error handler for rate limit exceeded
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request=Request, exc=RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"message": "Rate limit exceeded. Please try again later."},
    )

@app.get("/news")
@limiter.limit("5/minute")  #limit to 5 requests per minute
def get_news(request: Request):
    return {"message": "successfull test for rate limiting"}