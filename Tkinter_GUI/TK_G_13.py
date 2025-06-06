# Make Sliders

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Slider tutorial")


# myslider2.get()  give the value that you are assign in that slider
def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account ")
    tmsg.showinfo("Ammount Credited!",f"You have credited {myslider2.get()} dollars to your bank account ")


# # Vertical Slider 
# myslider1 = Scale(root,from_=0,to=100)
# myslider1.pack()

# Horizontal Slider
Label(root,text="How many dollars do you want ").pack()
# tickinterval give the interval of that slider
myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
# Set Initial value of slider 
myslider2.set(5)
myslider2.pack()

# Botton
Button(root,text="Get Dollars!",padx=10,command=getdollar).pack(pady=5)


root.mainloop()