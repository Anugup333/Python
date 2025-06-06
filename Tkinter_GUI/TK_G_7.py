from tkinter import *

def getvals():
    print(uservalue.get())
    print(passwordvalue.get())

root = Tk()
root.geometry("655x333")

user = Label(root,text="Username")
password = Label(root,text="Password")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passwordvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passwordentry = Entry(root,textvariable=passwordvalue)

userentry.grid(row= 0,column= 1)
passwordentry.grid(row= 1, column= 1)

Button(text="Submit",command=getvals).grid()
root.mainloop()