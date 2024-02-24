from typing import Union

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import get_db

app = FastAPI()


@app.get("/")
def read_root(db: Session = Depends(get_db)):
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}