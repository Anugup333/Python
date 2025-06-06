from tkinter import *
import time

def upload():
    statusvar.set("Busy...")
    sbar.update()
    time.sleep(2)
    statusvar.set("Ready Now")

root = Tk()
root.geometry("455x233")
root.title("Status bar tutorial")


statusvar = StringVar()
statusvar.set("Ready")
# textvariable = statusvar ki jagah aur kuch bhi likh sakte h
# text = statusvar.get()
sbar = Label(root,textvariable=statusvar,relief=SUNKEN,anchor="w",padx=10)
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=upload).pack()

root.mainloop()