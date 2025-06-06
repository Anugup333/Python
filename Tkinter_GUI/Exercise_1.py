import tkinter as tk
root = tk.Tk()
root.title("single Strip ")
root.geometry("500x600")
root_label = tk.Label(text="READY",bg="black",fg="white",padx=500,pady=10,font=("Serif",13,"bold"),borderwidth=4,relief="groove")
root_label.pack(side="bottom",anchor="s",fill="both",padx=20)
root.mainloop()