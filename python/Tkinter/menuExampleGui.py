#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window(self.master)

	def init_window(self,master):
		self.master.title("数据预测")
		self.center_window(master,900,600)
		self.pack(fill=BOTH, expand=1)

		# 实例化一个Menu对象，这个在主窗体添加一个菜单
		menu = Menu(self.master)
		self.master.config(menu=menu)

		# 创建File菜单，下面有Save和Exit两个子菜单
		file = Menu(menu)
		file.add_command(label='Save')
		file.add_command(label='Exit', command=self.client_exit)
		menu.add_cascade(label='File', menu=file)

		# 创建Edit菜单，下面有一个Undo菜单
		edit = Menu(menu)
		edit.add_command(label='Undo')
		edit.add_command(label='Show  Image', command=self.showImg)
		edit.add_command(label='Show  Text', command=self.showTxt)
		menu.add_cascade(label='Edit', menu=edit)

	#使初始界面位于屏幕的中间区域
	def get_screen_size(self,window):
		return window.winfo_screenwidth(), window.winfo_screenheight()

	def get_window_size(self,window):
		return window.winfo_reqwidth(), window.winfo_reqheight()

	def center_window(self,master, width, height):
		screenwidth = master.winfo_screenwidth()
		screenheight = master.winfo_screenheight()
		size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) /4 )
		master.geometry(size)

	#回调函数
	def client_exit(self):
		exit()

	def showImg(self):
		load = Image.open('1.jpg')
		render = ImageTk.PhotoImage(load)
		img = Label(self, image=render)
		img.image = render
		img.place(x=0, y=0)

	def showTxt(self):
		text = Label(self, text='GUI图形编程')
		text.pack()
	#以上为各回调函数

#函数执行主体

def main():
	root = Tk()
	app = Window(root)
	root.protocol('WM_DELETE_WINDOW', root.quit)
	root.mainloop()
if __name__ == '__main__': main()





