from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()
def get_item_id(item_id: int = None):
    print("Received item_id:", item_id)  # <-- Add this line
    if item_id is None:
        raise HTTPException(status_code=400, detail="Item ID is required")
        return item_id

def get_token(x_token: str = Header(...)):
    if x_token != "mysecrettoken":
        raise HTTPException(status=403, detail="Invalid or Missing Token")
        return x_token

@app.get("/favorite")
def get_favorite_item(
    token: str = Depends(get_token),
    item_id: int = Depends(get_item_id)
):
    return {
        "user": "authorized",
        "favorite_item": f"Item {item_id}"
    }