from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from src.auth.models import User
from src.auth.manager import get_user_manager
from src.auth.auth import auth_backend
from src.auth.schemas import UserRead, UserCreate


router = APIRouter(tags=['Auth'])

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
