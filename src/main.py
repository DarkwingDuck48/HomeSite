"""
    Entry point for all site packages
"""

from typing import Union

from fastapi import FastAPI


from src.budget.router import router as budget_router

from src.database import ENGINE
from src.budget.models import Base



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