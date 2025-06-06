from tkinter import *
from PIL import Image,ImageTk

anuj_root = Tk()

anuj_root.geometry("900x900")

# for png Images 
photo = PhotoImage(file = "Intro_Of_tkinter.png")

# For Jpg Images 
# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)

anuj_label = Label(image=photo)
anuj_label.pack()

anuj_root.mainloop()