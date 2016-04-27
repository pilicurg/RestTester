#!usr/bin/python
# RestTester.py
# a controller of this project

import os
from Parser import Parser


def get_list_file():
    file_name = "TC/TC_list.json"

    project_dir = os.path.normpath(os.path.join(os.path.dirname(__file__),'..'))
    list_file = os.path.normpath(os.path.join(project_dir, file_name))

    return list_file

def main():
    list_file = get_list_file()

    p = Parser(list_file)
    p.encode()

if __name__ == '__main__':
    main()



