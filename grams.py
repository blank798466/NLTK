#coding=utf-8
from nltk.util import ngrams
import codecs

filename1 = 'D:/ZJW/zjw_Python/tangshi/test.txt'
filename2 = 'D:/ZJW/zjw_Python/tangshi/grams.txt'
list_2 = list()
lines1 = codecs.open(filename1,'r',encoding='utf-8')
for line in lines1:
	raw = line.split(' ')
	#print(raw)
	for i in range(1, len(raw)-1):
		grams_raw = ngrams(raw[i], 2)
		for j in grams_raw:
			list_2.append(j)
#print(list_2)

with open(filename2, 'w') as lines:
	for line in list_2:
		lines.write(line[0].encode('utf-8')+line[1].encode('utf-8')+' ')

