from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun.get_name() == 'Булка' and burger.bun.get_price() == 1.25

    def test_add_ingredients(self, burger):
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))
        assert len(burger.ingredients) == 3 and burger.ingredients[0].get_name() == "hot sauce" and burger.ingredients[1].get_type() == "FILLING" and burger.ingredients[2].get_price() == 300

    def test_remove_ingredient(self, burger):
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].get_name() == "hot sauce" and burger.ingredients[1].get_name() == "sausage"

    def test_move_ingredient(self, burger):
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))
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
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300))
        assert burger.get_receipt() == '''(==== Булка ====)
= sauce hot sauce =
= filling cutlet =
= filling sausage =
(==== Булка ====)

Price: 502.5'''

