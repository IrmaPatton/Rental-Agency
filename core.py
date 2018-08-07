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


def get_rent_input():
    # check if int and right numbers
    # the pick number are the indexes so just check if that index exist
    # check_number is how much things in inventory, it not say zero but count it anyway
    # if user_input is lower or higher than check_number(beside zero) it wrong
    user_input = input('What do you want to rent? ')
    check_number = len(inventory)
    check_number -= 1
    while True:
        if user_input == '0':
            return user_input
        elif user_input < check_number:
            print('Invaded number try again')
        elif user_input > check_number:
            print('Invaded number try again')
        elif user_input not 


def renting(inventory):


def customer_side(inventory):
    print('''X - Rent
Y - Return''')
    while True:
        user_input = input('Are you renting or returning? ')
        if user_input == 'X':
            format_rent_stuff(inventory)
            renting(inventory)
        elif user_input == 'Y':
            here
        else:
            print('Try typing in X or Y.')


def employee_side():
    print('who who')
