from fastapi import APIRouter, status, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated

from core.models import MainMenuORM, SubmenuORM, DishRecipeORM
from api_v1 import menu_crud
from api_v1.menu_schemas import (
    MainMenu,
    MainMenuCreate,
    MainMenuUpdatePatch,
    Submenu,
    SubmenuCreate,
    SubmenuUpdatePatch,
    DishRecipe,
    DishRecipeCreate,
    DishRecipeUpdatePatch,
    MainMenuRel,
    MenuRel,
)
from core.database import db
from api_v1.menu_dependencies import menu_by_id, submenu_by_id, dish_recipe_by_id


#
#
# ------Main Menu------
main_menu_router = APIRouter(prefix="/main_menu", tags=["Main Menu"])


@main_menu_router.get(
    "/",
    response_model=list[MainMenu],
)
async def get_main_menu_items(
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)]
):
    return await menu_crud.get_entries(
        session=session,
        class_orm=MainMenuORM,
    )


@main_menu_router.post(
    "/",
    response_model=MainMenu,
    status_code=status.HTTP_201_CREATED,
)
async def create_main_menu_item(
    menu_in: MainMenuCreate,
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.create_entry(
        session=session,
        obj_in=menu_in,
        class_orm=MainMenuORM,
    )


@main_menu_router.get(
    "/{menu_id}/",
    response_model=MainMenu,
)
async def get_main_menu_item(
    menu_id: int,
    session: Annotated[AsyncSession, Depends(menu_by_id)],
):
    return await menu_crud.get_entry(
        session=session,
        obj_id=menu_id,
        class_orm=MainMenuORM,
    )


@main_menu_router.patch(
    "/{menu_id}/",
    response_model=MainMenu,
)
async def update_main_menu_item(
    menu_update: MainMenuUpdatePatch,
    menu: Annotated[MainMenu, Depends(menu_by_id)],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.update_entry(
        session=session,
        model_orm=menu,
        obj_update=menu_update,
    )


@main_menu_router.delete(
    "/{menu_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Deleting an item also deletes all related items in other tables!",
)
async def delete_main_menu_item(
    menu: Annotated[MainMenu, Depends(menu_by_id)],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.delete_entry(
        session=session,
        obj=menu,
    )


#
#
# ------Submenu------
submenu_router = APIRouter(prefix="/submenu", tags=["Submenu"])


@submenu_router.get(
    "/",
    response_model=list[Submenu],
)
async def get_submenu_items(
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)]
):
    return await menu_crud.get_entries(
        session=session,
        class_orm=SubmenuORM,
    )


@submenu_router.post(
    "/",
    response_model=Submenu,
    status_code=status.HTTP_201_CREATED,
)
async def create_submenu_item(
    submenu_in: SubmenuCreate,
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.create_entry(
        session=session,
        obj_in=submenu_in,
        class_orm=SubmenuORM,
    )


@submenu_router.get(
    "/{submenu_id}/",
    response_model=Submenu,
)
async def get_submenu_item(
    submenu_id: int,
    session: Annotated[AsyncSession, Depends(submenu_by_id)],
):
    return await menu_crud.get_entry(
        session=session,
        obj_id=submenu_id,
        class_orm=SubmenuORM,
    )


@submenu_router.patch(
    "/{submenu_id}/",
    response_model=Submenu,
)
async def update_submenu_item(
    submenu_update: SubmenuUpdatePatch,
    submenu: Annotated[Submenu, Depends(submenu_by_id)],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.update_entry(
        session=session,
        model_orm=submenu,
        obj_update=submenu_update,
    )


@submenu_router.delete(
    "/{submenu_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Deleting an item also deletes all related items in other tables!",
)
async def delete_submenu_item(
    submenu: Annotated[Submenu, Depends(submenu_by_id)],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.delete_entry(
        session=session,
        obj=submenu,
    )


#
#
# ------Dish and Recipe------
dish_recipe_router = APIRouter(prefix="/dish_recipe", tags=["Dish and Recipe"])


@dish_recipe_router.get(
    "/",
    response_model=list[DishRecipe],
)
async def get_dish_recipe_items(
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)]
):
    return await menu_crud.get_entries(
        session=session,
        class_orm=DishRecipeORM,
    )


@dish_recipe_router.post(
    "/",
    response_model=DishRecipe,
    status_code=status.HTTP_201_CREATED,
)
async def create_dish_recipe_item(
    dish_recipe_in: DishRecipeCreate,
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.create_entry(
        session=session,
        obj_in=dish_recipe_in,
        class_orm=DishRecipeORM,
    )


@dish_recipe_router.get(
    "/{dish_recipe_id}/",
    response_model=DishRecipe,
)
async def get_dish_recipe_item(
    dish_recipe_id: int,
    session: Annotated[AsyncSession, Depends(dish_recipe_by_id)],
):
    return await menu_crud.get_entry(
        session=session,
        obj_id=dish_recipe_id,
        class_orm=DishRecipeORM,
    )


@dish_recipe_router.patch(
    "/{dish_recipe_id}/",
    response_model=DishRecipe,
)
async def update_dish_recipe_item(
    dish_recipe_update: DishRecipeUpdatePatch,
    dish_recipe: Annotated[DishRecipe, Depends(dish_recipe_by_id)],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.update_entry(
        session=session,
        model_orm=dish_recipe,
        obj_update=dish_recipe_update,
    )


@dish_recipe_router.delete(
    "/{dish_recipe_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Deleting an item also deletes all related items in other tables!",
)
async def delete_dish_recipe_item(
    dish_recipe: Annotated[DishRecipe, Depends(dish_recipe_by_id)],
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)],
):
    return await menu_crud.delete_entry(
        session=session,
        obj=dish_recipe,
    )


#
#
# ------Combined Menu------
get_combined_menu_router = APIRouter(prefix="/menu", tags=["Combined Menu"])


@get_combined_menu_router.get(
    "/",
    response_model=list[MenuRel],
)
async def get_combined_menu_items(
    session: Annotated[AsyncSession, Depends(db.scoped_session_dependency)]
):
    return await menu_crud.get_menu_items(
        session=session,
    )


html_router = APIRouter(prefix="/index", tags=["Menu"])


@html_router.get("/", response_class=HTMLResponse)
async def read_all_items():
    return """
    <!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="utf-8">

    <link href="https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/9.10.2/jsoneditor.css" rel="stylesheet" type="text/css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jsoneditor/9.10.2/jsoneditor.min.js"></script>
</head>
<body>
    <div style="display: flex; justify-content: center;">
        <div id="jsoneditor" style="width: 1200px; height: 650px;"></div>
    </div>
<script>
    // create the editor
    var container = document.getElementById("jsoneditor");
    var editor = new JSONEditor(container);

    // set json
    async function setJSON () {
        const response = await fetch('http://localhost:8000/api/v1/menu/');
        const data = await response.json()
        editor.set(data);
    }

    // get json
    function getJSON() {
        var json = editor.get();
        alert(JSON.stringify(json, null, 2));
    }

    document.addEventListener('DOMContentLoaded', function(event) {
        setJSON()
    });
</script>
</body>
</html>
    """
