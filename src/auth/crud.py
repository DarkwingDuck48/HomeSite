from fastapi import APIRouter, status, Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from src.budget import router

from src.database import database

from src.auth.models import User


async def get_user_db(session: AsyncSession = Depends(database.scoped_session_dependecy)):
    yield SQLAlchemyUserDatabase(session, User)


