from tkinter import *
# Message box 
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")
root.title("Visual Studio")
def myfun():
    print("Mai ek bahut hi natkhat aur saitan function hoon")

def help():
    print("I will help you!")
    # Information  Show 
    tmsg.showinfo("Help","Harry will help you with this GUI")

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good","You used this GUI... Was your experience good")
    if value == "yes":
        msg = "Great. rate us on appstore Please"
    else:
        msg = "Tell me what went wrong. We will call you soon"
    tmsg.showinfo("Experience",msg)

# Menu with label
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

third_option = Menu(main_menu,tearoff=0)
third_option.add_command(label="Help",command=help)
third_option.add_command(label="Rate us",command=rate)
main_menu.add_cascade(label="Help",menu=third_option)
root.config(menu=main_menu)


root.mainloop()
