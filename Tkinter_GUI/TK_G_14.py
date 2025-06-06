from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("644x644")
root.title("RadioButton Tutorial")

def order():
    tmsg.showinfo("Order Received!",f"We have received your order for {var.get()}. Thanks for Ordering")

var = StringVar()
var.set("Radio")

Label(root,text="What would you like to have Sir?",
font="lucida 13 bold ",justify=LEFT,padx=10).pack()

radio = Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor="w")
radio = Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor="w")
radio = Radiobutton(root,text="Paratha",padx=14,variable=var,value="Paratha").pack(anchor="w")
radio = Radiobutton(root,text="Samosa",padx=14,variable=var,value="Samosa").pack(anchor="w")

Button(root,text="Order Now!",command=order).pack()
root.mainloop()
