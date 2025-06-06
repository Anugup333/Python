class Employee:
    def __init__(self):
        print("I am in Constructor ")
        self.eno=10
        self.name = "RS"
        print(f"{self.eno} and {self.name}")
    
    def __del__(self):
        print("Gc calls destructor for de-allocationg the memory")



# main program 
e1 = Employee()
del e1 # Gc calls  __del__(self)
e2 = Employee()
del e2 # Gc calls  __del__(self)
e3 = Employee()