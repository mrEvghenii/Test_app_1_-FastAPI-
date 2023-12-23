from httpx import AsyncClient


async def test_data_insert_main_menu(ac: AsyncClient):
    main_dishes_1 = await ac.post(
        "/api/v1/main_menu/", json={"main_menu_item": "Главные блюда"}
    )
    assert main_dishes_1.status_code == 201
    assert main_dishes_1.json()["id"] == 1

    second_dishes_2 = await ac.post(
        "/api/v1/main_menu/",
        json={"main_menu_item": "Вторые блюда"},
    )

    assert second_dishes_2.status_code == 201

    beverages_3 = await ac.post(
        "/api/v1/main_menu/",
        json={"main_menu_item": "Напитки"},
    )

    assert beverages_3.status_code == 201


async def test_data_insert_submenu(ac: AsyncClient):
    soups_1_1 = await ac.post(
        "/api/v1/submenu/",
        json={"main_menu_id": 1, "submenu_item": "Супы"},
    )
    rolls_1_2 = await ac.post(
        "/api/v1/submenu/",
        json={"main_menu_id": 1, "submenu_item": "Роллы"},
    )
    soups_2_3 = await ac.post(
        "/api/v1/submenu/",
        json={"main_menu_id": 2, "submenu_item": "Салаты"},
    )
    beverages_alc_3_4 = await ac.post(
        "/api/v1/submenu/",
        json={"main_menu_id": 3, "submenu_item": "Алкогольные напитки"},
    )
    beverages_noalc_3_5 = await ac.post(
        "/api/v1/submenu/",
        json={"main_menu_id": 3, "submenu_item": "Безалкогольные напитки"},
    )

    assert soups_1_1.status_code == 201
    assert rolls_1_2.status_code == 201
    assert soups_2_3.status_code == 201
    assert beverages_alc_3_4.status_code == 201
    assert beverages_noalc_3_5.status_code == 201


async def test_data_insert_dish_recipes(ac: AsyncClient):
    red_borscht_1_1_1 = await ac.post(
        "/api/v1/dish_recipe/",
        json={"submenu_items_id": 1, "dish": "Красный борщ"},
    )
    roll_california_1_2_2 = await ac.post(
        "/api/v1/dish_recipe/",
        json={
            "submenu_items_id": 2,
            "dish": "Ролл Калифорния",
            "dish_recipe": "Рецепт неизвестен",
        },
    )
    soups_proshuto_2_3_3 = await ac.post(
        "/api/v1/dish_recipe/",
        json={"submenu_items_id": 3, "dish": "Прошутто с микс салатом и моцареллой"},
    )
    mahito_alc_3_4_4 = await ac.post(
        "/api/v1/dish_recipe/",
        json={"submenu_items_id": 4, "dish": "Алкогольный Махито"},
    )
    mahito_noalc_3_5_5 = await ac.post(
        "/api/v1/dish_recipe/",
        json={"submenu_items_id": 5, "dish": "Безалкогольный Махито"},
    )
    mahito_noalc_3_5_6 = await ac.post(
        "/api/v1/dish_recipe/",
        json={"submenu_items_id": 5, "dish": "Лимонад"},
    )

    assert red_borscht_1_1_1.status_code == 201
    assert roll_california_1_2_2.status_code == 201
    assert soups_proshuto_2_3_3.status_code == 201
    assert mahito_alc_3_4_4.status_code == 201
    assert mahito_noalc_3_5_5.status_code == 201
    assert mahito_noalc_3_5_6.status_code == 201
