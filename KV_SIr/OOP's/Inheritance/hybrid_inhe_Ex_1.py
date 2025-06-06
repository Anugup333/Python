class C1:
    def x(self):
        print("C1 -- x()")
        
class C2(C1):
    def y(self):
        print("C2 -- y()")
        
class C3(C1):
    def z(self):
        print("C3 -- z()")
        
class C4(C2,C3):
    def k(self):
        print("C4 -- k()")


# main program 
o4 = C4()
o4.k()
o4.z()
o4.y()
o4.x()