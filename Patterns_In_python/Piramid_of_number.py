def piramid_number(row):
    for i in range(row):
        for j in range(row-i-1,0,-1):
            print(end=" ")
        for k in range(i+1,0,-1):
            print(k,end="")
        for l in range(1,i+1):
            if l >=1 :
                print(l+1,end="")
        print()


n = int(input("Enter the no of rows : "))
piramid_number(n)