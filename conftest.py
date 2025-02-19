import pytest

from data import DataTest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    database = Database()
    return database


@pytest.fixture
def bun():
    bun = Bun(DataTest.TEST_BUN_NAME, DataTest.TEST_BUN_PRICE)
    return bun


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def ingredient():
    ingredient = Ingredient(DataTest.TEST_INGREDIENT_TYPE, DataTest.TEST_INGREDIENT_NAME, DataTest.TEST_INGREDIENT_PRICE)
    return ingredient


