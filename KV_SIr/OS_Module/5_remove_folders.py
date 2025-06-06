import os
try:
    d = os.getcwd()
    # os.removedirs("C:\\Users\\DELL\\OneDrive\\Desktop\\Python\\KV_SIr\\Anuj\\Name")
    os.removedirs(f"{d}\\Anuj")
    print("Folders Removed Succssfully ")
except FileNotFoundError:
    print("="*50)
    print("Folders doesn't Exists ")
except PermissionError:
    print("="*50)
    print("Folder is in Use ")
    print("So U cann't Remove that Folder ")
except OSError:
    print("="*50)
    print("remove those folder which are empty-Check ur path of folder names")
    