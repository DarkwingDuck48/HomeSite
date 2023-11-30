""" Модуль для хранения путей для конкретного логического узла приложения
    Через роутер настраиваем основную логику запросов, какой запрос что вызывает
    Далее роутер подключается к app в main.py и указывается префикс, при котором будет выполнен запрос
"""

from fastapi import APIRouter

from src.budget.methods.accounts import router_accounts
from src.budget.methods.operations import router_operations
from src.budget.methods.categories import router_categories


router = APIRouter(tags=["Budget"])
router.include_router(router=router_accounts, prefix="/accounts")
router.include_router(router=router_operations, prefix="/operations")
router.include_router(router=router_categories, prefix="/categories")