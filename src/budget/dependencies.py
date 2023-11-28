from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import database
from src.budget.models import Account, Operation

from src.budget import crud


async def account_by_id(
        account_id = Annotated[int, Path],
        session: AsyncSession = Depends(database.scoped_session_dependecy)
    ) -> Account:
    account = await crud.get_account(session=session, account_id=account_id)
    if account:
        return account
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Account with {account_id} is not found"
    )

async def operation_by_id(
        operation_id = Annotated[int, Path],
        session: AsyncSession = Depends(database.scoped_session_dependecy)
) -> Operation:
    operation = await crud.get_operation(session=session, operation_id=operation_id)
    if operation:
        return operation
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Account with {operation_id} is not found"
    )