class Test:
    # that is shared to all objects 
    x = 5  # Class variable / Static variable 
    
    def __init__(self,first,sec) -> None:
        self.a = first  # that is unique for every object
        self.b = sec
    
    # Instance Method (is that method with have exactly one argument self)
    # that is called by using the instance object of the class
    def in_method(self):
        print(self.a,self.b)
    
    # Static method (is that defined by first use the identation)
    # Static method is called by using both instance and Class Object
    @staticmethod
    def st_method():
        pass
        # print(x) can no be use x here give error
    
    # Class method (is that which have exactly one argument cls )
    # Class method is only be called by Class object 
    @classmethod
    def cl_method(cls):
        print(cls.x)
    

t1 = Test(11,22)
t2 = Test(33,44)
t1.in_method()
Test.cl_method()
Test.st_method()