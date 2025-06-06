def space_piramid(num):
    for i in range(0,num):
        for j in range(0,num-i-1):
            print(end=" ")
        
        for j in range(0,i+1):
            print("*",end=" ")
        print()

def piramid(num):
    for i in range(0,num):
        for j in range(0,num-i-1):
            print(end=" ")
        
        for j in range(0,2*i+1):
            print("*",end="")
        print()
            
n = int(input("Enter the number of rows: "))
space_piramid(n)
piramid(n)