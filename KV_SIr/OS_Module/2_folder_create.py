import os
try:
    d= os.getcwd()
    os.mkdir(f"{d}\\Python")
    print("Folder Created Successfully ")
except FileExistsError:
    print("Folder Already Exists ")
except FileNotFoundError:
    print("mkdir() can create only one folder at a time ")
except OSError:
    print("Check ur path or folder names ")