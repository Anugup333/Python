from typing import List
from math import sqrt

def printDivisors(n: int):
    a = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            a.append(i)
            if n // i != i:
                a.append(n//i)
    a.sort()
    return a

print(printDivisors(6))