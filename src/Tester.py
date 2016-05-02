#!usr/bin/python


class Tester(object):
    def __init__(self, test):
        print "from tester", test
        self._test = test

    def test(self, res):
        print 'res', res
        for path, assertion in self._test.iteritems():
            print path, assertion
            elem_value = self._get_elem(res, path)
            for comparator, assert_value in assertion.iteritems():
                getattr(self, "_" + comparator)(path, elem_value, assert_value)

    @staticmethod
    def _get_elem(res, path):
        chain = path.split('.')
        part = res.get(chain.pop(0))
        for section in chain:
            part = part.get(section)

        return part

    def _is(self, name, left, right):
        if left == right:
            print "[PASS] {} is {}".format(name, right)
        else:
            print "[FAIL] {} is {}, not {}".format(name, left, right)

    def _has(self, name, obj, elem):
        if elem in obj:
            print "[PASS] {} has {}".format(name, elem)
        else:
            print "[FAIL] {} does have {}".format(name, elem)

    def _sorted(self, name, array, direction):
        if direction == 'asc':
            if array and all([array[i+1] > array[i] for i in range(len(array)-1)]):
                print "[PASS] {} is in ascending order".format(name)
            else:
                print "[FAIL] {} is not in ascending order".format(name)
        elif direction == 'desc':
            if array and all([array[i+1] < array[i] for i in range(len(array)-1)]):
                print "[PASS] {} is in descending order".format(name)
            else:
                print "[FAIL] {} is not in descending order".format(name)

    def _max(self, name, array, maximum):
        if max(array) == maximum:
            print "[PASS] the maximum of {} is {}".format(name, maximum)
        else:
            print "[FAIL] the maximum of {} is {}, not {}".format(name, max(array), maximum)
