from tkinter import *

def click(event):
    global scvalue
    # how to take text of any button 
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                print(e)
                value = "Error"
        
        scvalue.set(value)
        screen.update()
        
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
root = Tk()
root.geometry("644x950")
root.title("Calculator By CodeWithAnuj")
root.wm_iconbitmap("CalculatorIcon.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

l = [["9","8","7"],["6","5","4"],["3","2","1"],["0","-","*"],["/","%","="],["C",".","00"]]

for i in range(6):
    f = Frame(root,bg="grey")
    b = Button(f,text=l[i][0],font="lucida 25 bold",padx=5,pady=5)
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)

    b = Button(f,text=l[i][1],font="lucida 25 bold",padx=5,pady=5)
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)

    b = Button(f,text=l[i][2],font="lucida 25 bold",padx=5,pady=5)
    b.pack(side=LEFT,padx=5,pady=5)
    b.bind("<Button-1>",click)

    f.pack()

root.mainloop()