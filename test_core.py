from core import *
from bcca.test import *


def test_format_rent_stuff():
    rent_stuff = [[1, 3, 4, 15], [1, 1, 1, 15], [3, 3, 3, 15], [4, 4, 4, 15]]
    assert format_rent_stuff(rent_stuff) == print('''SPACE THEMED VEHICLES
1 - Medium Spaceship:
        - Rental rate for a month: $5000
        - Deposit: $1000
        - Left in stock: 15
2 - Podracers:
        - Rental rate for 5 days: $1000
        - Deposit: $500
        - Left in stock: 15
3 - Space Invader:
        - Rental rate for a week: $4000
        - Deposit: $800
        - Left in stock: 15
4 - Star Destroyer:
        - Rental rate for a 5 days: $10000
        - Deposit: $10000
        - Left in stock: 15''')


@with_inputs
def test_rent_input_check():
    input_str = '3'
    assert rent_input_check(input_str)
