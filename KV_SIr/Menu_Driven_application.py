# Program Implements menu driven Appliaction for computing all arithmatic Operations by using match case
print("="*40)
print("\t Arithmatic Operation")
print("="*40)
print("\t 1. Addition")
print("\t 2. Substraction")
print("\t 3. Multiplication")
print("\t 4. Division")
print("\t 5. Floor Division")
print("\t 6. Modulo Division")
print("\t 7. Exponential") 
print("\t 8. Exit")
print("="*40)
ch = int(input("Enter Your Choice : "))
match(ch):
    case 1:
        n1= float(input("Enter the first value: ")) 
        n2= float(input("Enter the Second value: ")) 
        print("sum({},{}) = {}".format(n1,n2,n1+n2))
    case 2:
        n1= float(input("Enter the first value: ")) 
        n2= float(input("Enter the Second value: "))
        print("sub({},{}) = {}".format(n1,n2,n1-n2))
    case 3:
        n1= float(input("Enter the first value: ")) 
        n2= float(input("Enter the Second value: "))
        print("mul({},{}) = {}".format(n1,n2,n1*n2))
    case 4:
        n1= float(input("Enter the first value: ")) 
        n2= float(input("Enter the Second value: "))
        print("Div({},{}) = {}".format(n1,n2,n1/n2))
    case 5:
        n1= float(input("Enter the first value: ")) 
        n2= float(input("Enter the Second value: "))
        print("Floor_Div({},{}) = {}".format(n1,n2,n1//n2))
    case 6:
        n1= float(input("Enter the first value: ")) 
        n2= float(input("Enter the Second value: "))
        print("Mod_Div({},{}) = {}".format(n1,n2,n1%n2))
    case 7:
        n1= float(input("Enter the first value: ")) 
        n2= float(input("Enter the Second value: "))
        print("exp({},{}) = {}".format(n1,n2,n1**n2))
    case 8:
        exit()
    case _:
        print("Enter the Valid choice ")
