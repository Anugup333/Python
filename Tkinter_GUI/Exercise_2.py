from tkinter import *
from PIL import ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text +="\n"
    return final_text

root = Tk()
root.title("CodeWithHarry News - Aapka Apna Akhabaar ")
root.geometry("1000x1000")

texts = []
photos = []

for i in range(0, 3):
    with open(f"TK_G_{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
    
    image = Image.open(f"{i+1}.png")
    # TODO: Resize these images
    image = image.resize((150,150))
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width=800,height=70)
Label(f0, text="Code With Harry News",font="lucida 33 bold").pack()
Label(f0, text="February 20 2024",font="lucida 13 bold").pack()
f0.pack()
for i in range(3):
    f1 = Frame(root,width=900,height=200)
    Label(f1,text=texts[i],padx=23,pady=23).pack(side=LEFT,)
    Label(f1,image=photos[i],anchor="e").pack(side=RIGHT)
    f1.pack(anchor="w")



root.mainloop()