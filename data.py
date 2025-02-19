from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class DataTest:
    # Тестовая булка
    TEST_BUN_NAME = "Булка"
    TEST_BUN_PRICE = 1.25

    # Тестовый ингредиент
    TEST_INGREDIENT_TYPE = INGREDIENT_TYPE_FILLING
    TEST_INGREDIENT_NAME = 'Котлета'
    TEST_INGREDIENT_PRICE = 5.50

    # Тестовые ингредиенты
    TEST_INGREDIENTS = [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]

    # Ожидаемый рецепт
    EXPECTED_RECEIPT = """(==== Булка ====)
= sauce hot sauce =
= filling cutlet =
= filling sausage =
(==== Булка ====)

Price: 502.5"""

    # Ожидаемые цены
    EXPECTED_PRICE_WITHOUT_INGREDIENTS = 2.5
    EXPECTED_PRICE_WITH_INGREDIENT = 8

    PARAMETRIZE_AVAILABLE_BUNS = [(0, "black bun", 100), (1, "white bun", 200), (2, "red bun", 300)]
    PARAMETRIZE_AVAILABLE_INGREDIENTS = [(0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
     (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
     (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
     (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
     (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
     (5, INGREDIENT_TYPE_FILLING, "sausage", 300)]