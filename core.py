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


def get_rent_input(inventory):
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


def renting(inventory):
    pass


def customer_side(inventory):
    pass
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
