from sqlalchemy import String
from typing import Annotated
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


str_50 = Annotated[str, mapped_column(String(50), unique=True, index=True)]


class BaseORM(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
