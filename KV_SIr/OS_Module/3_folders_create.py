import os
try:
    d= os.getcwd()
    os.makedirs(f"{d}\\Python\\Anuj")
    print("Folder Created Successfully ")
except FileExistsError:
    print("Folder Already Exists ")
except OSError:
    print("Check ur path or folder names ")