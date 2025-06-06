from tkinter import *
import tkinter.messagebox as tmsg

def rate():
    file1 = open("Rate.txt","a")
    file1.write(str(myslider.get())+"\n")

    print("Thank you for give me rating",myslider.get())
    tmsg.showinfo("Rate",f"Thank You! for give me {myslider.get()} Rating")

root = Tk()
root.geometry("544x544")
root.title("Rate my Restaurant ")

Label(root,text="Rate us",font="Helvetica 16 bold").pack()
myslider = Scale(root,from_=0,to=10,orient=HORIZONTAL,width=10)
myslider.pack()
Button(root,text="Rate!",command=rate).pack()



root.mainloop()