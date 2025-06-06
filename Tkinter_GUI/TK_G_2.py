from tkinter import *

anuj_root = Tk()
anuj_root.title("Window")
# Normal Window size Width x Height
anuj_root.geometry("555x555")

# Min Window size width, height
anuj_root.minsize(300,100)

# Max Window size width, height 
anuj_root.maxsize(1200,988)

# label 
somil = Label(text= "Somil is a good boy and this is his GUI")
somil.pack()

anuj_root.mainloop()