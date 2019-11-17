from tkinter import Button

class CustomButton(Button):
  def __init__(self,master):
    super().__init__(master,text="按钮",command=self.click)
  def click(self):
    print("clicked")