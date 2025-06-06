class Test:
    def __init__(self,a=10,b=20):
        print("I am from Default / Parameterized Constructor ")
        self.a = a
        self.b = b
        print("Value of a ",self.a)
        print("Value of b ",self.b)



# main program 
t1 = Test()
# print("Content of t1 ",t1.__dict__)
t2 = Test(a=100,b=200)
# print("Content of t2 ",t2.__dict__)
t3 = Test(a=1000,b=2000)
# print("Content of t3 ",t3.__dict__)