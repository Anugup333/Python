from tkinter import *

root = Tk()
root.geometry("455x233")
root.title("Scrollbar tutorial")

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)


# Listbox ke liye scrollbar 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

# listbox = Listbox(root,yscrollcommand= scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"Item {i}")

# listbox.pack(fill="both",padx=22)
# scrollbar.config(command=listbox.yview)

# Text ke liye scrollbar

text = Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH,padx=12)

scrollbar.config(command=text.yview)

root.mainloop()