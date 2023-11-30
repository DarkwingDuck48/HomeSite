from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, status, Depends

from src.database import database

from src.budget import crud
from src.budget.dependencies import category_by_id
from src.budget.models import Category
from src.budget.schemas import CategorySchema, CategoryCreateSchema, CategoryPartialUpdateSchema, CategoryUpdateSchema



router_categories = APIRouter(tags=["Categories"])


@router_categories.post("/create_category", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
async def create_category(
        category: CategoryCreateSchema,
        session: AsyncSession = Depends(database.scoped_session_dependecy)
    ): 
    return await crud.create_category(session=session, category=category)

@router_categories.get("/{category_id}", response_model=CategorySchema)
async def get_category(
        category: Category = Depends(category_by_id)
    ) -> Category:
    return category

@router_categories.put("/{category_id}/")
async def update_category(
    category_update: CategoryUpdateSchema,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy)
):
    return await crud.update_category(session=session, category=category, category_update=category_update)

@router_categories.patch("/{category_id}/")
async def update_category_partial(
    category_update: CategoryPartialUpdateSchema,
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy),
    partial: bool = True
):
    return await crud.update_category(session=session, category=category, category_update=category_update, partial=partial)

@router_categories.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category: Category = Depends(category_by_id),
    session: AsyncSession = Depends(database.scoped_session_dependecy)
) -> None:
    await crud.delete_category(session=session, category=category)

@router_categories.get("/", response_model=list[CategorySchema])
async def get_categories(session: AsyncSession = Depends(database.scoped_session_dependecy)):
    return await crud.get_categories(session=session)
