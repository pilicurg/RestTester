#!usr/bin/python
# RestTester.py
# a controller of this project

import os
import sys
import json
import requests


class TestCase(object):
    def __init__(self, params):
        self._params = params
        self.tester = Tester(self._params.pop('test'))
        self._name = self._params.pop('name', 'no_name')

    def _print_title(self):
        length = 30
        print '-'*length
        print 'Running {}'.format(self._name)
        print '-'*length

    def run(self, session=None):
        self._print_title()
        if self._params.get('type') == 'auth':
            del self._params['type']
            session = requests.Session()
            res = session.request(**self._params)
            # print 'auth', res
        elif self._params.get('type') == 'tc':
            del self._params['type']
            res = session.request(**self._params)
            print 'tc', res.text
        print self.tester.test(res.json())
        return session

class Params(object):
    def __init__(self, **kwargs):
        self._data = self._build(**kwargs)

    def _build(self,**kwargs):
        self._method = kwargs.setdefault('method','GET')
        self._url = kwargs.get('host') + kwargs.setdefault('method','GET')

    def request(self):
        pass



class Parser(object):
    def __init__(self, suite):
        self._load_suite(suite)
        self._parsed = []
        self._suite = suite

    def _load_suite(self, suite, list_name="TC_list.json"):
        tc_list = os.path.join(suite, list_name)
        with open(tc_list) as f:
            self.data = json.load(f)

    def _parse_auth(self):
        if self.data.get('auth'):
            self._insert(self.data.get('auth'), 'auth', 'Authentication')

    def _parse_tc(self):
        for tc_name in self.data.get('list'):
            tc_file = os.path.join(self._suite, tc_name)
            with open(tc_file) as tc:
                data = json.load(tc)
            self._insert(data, 'tc', tc_name)

    def _insert(self, data, types, tc_name=''):
        d = dict(method=data.pop('method', 'GET'),
                                 url=self.host + data.pop('url'),
                                 headers=data.pop('headers',{}),
                                 data=json.dumps(data.pop('body',{})),
                                 test=data.pop('test', {}),
                                 type=types,
                                 name=tc_name)
        self._parsed.append(dict(d, **data))

    def parse(self):
        self.host = self.data.get('host','')
        self._parse_auth()
        self._parse_tc()

        return self._parsed


class Executor(object):
    def __init__(self, test_suite):
        self.parser = Parser(test_suite)
        self.exec_list = list()
        self._factory()

    def _factory(self):
        for params in self.parser.parse():
            self.exec_list.append(TestCase(params))

    def execute(self):
        # print self.exec_list
        session = None
        for tc in self.exec_list:
            session = tc.run(session)

class RestTester(object):
    def __init__(self, test_suite):
        self.executor = Executor(test_suite)

    def execute(self):
        self.executor.execute()


class Tester(object):
    def __init__(self, test):
        self._test = test

    def test(self, res):
        passed = 0
        total = 0
        for path, assertion in self._test.iteritems():
            elem_value = self._get_elem(res, path)
            for comparator, assert_value in assertion.iteritems():
                total = total+1
                if getattr(self, "_" + comparator)(path, elem_value, assert_value):
                    passed = passed+1

        return "{}/{} passed.".format(passed, total)

    def _get_elem(self, res, path):
        chain = path.split('.')
        print chain
        part = res.get(chain.pop(0))
        print part
        for section in chain:
            print part, section
            part = part.get(section)

        return part

    def _is(self, name, left, right):
        if left == right:
            print "[PASS] {} is {}".format(name, right)
            return True
        else:
            print "[FAIL] {} is {}, not {}".format(name, left, right)
            return False

    def _has(self, name, obj, elem):
        if elem in obj:
            print "[PASS] {} has {}".format(name, elem)
            return True
        else:
            print "[FAIL] {} does have {}".format(name, elem)
            return False

    def _sorted(self, name, array, direction):
        if direction == 'asc':
            if array and all([array[i+1] > array[i] for i in range(len(array)-1)]):
                print "[PASS] {} is in ascending order".format(name)
                return True
            else:
                print "[FAIL] {} is not in ascending order: {}".format(name, array)
                return False

        elif direction == 'desc':
            if array and all([array[i+1] < array[i] for i in range(len(array)-1)]):
                print "[PASS] {} is in descending order".format(name)
                return True
            else:
                print "[FAIL] {} is not in descending order: {}".format(name, array)
                return False

    def _max(self, name, array, maximum):
        if max(array) <= maximum:
            print "[PASS] the maximum of {} is {}".format(name, maximum)
            return True
        else:
            print "[FAIL] the maximum of {} is {}, not {}".format(name, max(array), maximum)
            return False

    def _min(self, name, array, minimum):
        if min(array) >= minimum:
            print "[PASS] the minimum of {} is {}".format(name, minimum)
            return True
        else:
            print "[FAIL] the minimum of {} is {}, not {}".format(name, min(array), minimum)
            return False


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



