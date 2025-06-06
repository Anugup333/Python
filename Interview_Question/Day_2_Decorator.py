print(''' ---------  Fuction Decorators --------- ''')

print("-------  Example 1 --------")
def decorator_func(func):
    def wrapper_func():
        print("wrapper_func Worked")
        return func()
    print("decorator_func Worked")
    return wrapper_func

''' Both are Same we can use as both '''

def show():
    print("Show Worked")
decorator_show = decorator_func(show)
decorator_show()

@decorator_func
def anuj():
    return f"hello Anuj"

print(anuj())


print("\n------- Example 2 -------")

def decor(addition):
    def inner_fun():
        result = addition()  # existing functionality
        # add the new Funcanality
        num3 = float(input("Enter the Third Number: "))
        result = result + num3
        return result
    return inner_fun
        
@decor     
def addition():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the Second number: "))
    result = num1 + num2
    return result

print("Addition : ", addition())

print(''' --------- Decorators with arguments --------- ''')

def dec_with_arg(num1):
    def decor(addition):
        def inner_fun(*args,**kwargs):
            result = addition(*args,**kwargs)  # existing functionality
            # add the new Funcanality
            result = result * num1
            return result
        return inner_fun
    return decor
        
@dec_with_arg(10)
def multiplication(a,b):
    result = a * b
    return result

print("Multiplication : ", multiplication(10,20))


print(''' --------- Class Decorators  --------- ''')

def class_decorator(cls):
    class inner_class(cls):
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.extra = "Extra Attribute"
        
        def divide(self):
            return self.first // self.second
        
        def display(self):
            return self.extra
        
    return inner_class
            
@class_decorator
class Name:
    def __init__(self,a,b) -> None:
        self.first = a
        self.second = b
    
    def addition(self):
        return self.first + self.second

    def multiplication(self):
        return self.first * self.second
    
obj = Name(10,20)
print("Addition: ",obj.addition())
print("Multiplication: ",obj.multiplication())
print("Division: ",obj.divide())
print(obj.display())