from datetime import date
from typing import Optional
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import Float

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    telegramID: Mapped[Optional[str]]
    owned_accounts: Mapped[List["Accounts"]] = relationship(back_populates="owner")
    user_operations: Mapped[List["Operations"]] = relationship(back_populates="user_id")

    def __repr__(self) -> str:
        return f"User({self.id=}, {self.name=}, {self.telegramID=})"


class Accounts(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    bank: Mapped[str] = mapped_column(String(120), nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["Users"] = relationship(back_populates="owned_accounts")

    def __repr__(self) -> str:
        return f"Account({self.id=}, {self.name=}, {self.bank=}, {self.owner=})"


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(120), nullable=False)
    limit: Mapped[float] = mapped_column(Float(3), nullable=True)

    def __repr__(self) -> str:
        return f"Category({self.name=}, {self.limit})"


class Operations(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(primary_key=True)
    operation_date: Mapped[date] = mapped_column(Date)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    amount: Mapped[float] = mapped_column(Float(3), nullable=False)
    user: Mapped["Users"] = relationship(back_populates="user_operations")
