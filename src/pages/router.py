from tkinter.messagebox import RETRY
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from src.budget.methods.accounts import get_accounts, get_account

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")

@router.get("/accounts")
def get_accounts_page(request: Request, accounts = Depends(get_accounts)):
    return templates.TemplateResponse(
        "accounts.html", 
        {
            "request": request, 
            "application": "Budgeting", 
            "accounts": accounts
        }
    )

@router.get("/accounts/{account_id}")
def get_account_page(request: Request, account = Depends(get_account)):
    """Понятно, что нужно править шаблон на более детальный, но принцип получения и передачи параметра в функцию показан"""
    return templates.TemplateResponse(
        "accounts.html", 
        {
            "request": request, 
            "application": "Budgeting", 
            "accounts": [account]
        }
    )