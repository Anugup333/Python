class Test:
    def __init__(self):
        print("I am from Default Constructor ")
        self.a = 10
        self.b = 20
        print("Value of a ",self.a)
        print("Value of b ",self.b)



# main program 
t1 = Test()
# print("Content of t1 ",t1.__dict__)
t2 = Test()
# print("Content of t2 ",t2.__dict__)
t3 = Test()
# print("Content of t3 ",t3.__dict__)