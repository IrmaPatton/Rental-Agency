from disk import open_file, file_list_split, make_inventory_list, write_inventory, write_revenue, write_history
from bcca.test import fake_file


@fake_file({'mock_file.txt': '''Title:
cat
done
bang'''})
def test_open_file():
    assert open_file('mock_file.txt') == ['cat\n', 'done\n', 'bang']


def test_file_list_split():
    file_str_list = ['cat\n', 'done\n', 'bang']
    assert file_list_split(file_str_list) == ['cat', 'done', 'bang']


def test_make_inventory_list():
    file_list = ['cat, 12, 12, 12', 'done, 1, 1, 1']
    assert make_inventory_list(file_list) == [['cat', 12, 12, 12],
                                              ['done', 1, 1, 1]]


@fake_file({'fake.txt': 'cat, 12, 12, 12'})
def test_write_inventory():
    fake_string = 'duh duh duh'
    with open('fake.txt', 'w') as f:
        f.write(fake_string)
    assert open('fake.txt').read() == 'duh duh duh'


@fake_file({'mock_file.txt': 'i will change'})
def test_write_revenue():
    string = 'I HAVE CHANGED, FEAR ME!'
    with open('mock_file.txt', 'w') as f:
        f.write(string)
    assert open('mock_file.txt').read() == 'I HAVE CHANGED, FEAR ME!'


@fake_file({'fake.txt': 'i am lonely :-(\n'})
def test_write_history():
    string = 'I will be your friend :-D'
    with open('fake.txt', 'a') as f:
        f.write(string)
    assert open('fake.txt').read() == '''i am lonely :-(
I will be your friend :-D'''
