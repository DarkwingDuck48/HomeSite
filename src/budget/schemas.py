from datetime import date, datetime
from pydantic import BaseModel, Field, PositiveInt


class User(BaseModel):
    user_id: PositiveInt
    name: str
    telegramID: str



class Operation(BaseModel):
    id: int
    operation_date: date = Field(default_factory=datetime.now)
    account_id: PositiveInt
    category_id: PositiveInt
    user_id: PositiveInt
    amount: float = Field()
