# Create a gui Window which takes as input width and height
# and upon clicking apply , it should be able 
# to change its size accordingly

from tkinter import *

root = Tk()
root.geometry("333x333")

def change_window():
    root.geometry(f"{width_value.get()}x{height_value.get()}")

Label(root,text="Convert the Window Size",font="lucida 13 bold",pady=12).grid(row=0,column=2)

width_value = StringVar()
height_value = StringVar()

width_entry = Entry(root,textvariable=width_value)
height_entry = Entry(root,textvariable=height_value)

width_entry.grid(row=1,column=2)
height_entry.grid(row=2,column=2)

Label(root,text="Width",pady=3).grid(row=1,column=1)
Label(root,text="Height",pady=3).grid(row=2,column=1)

Button(root,text="Apply",command=change_window,padx=3).grid(row=3,column=2)


    

root.mainloop()