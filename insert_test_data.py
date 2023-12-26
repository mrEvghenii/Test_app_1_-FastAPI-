from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.models.base import BaseORM
from config import settings
from core.models import MainMenuORM, SubmenuORM, DishRecipeORM


sync_engine = create_engine(
    url=settings.url_sync,
    echo=False,
)

session_factory = sessionmaker(sync_engine)


def prepare_database():
    BaseORM.metadata.drop_all(sync_engine)
    print("База данных очищена")
    BaseORM.metadata.create_all(sync_engine)
    print("Добавлены таблицы в базу данных")


def insert_main_menu():
    with session_factory() as session:
        main_dishes_1 = MainMenuORM(main_menu_item="Главные блюда")
        second_dishes_2 = MainMenuORM(main_menu_item="Вторые блюда")
        beverages_3 = MainMenuORM(main_menu_item="Напитки")
        session.add_all([main_dishes_1, second_dishes_2, beverages_3])
        session.commit()


def insert_submenu():
    with session_factory() as session:
        soups_1_1 = SubmenuORM(main_menu_id=1, submenu_item="Супы")
        rolls_1_2 = SubmenuORM(main_menu_id=1, submenu_item="Роллы")
        soups_2_3 = SubmenuORM(main_menu_id=2, submenu_item="Салаты")
        beverages_alc_3_4 = SubmenuORM(
            main_menu_id=3, submenu_item="Алкогольные напитки"
        )
        beverages_noalc_3_5 = SubmenuORM(
            main_menu_id=3, submenu_item="Безалкогольные напитки"
        )
        session.add_all(
            [soups_1_1, rolls_1_2, soups_2_3, beverages_alc_3_4, beverages_noalc_3_5]
        )
        session.commit()


def insert_dish_recipes():
    with session_factory() as session:
        red_borscht_1_1_1 = DishRecipeORM(submenu_items_id=1, dish="Красный борщ")
        roll_california_1_2_2 = DishRecipeORM(
            submenu_items_id=2, dish="Ролл Калифорния", dish_recipe="Рецепт неизвестен"
        )
        soups_proshuto_2_3_3 = DishRecipeORM(
            submenu_items_id=3, dish="Прошутто с микс салатом и моцареллой"
        )
        mahito_alc_3_4_4 = DishRecipeORM(submenu_items_id=4, dish="Алкогольный Махито")
        mahito_noalc_3_5_5 = DishRecipeORM(
            submenu_items_id=5, dish="Безалкогольный Махито"
        )
        mahito_noalc_3_5_6 = DishRecipeORM(submenu_items_id=5, dish="Лимонад")
        session.add_all(
            [
                red_borscht_1_1_1,
                roll_california_1_2_2,
                soups_proshuto_2_3_3,
                mahito_alc_3_4_4,
                mahito_noalc_3_5_5,
                mahito_noalc_3_5_6,
            ]
        )
        session.commit()


prepare_database()
insert_main_menu()
insert_submenu()
insert_dish_recipes()
print("Добавлены данные в таблицы")
