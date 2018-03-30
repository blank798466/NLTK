#coding=utf-8
from nltk.util import ngrams
import codecs

filename1 = 'D:/ZJW/zjw_Python/tangshi/data.txt'
filename2 = 'D:/ZJW/zjw_Python/tangshi/test.txt'
list_s = list()
lines = codecs.open(filename1,'r',encoding='utf-8')
for line in lines:
	# print(line.encode('utf-8'))
	if u'】' in line:
		raw = line.split(u'】')
		list_s.append(raw[1])
	else:
		continue
'''
	if u'李世民' in line:
		raw = line.split(u'】')
		list_s.append(raw[1])
		'''
'''		
for l in list_s:
	print(l)
'''
with open(filename2, 'w') as lines:
	for line in list_s:
		lines.write(line.encode('utf-8')+'\n')
