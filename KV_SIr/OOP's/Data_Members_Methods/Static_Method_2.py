# This Program Demonstrate the concept of calculator Method

class Calc:
    # Static Method is Used to Perform Unique and Utility Operation
    @staticmethod
    def calculate(obj):
        match(obj.op):
            case "+":
                print(f"Sum ({obj.a} , {obj.b}) = {obj.a+obj.b}")
            case "-":
                print(f"Sub ({obj.a} , {obj.b}) = {obj.a+obj.b}")
            case "*":
                print(f"Mul ({obj.a} , {obj.b}) = {obj.a*obj.b}")
            case "/":
                try:
                    print(f"Div ({obj.a} , {obj.b}) = {obj.a/obj.b}")
                except ZeroDivisionError:
                    print("Don't Enter Zero as a Denominator.... ")
            case "//":
                print(f"Floor ({obj.a} , {obj.b}) = {obj.a//obj.b}")
            case "%":
                print(f"Mod ({obj.a} , {obj.b}) = {obj.a%obj.b}")
            case "**":
                print(f"Expo ({obj.a} , {obj.b}) = {obj.a**obj.b}")
            case _:
                print(f"{obj.op} This is not an Arithamtic Operator ")

class Numbers:
    def getvalues(self):
        self.a = float(input("Enter First Value : "))
        self.b = float(input("Enter Second Value : "))
        self.op = input("Enter any Arithamtic Operator : ")


# main Program 
n = Numbers()
try:
    n.getvalues()
except ValueError:
    print("Enter the Correct Type.... ")
else:
    Calc.calculate(n)
