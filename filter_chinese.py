#!/usr/bin/python
#coding=utf-8 
import imp 
import sys 
imp.reload(sys) 
sys.setdefaultencoding('utf-8') #设置默认编码,只能是utf-8,下面\u4e00-\u9fa5要求的
import re   


#pchinese=re.compile(ur'([\u4e00-\u9fa5]+)+?') #判断是否为中文的正则表达式
files = ["language_ch.json","config.json"]
temp = {}
for file_data in files:
	pchinese=re.compile(u'[^\u4E00-\u9FA5]')
	f=open(file_data) #打开要提取的文件

	for line in f.readlines():   #循环读取要读取文件的每一行
		line=line.decode('utf-8')#普通字符串转成unicode字符串
		str2=pchinese.sub(r' ', line)#replace
		str2=str2.replace(" ","")
		###########过滤掉重复的中文字体###########
		for char in list(str2):
			str3=''.join(char)
			temp[str3] = 1
fw = open("2.txt","w")
for key in temp.keys():
	fw.write(key)

f.close()
fw.close()#打开的文件记得关闭哦!
