import sys,gc
class Employee:
    def __init__(self,eno,ename):
        print("I am in the Parameterized Constructor ID - ",id(self))
        self.eno = eno
        self.ename = ename
        print("Employee Number = ",self.eno)
        print("Employee Name = ",self.ename)
    
    def __del__(self):
        print("Gc Call __del__ for De-allocating the Memory Space - Id = ",id(self))
        global totmemspace 
        totmemspace = totmemspace - sys.getsizeof(self)
        print("Now Available Memory Space =  ",totmemspace)
    

# main Program 
print("="*50)
print("Program Execution Started ")
print("Initially, Is Gc Running = ",gc.isenabled()) # True
e1 = Employee(101,"Anuj")
e2= Employee(102,"Ram")
e3 = Employee(103,"Manoj")
gc.disable()
totmemspace = sys.getsizeof(e1) + sys.getsizeof(e2) + sys.getsizeof(e3)
print("Initially, The Total Memory Space  = ",totmemspace)
print("Now is Gc Running = ",gc.isenabled())  # False
print("Program Execution Ended ")
# Gc calls Destructor by default at the end of the Program 
# Automatically known as Automatic Garbage Collector 
        