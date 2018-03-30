#coding=utf-8
import codecs
import collections
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

filename1 = 'D:/ZJW/zjw_Python/tangshi/grams.txt'
filename2 = 'D:/ZJW/zjw_Python/tangshi/nltk.txt'
list_2 = list()
lines1 = codecs.open(filename1,'r',encoding='utf-8')
line = lines1.readline()


list_2 = collections.Counter(line.split()).most_common(8000)
#print(list_2)
'''
with open(filename2, 'w') as lines:
	for line in list_2:
		lines.write(line[0].encode('utf-8') + ':' + str(line[1]) +'\n')
'''
color_mask = np.array(Image.open('D:\\ZJW\\zjw_Python\\wordcloud\\demo\\1.jpg'))  # 读取背景图片
cloud = WordCloud(
	# 设置字体，不指定就会出现乱码
	#font_path = os.environ,get("FONT_PATH", os.path.join(os.path.dirname(__file__),"msyh.ttf")),
	prefer_horizontal = 1.0,
	#font_path = path.join(d, "D:\\ZJW\\zjw_Python\\wordcloud\\fonts\\msyh.tff"),
	font_path=r'D:\\ZJW\\zjw_Python\\wordcloud\\fonts\\msyh.ttf',
	# 设置背景色
	background_color='white',
	# 词云形状
	mask=color_mask,
	# 允许最大词汇
	max_words = 3000,
	#color_func=yellow,
	#font_step=1,
	#relative_scaling = 0.8,  # 词频和字体大小的关联性
	# 最大号字体
	#collocations = True,  # 是否包括两个词的搭配
	min_font_size = 5,
	max_font_size = 70
)
word_cloud = cloud.generate(line)  # 产生词云
word_cloud.to_file("qsmy_cloud%d.png" % 1)  # 保存图片
# 显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
plt.close()
