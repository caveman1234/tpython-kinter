from tkinter import *



class Frame_1():
  def __init__(self,root):
    self.root = root
    self.frame = Frame(root)
    self.create_wedget()
  def create_wedget(self):
    Button(self.frame,text="按钮1").pack(side=LEFT,anchor=NW)
    Button(self.frame,text="按钮2").pack(side=RIGHT,anchor=NW)
    Button(self.frame,text="按钮3").pack(side=LEFT,anchor=CENTER)
  def pack(self,*args,**kw):
    self.frame.pack(*args,**kw)

















