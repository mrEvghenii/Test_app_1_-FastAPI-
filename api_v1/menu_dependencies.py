from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db
from core.models import MainMenuORM, SubmenuORM, DishRecipeORM
from .menu_crud import get_entry


async def row_by_id(
    obj_id: Annotated[int, Path()],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
    class_orm: Annotated[MainMenuORM, SubmenuORM, DishRecipeORM],
):
    obj = await get_entry(session=session, obj_id=obj_id, class_orm=class_orm)
    if obj is not None:
        return obj

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Object by ID: {obj_id} - NOT FOUND!",
    )


async def menu_by_id(
    menu_id: Annotated[int, Path()],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
) -> MainMenuORM:
    return await row_by_id(
        obj_id=menu_id,
        session=session,
        class_orm=MainMenuORM,
    )


async def submenu_by_id(
    submenu_id: Annotated[int, Path()],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
) -> SubmenuORM:
    return await row_by_id(
        obj_id=submenu_id,
        session=session,
        class_orm=SubmenuORM,
    )


async def dish_recipe_by_id(
    dish_recipe_id: Annotated[int, Path()],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
) -> DishRecipeORM:
    return await row_by_id(
        obj_id=dish_recipe_id,
        session=session,
        class_orm=DishRecipeORM,
    )


# async def menu_by_id(
#     menu_id: Annotated[int, Path()],
#     session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
# ) -> MenuORM:
#     menu = await crud.get_menu_item(session=session, menu_id=menu_id)
#     if menu is not None:
#         return menu
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"Munu by ID: {menu_id} - NOT FOUND!",
#     )
#
#
# async def submenu_by_id(
#     submenu_id: Annotated[int, Path()],
#     session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
# ) -> SubmenuORM:
#     submenu = await crud.get_submenu_item(session=session, submenu_id=submenu_id)
#     if submenu is not None:
#         return submenu
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"Submenu by ID: {submenu_id} - NOT FOUND!",
#     )
#
#
# async def dish_recipe_by_id(
#     dish_recipe_id: Annotated[int, Path()],
#     session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
# ) -> DishRecipeORM:
#     dish_recipe = await crud.get_dish_recipe(
#         session=session, dish_recipe_id=dish_recipe_id
#     )
#     if dish_recipe is not None:
#         return dish_recipe
#
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"Dish and Recipe by ID: {dish_recipe_id} - NOT FOUND!",
#     )
