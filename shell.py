from disk import disk_main, write_inventory, write_history, open_history, open_revenue, write_revenue
import core


def greet():
    print('''                       Welcome to 
                  Farspace Rental Company!
The space themed vehicle rental company that reaches for the stars.
''')


def make_inventory():
    inventory = disk_main()
    return inventory


def customer_or_employee(inventory, revenue):
    print('''C - Customer
E - Employee''')
    while True:
        user_input = input('Are you a customer or employee? ').upper().strip()
        if user_input == 'C':
            customer_side(inventory, revenue)
        elif user_input == 'E':
            employee_side(inventory, revenue)
            break
        else:
            print('Try typing in C or E.')


def renting(inventory, revenue):
    while True:
        user_input = input('What do you want to rent?: ').upper().strip()
        check_number = len(inventory)
        if user_input == 'E':
            exit()
        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input in range(0, check_number):
                if core.out_of_stock(inventory, user_input) == True:
                    print('This item is out of stock, try again.')
                else:
                    #inventory stuff
                    inventory[user_input][3] += -1
                    inventory_string = core.make_inventory_string(inventory)
                    write_inventory('inventory.txt', inventory_string)
                    #history stuff
                    history_string = core.make_history_string(
                        inventory[user_input][0], 'Rented')
                    write_history('history.txt', history_string)
                    #revenue stuff
                    core.add_revenue(revenue, inventory[user_input][1],
                                     inventory[user_input][2])
                    revenue_string = core.make_revenue_string(revenue)
                    write_revenue('revenue.txt', revenue_string)
                    break
            else:
                print(
                    'Please type in the number closest to what you want to rent.'
                )
        else:
            print('Please type a number.')


def returning(inventory, revenue):
    while True:
        user_input = input('What do you want to return?: ').upper().strip()
        check_number = len(inventory)
        if user_input == 'E':
            exit()
        elif user_input.isdigit():
            user_input = int(user_input)
            if user_input in range(0, check_number):
                #inventory stuff
                inventory[user_input][3] += 1
                inventory_string = core.make_inventory_string(inventory)
                write_inventory('inventory.txt', inventory_string)
                #history stuff
                history_string = core.make_history_string(
                    inventory[user_input][0], 'Returned')
                write_history('history.txt', history_string)
                #revenue stuff
                core.subtract_revenue(revenue, inventory[user_input][2])
                revenue_string = core.make_revenue_string(revenue)
                write_revenue('revenue.txt', revenue_string)
                break
            else:
                print(
                    'Please type in the number closest to what you want to return.'
                )
        else:
            print('Please type a number.')


def format_return_stuff(inventory):  # not needed in main
    print('Return Item:')
    for item in inventory:
        deposit_cost = item[2] / 10
        index_number = inventory.index(item)
        name = item[0]
        stock = item[3]
        print(f'{index_number} - {name}:')
        print('    - Deposit: $', deposit_cost, sep="")
    print('E - Exit program')


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


def employee_side(inventory, revenue):  # not needed in main
    print('''Actions:
S - See stock
H - Review transaction history
R - Get total revenue
E - Exit''')
    while True:
        user_input = input('What would you like to do?: ').upper().strip()
        if user_input == 'E':
            exit()
        elif user_input == 'S':
            see_stock(inventory)
        elif user_input == 'H':
            contents = open_history('history.txt')
            print(contents)
        elif user_input == 'R':
            print("Revenue: {:.2f}".format(revenue['total']))
        else:
            print('blab')


def see_stock(inventory):
    print('Stock:')
    for item in inventory:
        name = item[0]
        stock = item[3]
        print(f'{name}:')
        print('    - Left in stock: ', stock, sep="")
    print('E - Exit program')


def customer_side(inventory, revenue):  # not needed in main
    pass
    print('''X - Rent
Y - Return''')
    while True:
        user_input = input('Are you renting or returning? ').upper().strip()
        if user_input == 'X':
            format_rent_stuff(inventory)
            renting(inventory, revenue)  # user receipt
            exit()
        elif user_input == 'Y':
            format_return_stuff(inventory)
            returning(inventory, revenue)  # user receipt
            exit()
        else:
            print('Try typing in X or Y.')


def main():
    greet()
    inventory = make_inventory()
    revenue_list = open_revenue('revenue.txt')
    revenue = core.make_revenue_dictionary(revenue_list)
    customer_or_employee(inventory, revenue)


if __name__ == '__main__':
    main()
