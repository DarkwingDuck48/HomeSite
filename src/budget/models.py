from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import Float

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from src.models import Base
from src.auth.models import User


class Account(Base):

    name: Mapped[str] = mapped_column(String(120), nullable=False)
    bank: Mapped[str] = mapped_column(String(120), nullable=False)

    def __repr__(self) -> str:
        return f"Account({self.id=}, {self.name=}, {self.bank=})"


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[int] = mapped_column(String(120), nullable=False)
    category_limit: Mapped[float] = mapped_column(Float(3), nullable=True)

    def __repr__(self) -> str:
        return f"Category({self.name=}, {self.category_limit=})"


class Operation(Base):

    operation_date: Mapped[date] = mapped_column(Date)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float(3), nullable=False)
