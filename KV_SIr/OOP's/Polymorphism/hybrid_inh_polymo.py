class C1:
    def x(self):
        print("C1 -- x()")
        
class C2(C1):
    def x(self):
        print("C2 -- x()")
        
class C3(C1):
    def x(self):
        print("C3 -- x()")
        
class C4(C2,C3):
    def x(self):
        print("C4 -- x()")
        
        C3.x(self)
        C2.x(self)    # super().x()
        C1.x(self)


# main program 
o4 = C4()
o4.x()