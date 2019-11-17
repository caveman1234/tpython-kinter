from tkinter import *
from tkinter import ttk
from tkinter import messagebox,filedialog

root = Tk()
root.geometry("500x500")
root.title("测试tkinter")

def func(event):
  file = filedialog.askdirectory(
    title="打开一个文件。。。。。",
    # filetypes=[("文本文件","*.txt"),("python文件","*.py")]
    # initialdir="/Users"
  )
  print(file)

label = Label(root,text="i am is label")
label.bind("<Button-1>",func)


label.pack()

root.mainloop()