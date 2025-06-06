import time
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
e2 = e1  # deep copy 
print("No Longer Interested to maintain e1 memory space")
time.sleep(10)
del e1   # here Gc will not call __del(self) bcz e2 points to that object
print("No Longer Interested to maintain e2 memory space")
time.sleep(10)
del e2   
# here Gc will call __del__(self) bcoz e2 is no where and 
# no object points memory space  