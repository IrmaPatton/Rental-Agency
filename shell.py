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


def user_rent_input():
    while True:
        input_str = rent_input()
        if rent_input_check(input_str) == None:
            print('''
Try again with a number 1 - 5.''')
        else:
            input_number = input_str
            return input_number


#def rent_time(user_number, inventory):
#    number = user_number blab blab blabs


def main():
    greet()
    inventory = make_inventory()
    show_what_to_rent(inventory)
    user_number = user_rent_input()


if __name__ == '__main__':
    main()
