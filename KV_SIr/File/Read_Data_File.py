
try:
    filename = input("Enter any File name : ")
    with open(filename,"r") as fp:
        filedata = fp.read()
        print("="*50)
        print('Type of filedata = ',type(filedata))
        print("="*50)
        print("File Content ")
        print("="*50)
        print(filedata)
except FileNotFoundError:
    print(f"{filename}  File doesn't Exist! ")
    