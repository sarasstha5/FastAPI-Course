from fastapi import FastAPI,Request, status
from fastapi.responses import JSONResponse

app = FastAPI()
#custom exception handling
# 1. Create custom exception
class ItemNotFoundException(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id
        self.message = f"Item_id not found: {item_id}"

#2. create exception handler
@app.exception_handler(ItemNotFoundException)
async def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"Item_id not found: {exc.item_id}"}
    )

#3. create exception raiser function
@app.get("/users/{item_id}")
def get_user(item_id: int):
    if item_id != 1:
        raise ItemNotFoundException(item_id)      #raise the custom exception if item_id is not 1
    return{
        "item_id": item_id
    }
