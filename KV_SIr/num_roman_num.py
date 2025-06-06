num = int(input("Enter the number that you find to Roman: "))
if (num<0):
    print("="*50)
    print(f"{num} This is not a valid Number Plase Enter the valid Number")
else:
    print(f"{num} = ",end="")
    while num >= 1000:
        print("M",end="")
        num -= 1000
    if num >= 900:
        print("CM",end="")
        num -= 900
    if num >= 500:
        print("D",end="")
        num -= 500
    if num >= 400:
        print("CD",end="")
        num -= 400
    while num >= 100:
        print("C",end="")
        num -= 100
    if num >= 90:
        print("XC",end="")
        num -= 90
    if num >= 50:
        print("L",end="")
        num -= 50
    if num >= 40:
        print("XL",end="")
        num -= 40
    while num >= 10:
        print("X",end="")
        num -= 10
    if num >= 9:
        print("IX",end="")
        num -= 9
    if num >= 5:
        print("V",end="")
        num -= 5
    if num >= 4:
        print("IV",end="")
        num -= 4
    while num >= 1:
        print("I",end="")
        num -= 1
    print()