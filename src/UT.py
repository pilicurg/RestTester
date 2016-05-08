import unittest
import RestTester


class TestParams(unittest.TestCase):
    def setUp(self):
        self._data = {'url': '/api/test',
                      'type': 'tc',
                      'name': 'UT'}
        self.p = RestTester.Params()

    def test_get_value(self):
        method = self.p.get_value('method')
        self.assertEqual(method, 'GET')

    def test_get_value2(self):
        method = self.p.get_params_for_request()
        self.assertIn('url', method)
        self.assertIn('headers', method)
        self.assertIn('data', method)
        self.assertIn('method', method)


class TestTestCase(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
