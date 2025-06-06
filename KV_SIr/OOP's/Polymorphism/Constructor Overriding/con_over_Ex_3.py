# Multiple Inheritance

class Test:
    def __init__(self,a):   # Original Constructor
        print("Test Class Constructor : a = ",a)


class Sample: 
    def __init__(self,b):  # Original Constructor
        print("Sample Class Constructor : b = ",b)


class Python: 
    def __init__(self,c,d):  # Original Constructor
        print("Python Class Constructor : c = {} and d = {}".format(c,d))


class Hyd(Python,Test,Sample):
    def __init__(self,name):   # Overridden Constructor 
        print("Hyd Class Constructor : name = ",name)
        
        Sample.__init__(self,10)
        Test.__init__(self,20)
        
        # Python.__init__(self,30,40)
        super().__init__(30,40)



# main program
h = Hyd("Rossom")
