from tkinter import *
from tkinter import ttk
from tkinter import messagebox,filedialog

root = Tk()
root.geometry("1000x1000")
root.title("测试tkinter")

file1_src = ""
file2_src = ""
def func1(event):
  global file1_src
  file1_src = filedialog.askopenfilename()
  label1['text'] = label1['text'] + file1_src
def func2(event):
  global file2_src
  file2_src = filedialog.askopenfilename()
  label2['text'] = label2['text'] + file2_src

btn1 = Button(root,text="请选择需要修改的文件")
btn2 = Button(root,text="请选择文件二")
btn3 = Button(root,text="确认转换")
label1 = Label(root,text="需要修改的文件路径为:")
label2 = Label(root,text="文件二路径为:")

btn1.bind("<Button-1>",func1)
btn2.bind("<Button-1>",func2)

btn1.grid(row=0,column=0,sticky=W)
btn2.grid(row=0,column=1,sticky=W)
label1.grid(row=1,column=0,sticky=W)
label2.grid(row=2,column=0,sticky=W)
btn3.grid(row=3,column=0,sticky=W)


root.mainloop()