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


def file_list_to_dictionary(file_list):
    for string in file_list:
        for character in string:
            if character == ',':
                index_numb = character.find(',')
            new_str = 
            key = string[:(index_numb - 1)]
            values_in_str = string[(index_numb + 2):]
            #slice numb out
        for 
