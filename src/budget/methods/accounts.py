from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends

from src.database import database

from src.budget import crud
from src.budget.dependencies import account_by_id
from src.budget.models import Account
from src.budget.schemas import AccountSchema, AccountCreateSchema, AccountPartialUpdateSchema, AccountUpdateSchema



router_accounts = APIRouter(tags=["Accounts"])

@router_accounts.post("/create_account", response_model=AccountSchema, status_code=status.HTTP_201_CREATED)
async def create_account(
        account: AccountCreateSchema,
        session: AsyncSession = Depends(database.scoped_session_dependecy)
    ): 
    return await crud.create_account(session=session, account=account)

@router_accounts.get("/{account_id}", response_model=AccountSchema)
async def get_account(
        account: Account = Depends(account_by_id)
    ) -> Account:
    return account

@router_accounts.put("/{account_id}/")
async def update_account(
    account_update: AccountUpdateSchema,
    account: Account = Depends(account_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy)
):
    return await crud.update_account(session=session, account=account, account_update=account_update)

@router_accounts.patch("/{account_id}/")
async def update_account_partial(
    account_update: AccountPartialUpdateSchema,
    account: Account = Depends(account_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy),
    partial: bool = True
):
    return await crud.update_account(session=session, account=account, account_update=account_update, partial=partial)

@router_accounts.delete("/{account_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_account(
    account: Account = Depends(account_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy)
) -> None:
    await crud.delete_account(session=session, account=account)

@router_accounts.get("/", response_model=list[AccountSchema])
async def get_accounts(session: AsyncSession = Depends(database.scoped_session_dependecy)):
    return await crud.get_accounts(session=session)