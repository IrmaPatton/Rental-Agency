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


def customer_or_employee(inventory):
    # ask if customer or employee and goes to actions based on the input
    print('''C - Customer
E - Employee''')
    while True:
    user_input = input('Are you a customer or employee? ')
    if user_input == 'C':
        customer_side()
    elif user_input == 'E':
        employee_side()
    else:
        print('Try typing in C or E.')


def main():
    greet()
    inventory = make_inventory()


if __name__ == '__main__':
    main()
