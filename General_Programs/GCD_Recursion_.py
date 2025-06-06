def gcd(a,b):
    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b,rem)

a = int(input("Enter first Number: "))
b = int(input("Enter Second Number: "))
print(f"GCD of {a} and {b} is {gcd(a,b)}")