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


def rent_input_check():
    #function that checks if input is a number 1 - 5
    while True:
        input_str = input('What do you want to rent?: ')
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
                print('Try again with a number 1 - 5.')
        else:
            print('Try again with a number 1 - 5.')
