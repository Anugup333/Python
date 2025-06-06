# Multiple Inheritance

class Test:
    def __init__(self):   # Original Constructor
        print("Test Class Constructor ")


class Sample: 
    def __init__(self):  # Original Constructor
        print("Sample Class Constructor ")

class Python: 
    def __init__(self):  # Original Constructor
        print("Python Class Constructor ")

class Hyd(Python,Test,Sample):
    def __init__(self):
        print("Hyd Class Constructor ")
        
        super().__init__()
        Sample.__init__(self)
        Test.__init__(self)



# main program
h = Hyd()
