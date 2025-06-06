from tkinter import *
anuj_root = Tk()
anuj_root.title("My GUI with Harry")
anuj_root.geometry("700x433")

# Important Label Options(attributes)
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 2 types 
# 1. font= ("comicsansms",12,"bold")
# 2. font= "comicsansms",12,"bold"

# padx - x padding 
# pady - y padding
# relief - border stying - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text= '''Virat Kohli  born 5 November 1988) is an Indian international 
\ncricketer and the former captain of the Indian national cricket team. 
\nHe is a right-handed batsman and an occasional 
\nmedium-fast bowler. He currently represents Royal 
\nChallengers Bangalore in the IPL and Delhi in domestic cricket.
\nKohli is widely regarded as one of the greatest batsmen in the history of
\ncricket and the best of the 21st century.[3] 
\nHe holds the record as the highest run-scorer in T20I and IPL, 
\nranks third in ODI, and stands as the fourth-highest in international cricket.[4] 
\nHe also holds the record for scoring the most centuries in ODI cricket and stands second 
\nin the list of most international centuries scored. Kohli was a member of the Indian team that 
\nwon the 2011 Cricket World Cup, 2013 ICC Champions Trophy, 
\nand captained India to win the ICC Test mace three consecutive times in 2017, 2018, and 2019.[5]
''',bg = "green",fg = "white",padx = 10,pady =12,font= "comicsansms 7 bold", borderwidth=3, relief= SUNKEN)

# Important Pack Options 
# anchor = nw(North West)
# side = top, bottom, left, right
# fill(x or y)  means which side we want to fill 
# padx 
# pady
# title_label.pack(side=BOTTOM,anchor="sw",fill=X)
title_label.pack(side=LEFT,anchor="sw",fill=Y,padx=25,pady=25)

anuj_root.mainloop()