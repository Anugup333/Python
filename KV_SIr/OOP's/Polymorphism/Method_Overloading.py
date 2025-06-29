#  Date- 28/01/2024
''' Python does not allow method overloading based on {type} as 
  it is not strongly type language 
  We will perform method overloading by using this type  '''  

''' 
                           Is Function overloading allowed in python? 
    
    In Python, function overloading as seen in languages like C++ or Java is not directly supported. 
    However, Python provides several ways to achieve similar behavior through default arguments, 
    variable-length arguments, and more advanced techniques like using functools.singledispatch. 
    
    Here are a few methods to achieve function overloading in Python: 
       
         '''


'''    1. Using Default Arguments 
            
        You can use default arguments to provide different behavior based on the number of arguments passed
'''

def greet(name,greeting ="Hello"):
    return f"{greeting} , {name}"

print(greet("Anuj"))
print(greet("Hello","Anuj"))


'''    2. Variable-length arguments
            
        You can use default arguments to provide different behavior based on the number of arguments passed
'''


class methodOverloading :
    result = 0
    def add(self,type = None, *args):
        if type == 'int':
            self.result = 0
        if type == 'str':
            self.result = ''
        for i in args:
            self.result += i
        return self.result

class greet :
    def greeting(self,name = None):
        if name is not None:
            print("Welcome ",name)
        else:
            print("Welcome")
    
g1 = greet()         
g1.greeting()
g1.greeting("Anuj Gupta ")

m1 = methodOverloading()
print(m1.add('int',23,34,23,23))
print(m1.add('str',"I ","Love ","Python ","Programming"))