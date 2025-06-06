from tkinter import *
def anuj(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()
root.title("Events in Tkinter ")
root.geometry("644x534")

widget = Button(root,text="Click me Please!")
widget.pack()

widget.bind('<Button-1>',anuj)
widget.bind('<Double-1>',quit)


root.mainloop()