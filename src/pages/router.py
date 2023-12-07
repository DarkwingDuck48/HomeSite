from tkinter.messagebox import RETRY
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from src.budget.methods.accounts import get_accounts, get_account
from src.budget.methods.operations import get_operations

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="src/templates")

@router.get("/")
def get_def_page(request: Request):
    pass


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

@router.get("/operations")
def get_operations_page(request: Request, accounts=Depends(get_accounts)):
    return templates.TemplateResponse(
        "operations.html",
        {
            "request": request, 
            "application": "Budgeting",
            "accounts": [accounts],
            
        }
    )