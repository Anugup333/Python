"Pickle"
import pickle

def pickling():
    with open("student.txt",'ab') as sp:
        while True:
            print("="*50)
            # User Input 
            sno = int(input("Enter Student Number : "))
            sname = input("Enter Student Name : ")
            smarks = int(input("Enter Student Marks : "))
            uname = input("Enter Student University Name : ")
            # create the list obj that saved in the file 
            l = list()
            l.append(sno)
            l.append(sname)
            l.append(smarks)
            l.append(uname)
            # save object l in file
            pickle.dump(l,sp)
            print('='*50)
            print("Student Record Saved in a file: ")
            print('='*50)
            ch= input("Do u want to Insert another Record( yes or no): ")
            if ch.lower() == "no":
                print("Thanks for using this program ")
                break
            if ch.lower() != "yes":
                print("Enter 'yes' for continuing the data to insert ")
                break

def unpicking():
    try:
        with open("student.txt","rb") as sp:
            print('='*50)
            print("Student Record ")
            print("="*50)
            print(f"\tSno\tSname\tSmarks\tUname")
            print("="*50)
            while True:
                try:
                    obj = pickle.load(sp)
                    for value in obj:
                        print(f"\t {value}",end=" ")
                    print()
                except EOFError:
                    print("="*50)
                    break
                
    except FileNotFoundError:
        print("File Does not Exist ")


# pickling()
unpicking()