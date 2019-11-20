from tkinter import *
from tkinter import ttk


root = Tk()
winfo_screenwidth = root.winfo_screenwidth()
winfo_screenheight = root.winfo_screenheight()
width = 1000
height = 600

size = "{}x{}+{}+{}".format(width,height,int((winfo_screenwidth-width)/2),int((winfo_screenheight - height)/2))
root.geometry(size)



label = Label(root,text="标题一",width=60,height=1,bg="yellow")
label.grid(row=0,column=0,columnspan=10)

fr1 = LabelFrame(root,text="登陆",width=400)
fr1.grid(row=1,column=0)

Label(fr1,text="button1").grid(row=0,column=0,columnspan=2,sticky=E)#strict 对齐
Entry(fr1).grid(row=0,column=2,columnspan=4)
Label(fr1,text="按钮三111").grid(row=1,column=0,columnspan=2,sticky=E)
Entry(fr1).grid(row=1,column=2,columnspan=4)

photo = PhotoImage(file="src/images/bd_logo1.png")
label1 = Label(fr1,image=photo)
label1.grid(row=0,column=7,columnspan=2,rowspan=2,sticky=W+E+N+S)

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl) 
tabControl.add(tab1, text='Tab 1')     
tab2 = ttk.Frame(tabControl)            
tabControl.add(tab2, text='Tab 2')   
tabControl.grid(row=2,column=0,sticky=W)

Label(tab1,text="11111111").pack()
Label(tab2,text="2222222").pack()

Frame(root,width=200,height=200,bg='blue',borderwidth=2).grid(row=3,column=0,sticky=W)











root.mainloop()











