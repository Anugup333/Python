from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("444x444")
    
    def update(self):
        pass
    
    def update(self):
        pass
    
    def create_front_label(self,name_label):
        Label(self,text=name_label).grid(row=0,column=2)
    
    def create_width_label(self):
        Label(self,text="width").grid(row=1,column=0)
    
    def create_height_label(self):
        Label(self,text="height").grid(row=2,column=0)
    
    
    def create_button(self,name_button):
        Button(self,text=name_button,command=self.update).pack()


if __name__ == '__main__':
    window = GUI()
    
    
    window.mainloop()