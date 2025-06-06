from Custom_Exception import AnujDivisionError,division
s1 = input("enter the first value: ")
s2 = input("enter the second value: ")
try:
    a = int(s1)
    b = int(s2)
    c = division(a,b)
    lst = [12,23,24]
    print(lst[6])
except AnujDivisionError:
    print("Don't Enter Zero for Denomenator ")
except ValueError:
    print("Don't Enter strs / symbols / alpha-numeric ")
except Exception as e:
    print("Something Went wrong take-care ",e)
except:
    print("Something Went Wrong: ")
else:
    print("Val of a = ",a)
    print("Val of a = ",b)
    print("Div = ",c)