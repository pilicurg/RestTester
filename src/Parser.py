#!/usr/bin/python
# Parser.py
# loads json files and parse into Python data types

import os.path
import json

class Parser(object):
    def __init__(self):
        self.list_name = "TC_list.json"
        self._parsed = []
        
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
            d={}
            d['method'] = 'GET'
            d['url'] = self.data.get(u'host').get('url') + self.data.get(u'auth').get('url')

            self._parsed.append(d)

    def _parse_tc(self):
        for tc_name in self.data:
            tc_file = os.path.join(self.suite, tc_name)
            with open(tc_file) as tc:
                tc_data = json.load(tc)

            d={}
            d['method'] = tc_data.get('method','GET')
            d['url'] = tc_data.get('url')
            d['headers'] = tc_data.get('headers')
            d['data'] = tc_data.get('body')
            d['test'] = tc_data.get('test')

            self.

    def parse(self):
        self._parse_auth()
        self._parse_tc()




if __name__ == '__main__':
    p = Parser()

    suite = os.path.normpath(os.path.join(os.path.dirname(__file__),'../TC'))
    p.set_suite(suite)

    print p.get_data()
    print p.parse()