#!/usr/bin/python
# Factory.py
# an object factory based on TC class

import Parser
import TestCase


class Executor(object):
    def __init__(self, test_suite):
        self.parser = Parser.Parser(test_suite)
        self.exec_list = list()
        self._factory()

    def _factory(self):
        for params in self.parser.parse():
            self.exec_list.append(TestCase.TestCase(params))

    def execute(self):
        # print self.exec_list
        session = None
        for tc in self.exec_list:
            session = tc.run(session)
