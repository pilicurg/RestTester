#!/usr/bin/python
# Parser.py
# loads json files and parse into Python data types

import os.path
import json

class Parser(object):
    def __init__(self):
        self.list_name = "TC_list.json"
        self.parsed = []
        
    def set_suite(self, suite):
        self.suite = suite
        self._load_suite()

    def _load_suite(self):
        tc_list = os.path.join(self.suite, self.list_name)
        with open(tc_list) as f:
            self.data = json.load(f)

    def get_data(self):
        return self.data

    def _parse_auth(self):
        if self.data.get(u'auth'):
            self.parsed.append({'url':self.data.get(u'auth').get('url'),
                                ''



                                })



    def parse(self):
        self._parse_auth()
        self._parse_tc()




if __name__ == '__main__':
    p = Parser()

    suite = os.path.normpath(os.path.join(os.path.dirname(__file__),'../TC'))
    p.set_suite(suite)

    print p.get_data()
    print p.parse()