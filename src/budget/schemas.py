from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, PositiveInt


class AccountBase(BaseModel):
    
    name: str
    bank: str

class AccountSchema(AccountBase):
    """Returning Account schema"""
    model_config = ConfigDict(from_attributes=True)
    id: int

class AccountCreateSchema(AccountBase):
    """Creating Account schema"""
    pass


class AccountUpdateSchema(AccountBase):
    """Update Account schema"""
    pass

class AccountPartialUpdateSchema(AccountBase):
    """Creating Account schema"""
    name: str | None = None
    bank: str | None = None


class OperationBase(BaseModel):
    operation_date: date = Field(default_factory=datetime.now)
    account_id: PositiveInt
    category_id: PositiveInt
    user_id: PositiveInt
    amount: float = Field(ge=0)


class OperationSchema(OperationBase):
    """Returning Operation schema"""
    model_config = ConfigDict(from_attributes=True)
    id: int

class OperationCreateSchema(OperationBase):
    """Creating Operation schema"""
    pass

class OperationUpdateSchema(OperationBase):
    """Update Operation"""
    pass

class OperationPartialUpdateSchema(OperationBase):
    """Partial Update Operation schema"""
    operation_date: date | None = None
    account_id: PositiveInt | None = None
    category_id: PositiveInt | None = None
    user_id: PositiveInt | None = None
    amount: float | None = None


class CategoryBase(BaseModel):
    """Base Category Model"""
    name: str
    category_limit: float

class CategorySchema(CategoryBase):
    """Returning Category schema"""
    model_config = ConfigDict(from_attributes=True)
    id: int

class CategoryCreateSchema(CategoryBase):
    """Creating Category schema"""
    pass

class CategoryUpdateSchema(CategoryBase):
    """Update Category"""
    pass

class CategoryPartialUpdateSchema(CategoryBase):
    """Partial Update Category schema"""
    name: str | None = None
    category_limit: float | None = None


