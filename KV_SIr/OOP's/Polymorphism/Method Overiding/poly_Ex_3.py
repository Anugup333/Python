# This program is used to calculate of area of different figure such as Circle and Square 
 
# Multiple Inheritance

class Circle:
    def area(self): # Original Method
        self.r = float(input("Enter Radius: "))
        self.ac = 3.14*self.r**2
        print("Area of Circle = ",self.ac)
        print('='*50)


class Square:
    def area(self): 
        self.s = float(input("Enter Side "))
        self.ac = self.s**2
        print("Area of Square = ",self.ac)
        print('='*50) 
        
class Rect(Circle,Square):
    def area(self):   # Overridden  Method
        self.l = float(input("Enter Length : "))
        self.b = float(input("Enter Breadth : "))
        self.ac = self.l*self.b
        print("Area of Rectangle = ",self.ac)
        print('='*50)
                
        # --------------------
        Circle.area(self)
        Square.area(self)  
                
# main program
r = Rect()
r.area()
