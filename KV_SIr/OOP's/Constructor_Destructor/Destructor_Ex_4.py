import time
class Employee:
    def __init__(self):
        print("I am in Constructor ")
        self.eno=10
        self.name = "RS"
        print(f"{self.eno} and {self.name}")
    
    # then there is no need to crete destructor bcoz it is 
    # automatic calling by the gc
    def __del__(self):
        print("Gc calls destructor for de-allocationg the memory")



# main program 
e1 = Employee()
e1 = None   # Gc calls __del__(self) forcefully calling Gc

e2 = Employee()
e2 = None   # Gc calls __del__(self) forcefully calling Gc

e3 = Employee()
# Automatically Calling Gc 