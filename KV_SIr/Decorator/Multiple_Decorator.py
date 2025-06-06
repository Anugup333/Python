def cube(func):
    def wrapper():
        n,sqrVal,sqrtVal = func()
        cbVal = n**3
        return n,cbVal,sqrVal,sqrtVal
    return wrapper

def square(func):
    def wrapper():
        n,sqrtVal = func()
        sqrVal = n**2
        return n,sqrVal,sqrtVal
    return wrapper


def square_root(func):
    def wrapper():
        n = func()
        sqrtVal = n**0.5
        return n,sqrtVal
    return wrapper

@cube
@square
@square_root
def get_value():
    return float(input("enter the Number: "))

n,cbval,sqval,sqrtval = get_value()
print(f"Number : {n}")
print(f"Cube : {cbval}")
print(f"Square : {sqval}")
print(f"Square Root : {sqrtval:0.4f}")