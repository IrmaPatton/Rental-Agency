from core import *
from disk import *


def greet():
    print('''                       Welcome to 
                  Farspace Rental Company!
The space themed vehicle rental company that reaches for the stars.
  ''')


def make_inventory():
    inventory = disk_main()
    return inventory


def customer_or_employee():
    # ask if customer or employee and goes to actions based on the input


def main():
    greet()
    inventory = make_inventory()


if __name__ == '__main__':
    main()
