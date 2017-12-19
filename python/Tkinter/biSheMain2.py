#!/usr/bin/env python
# coding:utf-8

#按名字杀掉进程并加上退出窗口
from Tkinter import *
import tkFont
import Tkinter
from PIL import Image, ImageTk
import threading
import os
import re
import tkMessageBox

class timer(threading.Thread):  # The timer class is derived from the class threading.Thread
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.thread_num = num
		self.thread_stop = False

	def run(self):  # Overwrite run() method, put what you want the thread do here
		if self.thread_num == 1:
			os.system('gedit')
		elif self.thread_num == 2:
			os.system('vim')
		else:
			print 'error'

	def stop(self):
		self.thread_stop = True

def kill_by_name(name):
	cmd='ps aux|grep %s'%name
	f=os.popen(cmd)
	regex=re.compile(r'\w+\s+(\d+)\s+.*')
	txt=f.read()
	if len(txt)<5:
		print 'there is no thread by name or command %s'%name
		return

	ids=regex.findall(txt)
	cmd="kill %s"%' '.join(ids)
	os.system(cmd)

def Start():
	global thread1
	thread1 = timer(1)
	thread1.start()

def SLAM():
	global thread2
	thread2 = timer(2)
	thread2.start()

def Reset():
	kill_by_name('gedit')
	kill_by_name('vim')

def Off(window):
	if tkMessageBox.askyesno("", "关闭窗口(Yes/No)", icon="question"):
		window.destroy()

def main():
	root = Tk()
	root.title("定位与建图系统")
	screenwidth = root.winfo_screenwidth()
	screenheight = root.winfo_screenheight()
	width_window=500
	height_window=450
	padx_window=(screenwidth-width_window)/2
	pady_window=(screenheight-height_window)/3
	size = '%dx%d+%d+%d' % (width_window, height_window, padx_window, pady_window )
	root.geometry(size)

	canvas = Tkinter.Canvas(root, width=width_window,  # 指定Canvas组件的宽度
							height=height_window,  # 指定Canvas组件的高度
							bg='white')  # 指定Canvas组件的背景色
	image = Image.open("5.jpg")
	im = ImageTk.PhotoImage(image)
	canvas.create_image(250,225, image=im)  # 两个值分别为Canvas的一半大小
	ft1 = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
	canvas.create_text(250, 40,font=ft1,text='基于多传感器的室内机器人')
	canvas.create_text(250, 80, font=ft1, text='定位与建图系统')
	canvas.pack()

	ft2 = tkFont.Font(family='Fixdsys', size=14)
	Button(canvas, text='开始', width=15, height=2, font=ft2, command=Start).place(x = 80, y = 160, width=130, height=50)
	Button(canvas, text='SLAM', width=15, height=2, font=ft2, command=SLAM).place(x = 290, y = 160, width=130, height=50)
	Button(canvas, text='复位', width=15, height=2, font=ft2, command=Reset).place(x = 80, y = 300, width=130, height=50)
	Button(canvas, text='退出', width=15, height=2, font=ft2, command=lambda: Off(root)).place(x = 290, y = 300, width=130, height=50)

	canvas.create_text(400, 420,text='powerd by jixiaonan')
	# 启动事件循环
	root.mainloop()

if __name__ == '__main__':main()

