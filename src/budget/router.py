"""Модуль для хранения путей для конкретного логического узла приложения
    Через роутер настраиваем основную логику запросов, какой запрос что вызывает
    Далее роутер подключается к app в main.py и указывается префикс, при котором будет выполнен запрос
"""

from fastapi import APIRouter

from src.budget.schemas import Operation

router = APIRouter()

@router.get("/")
def read_root():
    return [
        {
            "id": 1,
            "name": "first"
        }
    ]

@router.get("/{item_id}")
def reat_item(item_id: int):
    return {"item_id": item_id, "name": "Maxim"}


@router.post("/operations")
def add_operation(operation: Operation):
    pass