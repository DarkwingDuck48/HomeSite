"""
    Entry point for all site packages
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from src.database import database

from src.models import Base
from src.auth.models import User
from src.budget.models import Account, Operation, Category

from src.auth.router import router as auth_router
from src.budget.router import router as budget_router
from src.pages.router import router as pages_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before application start
    async with database.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # after application close

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/", response_class=RedirectResponse, status_code=302)
def redirect_to_pages():
    return "/pages/accounts"

app.include_router(
    router=auth_router,
    prefix='/auth'
)

app.include_router(
    router= budget_router,
    prefix='/budget'
)

app.include_router(
    router=pages_router
)
