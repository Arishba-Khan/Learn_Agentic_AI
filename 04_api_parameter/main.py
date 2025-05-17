from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str = Path(...)):
    return {"item_id" : item_id}

# This is a path parameter — it works like a dynamic URL that changes based on user input.
# A path parameter is included directly in the URL and is used to locate a specific resource.


@app.get("/items")
async def read_item(item_id : str = None):
    return {"item_id" : item_id}

# This is a query parameter — it is included in the URL after a question mark and is used to filter or modify the request.