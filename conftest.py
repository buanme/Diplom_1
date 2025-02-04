import pytest

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
    bun = Bun('Булка', 1.25)
    return bun


@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def ingredient():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Котлета', 5.50)
    return ingredient


