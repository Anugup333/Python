# Print rotation of string

import itertools

def leftRotatedString(name):
    size = len(name)
    for i in range(size):
        for j in range(size):
            print(name[(i+j)%size],end="")    
        print()


string = "ABCD"
leftRotatedString(string)