#!/usr/bin/env python
# coding:utf-8

from Tkinter import *
import tkFont
import Tkinter
from PIL import Image, ImageTk

def Start():
	print "hello"

def SLAM():
	print "world"

def Reset():
	print "hi"

def Stop():
	print "xiaonan"

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
	Button(canvas, text='停止', width=15, height=2, font=ft2, command=Stop).place(x = 290, y = 300, width=130, height=50)

	canvas.create_text(400, 420,text='powerd by jixiaonan')
	# 启动事件循环
	root.mainloop()

if __name__ == '__main__':main()

