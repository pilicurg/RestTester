#!/usr/bin/python

#test.py

import requests

# r=requests.get("https://api.github.com/user",auth=('',''))
# print r.status_code

# # r=requests.request('get',url="https://test.youdata.com/api/login/simulate?email=admin@corp.netease.com",verify=False,headers={})
# payload='{"reportId":"3284","query":{"$type":"VisualQuery","column":[{"$type":"DimensionPill","tableId":0,"tableName":"inventory_fact_1997","role":"Dimension","field":"store_id","alias":"store_id","interpretation":"Discrete","dataType":"Whole","isCalc":false,"granularity":"g0","fieldId":"2018","_cid":7}],"row":[{"$type":"MeasurePill","tableId":0,"tableName":"inventory_fact_1997","role":"Measure","field":"store_invoice","alias":"store_invoice","interpretation":"Continuous","dataType":"Decimal","isCalc":false,"aggregator":"SUM","granularity":"g0","fieldId":"2264","_cid":14}],"measures":[],"markMatrix":[],"mark":{"$type":"Mark","marktype":"Automatic","labels":[],"details":[]},"filter":[],"offsetLimit":[0,20]},"options":{"sizeMap":{},"chart":{"limit":20},"referenceline":{},"marksColor":{},"formatMap":{},"sort":{}},"skipCache":true}'
#
# # print r.status_code
#
#
# s=requests.Session()
# r=s.get(url="https://test.youdata.com/api/login/simulate?email=admin@corp.netease.com",verify=False)
# print r.status_code
# r=s.request(headers={u'charset': u'utf-8', u'Content-Type': u'application/json'},
#          url=u'https://test.youdata.com/api/report/query',
#          data=payload,
#          method=u'POST')
#
# print r.text

import re
import json

s="result.marksCount"
j="""{"code":200,"message":"","result":{"preSynthesizeResult":{"paneGraphicalDesigns":[[[[{"$type":"HorzScale","encodings":[{"$type":"FieldDescription'","name":"store_id","dataType":"Whole","interpretation":"Discrete","role":"Dimension","pid":"2018``","axisSetting":null,"members":13}]},{"$type":"VertScale","encodings":[{"$type":"FieldDescription","name":"store_invoice","dataType":"Decimal","interpretation":"Continuous","role":"Measure","pid":"2264`SUM`","axisSetting":null,"min-max":[988.8204,16151.0411]}]}],[{"$type":"PartitionedMarkSet","markset":{"$type":"MarkSet","id":"markset-352482","kind":"Bar","retinals":[],"encoding":{"$type":"FieldDescription","name":"@id","dataType":"Whole","interpretation":"Discrete","role":"Dimension","members":[]},"horz-pos":{"placed":{"$type":"HorzScale","encodings":[{"$type":"FieldDescription'","name":"store_id","dataType":"Whole","interpretation":"Discrete","role":"Dimension","pid":"2018``","axisSetting":null,"members":13}]},"encoding":{"$type":"FieldDescription'","name":"store_id","dataType":"Whole","interpretation":"Discrete","role":"Dimension","pid":"2018``","axisSetting":null,"members":13}},"vert-pos":{"placed":{"$type":"VertScale","encodings":[{"$type":"FieldDescription","name":"store_invoice","dataType":"Decimal","interpretation":"Continuous","role":"Measure","pid":"2264`SUM`","axisSetting":null,"min-max":[988.8204,16151.0411]}]},"encoding":{"$type":"FieldDescription","name":"store_invoice","dataType":"Decimal","interpretation":"Continuous","role":"Measure","pid":"2264`SUM`","axisSetting":null,"min-max":[988.8204,16151.0411]}},"subdataset":null,"group-fields":[]},"partitionTuples":[{}]}]]]],"pivotTableConfig":{"$type":"GraphicalPivotTable","marksCount":13,"nTotalCol":13,"colTitleTree":{"title":"store_id","sub":[],"titleList":["store_id"],"fieldNames":[]},"nCol":1,"nPaneRow":1,"datasetSize":13,"nTotalRow":1,"rowTitleTree":{"title":"","sub":[],"titleList":[],"fieldNames":[]},"nPaneCol":1,"paneColTitles":[],"measures":[],"datasetEntire":true,"nRow":1,"paneRowTitles":["store_invoice"]},"smallDatasets":[[[[{"$type":"Cell","empty":false,"nevOptions":{"data":[{"store_id":"2","store_invoice":1049.4587},{"store_id":"3","store_invoice":11659.6249},{"store_id":"6","store_invoice":5132.8974},{"store_id":"7","store_invoice":11634.9186},{"store_id":"11","store_invoice":4042.9596},{"store_id":"13","store_invoice":16151.0411},{"store_id":"14","store_invoice":988.8204},{"store_id":"15","store_invoice":11517.1251},{"store_id":"16","store_invoice":5781.9634},{"store_id":"17","store_invoice":16100.8297},{"store_id":"22","store_invoice":1093.7695},{"store_id":"23","store_invoice":5274.3375},{"store_id":"24","store_invoice":11850.663}]},"order":{"store_id":["2","3","6","7","11","13","14","15","16","17","22","23","24"]}}]]]]},"datasetSize":13,"datasetEntire":true,"marksCount":13}}"""
k=json.loads(j)


def ss(p,delimit):
    prog=re.compile(r'(\w+)((\[\d+\])*)',flags=re.IGNORECASE)
    indexp=re.compile(r'\[\d+\]')

    parts = delimit.split('.')
    left = p
    for part in parts:

        r=prog.match(part)
        print r.groups()
        key = r.group(1)
        index = r.group(2)


        print 'before',left,key,index
        left=left.get(key)
        print 'after',left
        index_list=[]
        if index:
            while True:
                index_prog = indexp.search(index)
                if index_prog is None:
                    break
                else:
                    first_part = index_prog.group(0)
                    index_list.append(int(first_part.strip('[]')))
                    index=index[len(first_part):]
            print index_list
            for i in index_list:
                left=left[int(i)]
    print left


ss(k,s)
