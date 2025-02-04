class TestIngredient:

    def test_get_price_ingredient(self, ingredient):
        assert ingredient.get_price() == 5.50

    def test_get_name_ingredient(self, ingredient):
        assert ingredient.get_name() == 'Котлета'

    def test_get_type_ingredient(self, ingredient):
        assert ingredient.get_type() == 'FILLING'
