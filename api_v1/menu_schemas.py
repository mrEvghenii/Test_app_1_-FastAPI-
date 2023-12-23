from pydantic import BaseModel, ConfigDict, Field


# --- MENU ---
class MainMenuCreate(BaseModel):
    main_menu_item: str = Field(max_length=50)


class MainMenuUpdatePatch(MainMenuCreate):
    main_menu_item: str | None = Field(max_length=50, default=None)


class MainMenu(MainMenuCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0)


# --- Submenu ---
class SubmenuCreate(BaseModel):
    submenu_item: str = Field(max_length=50)
    main_menu_id: int = Field(gt=0)


class SubmenuUpdatePatch(SubmenuCreate):
    submenu_item: str | None = Field(max_length=50, default=None)
    main_menu_id: int | None = Field(gt=0, default=None)


class Submenu(SubmenuCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0)


# --- DishRecipe ---
class DishRecipeCreate(BaseModel):
    dish: str = Field(max_length=50)
    dish_recipe: str | None = Field(max_length=5000, default=None)
    submenu_items_id: int = Field(gt=0)


class DishRecipeUpdatePatch(DishRecipeCreate):
    dish: str | None = Field(max_length=50, default=None)
    dish_recipe: str | None = Field(max_length=5000, default=None)
    submenu_items_id: int | None = Field(gt=0, default=None)


class DishRecipe(DishRecipeCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(gt=0)


class SubmenuRel(Submenu):
    dishes: list["DishRecipe"]


class MainMenuRel(MainMenu):
    submenu_items: list["Submenu"]


class MenuRel(MainMenu):
    submenu_items: list["SubmenuRel"]
