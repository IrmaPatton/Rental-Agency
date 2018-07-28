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


def show_what_to_rent(inventory):
    formated_inventory = format_rent_stuff(inventory)
    return formated_inventory


def user_input():
    #function that lets user pick what to rent for exit program


def main():
    greet()
    inventory = make_inventory()
    show_what_to_rent(inventory)


if __name__ == '__main__':
    main()
