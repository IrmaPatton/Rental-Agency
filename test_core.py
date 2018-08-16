import core


def test_make_inventory_string():
    fake_inventory = [['cat', 12, 12, 12], ['done', 1, 1, 1]]
    assert core.make_inventory_string(
        fake_inventory
    ) == 'Space themed vehicles: rental rate, replacement value, in stock\ncat, 12, 12, 12\ndone, 1, 1, 1\n'


def test_out_of_stock():
    fake_in = [['cat', 12, 12, 0], ['done', 1, 1, 1]]
    assert core.out_of_stock(fake_in, 0) == True


def test_make_history_string():
    assert core.make_history_string('dog', 'returned') == 'dog, returned\n'


def test_make_revenue_dictionary():
    revenue_list = ['total, 0']
    assert core.make_revenue_dictionary(revenue_list) == {'total': 0}


def test_make_revenue_string():
    revenue = {'total': 0}
    assert core.make_revenue_string(revenue) == 'total, 0'


def test_add_revenue():
    revenue = {'total': 0}
    assert core.add_revenue(revenue, 10, 100) == {'total': 20}


def test_subtract_revenue():
    revenue = {'total': 200}
    assert core.subtract_revenue(revenue, 100) == {'total': 190}
