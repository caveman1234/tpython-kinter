
import os
import sys
from tkinter import *


root = Tk()
winfo_screenwidth = root.winfo_screenwidth()
winfo_screenheight = root.winfo_screenheight()
width = 1000
height = 600

newGeometry = "{}x{}+{}+{}".format(width,height,int((winfo_screenwidth-width)/2),int((winfo_screenheight - height)/2))
root.geometry(newGeometry)

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

Label(f1,text='用户名',width=6).pack(side=LEFT,anchor=NW)

Entry(f1,width=20).pack(side=LEFT,anchor=NW,padx=50)

Label(f2,text='密码',width=6).pack(side=LEFT,anchor=NW)
Entry(f2,width=20,show='*').pack(side=LEFT,anchor=NW,padx=50)
Button(f3,text='登录',width=8).pack(side=LEFT)
Button(f3,text='取消',width=8).pack(side=LEFT)


f1.pack(fill=X)
f2.pack(fill=X)
f3.pack(fill=X)







root.mainloop()


