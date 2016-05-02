#!/usr/bin/python
# TestCase.py
# a base class of a test case

import Tester
import requests


class TestCase(object):
    def __init__(self, params):
        self._params = params
        self.tester = Tester.Tester(self._params.pop('test'))
        self._attr_list = ['method', 'url', 'headers', 'data', 'test', 'type']

    def run(self, session=None):
        if self._params.get('type') == 'auth':
            # s = requests.Session()
            # r = s.request(**self._params)
            r={
                "show": "a",
                "pro": {
                    "p": {"q": {"S": "T"}},
                    "S": "T"
                },
                "sort": [1, 2, 3, 4],
                "status_code": 200
               }
            self.tester.test(r)
            # return s
            print 'a'
            return 'a'
        elif self._params.get('type') == 'tc':
            # r = session.request(**self._params)

            r={
                "show": "a",
                "pro": {
                    "p": {"q": {"S": "T"}},
                    "S": "T"
                },
                "sort": [1, 2, 5, 4],
                "status_code": 200
               }

            self.tester.test(r)
            # return session
            print 'tc'
            return 'tc'

if __name__ == '__main__':
    info = {'headers': None, 'test': None, 'url': u'http://10.0.0.0/api/simulate',
            'data': None, 'type': 'auth', 'method': 'GET'}
    tc = TestCase(info)
    tc.run()
