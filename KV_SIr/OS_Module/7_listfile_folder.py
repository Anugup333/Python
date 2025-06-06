import os
try:
    d = os.getcwd()
    filenames = os.listdir(f".")
    print("="*50)
    print("List of Files")
    print("="*50)
    for file in filenames:
        print(file)
    print("="*50)
except FileNotFoundError:
    print("Folder dosn't Exists ")