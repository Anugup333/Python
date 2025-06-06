# This program is used to calculate of area of different figure such as Circle and Square 

class Circle:
    def area(self): # Original Method
        self.r = float(input("Enter Radius: "))
        self.ac = 3.14*self.r**2
        print("Area of Circle = ",self.ac)


class Square(Circle):
    def area(self): # Overridden  Method
        self.s = float(input("Enter Side "))
        self.ac = self.s**2
        print("Area of Square = ",self.ac) 
        # Access Super class overridden method
        super().area()
        
# main program
s = Square()
s.area()
