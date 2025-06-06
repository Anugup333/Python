from tkinter import *
root = Tk()
root.geometry("655x333")

f1 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side="left",fill="y")

f2 = Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side="top",fill="x")

l = Label(f1,text="Project Tkinter - Pycharm")
l.pack(pady=140)

l = Label(f2,text="Welcome to sublime text", font="Helvetica 16 bold",fg="red",padx=10)
l.pack()

root.mainloop()