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


def file_list_dictionary_setup(file_list):
    for string in file_list:

        for character in string:
            if character == ',':
                index_numb = character.find(',')
            key = string[:(index_numb - 1)]
            values_new_str = string[(index_numb + 1):]

        for character in values_new_str:
            if character == ',':
                index_numb = character.find(',')
            rental_rate = int(values_new_str[:(index_numb - 1)])
            values_str = values_new_str[(index_numb + 1):]

        for character in values_str:
            if character == ',':
                index_numb = character.find(',')
            replace_value = int(values_str[(index_numb - 1):])
            in_stock_str = values_str[(index_numb + 1):]
            in_stock = int(in_stock_str)
            setup_list = [key, rental_rate, replace_value, in_stock]
    return setup_lists
