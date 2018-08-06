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


def renting(inventory):
    here


def customer_side(inventory):
    print('''X - Rent
Y - Return''')
    while True:
        user_input = input('Are you renting or returning? ')
        if user_input == 'X':
            format_rent_stuff(inventory)
            here
        elif user_input == 'Y':
            here
        else:
            print('Try typing in X or Y.')


def employee_side():
    print('who who')
