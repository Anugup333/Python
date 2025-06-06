from tkinter import *



class GUI(Tk):
    # andhar self as root kam kaega 
    def __init__(self):
        super().__init__()
        self.geometry("744x377")
    
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self,textvariable=self.var,relief=SUNKEN,anchor="w",padx=10)
        self.statusbar.pack(side=BOTTOM,fill=X)
    
    def click(self):
        print("Botton Clicked!")
    
    def createbutton(self,inptext):
        Button(self,text=inptext,command=self.click).pack()



if __name__ == '__main__':
    # window as a root kam karega 
    window = GUI()
    window.status()
    window.createbutton("Click me!")
    
    window.mainloop()
    