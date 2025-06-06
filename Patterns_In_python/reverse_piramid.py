def reverse_space_piramid(num):
    for i in range(num,0,-1):
        for j in range(0,num-i):
            print(end=" ")
        
        for j in range(0,i):
            print("*",end=" ")
        
        print()
        
def reverse_piramid(num):
    for i in range(num,0,-1):
        for j in range(0,num-i):
            print(end=" ")
        
        for j in range(0,(i-1)*2+1):
            print("*",end="")
        
        print()


n = int(input("Enter the no of rows : "))
reverse_space_piramid(n)
reverse_piramid(n)