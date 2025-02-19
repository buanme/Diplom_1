from data import DataTest


class TestBurger:

    def add_test_ingredients(self, burger):
        for ingredient in DataTest.TEST_INGREDIENTS:
            burger.add_ingredient(ingredient)

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun.get_name() == DataTest.TEST_BUN_NAME and burger.bun.get_price() == DataTest.TEST_BUN_PRICE

    def test_add_ingredients(self, burger):
        self.add_test_ingredients(burger)
        assert (len(burger.ingredients) == len(DataTest.TEST_INGREDIENTS) and
               burger.ingredients[0].get_name() == DataTest.TEST_INGREDIENTS[0].get_name() and
               burger.ingredients[1].get_type() == "FILLING" and
               burger.ingredients[2].get_price() == DataTest.TEST_INGREDIENTS[2].get_price())

    def test_remove_ingredient(self, burger):
        self.add_test_ingredients(burger)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].get_name() == "hot sauce" and burger.ingredients[1].get_name() == "sausage"

    def test_move_ingredient(self, burger):
        self.add_test_ingredients(burger)
        burger.move_ingredient(2,0)
        assert burger.ingredients[0].get_name() == "sausage" and burger.ingredients[1].get_name() == "hot sauce"

    def test_get_price_burger_without_ingredient(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == 2.5

    def test_get_price_burger_with_ingredients(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 8

    def test_get_receipt(self, burger, bun):
        burger.set_buns(bun)
        self.add_test_ingredients(burger)
        assert burger.get_receipt() == DataTest.EXPECTED_RECEIPT
