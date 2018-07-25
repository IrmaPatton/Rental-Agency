def open_file(filename):
    ''' str -> [str]
    Opens file of filename. Returns a list of the line data,
    after the first line.'''

    with open(filename, 'r') as file:
        file.readline()
        file_str_list = file.readlines()
    return file_str


def file_str_list_split(file_str_list):
    for string in file_str_list:
        string.split('\n')
    return file_str_list
