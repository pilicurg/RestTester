#!usr/bin/python


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
        part = res.get(chain.pop(0))
        for section in chain:
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