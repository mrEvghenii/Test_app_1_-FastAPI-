from sqlalchemy import ForeignKey, Text, String
from typing import Annotated
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    relationship,
    mapped_column,
)
from .Base import BaseORM, str_50

# Структура (схема) подчинения таблиц: MenuORM -> SubmenuORM -> DishRecipeORM


class MainMenuORM(BaseORM):
    __tablename__ = "main_menu_items"

    main_menu_item: Mapped[str_50]

    submenu_items: Mapped[list["SubmenuORM"]] = relationship(
        back_populates="main_menu_items",
        cascade="all, delete",
        passive_deletes=True,
    )


class SubmenuORM(BaseORM):
    __tablename__ = "submenu_items"

    submenu_item: Mapped[str_50]
    main_menu_id: Mapped[int] = mapped_column(
        ForeignKey("main_menu_items.id", ondelete="CASCADE")
    )

    main_menu_items: Mapped["MainMenuORM"] = relationship(
        back_populates="submenu_items",
    )

    dishes: Mapped[list["DishRecipeORM"]] = relationship(
        back_populates="submenu_item",
        cascade="all, delete",
        passive_deletes=True,
    )


class DishRecipeORM(BaseORM):
    __tablename__ = "dish_recipes"

    dish: Mapped[str_50]
    dish_recipe: Mapped[str | None] = mapped_column(Text, nullable=True)

    submenu_items_id: Mapped[int] = mapped_column(
        ForeignKey("submenu_items.id", ondelete="CASCADE")
    )

    submenu_item: Mapped["SubmenuORM"] = relationship(back_populates="dishes")
