try:
    fp = open("name.txt","r") 
except FileNotFoundError:
    print("File Does not Exist ")
else:
    print("File Opened in Read Mode Successfully ")
    print("Type of fp = ",type(fp))
    print("="*50)
    print("File Name = ",fp.name)
    print("File Mode = ",fp.mode)
    print(f"is {fp.name} is Readable? = ",fp.readable())
    print(f"is {fp.name} is Writable? = ",fp.writable())
    print(f"is {fp.name} is Closed? = ",fp.closed)
    print("="*50)
finally:
    fp.close()
    print(f"is {fp.name} is Closed? = ",fp.closed)