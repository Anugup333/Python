from tkinter import *

root = Tk()
root.geometry("455x455")
root.title("Listbox Tutorial")

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i += 1
    
i = 0
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our listbox")

Button(root,text="Add Item",command=add).pack()

root.mainloop()