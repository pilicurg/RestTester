#!/usr/bin/python
# Parser.py
# loads json files and parse into Python data types

import os.path
import json

class Parser(object):
    def __init__(self, list_file):
        self._d = {}
        with open(list_file) as f:
            self._data = json.load(f)

    def _tc_files(self):
         return self._data.get(u'list',[])

    def get_data(self):
        return self._data

    def encode(self):
        for tc in self._tc_files():
            tc_name = os.path.basename(tc)
            self._d[tc_name] = {}


if __name__ == '__main__':
    
    file_name = "TC/TC_list.json"
    project_dir = os.path.normpath(os.path.join(os.path.dirname(__file__),'..'))
    list_file = os.path.normpath(os.path.join(project_dir, file_name))

    p = Parser(list_file)
    p.encode()