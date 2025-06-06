#  Date- 28/01/2024
''' Python does not allow method overloading based on {type} as 
  it is not strongly type language 
  We will perform method overloading by using this type  '''  

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