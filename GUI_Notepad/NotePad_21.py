from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os 

def newFile():
    global file
    root.title("Notepad")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
        filetypes=[("All Files","*.*"),
                   ("Text Files","*.txt")])
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0 , f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitle.txt",defaultextension="*.txt",
            filetypes=[("All File","*.*"),("Text File","*.txt")])
        
        if file == "":
            file = None
        else:
            # Save as a new file 
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file 
        f = open(file, "w")
        f.write(TextArea.get(1.0 , END))
        f.close()

def exitApp():
    root.quit()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Code with Anuj")
    


if __name__ == '__main__':
    # Basic tkinter setup 
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("2.ico")
    root.geometry("600x600")
    
    # Add TextArea
    
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand=TRUE,fill=BOTH)
    
    # Lets Create a Menubar 

    # File Menu Starts 
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar,tearoff=0)
    # To Open New File
    FileMenu.add_command(label="New",command=newFile)
    
    # To Open already existing File
    FileMenu.add_command(label="Open",command=openFile)
    
    # To Save the File 
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    # To Exit the app
    FileMenu.add_command(label="Exit",command=exitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    
    # Edit Menu Starts 
    EditMenu = Menu(MenuBar,tearoff=0)
    # To give the feature of cut, copy and paste 
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=EditMenu) 
    
    # Help Menu Starts 
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad!",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    
    # adding Scrollbar 
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)    
    
    root.config(menu=MenuBar)
    
    
    
    root.mainloop()