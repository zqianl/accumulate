#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
from Tkinter import *
from tkFileDialog import *
from tkFont import Font
try:
    from ttk import Button, Scrollbar
except ImportError:
    pass

class Edit_save(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('EditSave')
        self.root.geometry('+120+50')
        self.font_en = Font(self.root, size=12)
        self.font_text = Font(self.root,family="Helvetica",
                        size=12, weight='normal')

        self.menubar = Menu(self.root, bg='purple')
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label='Open', accelerator='Ctrl+o',
                command=self.__open, underline=0)
        self.filemenu.add_command(label='Save', accelerator='Ctrl+s',
                command=self.__save, underline=0)
        self.filemenu.add_command(label='Save As', accelerator='Ctrl+Shift+s',
                command=self.__save_as, underline=5)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Quit', accelerator='Alt+F4',
                command=self.root.destroy, underline=0)
        self.menubar.add_cascade(label='File', underline=0, menu=self.filemenu)
        self.helpmenu = Menu(self.menubar)
        self.helpmenu.add_command(label='About', underline=0,
                                  command=About_editsave)
        self.menubar.add_cascade(label='Help', underline=0, menu=self.helpmenu)
        self.editmenu = Menu(self.menubar, tearoff=False)
        self.editmenu.add_command(label='Refresh', accelerator='F5',
                command=self.root.update)
        self.editmenu.add_command(label='Copy', accelerator='Ctrl+C',
                command=lambda : self.text.event_generate('<<Copy>>'))
        self.editmenu.add_command(label='Paste', accelerator='Ctrl+V',
                command=lambda : self.text.event_generate('<<Paste>>'))
        self.editmenu.add_command(label='Cut', accelerator='Ctrl+X',
                command=lambda : self.text.event_generate('<<Cut>>'))
#       self.editmenu.add_command(label='Undo', accelerator='Ctrl+Z',
#               command=lambda : self.text.event_generate('<<Undo>>'))
#       self.editmenu.add_command(label='Redo', accelerator='Ctrl+Y',
#               command=lambda : self.text.event_generate('<<Redo>>'))
        self.editmenu.add_command(label='select_all', accelerator='Ctrl+A',
                command=lambda : self.text.tag_add('sel', '1.0', 'end'))

        self.fm_base = Frame(self.root)
        self.fm_up = Frame(self.fm_base)
        self.var = StringVar()
        self.en = Entry(self.fm_up, font=self.font_en,
                        textvariable=self.var, width=20)
        self.bt_open = Button(self.fm_up, text='Open',)
        self.bt_quit = Button(self.fm_up, text='Quit', underline=0)
        self.bt_quit.pack(side=RIGHT, padx=10)
        self.bt_open.pack(side=RIGHT, padx=5)
        self.en.pack(side=RIGHT, pady=5)
        self.bt_open.config(command=self.__open)
        self.bt_quit.config(command=self.root.destroy)
        self.fm_up.pack(fill=X)
        self.fm_base.pack(fill=X)

        self.fm_down =  Frame(self.root)
        self.text = Text(self.fm_down, font=self.font_text,
                        width=50, height=20)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        self.scb = Scrollbar(self.fm_down)
        self.scb.pack(side=LEFT, fill=Y)
        self.text.config(yscrollcommand=self.scb.set)
        self.scb.config(command=self.text.yview)
        self.fm_down.pack(fill=BOTH, expand=True)

        self.root.bind('<Control-o>', self.__invoke_open)
        self.root.bind('<Control-O>', self.__invoke_open)
        self.root.bind('<Control-s>', self.__invoke_save)
        self.root.bind('<Control-S>', self.__invoke_save_as)
        self.root.bind('<Button-3>', self.__popupmenu)
        self.root.bind('Alt-F4', lambda event:  self.root.destroy)
        self.root.bind('<F5>', lambda event: self.root.update)
        self.root.bind('<Control-C>',
                        lambda event: self.text.event_generate('<<Copy>>'))
        self.root.bind('<Control-V>',
                        lambda event: self.text.event_generate('<<Paste>>'))
        self.root.bind('<Control-X>',
                        lambda event: self.text.event_generate('<<Cut>>'))
        for i in 'a', 'A':
            self.root.bind('<Control-%s>' % i,
                        lambda event: self.text.tag_add('sel', '1.0', 'end'))
#       for i in 'z', 'Z':
#           self.root.bind('<Control-%s>' % i,
#                       lambda event: self.text.event_generate('<<Undo>>'))
#       for i in 'y', 'Y':
#           self.root.bind('<Control-%s>' % i,
#                       lambda event: self.text.event_generate('<<Redo>>'))

        self.root.config(menu=self.menubar)
        self.root.mainloop()

    def __open(self):
        filetypes = [
                ("All Files", '*'),
                ("Python Files", '*.py', 'TEXT'),
                ("Text Files", '*.txt', 'TEXT'),
                ("Config Files", '*.conf', 'TEXT')]
        fobj = askopenfile(filetypes=filetypes)
        if fobj:
            self.text.delete('1.0', END)
            self.text.insert('1.0', fobj.read())
            self.en.delete(0, END)
            self.en.insert(0, fobj.name)

    def __save(self):
        value = self.var.get().strip()
        if value:
            f = open(value, 'w')
            f.write(self.text.get('1.0', END).strip() + '\n')
            f.close()
        else:
            self.__save_as()

    def __save_as(self):
        text_value = self.text.get('1.0', END).strip()
        if text_value:
            fobj = asksaveasfile()
            if fobj:
                fobj.write(text_value + '\n')

    def __invoke_open(self, event):
        self.__open()

    def __invoke_save(self, event):
        self.__save()

    def __invoke_save_as(self, event):
        self.__save_as()

    def __popupmenu(self, event):
        self.editmenu.post(event.x_root, event.y_root)

class About_editsave(object):
    def __init__(self):
        self.root = Tk()
        self.root.title('EditSave')
        self.root.geometry('380x450+200+80')
        self.root.resizable(False, False)
        self.text='''''Author : WANG Jicheng
Date : Mon Feb 15 14:35:44 CST 2016

Summary:
This is a test gui
which is about a document edit and save'''

        self.fm_full = Frame(self.root, bg='gray')

        self.fm_up = Frame(self.fm_full)
        self.lb1 = Label(self.fm_up, text='EditSave 1.0',
                        font='Helvetica -20 bold')
        self.lb1.pack(expand=True)
        self.fm_up.pack(fill=BOTH, expand=True)

        self.fm_middle = Frame(self.fm_full)
        self.fm_separator = Frame(self.fm_middle, height=2, bd=1, relief=SUNKEN)
        self.fm_separator.pack(fill=X, padx=5, pady=5)
        self.lb2 = Label(self.fm_middle, text=self.text, justify=LEFT)
        self.lb2.pack()
        self.lb2.config(font='Helvetica -16 bold')
        self.fm_middle.pack(fill=BOTH, expand=True)

        self.fm_down = Frame(self.fm_full)
        self.fm_separator = Frame(self.fm_down, height=2, bd=1, relief=SUNKEN)
        self.fm_separator.pack(fill=X, padx=5, pady=5)
        self.bt = Button(self.fm_down, text='Quit',
                         command=self.root.destroy)
        self.bt.pack(side=BOTTOM, anchor=E, padx=5, pady=5)
        self.fm_down.pack(fill=BOTH, expand=True)

        self.fm_full.pack(fill=BOTH, expand=True)

        self.root.mainloop()

if __name__ == "__main__":
    Edit_save()