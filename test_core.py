from core import make_inventory_string, out_of_stock


def test_make_inventory_string():
    fake_inventory = [['cat', 12, 12, 12], ['done', 1, 1, 1]]
    assert make_inventory_string(
        fake_inventory
    ) == 'Space themed vehicles: rental rate, replacement value, in stock\ncat, 12, 12, 12\ndone, 1, 1, 1\n'


def test_out_of_stock():
    fake_in = [['cat', 12, 12, 0], ['done', 1, 1, 1]]
    assert out_of_stock(fake_in, 0) == True
