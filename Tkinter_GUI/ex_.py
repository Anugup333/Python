from tkinter import *
root = Tk()
root.title("Anuj")
root.geometry("500x500")

# Menu

main_menu = Menu(root)
# first option
first_option = Menu(main_menu,tearoff=0)
first_option.add_command(label="Name1",command=quit)
first_option.add_separator()
first_option.add_command(label="Name2",command=quit)
first_option.add_command(label="Name3",command=quit)
root.config(menu=main_menu)
main_menu.add_cascade(label="File",menu=first_option)
root.mainloop()