from data import DataTest


class TestIngredient:

    def test_get_price_ingredient(self, ingredient):
        assert ingredient.get_price() == DataTest.TEST_INGREDIENT_PRICE

    def test_get_name_ingredient(self, ingredient):
        assert ingredient.get_name() == DataTest.TEST_INGREDIENT_NAME

    def test_get_type_ingredient(self, ingredient):
        assert ingredient.get_type() == DataTest.TEST_INGREDIENT_TYPE
