"""
    Entry point for all site packages
"""

from typing import Union

from fastapi import FastAPI

from routers.budget import router as budget_router

from models.models import Base
from models.database import ENGINE


Base.metadata.create_all(bind=ENGINE)


app = FastAPI()

app.include_router(
    router= budget_router,
    prefix='/budget'
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}