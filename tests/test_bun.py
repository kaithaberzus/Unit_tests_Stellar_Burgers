from prakticum.bun import Bun


class TestBun:

    bun = Bun("black bun", 100.0)

    def test_get_name(self):
        assert self.bun.get_name() == "black bun"

    def test_get_price(self):
        assert self.bun.get_price() == 100

    def test_get_name_type_of_name_str(self):
        assert type(self.bun.get_name()) == str

    def test_get_price_type_of_price_float(self):
        assert type(self.bun.get_price()) == float