def decorator_fun(fun):
    def wrapper_fun():
        print("Wrapper ")
        return fun()
    print("decorator Fun")
    return wrapper_fun
@decorator_fun
def anuj():
    return "anuj"

print(anuj())