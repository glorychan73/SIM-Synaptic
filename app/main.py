from fastapi import FastAPI
from app.schemas.item import ItemCreate
from fastapi import FastAPI

from app.core.database import Base, engine
from app.models.item import Item

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Mon API")


@app.get("/")
def read_root():
    return {"message": "Hello, débutant !"}


@app.post("/items")
def create_item(item: ItemCreate):
    return {
        "message": "Item créé avec succès",
        "item": item,
    }

