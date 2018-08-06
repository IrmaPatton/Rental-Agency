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


def rent_input():
    rent_str = input('''
What would you like to rent? ''')
    return rent_str


def rent_input_check(input_str):
    if input_str.isdigit():
        if input_str == '1':
            return input_str
        elif input_str == '2':
            return input_str
        elif input_str == '3':
            return input_str
        elif input_str == '4':
            return input_str
        elif input_str == '5':
            return input_str
        else:
            None
    else:
        None


def customer_side():
    pass


def employee_side():
    pass
