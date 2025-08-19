from unittest.mock import patch
from unittest.mock import Mock
from prakticum.burger import Burger


class TestBurger:


    def test_get_price_burger_true(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 250

    def test_get_price_burger_type_of_price_float(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert type(burger.get_price()) == float

    @patch('prakticum.burger.Burger.get_price', return_value = 250)
    def test_get_ricept_true(self, mock_get_burger_price, mock_bun, mock_ingredient):
        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 250"
        )

        assert burger.get_receipt() == expected

    @patch('prakticum.burger.Burger.get_price', return_value=250)
    def test_get_ricept_type_of_ricept_str(self, mock_burger_price, mock_bun, mock_ingredient):
        burger = Burger()

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert type(burger.get_receipt()) == str

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_true(self, mock_ingredient):
        burger = Burger()

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_true(self, mock_ingredient):
        burger = Burger()

        burger.add_ingredient(mock_ingredient)

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 100.0
        mock_ingredient_1.get_name.return_value = "cutlet"
        mock_ingredient_1.get_type.return_value = "FILLING"
        burger.add_ingredient(mock_ingredient_1)

        burger.move_ingredient(0, 1)
        
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient]