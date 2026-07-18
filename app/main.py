from fastapi import FastAPI

from app.core.database import Base, engine
from app.routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mon API")


@app.get("/")
def read_root():
    return {"message": "Hello, débutant !"}


app.include_router(items.router)