def square(func):
    def wrapper():
        num = func()
        result = num**2
        return num,result
    return wrapper

@square
def get_value():
    return float(input("Enter the Number: "))

print(get_value())