#!/usr/bin/python
#encoding:utf8
import sqlite3
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json


NAME = 'skill.xls'

def write_file(file_path,data):   ##写文件
	output = open(file_path,"w")
	output.write('([\n')
	for (k,v) in data.items():
		text = "%d:%s" % (v['cid'],json.dumps(v,ensure_ascii=False))
		text = text.replace(' ','')
		text = text.replace('{','(<')
		text = text.replace('}',',>)')
		text = text.replace('[','({')
		text = text.replace(']',',})')
		text = text.replace('<','[')
		text = text.replace('>',']')
		if isinstance(text, unicode):
			text = text.encode('utf-8')
		output.write(text + ',\n')
	output.write('])\n')
	output.close()

def read_data(file_path):  ##php 读excel文件，将每一行的数据存成键值对
	all_data = {}
	# 打开excel模板文件
	book = xlrd.open_workbook(file_path) 
	# 遍历excel文件中的sheet
#	for shn in range(book.nsheets):
	sh = book.sheet_by_index(0)
	for col in range(sh.ncols):
		name = sh.cell_value(1,col)	##第一行第X列的数据

		if name == '': 
			continue	
		name_str = name.strip()	##作为key，转成字符串

		for row in range(2,sh.nrows):
			val = sh.cell_value(row,col)

			try:
				val = int(val)
			except:
				val = val.strip()
				if val == '':
					continue

			if all_data.get(row,0) == 0:
				all_data[row] = {};

			all_data[row][name_str] = val
	return all_data

def insert_data(file,all_data):
	cx = sqlite3.connect("test.db")

	for data in all_data:
		if file == 'skill.xls':
			sql="insert into test(id,name) values (%d,'%s')"%(int(data[0]),str(data[1])) 
		cx.execute(sql)

	cx.commit()
	cx.close()

def excel_data(file_path):
	all_data = []

	book = xlrd.open_workbook(file_path)
	# 打开excel模板文件
	sh = book.sheet_by_index(0)
	# 遍历excel文件中的sheet
	for row in  range(2,sh.nrows):
		data = sh.row_values(row) 	#某一行数据
		all_data.insert(row-2,data)	#插入数组某个位置

	return all_data

def handle_data(file_name):		##操作文件借口
	in_file = file_name
	out_file = "skill"
	data = read_data(in_file)
	print "read data from",in_file
	write_file(out_file,data)
	print "write data to",out_file
	print
	print len(data),'%s data create success' % file_name
	print '###############写入sqlite数据库##################'
	excel = excel_data(file_name)
	print 
	insert_data(file_name,excel)

if __name__ == "__main__":
	handle_data(NAME)

