from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.models import MainMenuORM, SubmenuORM, DishRecipeORM
from api_v1.menu_schemas import (
    MainMenuCreate,
    MainMenuUpdatePatch,
    SubmenuCreate,
    SubmenuUpdatePatch,
    DishRecipeCreate,
    DishRecipeUpdatePatch,
    MainMenuRel,
    MenuRel,
)


async def get_entries(
    class_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    session: AsyncSession,
):
    stmt = select(class_orm).order_by(class_orm.id)
    result: Result = await session.execute(stmt)
    obj = result.scalars().all()
    return list(obj)


async def create_entry(
    session: AsyncSession,
    obj_in: MainMenuCreate | SubmenuCreate | DishRecipeCreate,
    class_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
):
    obj = class_orm(**obj_in.model_dump(exclude_unset=True))
    session.add(obj)
    await session.commit()
    return obj


async def get_entry(
    session: AsyncSession,
    class_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    obj_id: int,
):
    return await session.get(class_orm, obj_id)


async def update_entry(
    session: AsyncSession,
    model_orm: MainMenuORM | SubmenuORM | DishRecipeORM,
    obj_update: MainMenuUpdatePatch | SubmenuUpdatePatch | DishRecipeUpdatePatch,
):
    for name, value in obj_update.model_dump(exclude_unset=True).items():
        setattr(model_orm, name, value)
    await session.commit()
    return model_orm


async def delete_entry(
    session: AsyncSession,
    obj: MainMenuORM | SubmenuORM | DishRecipeORM,
) -> None:
    await session.delete(obj)
    await session.commit()


async def get_menu_items(
    session: AsyncSession,
):
    query = select(MainMenuORM).options(
        selectinload(MainMenuORM.submenu_items).selectinload(SubmenuORM.dishes)
    )
    result: Result = await session.execute(query)
    result_orm = result.scalars().all()
    result_sc = [
        MenuRel.model_validate(row, from_attributes=True) for row in result_orm
    ]
    return result_sc
