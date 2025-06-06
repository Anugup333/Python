import os
try:
    d = os.getcwd()
    os.rename(f"{d}\\Python",f"{d}\\Anuj")
    print("Folder Renamed Successfully ")
except FileNotFoundError:
    print("File Doesn't Exists")
