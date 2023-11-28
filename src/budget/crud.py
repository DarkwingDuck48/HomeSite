"""
    Base CRUD operations for budget application
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from src.budget.models import Account, Operation
from src.budget.schemas import AccountCreateSchema, AccountUpdateSchema, AccountPartialUpdateSchema
from src.budget.schemas import OperationCreateSchema, OperationUpdateSchema, OperationPartialUpdateSchema


# Accounts CRUD
async def get_accounts(session: AsyncSession) -> list[Account]:
    stmt = select(Account).order_by(Account.id)
    result: Result = await session.execute(stmt)
    accounts = result.scalars().all()
    return list(accounts)

async def get_account(session: AsyncSession, account_id: int) -> Account | None:
    return await session.get(Account, account_id)

async def create_account(session: AsyncSession, account: AccountCreateSchema) -> Account:
    new_account = Account(**account.model_dump())
    session.add(new_account)
    await session.commit()
    await session.refresh(new_account)
    return new_account

async def update_account(
        session: AsyncSession,
        account: Account,
        account_update: AccountUpdateSchema | AccountPartialUpdateSchema, 
        partial: bool = False
    ) -> Account:
    for name, value in account_update.model_dump(exclude_unset=partial).items():
        setattr(account, name, value)
    await session.commit()
    return account

async def delete_account(
        session: AsyncSession, 
        account: Account
) -> None:
    await session.delete(account)
    await session.commit()

# Operations CRUD
async def get_operations(session: AsyncSession) -> list[Operation]:
    stmt = select(Operation).order_by(Operation.operation_date)
    result: Result = await session.execute(stmt)
    operations = result.scalars().all()
    return list(operations)

async def get_operation(session: AsyncSession, operation_id: int) -> Operation | None:
    return await session.get(Operation, operation_id)

async def create_operation(session: AsyncSession, operation: OperationCreateSchema) -> Operation:
    new_operation = Operation(**operation.model_dump())
    session.add(new_operation)
    await session.commit()
    await session.refresh(new_operation)
    return new_operation

async def update_operation(
        session: AsyncSession,
        operation: Operation,
        operation_update: OperationUpdateSchema | OperationPartialUpdateSchema, 
        partial: bool = False
    ) -> Operation:
    for name, value in operation_update.model_dump(exclude_unset=partial).items():
        setattr(operation, name, value)
    await session.commit()
    return operation

async def delete_operation(
        session: AsyncSession, 
        operation: Operation
) -> None:
    await session.delete(operation)
    await session.commit()