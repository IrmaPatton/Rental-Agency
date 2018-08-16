def make_inventory_string(inventory):
    s = 'Space themed vehicles: rental rate, replacement value, in stock\n'
    for item in inventory:
        s += '{}, {}, {}, {}\n'.format(item[0], item[1], item[2], item[3])
    return s


def out_of_stock(inventory, index):
    if inventory[index][3] <= 0:
        return True
    else:
        return False
