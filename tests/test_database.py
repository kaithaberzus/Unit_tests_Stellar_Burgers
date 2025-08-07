from prakticum.database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE
from ingredient_types import INGREDIENT_TYPE_FILLING
import pytest


class TestDatabase:

    database = Database()

    @pytest.mark.parametrize('num, bun, price', [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ]
                             )
    def test_available_true(self, num, bun, price):
        av_buns = self.database.available_buns()

        assert len(av_buns) == 3 and av_buns[num].name == bun and av_buns[num].price == price

    @pytest.mark.parametrize('num, name, price, type', [
        (0, "hot sauce", 100, INGREDIENT_TYPE_SAUCE),
        (1, "sour cream", 200, INGREDIENT_TYPE_SAUCE),
        (2, "chili sauce", 300, INGREDIENT_TYPE_SAUCE),
        (3, "cutlet", 100, INGREDIENT_TYPE_FILLING),
        (4, "dinosaur", 200, INGREDIENT_TYPE_FILLING),
        (5, "sausage", 300, INGREDIENT_TYPE_FILLING)
    ]
                             )
    def test_available_ingredients(self, num, name, price, type):
        av_ingr = self.database.available_ingredients()

        assert len(av_ingr) == 6 and av_ingr[num].type == type and av_ingr[num].name == name and av_ingr[num].price == price
