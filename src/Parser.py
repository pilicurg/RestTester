#!/usr/bin/python
# Parser.py
# load json files and parse into Python data types

import json

test_list = "../testcase/TestList.json"

with open(test_list) as l:
	d = json.load(l)

print d