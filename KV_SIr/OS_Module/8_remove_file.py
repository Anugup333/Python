import os
try:
    os.remove("C:\\Users\\DELL\\OneDrive\\Desktop\\os.pdf")
    print("File Name removed Successfully ")
except FileNotFoundError:
    print("File doesn't Exists ")
