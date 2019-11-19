
import os
import sys
from tkinter import *
from src.Frame_1.Frame_1 import Frame_1

root = Tk()
winfo_screenwidth = root.winfo_screenwidth()
winfo_screenheight = root.winfo_screenheight()
width = 1000
height = 600

newGeometry = "{}x{}+{}+{}".format(width,height,int((winfo_screenwidth-width)/2),int((winfo_screenheight - height)/2))
root.geometry(newGeometry)

class App():
  def __init__(self,root):
    self.root = root
    frame1 = Frame_1(self.root)
    frame1.pack(fill=X)










App(root)


root.mainloop()


