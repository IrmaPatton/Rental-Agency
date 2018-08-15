from disk import disk_main


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


def get_rent_input(inventory):  # used in renting in core but not here yet
    while True:
        user_input = input('What do you want to rent? ')
        check_number = len(inventory)
        if user_input == 'E':
            exit()
        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input in range(0, check_number):
                return str(user_input)
            else:
                print(
                    'Please type in the number closest to what you want to rent.'
                )
        else:
            print('Please type a number.')


def format_rent_stuff(inventory):  # not needed in main
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


def employee_side():  # not needed in main
    print('I\'m printed here to make shell work.')


def customer_side(inventory):  # not needed in main
    pass
    print('''X - Rent
Y - Return''')
    while True:
        user_input = input('Are you renting or returning? ')
        if user_input == 'X':
            format_rent_stuff(inventory)
            renting(inventory)
            print('Thats all it does, no stock updating.')
            exit()
        elif user_input == 'Y':
            print('I didn\'t get this far')
            exit()
        else:
            print('Try typing in X or Y.')


def main():
    greet()
    inventory = make_inventory()
    customer_or_employee(inventory)


if __name__ == '__main__':
    main()
