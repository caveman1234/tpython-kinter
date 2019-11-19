
import os
import sys
from tkinter import *
from src.test import func


root = Tk()
root.geometry("500x500")

class App():
  def __init__(self,root):
    self.root = root
    self.create_wedget()
  def create_wedget(self):
    btn = Button(self.root,text="按钮")
    btn.pack()
    btn.bind("<Button-1>",self.click1)
  def click1(self,event):
    
    print(os.path.abspath("."))
    print(os.getcwd())
    

    f = open("aaa.txt","a+")
    f.write(os.path.abspath("."))
    f.write("\n")
    f.write(os.getcwd())
    f.write(func())
    f.close()








App(root)


root.mainloop()


