from tkinter import *
root = Tk()
def hello():
    root1 = Tk()
    root1.geometry("234x234")
    label = Label(root1,text="Hello tkinter Buttons")
    label.pack()
    root1.mainloop()
    
root.geometry("655x333")
frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1 = Button(frame,fg="red",text="Print Now",command=hello)
b1.pack()

root.mainloop()