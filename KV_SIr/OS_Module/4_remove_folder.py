import os
try:
    d = os.getcwd()
    os.rmdir(f"{d}\\Anuj")
    print("Folder Removed Successfully ")
except FileNotFoundError:
    print("No Folder Exists ")
except OSError:
    print("rmdir() can remove those folder which are empty--- check ur path")
    