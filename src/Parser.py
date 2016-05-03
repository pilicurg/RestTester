#!/usr/bin/python
# Parser.py
# loads json files and parse into Python data types

import os.path
import json


class Parser(object):
    def __init__(self, suite):
        self._load_suite(suite)
        self._parsed = []
        self._suite = suite

    def _load_suite(self, suite, list_name="TC_list.json"):
        tc_list = os.path.join(suite, list_name)
        with open(tc_list) as f:
            self.data = json.load(f)

    def get_data(self):
        return self.data

    def _parse_auth(self):
        if self.data.get('auth'):
            self._insert(self.data.get('auth'), 'auth', 'Authentication')

    def _parse_tc(self):
        for tc_name in self.data.get('list'):
            tc_file = os.path.join(self._suite, tc_name)
            with open(tc_file) as tc:
                data = json.load(tc)
            self._insert(data, 'tc', tc_name)

    def _insert(self, data, types, tc_name=None):
        self._parsed.append(dict(method=data.get('method', 'GET'),
                                 url=self.data.get('host', '') + data.get('url'),
                                 headers=data.get('headers', {}),
                                 data=data.get('body', {}),
                                 test=data.get('test', {}),
                                 type=types,
                                 name=tc_name))

    def parse(self):
        self._parse_auth()
        self._parse_tc()

        return self._parsed


if __name__ == '__main__':
    suite_folder = os.path.normpath(os.path.join(os.path.dirname(__file__), '../TC'))
    print suite_folder
    p = Parser(suite_folder)
    print p.get_data()
    print p.parse()
