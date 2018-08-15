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
            customer_side(inventory)
        elif user_input == 'E':
            employee_side()
            break
        else:
            print('Try typing in C or E.')


# functions that deal with printing and inputs
def format_rent_stuff(inventory):
    print('Rent Items:')
    for item in inventory:
        deposit_cost = item[2] / 10
        index_number = inventory.index(item)
        name = item[0]
        rental_cost = item[1]
        stock = item[3]
        print(f'{index_number} - {name}:')
        print('    - Rental rate: $', rental_cost, sep="")
        print('    - Deposit: $', deposit_cost, sep="")
        print('    - Left in stock: ', stock, sep="")
    print('E - Exit program')


def format_rent_stuff(inventory):
    print('Rent Items:')
    for item in inventory:
        deposit_cost = item[2] / 10
        index_number = inventory.index(item)
        name = item[0]
        rental_cost = item[1]
        stock = item[3]
        print(f'{index_number} - {name}:')
        print('    - Rental rate: $', rental_cost, sep="")
        print('    - Deposit: $', deposit_cost, sep="")
        print('    - Left in stock: ', stock, sep="")
    print('E - Exit program')


def employee_side():
    print('I\'m printed here to make shell work.')


def main():
    greet()
    inventory = make_inventory()
    customer_or_employee(inventory)


if __name__ == '__main__':
    main()
