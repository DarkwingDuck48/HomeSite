"""
    Entry point for all site packages
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.database import database

from src.models import Base
from src.auth.models import User
from src.budget.models import Account, Operation, Category

from src.auth.router import router as auth_router
from src.budget.router import router as budget_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before application start
    async with database.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # after application close



app = FastAPI(lifespan=lifespan)

app.include_router(
    router=auth_router,
    prefix='/auth'
)

app.include_router(
    router= budget_router,
    prefix='/budget'
)
