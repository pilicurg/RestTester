#!/usr/bin/python

#test.py

import requests

# r=requests.get("https://api.github.com/user",auth=('',''))
# print r.status_code

# r=requests.request('get',url="https://test.youdata.com/api/login/simulate?email=admin@corp.netease.com",verify=False,headers={})
payload='{"reportId":"3284","query":{"$type":"VisualQuery","column":[{"$type":"DimensionPill","tableId":0,"tableName":"inventory_fact_1997","role":"Dimension","field":"store_id","alias":"store_id","interpretation":"Discrete","dataType":"Whole","isCalc":false,"granularity":"g0","fieldId":"2018","_cid":7}],"row":[{"$type":"MeasurePill","tableId":0,"tableName":"inventory_fact_1997","role":"Measure","field":"store_invoice","alias":"store_invoice","interpretation":"Continuous","dataType":"Decimal","isCalc":false,"aggregator":"SUM","granularity":"g0","fieldId":"2264","_cid":14}],"measures":[],"markMatrix":[],"mark":{"$type":"Mark","marktype":"Automatic","labels":[],"details":[]},"filter":[],"offsetLimit":[0,20]},"options":{"sizeMap":{},"chart":{"limit":20},"referenceline":{},"marksColor":{},"formatMap":{},"sort":{}},"skipCache":true}'

# print r.status_code


s=requests.Session()
r=s.get(url="https://test.youdata.com/api/login/simulate?email=admin@corp.netease.com",verify=False)
print r.status_code
r=s.request(headers={u'charset': u'utf-8', u'Content-Type': u'application/json'},
         url=u'https://test.youdata.com/api/report/query',
         data=payload,
         method=u'POST')

print r.text