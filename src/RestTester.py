#!usr/bin/python
# RestTester.py
# a controller of this project

import os
import sys
import Executor


class RestTester(object):
    def __init__(self, test_suite):
        self.executor = Executor.Executor(test_suite)

    def execute(self):
        self.executor.execute()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        tc_folder = sys.argv[1]
        suite_folder = os.path.normpath(os.path.join(os.path.dirname(__file__), '../%s' % tc_folder))
        rt = RestTester(suite_folder)
        rt.execute()
    else:
        print "Usage: RestTester.py tc_folder_name"



