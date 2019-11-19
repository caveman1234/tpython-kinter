from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
fr4 = Frame(root)

fr1.pack(anchor=NW)
fr2.pack(anchor=NW,fill=X)
fr3.pack(anchor=NW)
fr4.pack(anchor=NW)

Button(fr1,text="按钮1").pack()

Button(fr2,text="按钮2-1").pack(side=LEFT)
Button(fr2,text="按钮2-2").pack(side=RIGHT)
Button(fr2,text="按钮2-3").pack(anchor=CENTER)

Button(fr3,text="按钮3").pack(anchor=NW)
Entry(fr3).pack(anchor=NW)
Label(fr3,text="默认LABEL").pack(anchor=NW)

Button(fr4,text="按钮4").pack(anchor=NW)




root.mainloop()





