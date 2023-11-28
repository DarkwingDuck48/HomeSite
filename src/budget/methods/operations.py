
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends

from src.database import database

from src.budget import crud
from src.budget.dependencies import operation_by_id
from src.budget.models import Operation
from src.budget.schemas import OperationSchema, OperationCreateSchema, OperationPartialUpdateSchema, OperationUpdateSchema


router_operations = APIRouter(tags=["Operations"])

@router_operations.post("/create_operation", response_model=OperationSchema, status_code=status.HTTP_201_CREATED)
async def create_operation(
        operation: OperationCreateSchema,
        session: AsyncSession = Depends(database.scoped_session_dependecy)
):
    return await crud.create_operation(session=session, operation=operation)

@router_operations.get("/operations/{operation_id}", response_model=OperationSchema)
async def get_operation(
    operation: Operation = Depends(operation_by_id)
) -> Operation:
    return operation

@router_operations.put("/operations/{operation_id}")
async def update_operation(
    operation_update: OperationUpdateSchema,
    operation: Operation = Depends(operation_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy)
):
    return await crud.update_operation(session=session, operation=operation, operation_update=operation_update)

@router_operations.patch("/operations/{operation_id}")
async def update_operation_partial(
    operation_update: OperationPartialUpdateSchema,
    operation: Operation = Depends(operation_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy),
    partial: bool = True
):
    return await crud.update_operation(session=session, 
                                       operation=operation, 
                                       operation_update=operation_update,
                                       partial=partial)

@router_operations.delete("/operations/{operation_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_operation(
    operation: Operation = Depends(operation_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy)
) -> None:
    await crud.delete_operation(session=session, operation=operation)

@router_operations.get("/operations", response_model=list[OperationSchema])
async def get_operations(session: AsyncSession = Depends(database.scoped_session_dependecy)):
    return await crud.get_operations(session=session)