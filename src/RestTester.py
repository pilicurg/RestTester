#!usr/bin/python
# RestTester.py
# a controller of this project

import os
import argparse
import Executor


class RestTester(object):
    def __init__(self, test_suite):
        self.executor = Executor.Executor(test_suite)
        # self.reporter =

    def execute(self):
        self.executor.execute()


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Collect test suite path')
    # parser.add_argument('test suite path', 
    #                     type=str, 
    #                     default='TC'
    #                     help='the path of the test suite being executed.')

    # args = parser.parse_args()
    # print args.accumulate(args.integers)

    suite_folder = os.path.normpath(os.path.join(os.path.dirname(__file__), '../TC'))
    t = RestTester(suite_folder)
    t.execute()

