#!/usr/bin/env python
# coding:utf-8

import numpy as np
from Tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import Series, DataFrame
import pandas as pd
from sklearn.linear_model import LinearRegression
import tkMessageBox
import tkFont
from tkFileDialog import *
import os

# ----------------------------------------------------------------------
def TrainModel(X_train, y_train, X_test, y_test):
	if var_option.get()=="model1":
		model = LinearRegression(normalize=True)
	elif var_option.get() == "model2":
		model = LinearRegression(normalize=True)
	elif var_option.get() == "model3":
		model = LinearRegression(normalize=True)
	else:
		model = LinearRegression(normalize=True)
	model.fit(X_train, y_train)
	y_predict = model.predict(X_test)
	return y_predict

# 生成测试集与训练集
def Requiem(tw1, tw2, dur):
	tf6 = "dataSets\\training\\volume(table 6)_training.csv"
	t6 = pd.read_csv(tf6)
	tft6 = "dataSets\\testing_phase1\\volume(table 6)_test1.csv"
	tt6 = pd.read_csv(tft6)

	# 删除Table 6中的无效信息
	t6.drop(['vehicle_model', 'has_etc', 'vehicle_type'], axis=1, inplace=True)
	tt6.drop(['vehicle_model', 'has_etc', 'vehicle_type'], axis=1, inplace=True)

	# 将表按收费站编号分开
	# 合并训练集和测试集
	tollgate_1 = t6[t6['tollgate_id'] == 1].append(tt6[tt6['tollgate_id'] == 1])
	tollgate_2 = t6[t6['tollgate_id'] == 2].append(tt6[tt6['tollgate_id'] == 2]).reset_index(drop=True)
	tollgate_3 = t6[t6['tollgate_id'] == 3].append(tt6[tt6['tollgate_id'] == 3])

	# 再将表按方向分开，并重置索引
	tol_1_dire_0 = tollgate_1[tollgate_1['direction'] == 0].reset_index(drop=True)
	tol_1_dire_1 = tollgate_1[tollgate_1['direction'] == 1].reset_index(drop=True)
	tol_3_dire_0 = tollgate_3[tollgate_3['direction'] == 0].reset_index(drop=True)
	tol_3_dire_1 = tollgate_3[tollgate_3['direction'] == 1].reset_index(drop=True)

	# 删除各表中的无效重复信息列
	tol_1_dire_0.drop(['direction', 'tollgate_id'], axis=1, inplace=True)
	tol_1_dire_1.drop(['direction', 'tollgate_id'], axis=1, inplace=True)
	tollgate_2.drop(['direction', 'tollgate_id'], axis=1, inplace=True)
	tol_3_dire_0.drop(['direction', 'tollgate_id'], axis=1, inplace=True)
	tol_3_dire_1.drop(['direction', 'tollgate_id'], axis=1, inplace=True)

	tol_dir_list = [tol_1_dire_0, tol_1_dire_1, tollgate_2, tol_3_dire_0, tol_3_dire_1]
	# 处理表中time列并计算time_window和week_day
	for n in range(len(tol_dir_list)):

		time = []
		date = []
		time_window = []
		week_day = []

		for i in tol_dir_list[n].time:
			temp = i.split(' ')
			date.append(temp[0])
			time.append(str(temp[1]))

		for j in date:
			mon = int(j[5]) * 10 + int(j[6])
			day = int(j[8]) * 10 + int(j[9])
			week_day.append((-16 + int((26 * (mon + 1)) / 10) + day) % 7)

		for k in time:
			hour = int(k[0]) * 10 + int(k[1])
			minu = int(k[3]) * 10 + int(k[4])
			time_window.append(hour * 3 + int(minu / 20) + 1)

		tol_dir_list[n]['date'] = date
		tol_dir_list[n]['time_window'] = time_window
		tol_dir_list[n]['week_day'] = week_day

		tol_dir_list[n].drop(['time'], axis=1, inplace=True)

	# 要删除的节假日
	day_to_del = ['2016-09-29', '2016-09-30', '2016-10-01', '2016-10-02', '2016-10-03', '2016-10-04', '2016-10-05',
				  '2016-10-06', '2016-10-07', '2016-10-08']

	for n in range(len(tol_dir_list)):
		# 提取车流量
		tol_dir_series = tol_dir_list[n].groupby(['date', 'time_window']).size()
		tol_dir_list[n] = tol_dir_series.unstack()
		# 删除节假日
		tol_dir_list[n] = tol_dir_list[n].drop(day_to_del)
		# 空值填充0
		tol_dir_list[n] = tol_dir_list[n].fillna(0)

	#######################  Table 6中信息处理   ###########################

	#######################  Table 7中信息处理   ###########################
	tf7 = "dataSets\\training\\weather (table 7)_training.csv"
	t7 = pd.read_csv(tf7)
	tft7 = "dataSets\\testing_phase1\\weather (table 7)_test1.csv"
	tt7 = pd.read_csv(tft7)

	# 删除Table 6中的无效信息
	t7.drop(['pressure', 'sea_pressure', 'wind_direction', 'wind_speed', 'temperature', 'rel_humidity'], axis=1,
			inplace=True)
	tt7.drop(['pressure', 'sea_pressure', 'wind_direction', 'wind_speed', 'temperature', 'rel_humidity'], axis=1,
			 inplace=True)

	# 合并训练集和测试集
	t7 = t7.append(tt7)

	# 设置date为index
	t7 = t7.set_index(['date', 'hour'])
	prec = t7.precipitation

	# 将降雨量正则化
	prec_max = max(prec)
	for i in range(len(prec)):
		if (prec[i] != 0):
			prec[i] = -prec[i] / prec_max
	#######################  Table 7中信息处理   ###########################

	#######################  Table 5中信息处理   ###########################
	tf5 = "dataSets\\training\\trajectories(table 5)_training.csv"
	t5 = pd.read_csv(tf5)
	tft5 = "dataSets\\testing_phase1\\trajectories(table 5)_test1.csv"
	tt5 = pd.read_csv(tft5)
	travel_seq = t5['travel_seq'].append(tt5['travel_seq'])

	# 第一次去分隔符‘；’并排序去重
	travel_seq_iter = (set(x.split(';')) for x in travel_seq)
	travel_seq_test = sorted(set.union(*travel_seq_iter))
	seq_test = pd.Series(travel_seq_test)

	link_id = []
	datetime = []
	travel_time = []

	for str1 in seq_test:
		temp = str1.split('#')
		link_id.append(int(temp[0]))
		datetime.append(temp[1])
		travel_time.append(float(temp[2]))

	data = {'link_id': link_id, 'datetime': datetime, 'travel_time': travel_time}
	travel_seq_split = DataFrame(data, index=link_id)
	travel_seq_split_final = travel_seq_split[['datetime', 'travel_time']]

	# 新建linklist存储24条link的历史travel_time记录
	linklist = []
	for i in np.arange(100, 124):
		linklist.append([i])

	# linklist[0]存储的link_id为100的路,并重置索引
	for i in np.arange(100, 124):
		temp = travel_seq_split_final.ix[i]
		linklist[i - 100] = temp.reset_index(drop=True)

	# 将datetime分开并存储于linklist[m]的date列和time列中，同时计算出该时间所处的time_window（编号从1开始）

	# link 113, 117, 122分别是最接近Tollgate1, 2, 3的link
	link_needed = [13, 17, 22]
	link_needed_list = []

	for i in link_needed:
		link_needed_list.append(linklist[i])

	for m in range(len(link_needed_list)):
		date = []
		time = []
		time_window = []
		week_day = []

		for n in np.arange(len(link_needed_list[m])):
			temp = link_needed_list[m].datetime[n].split(' ')
			date.append(temp[0])
			time.append(str(temp[1]))

		for k in time:
			hour = int(k[0]) * 10 + int(k[1])
			minu = int(k[3]) * 10 + int(k[4])
			time_window.append(hour * 3 + int(minu / 20) + 1)

		for w in date:
			mon = int(w[5]) * 10 + int(w[6])
			day = int(w[8]) * 10 + int(w[9])
			week_day.append((-16 + int((26 * (mon + 1)) / 10) + day) % 7)

		# 用不着week_day
		# link_needed_list[m]['week_day'] = week_day
		link_needed_list[m]['date'] = date
		link_needed_list[m]['time_window'] = time_window
		link_needed_list[m].drop(['datetime'], axis=1, inplace=True)
	#######################  Table 5中信息处理   ###########################
	day_train = ['2016-09-27', '2016-09-28', '2016-09-22', '2016-09-23', '2016-09-24', '2016-09-25', '2016-10-10']
	day_test = ['2016-10-11', '2016-10-12', '2016-10-13', '2016-10-14', '2016-10-15', '2016-10-16', '2016-10-17']
	day_predict = ['2016-10-18', '2016-10-19', '2016-10-20', '2016-10-21', '2016-10-22', '2016-10-23', '2016-10-24']

	X1_train = []
	X2_train = []
	X3_train = []
	X4_train = []
	X5_train = []
	y_train = []

	X1_test = []
	X2_test = []
	X3_test = []
	X4_test = []
	X5_test = []
	y_test = []

	for n in range(len(tol_dir_list)):
		# X1_train: 上周同时的车流量
		# X2_train: 本周前1个time_window的车流量
		# X3_train: 历史time_window平均
		# X4_train: 此时降雨量 prec.loc[day_test[i], int((k - 1) / 9) * 3]
		# X5_train: 上周同时车流量 - 上周前dur个time_window的车流量
		for k in range(tw2 - dur + 1, tw2 + 1):
			for i in range(7):
				X1_train.append(tol_dir_list[n].loc[day_train[i], k])
				X2_train.append(tol_dir_list[n].loc[day_test[i], tw1])
				X3_train.append(tol_dir_list[n][k].mean())
				X4_train.append(tol_dir_list[n][k + 1].mean())
				X5_train.append(tol_dir_list[n][k - 1].mean())
				y_train.append(tol_dir_list[n].loc[day_test[i], k])

				X1_test.append(tol_dir_list[n].loc[day_test[i], k])
				X2_test.append(tol_dir_list[n].loc[day_predict[i], tw1])
				X3_test.append(tol_dir_list[n][k].mean())
				X4_test.append(tol_dir_list[n][k + 1].mean())
				X5_test.append(tol_dir_list[n][k - 1].mean())
				y_test.append(tol_dir_list[n].loc[day_predict[i], k])

	X_train = pd.DataFrame({'1': X1_train, '2': X2_train, '3': X3_train, '4': X4_train, '5': X5_train})
	X_test = pd.DataFrame({'1': X1_test, '2': X2_test, '3': X3_test, '4': X4_test, '5': X5_test})
	y_train = pd.Series(y_train)
	y_test = pd.Series(y_test)
	return X_train, y_train, X_test, y_test

def center_window(root):
	screenwidth = root.winfo_screenwidth()
	screenheight = root.winfo_screenheight()
	size = '%dx%d+%d+%d' % (880, 756, screenheight*0.4, screenheight *0.015 )
	root.geometry(size)

def drawPicFun():
	drawPicPlt = drawPic.add_subplot(111)
	x_train, y_train, x_test, y_test = Requiem(21, 24, 3)
	y_predict = TrainModel(x_train, y_train, x_test, y_test)
	drawPicPlt.plot(x_test, y_predict, 'g.')
	drawPicPlt.plot(x_test,y_test,'r.')
	drawPicPlt.set_title('Demo: Flight data prediction')
	drawPicPlt.set_xlabel("x value")
	drawPicPlt.set_ylabel("y value")
	drawPic.canvas.show()
	#验证option、entry、checkbutton变量值是否好使，将其输出到listbox
	message_frame.listbox_insert("Run Success!!!")
	message_frame.listbox_insert("Use model: " + var_option.get())
	message_frame.listbox_insert("the undeterminted value1:"+ var_entry1.get())
	message_frame.listbox_insert("the undeterminted value2: " + var_entry2.get())
	message_frame.listbox_insert("checkbutton is selected(1:yes,0:no): " + str(var_checkbutton.get()))
	for i in y_predict:
		message_frame.listbox_insert(str(i))

def undeterminted():
	print "hello"

def cur_file_dir():
	#获取脚本路径
	path = sys.path[0]
	#判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
	if os.path.isdir(path):
		return path
	elif os.path.isfile(path):
		return os.path.dirname(path)

def savePic():
	if(message_frame.listbox.size() > 1): #表示已经运行过
		drawPic.savefig(cur_file_dir()+"\\a.pdf")

def saveLog():
	if (message_frame.listbox.size()>1):
		fobj = asksaveasfile()
		if fobj:
			for i in range(message_frame.listbox.size()):
				fobj.write(str(message_frame.listbox.get(i))+'\n')

def about_per():
	"""show the software info"""
	tkMessageBox.showinfo("About", """
	飞行数据预测
	------------------------------------
	version: 1.0
	author: 管冲冲
	Email:  管冲冲@163.com
	------------------------------------""")

def close_window(window):
	"""give prompt when user close the window"""
	if tkMessageBox.askyesno("", "关闭窗口(Yes/No)", icon="question"):
		window.destroy()

class ShowMessageFrame():
	"""will create a frame contanis a listbox and scrollbar"""

	def __init__(self):
		self.frame = Frame()
		self.message_ft = tkFont.Font(family="Arial", size=12)
		self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
		self.listbox = Listbox(self.frame, bg="grey", selectbackground="blue", selectmode="extended",font=self.message_ft, width=20)
		self.scrollbar.config(command=self.listbox.yview)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.listbox.config(yscrollcommand=self.scrollbar.set)
		self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
		self.listbox_insert("Welcome to Hello World!")

	def listbox_insert(self, args):
		self.listbox.insert(END, args)
def main():
	matplotlib.use('TkAgg')
	root = Tk()
	root.title("数据预测")
	center_window(root)

	menu = Menu(root)
	root.config(menu=menu)
	# 创建File菜单，下面有Save和Exit两个子菜单
	file = Menu(menu, tearoff=0)
	file.add_command(label='保存图片',command=savePic)
	file.add_command(label='保存运行日志',command=saveLog)
	file.add_separator()
	file.add_command(label='退出', command=lambda: close_window(root))
	menu.add_cascade(label='文件', menu=file)
	# 创建about菜单
	about = Menu(menu, tearoff=0)
	about.add_command(label='关于', command=about_per)
	menu.add_cascade(label='关于', menu=about)

	global var_option
	var_option=StringVar(root)
	var_option.set("model1")
	option=OptionMenu(root,var_option,"model1","model2","model3","model4").grid(row=0,column=0,padx=45,pady=10,sticky=W)

	global var_checkbutton
	var_checkbutton = IntVar()
	checkbutton = Checkbutton(root, text='是否选上', variable=var_checkbutton)
	checkbutton.grid(row=1,column=0, padx=45, pady=5, sticky=W)

	Label(root,text="待定1").grid(row=0,column=1, padx=20, pady=10,sticky=E)
	Label(root, text="待定2").grid(row=1, column=1, padx=20, pady=5, sticky=E)

	global var_entry1,var_entry2
	var_entry1=StringVar()
	var_entry1.set("default value1")
	var_entry2=StringVar()
	var_entry2.set("default value2")
	Entry(root,textvariable=var_entry1).grid(row=0, column=2, padx=0, pady=10,sticky=W)
	Entry(root, textvariable=var_entry2).grid(row=1, column=2, padx=0, pady=5,sticky= W)
	# 放置标签、文本框和按钮等部件，并设置文本框的默认值和按钮的事件函数
	Button(root, text='画图', width=12, height=1, command=drawPicFun).grid(row=0, column=3, padx=45, pady=10,sticky=E )
	Button(root, text='待定', width=12, height=1, command=undeterminted).grid(row=1, column=3, padx=45, pady=5,sticky= E )

	# 在Tk的GUI上放置一个画布，并用.grid()来调整布局
	global drawPic
	screenwidth = root.winfo_screenwidth()
	screenheight = root.winfo_screenheight()
	drawPic = Figure(figsize=(np.ceil(screenwidth/150), np.ceil(screenheight/180)))
	drawPic.canvas = FigureCanvasTkAgg(drawPic, master=root)
	drawPic.canvas.show()
	drawPic.canvas.get_tk_widget().grid(row=2, columnspan=4, padx=45, pady=10,sticky=S + N + E + W)

	global message_frame
	message_frame = ShowMessageFrame()
	message_frame.frame.grid(row=3, columnspan=4, padx=45, pady=5, sticky=S + N + E + W)

	Label(root, text="powerd by Lab204").grid(row=4, column=3, padx=45, pady=5, sticky=E)
	# 启动事件循环
	root.mainloop()

if __name__ == '__main__':main()

