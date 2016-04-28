#!/usr/bin/python

#test.py

import requests

r=requests.get("https://api.github.com/user",auth=('',''))
print r.status_code