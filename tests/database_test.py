import pytest

from data import DataTest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize("index, expected_name, expected_price", DataTest.PARAMETRIZE_AVAILABLE_BUNS)
    def test_available_buns(self, database, index, expected_name, expected_price):
        buns = database.available_buns()
        bun = buns[index]
        assert bun.get_name() == expected_name and bun.get_price() == expected_price

    @pytest.mark.parametrize("index, expected_type, expected_name, expected_price", DataTest.PARAMETRIZE_AVAILABLE_INGREDIENTS)
    def test_available_ingredients(self, database, index, expected_type, expected_name, expected_price):
        ingredients = database.available_ingredients()
        ingredient = ingredients[index]
        assert ingredient.get_type() == expected_type and ingredient.get_name() == expected_name and ingredient.get_price() == expected_price
