#!usr/bin/python


import Tester
import requests
import json
import os.path

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

        if "_comment" in self._others:
            del self._others["_comment"]

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
