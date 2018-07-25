from disk import *
from bcca.test import *


@fake_file({'mock_file.txt': '''Title:
cat
done
bang'''})
def test_open_file():
    assert open_file('mock_file.txt') == ['cat\n', 'done\n', 'bang']


def test_file_list_split():
    file_str_list = ['cat\n', 'done\n', 'bang']
    assert file_list_split(file_str_list) == ['cat', 'done', 'bang']
