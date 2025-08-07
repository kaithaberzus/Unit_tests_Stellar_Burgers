from prakticum.ingredient import Ingredient


class TestIngredient:

    ingredient = Ingredient('SAUCE', "hot sauce", 100.0)

    def test_get_price_true(self):

        assert self.ingredient.get_price() == 100

    def test_get_name_true(self):

        assert self.ingredient.get_name() == "hot sauce"

    def test_get_type_true(self):

        assert self.ingredient.get_type() == 'SAUCE'

    def test_get_price_type_of_price_float(self):

        assert type(self.ingredient.get_price()) == float

    def test_get_name_type_of_name_str(self):

        assert type(self.ingredient.get_name()) == str

    def test_get_type_type_of_type_str(self):

        assert type(self.ingredient.get_type()) == str
