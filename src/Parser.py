#!/usr/bin/python
# Parser.py
# load json files and parse into Python data types

import os.path
import json


if __name__ == '__main__':
    project_dir = os.path.join(os.path.dirname(__file__),'..')
    print project_dir
    test_list = os.path.join(project_dir,"/TC/TC_list.json")
    # with open(test_list) as l:
    #     d = json.load(l)
    # print d