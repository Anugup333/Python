#  Date- 28/01/2024
''' We will perform operator overloading by using this type  '''  
# By both Arithmatic and Comparison operation

class opratorOverloading:
    def __init__(self,x) -> None:
        self.X = x
        
      # Arithmatic operation
    def __add__(self,other):
        print(f"Addition of {self.X} and {other.X} is {self.X + other.X}")
        
    def __sub__(self,other):
        print(f"Subtraction of {self.X} and {other.X} is {self.X - other.X}")
    
    def __mul__(self,other):
        print(f"Multiplication of {self.X} and {other.X} is {self.X * other.X}")
    
    def __truediv__(self,other):
        print(f"True Division of {self.X} and {other.X} is {self.X / other.X}")
    
    def __floordiv__(self,other):
        print(f"Floor Division of {self.X} and {other.X} is {self.X // other.X}")
    
    def __mod__(self,other):
        print(f"Remainder of {self.X} and {other.X} is {self.X % other.X}")
    
    # Comparison Operation
    def __eq__(self,other):
        print(f"{self.X} are {other.X} equal {self.X == other.X}")
     
    # same as other

obj1 = opratorOverloading(30)
obj2 = opratorOverloading(20)
obj3 = obj1 + obj2 
obj4 = obj1 - obj2 
obj5 = obj1 * obj2 
obj6 = obj1 / obj2 
obj7 = obj1 // obj2 
obj8 = obj1 % obj2 
obj9 = obj1 == obj2  