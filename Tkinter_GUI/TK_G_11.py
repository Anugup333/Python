# Menus and Menu Bars

from tkinter import *

root = Tk()
root.geometry("733x566")
root.title("Visual Studio")
def myfun():
    print("Mai ek bahut hi natkhat aur saitan function hoon")

# Use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myfun)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

# Menu with labels

main_menu = Menu(root)

# First Menu
# tearsoff is you can not take menu anywhere 
first_option = Menu(main_menu,tearoff=0)
first_option.add_command(label="New Project",command=myfun)
first_option.add_command(label="Save",command=myfun)
first_option.add_separator() # it is used to seperate the first and last two munu
first_option.add_command(label="Save as",command=myfun)
first_option.add_command(label="Print",command=myfun)
# it means Ha bhai isme dalna first_option isme dalna h 
root.config(menu=main_menu)

main_menu.add_cascade(label="File",menu=first_option)

# Second Menu 
second_option = Menu(main_menu,tearoff=0)
second_option.add_command(label="Cut",command=myfun)
second_option.add_command(label="Copy",command=myfun)
second_option.add_separator() # it is used to seperate the first and last two munu
second_option.add_command(label="Paste",command=myfun)
second_option.add_command(label="Find",command=myfun)

root.config(menu=main_menu)

main_menu.add_cascade(label="Edit",menu=second_option)

root.mainloop()