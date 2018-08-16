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


def make_history_string(item, action):
    string = "{}, {}\n".format(item, action)
    return string


def make_revenue_dictionary(revenue_list):
    revenue = {}
    for i in revenue_list:
        items = i.split(',')
        key = items[0]
        value = float(items[1])
        revenue[key] = value
    return revenue


def make_revenue_string(revenue):
    for key in revenue:
        string = "{}, {}".format(key, revenue[key])
    return string


def add_revenue(revenue, rate, replacement):
    for key in revenue:
        revenue[key] += rate + (replacement * .10)
    return revenue


def subtract_revenue(revenue, replacement):
    for key in revenue:
        revenue[key] -= (replacement * .10)
    return revenue
