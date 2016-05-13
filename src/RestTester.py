#!usr/bin/python
#
# RestTester.py
# the a controller of this project


import os
import sys
import TestCase

class Executor(object):
    def __init__(self, test_suite):
        self.parser = TestCase.Parser(test_suite)
        self.exec_list = []
        self.result = []
        self._factory()

    def _factory(self):
        for params in self.parser.parse():
            self.exec_list.append(TestCase.TestCase(params))

    def execute(self):
        session = None
        for tc in self.exec_list:
            name, result = tc.run(session)
            self.result.append((name, result))
            session = tc.get_session()

    def get_result(self):
        return self.result

    def verdict(self):
        name, result = zip(*self.result)
        if result and all([x == "Passed" for x in result]):
            return "Passed"
        else:
            return "Failed"

class Reporter(object):
    def __init__(self):
        self._name_title = 'Test Case'
        self._result_title = 'Result'

    def report(self, data):
        self.calc_column_width(data)
        self._print_line()
        self._print_name()
        self._print_line()
        self._print_title()
        self._print_line()
        self._print_result(data)
        self._print_line()

    def calc_column_width(self, data):
        padding = 4
        name, result = zip(*data)
        self._name_width = max(len(self._name_title),len(max(name, key=len))) + padding
        self._result_width = max(len(self._result_title), len(max(result, key=len))) + padding
        self._no_width = 2 * (int((len(str(len(data))) + 1) / 2)) + padding
        self._whole_width = self._no_width + self._name_width + self._result_width + 2

    def _print_title(self):
        print '{:^{w1}}|{:^{w2}}|{:^{w3}}'.format('No', self._name_title, self._result_title,
                                                  w1=self._no_width,
                                                  w2=self._name_width,
                                                  w3=self._result_width)

    def _print_line(self):
        print '-'*self._whole_width

    def _print_name(self):
        print '{:^{w}}'.format('Test Summary', w=self._whole_width)

    def _print_result(self, data):
        i=1
        for name, result in data:
            print  '{:^{w1}}|{:^{w2}}|{:^{w3}}'.format(i, name, result,
                                                       w1=self._no_width,
                                                       w2=self._name_width,
                                                       w3=self._result_width)
            i=i+1

class RestTester(object):
    def __init__(self, test_suite):
        self.executor = Executor(test_suite)
        self.reporter = Reporter()

    def execute(self):
        self.executor.execute()
        self.reporter.report(self.executor.get_result())
        if self.executor.verdict() == "Passed":
            exit(0)
        elif self.executor.verdict() == "Failed":
            exit(1)


if __name__ == '__main__':
    if len(sys.argv)>1:
        tc_folder = sys.argv[1]
        suite_folder = os.path.normpath(os.path.join(os.path.dirname(__file__), '../%s' % tc_folder))
        rt = RestTester(suite_folder)
        rt.execute()
    else:
        print "Usage: RestTester.py tc_folder_name"



