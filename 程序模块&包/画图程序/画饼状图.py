import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

myfont=mpl.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc', size=20) #标签字体
mpl.rcParams.update({'font.size': 10}) # 改变刻度所有字体大小，改变其他性质类似

#画饼状图
def plopie(labels, colors, sizes, explode):
	plt.figure(figsize=(10,10)) #调节图形大小，宽，高。通过改变图形大小，可改变文本与图之间的间距
	patches,l_text,p_text = plt.pie(sizes,explode=explode, labels=labels, colors=colors, labeldistance=0.5, autopct='%3.1f%%', shadow=False, startangle=90, pctdistance=0.6)
		#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
		#labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
		#autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
		#shadow，饼是否有阴影
		#startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
		#pctdistance，百分比的text离圆心的距离
	for font in l_text: font.set_fontproperties(myfont) #该中文字体
	for t in l_text: #改变文本的大小；方法是把每一个text遍历。调用set_size方法设置它的属性
		t.set_size=(30)
	for t in p_text:
		t.set_size=(20)
	plt.axis('equal') #设置x，y轴刻度一致，这样饼图才能是圆的
	plt.legend(loc='upper left', prop=myfont) #中文显示prop
	plt.title('地域分布', fontsize=20, fontproperties=myfont)
	#plt.savefig('pie.png')
	plt.show()

labels = ['青海','云南', '四川', '南京'] #定义饼状图的标签，标签是列表
colors = ['red','yellowgreen','lightskyblue','green'] #饼图每个标签的颜色
sizes = [22/36,4/36,9/36,1/36] #每个标签占多大，会自动去算百分比; 22/36, 4/36; 9/36, 1/36
explode = (0.03, 0, 0, 0) #将某部分爆炸出来，使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
plopie(labels, colors, sizes, explode)
