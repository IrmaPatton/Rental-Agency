from core import *
from bcca.test import *


@should_print
def test_format_rent_stuff(output):
    fake_inventory = [['banana', 0, 20, 0], ['apple', 1, 20, 1],
                      ['peanut', 2, 20, 2], ['grape', 3, 20, 3]]
    assert format_rent_stuff(fake_inventory) is None
    assert output == '''Rent Items:
0 - banana:
    - Rental rate: $0
    - Deposit: $2.0
    - Left in stock: 0
1 - apple:
    - Rental rate: $1
    - Deposit: $2.0
    - Left in stock: 1
2 - peanut:
    - Rental rate: $2
    - Deposit: $2.0
    - Left in stock: 2
3 - grape:
    - Rental rate: $3
    - Deposit: $2.0
    - Left in stock: 3
E - Exit program'''


@with_inputs('1')
@should_print
def test_get_rent_input(output):
    fake_inventory = [['banana', 0, 20, 0], ['apple', 1, 20, 1]]
    assert get_rent_input(fake_inventory) == '1'
    assert output == '''What do you want to rent? 1'''
