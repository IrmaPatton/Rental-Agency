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


def change_invent_receipt(number, inventory):  #not completed
    # I'm not changing the inventory text file, i need to
    pass
    if input_str == '5':
        exit()
    elif input_str == '1':
        stock_number = inventory[0][3]
        new_stock_number = stock_number - 1
        inventory[0][3] = new_stock_number
        deposit = 1000
        charged = (inventory[0][1]) * .07
        print(f'''Farspace Rental Company
-Reach for the Stars!-
        Price - ${charged}
        Deposit - ${deposit}
-Don't forget to return it in a month.-''')
    elif input_str == '2':
        stock_number = inventory[1][3]
        new_stock_number = stock_number - 1
        inventory[1][3] = new_stock_number
        deposit = 500
        charged = (inventory[1][1]) * .07
        print(f'''Farspace Rental Company
-Reach for the Stars!-
        Price - ${charged}
        Deposit - ${deposit}
-Don't forget to return it in 5 days.-''')
    elif input_str == '3':
        here
    else:  # if it '4'
        here


def show_what_to_rent(inventory):  # not tested yet
    pass  # going to change format_rent_stuff function to be more any item friendly
    formated_inventory = format_rent_stuff(inventory)
    return formated_inventory


def user_rent_input():  # not tested yet
    pass
    while True:
        input_str = rent_input()
        if rent_input_check(input_str) == None:
            print('''
Try again with a number 1 - 5.''')
        else:
            input_number = input_str
            return input_number


def rent_time(user_number, inventory):  # not completed
    pass
