import pickle
def picking():
    noe = int(input("Enter How many Employees data u Have: "))
    if (noe<=0):
        print(f"{noe} Imvalid number of employees ")
    else:
        with open('emp.txt','ab') as fp:
            for i in range(1,noe+1):
                print("="*50)
                print(f"\nEnter {i} Employee Details : ")
                print("="*50)
                eno = int(input(f"Enter {i} Employee Number "))
                ename = input(f"Enter {i} Employee Name ")
                esal = int(input(f"Enter {i} Employee Salary "))
                # Create an empty List 
                lst = []
                #  Append the employees details
                lst.append(eno)
                lst.append(ename)
                lst.append(esal)
                # dump the data 
                pickle.dump(lst,fp)
                print("="*50)
                print(f"\n {i} Employee Record Saved Successfully in the File ")


def unpicking():
    try:
        with open('emp.txt','rb') as fp:
            print("Employee Records ")
            print("="*50)
            while True:
                try:
                    obj = pickle.load(fp)
                    for val in obj:
                        print(f"\t {val}",end="")
                    print()
                except EOFError:
                    print("="*50) 
                    break   
    except FileNotFoundError:
        print("Source File does not Exists: ")

unpicking()