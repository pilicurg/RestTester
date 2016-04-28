#!usr/bin/python
# RestTester.py
# a controller of this project

import os
import argparse
from Parser import Parser

class RestTester(object):
    def __init__(self, test_suite):
        self._suite = test_suite

    def show(self):
        print self._parser.get_data()

    def set_parser(self, parser):
        self._parser = parser
        self._parser.set_suite(self._suite)



if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Collect test suite path')
    # parser.add_argument('test suite path', 
    #                     type=str, 
    #                     default='TC'
    #                     help='the path of the test suite being executed.')

    # args = parser.parse_args()
    # print args.accumulate(args.integers)

    p = Parser()

    test_suite_name = 'TC'
    project_dir = os.path.normpath(os.path.join(os.path.dirname(__file__),'..'))
    test_suite = os.path.join(project_dir, test_suite_name)
    
    t = RestTester(test_suite)
    t.set_parser(p)
    t.show()

