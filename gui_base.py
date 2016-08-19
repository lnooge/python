#-*- coding: utf-8 -*-

import tkinter as tk
import os,sys



class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there['text'] = "hello world"
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='top')

        self.QUIT = tk.Button(self,text="QUIT",fg="red",\
	command = root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there,everyone!")


def exit():
    sys.exit()


root = tk.Tk()
root.title('清雅系统：'+ os.getcwd())
root.resizable(True,True)
root.minsize(100,100)
root.maxsize(600,400)
#tk.Button(root, text='退出', command=exit).pack()

app = Application(master=root)




if __name__ == '__main__':
    root.mainloop()
