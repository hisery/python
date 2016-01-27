#!/usr/bin/python
#-*-encoding:utf8
#version:2.7.6

import pymongo
import csv
import imp
import sys
imp.reload(sys)
sys.setdefaultencoding('utf-8') #设置默认编码,只能是utf-8,下面\u4e00-\u9fa5要求的

dbs = ["hctc-game-001"]
table_name = 'finance'
file_name = 'csvtest.csv'
keys = ['name','time','lvl']
##链接mongodb数据库
conn = pymongo.MongoClient('127.0.0.1', 27017)

for dbase in dbs:

	##选择具体的数据库
	db = conn[dbase]
	
	##数据库的某张表
	col = db[table_name]

	csvfile = file(file_name, 'wb')
	writer = csv.writer(csvfile)
	#writer.writerow(['id', 'url', 'keywords'])

	count = len(keys)
	for data in col.find():

		arr = []
		for i in range(count):
			arr.insert(i, data[keys[i]])

		writer.writerow(arr)
csvfile.close()
