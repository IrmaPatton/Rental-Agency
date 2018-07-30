def format_rent_stuff(inventory):
    print('''SPACE THEMED VEHICLES
1 - Medium Spaceship:
        - Rental rate for a month: $5000
        - Deposit: $1000
        - Left in stock: {}
2 - Podracers:
        - Rental rate for 5 days: $1000
        - Deposit: $500
        - Left in stock: {}
3 - Space Invader:
        - Rental rate for a week: $4000
        - Deposit: $800
        - Left in stock: {}
4 - Star Destroyer:
        - Rental rate for a 5 days: $10000
        - Deposit: $10000
        - Left in stock: {}
5 - Exit program'''.format(inventory[0][3], inventory[1][3], inventory[2][3],
                           inventory[3][3]))


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


def change_invent_receipt(number, inventory):
    # I'm not changing the inventory text file, i need to
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
