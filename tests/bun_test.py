class TestBun:

    def test_get_name_bun(self, bun):
        assert bun.get_name() == 'Булка'

    def test_get_price_bun(self, bun):
        assert bun.get_price() == 1.25
