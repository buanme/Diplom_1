from data import DataTest


class TestBun:

    def test_get_name_bun(self, bun):
        assert bun.get_name() == DataTest.TEST_BUN_NAME

    def test_get_price_bun(self, bun):
        assert bun.get_price() == DataTest.TEST_BUN_PRICE
