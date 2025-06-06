import time,gc
class Employee:
    def __init__(self):
        print("I am in Constructor ")
        self.eno=10
        self.name = "RS"
        print(f"{self.eno} and {self.name}")
    
    def __del__(self):
        print("Gc calls destructor for de-allocationg the memory")



# main program 
print("Is Garbage Collector running = ",gc.isenabled())  # True
e1 = Employee()
gc.disable()
print("Is Garbage Collector running = ",gc.isenabled())  # False
# gc.enable()
# print("Is Garbage Collector running = ",gc.isenabled())  # True
time.sleep(5)



# its clear indicating that  there is no effect of enabled and 
# disable of the garbage collector is always running 

# it's not running in the version <= 3.8 in python
