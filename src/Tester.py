#!usr/bin/python

import re


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
                if getattr(self, "_" + comparator)(path.encode('utf-8'), elem_value, assert_value):
                    passed = passed+1

        return passed, total

    def _get_elem(self, res, path):
        "addressing elements within nested dictionary by dotted notation"
        p_parts = re.compile(ur'([()+\-\w\u4e00-\u9fff]+)((\[\d+\])*)')
        p_index = re.compile(ur'\[\d+\]')
        parts = path.split('.')

        bulk = res
        for part in parts:
            matched = p_parts.match(part)

            # dictionary part
            key = matched.group(1)
            bulk = bulk.get(key)

            # list part
            index = matched.group(2)
            index_list = []
            if index:
                while True:
                    index_matched = p_index.search(index)
                    if index_matched is None:
                        break
                    else:
                        first_index = index_matched.group(0)
                        index_list.append(int(first_index.strip('[]')))
                        index=index[len(first_index):]
                for i in index_list:
                    bulk = bulk[int(i)]
        return bulk

    def _unify_format(self, token):
        if type(token) is unicode:
            return token.encode('utf-8')
        else:
            return str(token)

    def _equals(self, name, left, right):
        if left == right:
            print "{} equals {}".format(name, self._unify_format(right))
            return True
        else:
            print "[**FAIL**] {} equals {}, not {}".format(name, self._unify_format(left), self._unify_format(right))
            return False

    def _has(self, name, obj, elem):
        if elem in obj:
            print "{} has {}".format(name, self._unify_format(elem))
            return True
        else:
            print "[**FAIL**] {} does have {}".format(name, self._unify_format(elem))
            return False

    def _sorted(self, name, array, direction):
        if direction == 'asc':
            if array and all([float(array[i+1]) > float(array[i]) for i in range(len(array)-1)]):
                print "{} is in ascending order".format(name)
                return True
            else:
                print "[**FAIL**] {} is not in ascending order: {}".format(name, self._unify_format(array))
                return False

        elif direction == 'desc':
            if array and all([float(array[i+1]) < float(array[i]) for i in range(len(array)-1)]):
                print "{} is in descending order".format(name)
                return True
            else:
                print "[**FAIL**] {} is not in descending order: {}".format(name, self._unify_format(array))
                return False

    def _max(self, name, array, maximum):
        if max(array) <= maximum:
            print "the maximum of {} is {}".format(name, self._unify_format(maximum))
            return True
        else:
            print "[**FAIL**] the maximum of {} is {}, not {}".format(name, max(array), self._unify_format(maximum))
            return False

    def _min(self, name, array, minimum):
        if min(array) >= minimum:
            print "the minimum of {} is {}".format(name, self._unify_format(minimum))
            return True
        else:
            print "[**FAIL**] the minimum of {} is {}, not {}".format(name, min(array), self._unify_format(minimum))
            return False
