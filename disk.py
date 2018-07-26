def open_file(filename):
    ''' str -> [str]
    Opens file of filename. Returns a list of the line data,
    after the first line.'''

    with open(filename, 'r') as file:
        file.readline()
        file_str_list = file.readlines()
    return file_str_list


def file_list_split(file_str_list):
    file_list = []
    for string in file_str_list:
        new_str = string.strip('\n')
        file_list.append(new_str)
    return file_list


def make_inventory_list(file_list):

    for string in file_list:
        string.split(',')

    return
