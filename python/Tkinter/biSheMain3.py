#!/usr/bin/env python
# coding:utf-8

#重绘window
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
		elif self.thread_num == 3:
			os.system('gedit')
		elif self.thread_num == 4:
			os.system('vim')
		elif self.thread_num == 5:
			os.system('gedit')
		elif self.thread_num == 6:
			os.system('vim')
		elif self.thread_num == 7:
			os.system('gedit')
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
	thread1 = timer(1)
	thread1.start()

def Rviz():
	thread1 = timer(2)
	thread1.start()

def CloseInfrared():
	thread1 = timer(3)
	thread1.start()

def ActiveSLAM():
	thread2 = timer(4)
	thread2.start()

def SLAM():
	thread1 = timer(5)
	thread1.start()

def SaveMap():
	thread1 = timer(6)
	thread1.start()

def PosiNavi():
	thread1 = timer(7)
	thread1.start()

def Reset():
	kill_by_name('gedit')
	kill_by_name('vim')
	kill_by_name('1xx')
	kill_by_name('2xx')
	kill_by_name('3xx')
	kill_by_name('4xx')

def CloseWindow(window):
	if tkMessageBox.askyesno("", "关闭窗口(Yes/No)", icon="question"):
		window.destroy()

def main():
	root = Tk()
	root.title("定位与建图系统")
	screenwidth = root.winfo_screenwidth()
	screenheight = root.winfo_screenheight()
	width_window=600
	height_window=500
	padx_window=(screenwidth-width_window)/2
	pady_window=(screenheight-height_window)/3
	size = '%dx%d+%d+%d' % (width_window, height_window, padx_window, pady_window )
	root.geometry(size)

	canvas = Tkinter.Canvas(root, width=width_window,height=height_window,bg='white')
	image = Image.open("6.jpg")
	im = ImageTk.PhotoImage(image)
	canvas.create_image(300,250, image=im)
	ft1 = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
	canvas.create_text(300, 40,font=ft1,text='基于多传感器的室内机器人')
	canvas.create_text(300, 80, font=ft1, text='定位与建图系统')
	canvas.pack()

	ft2 = tkFont.Font(family='Fixdsys', size=12)
	Button(canvas, text='开始', width=15, height=2, font=ft2, command=Start).place(x = 50, y = 150, width=130, height=50)
	Button(canvas, text='Rviz', width=15, height=2, font=ft2, command=Rviz).place(x=50, y=270, width=130, height=50)
	Button(canvas, text='关闭红外', width=15, height=2, font=ft2, command=CloseInfrared).place(x=50, y=390, width=130, height=50)

	canvas.create_text(230, 130, text='功能1')
	Button(canvas, text='主动SLAM', width=15, height=2, font=ft2, command=ActiveSLAM).place(x=240, y=150, width=120, height=40)
	canvas.create_text(230, 230, text='功能2')
	Button(canvas, text='SLAM', width=15, height=2, font=ft2, command=SLAM).place(x=240, y=250, width=120, height=40)
	Button(canvas, text='保存地图', width=15, height=2, font=ft2, command=SaveMap).place(x=240, y=310, width=120, height=40)
	canvas.create_text(230, 380, text='功能3')
	Button(canvas, text='定位导航', width=15, height=2, font=ft2, command=PosiNavi).place(x=240, y=400, width=120, height=40)

	Button(canvas, text='复位', width=15, height=2, font=ft2, command=Reset).place(x = 420, y = 210, width=130, height=50)
	Button(canvas, text='退出', width=15, height=2, font=ft2, command=lambda: CloseWindow(root)).place(x=420, y=330, width=130, height=50)

	canvas.create_text(500, 470,text='powerd by jixiaonan')
	# 启动事件循环
	root.mainloop()

if __name__ == '__main__':main()

