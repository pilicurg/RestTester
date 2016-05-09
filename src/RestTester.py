#!usr/bin/python
# RestTester.py
# a controller of this project

import os
import sys
import json
import requests
import Tester

class TestCase(object):
    def __init__(self, params):
        self._params = params
        self.tester = Tester.Tester(self._params.get_value('test'))
        self._name = self._params.get_value('name')
        self._session = None

    def _print_title(self):
        length = 30
        print '-'*length
        print 'Running {}'.format(self._name)
        print '-'*length

    def run(self, session=None):
        self._print_title()
        res = self._make_request(session)
        passed, total = self.tester.test(res.json())
        if passed == total:
            result = "Passed"
        else:
            result = "Failed"
        print "{}/{} passed.".format(passed, total)

        return self._name, result

    def _make_request(self, session):
        if self._params.get_value('type') == 'auth':
            session = requests.Session()
            self._session = session
        return session.request(**self._params.get_params())

    def get_session(self):
        return self._session


class Params(object):
    def __init__(self,
                 method='GET',
                 host='',
                 url='',
                 headers=None,
                 body=None,
                 types='tc',
                 name='unknown',
                 test=None,
                 **kwargs):
        self._method = method
        self._host = host
        self._url = host+url
        self._headers = headers or {}
        self._data = body and json.dumps(body) or {}
        self._type = types
        self._name = name
        self._test = test or {}
        self._others = kwargs

    def get_params(self, key_list=None):
        if key_list is None:
            key_list = ['method', 'url', 'headers', 'data']
        basic_params = {key: getattr(self, '_'+key) for key in key_list}
        if self._type == 'auth':
            return dict(basic_params, **self._others)
        else:
            return basic_params

    def get_value(self, key):
        return getattr(self, '_'+key)

    def get_type(self):
        return self._type


class Parser(object):
    def __init__(self, suite):
        self.host = ''
        self._load_suite(suite)
        self._parsed = []
        self._suite = suite

    def _load_suite(self, suite, list_name="TC_list.json"):
        tc_list = os.path.join(suite, list_name)
        with open(tc_list) as f:
            self.data = json.load(f)

    def _parse_auth(self):
        p = Params(host=self.host,
                   types='auth',
                   name='Authentication',
                   **self.data.get('auth'))
        self._parsed.append(p)

    def _parse_tc(self):
        for tc_name in self.data.get('list'):
            tc_file = os.path.join(self._suite, tc_name)
            with open(tc_file) as tc:
                data = json.load(tc)
            p = Params(host=self.host,
                       types='tc',
                       name=tc_name,
                       **data)
            self._parsed.append(p)

    def parse(self):
        self.host = self.data.get('host', '')
        self._parse_auth()
        self._parse_tc()

        return self._parsed


class Executor(object):
    def __init__(self, test_suite):
        self.parser = Parser(test_suite)
        self.exec_list = []
        self.result = []
        self._factory()

    def _factory(self):
        for params in self.parser.parse():
            self.exec_list.append(TestCase(params))

    def execute(self):
        session = None
        for tc in self.exec_list:
            name, result = tc.run(session)
            self.result.append((name, result))
            session = tc.get_session()

    def get_result(self):
        return self.result


class Reporter(object):
    def __init__(self):
        self._name_title = 'Test Case'
        self._result_title = 'Result'

    def report(self, data):
        self.calc_column_width(data)
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
        self.no_width = 2*(int((len(str(len(data)))+1)/2)) + padding

    def _print_title(self):
        print '{:^{w1}}|{:^{w2}}|{:^{w3}}'.format('No', self._name_title, self._result_title,
                                                 w1=self.no_width,
                                                 w2=self._name_width,
                                                 w3=self._result_width)

    def _print_line(self):
        print '-'*(self.no_width + self._name_width + self._result_width + 2)

    def _print_result(self, data):
        i=1
        for name, result in data:
            print  '{:^{w1}}|{:^{w2}}|{:^{w3}}'.format(i, name, result,
                                                 w1=self.no_width,
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


if __name__ == '__main__':
    debug=True
    if len(sys.argv) > 1 or debug:
        if len(sys.argv)>1:
            tc_folder = sys.argv[1]
        else:
            tc_folder = "TC"
        suite_folder = os.path.normpath(os.path.join(os.path.dirname(__file__), '../%s' % tc_folder))
        rt = RestTester(suite_folder)
        rt.execute()
    else:
        print "Usage: RestTester.py tc_folder_name"



